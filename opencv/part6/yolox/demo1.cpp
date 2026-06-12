#include <iostream>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

#include <opencv2/dnn.hpp>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;
using namespace dnn;

vector<pair<int, int>> backendTargetPairs = {
    make_pair(DNN_BACKEND_OPENCV, DNN_TARGET_CPU)};

vector<string> labelYolox = {
    "person", "bicycle", "car", "motorcycle", "airplane", "bus",
    "train", "truck", "boat", "traffic light", "fire hydrant",
    "stop sign", "parking meter", "bench", "bird", "cat", "dog",
    "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe",
    "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee",
    "skis", "snowboard", "sports ball", "kite", "baseball bat",
    "baseball glove", "skateboard", "surfboard", "tennis racket",
    "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl",
    "banana", "apple", "sandwich", "orange", "broccoli", "carrot",
    "hot dog", "pizza", "donut", "cake", "chair", "couch",
    "potted plant", "bed", "dining table", "toilet", "tv", "laptop",
    "mouse", "remote", "keyboard", "cell phone", "microwave",
    "oven", "toaster", "sink", "refrigerator", "book", "clock",
    "vase", "scissors", "teddy bear", "hair drier", "toothbrush"};

class YoloX
{
private:
    Net net;
    string modelPath;
    Size inputSize;
    float confThreshold;
    float nmsThreshold;
    float objThreshold;
    int backendId;
    int targetId;
    int num_classes;
    vector<int> strides;
    Mat expandedStrides;
    Mat grids;

public:
    YoloX(
        string modPath,
        float confThresh = 0.35f,
        float nmsThresh = 0.5f,
        float objThresh = 0.5f,
        int bId = DNN_BACKEND_OPENCV,
        int tId = DNN_TARGET_CPU)
        : modelPath(modPath),
          confThreshold(confThresh),
          nmsThreshold(nmsThresh),
          objThreshold(objThresh),
          backendId(bId),
          targetId(tId)
    {
        num_classes = static_cast<int>(labelYolox.size());

        net = readNet(modelPath);
        net.setPreferableBackend(backendId);
        net.setPreferableTarget(targetId);

        inputSize = Size(640, 640);
        strides = vector<int>{8, 16, 32};

        generateAnchors();
    }

    Mat preprocess(const Mat &img)
    {
        Mat blob;

        blobFromImage(
            img,
            blob,
            1.0,
            Size(img.cols, img.rows),
            Scalar(),
            true,
            false,
            CV_32F);

        return blob;
    }

    Mat infer(const Mat &srcimg)
    {
        Mat inputBlob = preprocess(srcimg);

        net.setInput(inputBlob);

        vector<Mat> outs;
        net.forward(outs, net.getUnconnectedOutLayersNames());

        if (outs.empty())
        {
            return Mat();
        }

        return postprocess(outs[0]);
    }

    Mat postprocess(const Mat &outputs)
    {
        Mat dets = outputs.reshape(0, outputs.size[1]);

        Mat col01;
        add(dets.colRange(0, 2), grids, col01);

        Mat col23;
        exp(dets.colRange(2, 4), col23);

        vector<Mat> col = {col01, col23};

        Mat boxes;
        hconcat(col, boxes);

        float *ptr = expandedStrides.ptr<float>(0);

        for (int r = 0; r < boxes.rows; r++, ptr++)
        {
            boxes.rowRange(r, r + 1) = *ptr * boxes.rowRange(r, r + 1);
        }

        vector<Rect> boxesXYWH;
        vector<float> scores;
        vector<int> classIds;

        Mat classScores = dets.colRange(5, dets.cols).clone();

        for (int r = 0; r < boxes.rows; r++)
        {
            float objScore = dets.at<float>(r, 4);

            if (objScore < objThreshold)
            {
                continue;
            }

            Mat rowScores = classScores.row(r) * objScore;

            double minVal;
            double maxVal;
            Point minIdx;
            Point maxIdx;

            minMaxLoc(rowScores, &minVal, &maxVal, &minIdx, &maxIdx);

            float score = static_cast<float>(maxVal);
            int classId = maxIdx.x;

            if (score < confThreshold)
            {
                continue;
            }

            float cx = boxes.at<float>(r, 0);
            float cy = boxes.at<float>(r, 1);
            float w = boxes.at<float>(r, 2);
            float h = boxes.at<float>(r, 3);

            int left = cvRound(cx - w / 2.0f);
            int top = cvRound(cy - h / 2.0f);
            int width = cvRound(w);
            int height = cvRound(h);

            boxesXYWH.push_back(Rect(left, top, width, height));
            scores.push_back(score);
            classIds.push_back(classId);
        }

        vector<int> finalKeep;

        for (int cls = 0; cls < num_classes; cls++)
        {
            vector<Rect> clsBoxes;
            vector<float> clsScores;
            vector<int> clsOriginalIdx;

            for (size_t i = 0; i < classIds.size(); i++)
            {
                if (classIds[i] == cls)
                {
                    clsBoxes.push_back(boxesXYWH[i]);
                    clsScores.push_back(scores[i]);
                    clsOriginalIdx.push_back(static_cast<int>(i));
                }
            }

            vector<int> keep;
            NMSBoxes(clsBoxes, clsScores, confThreshold, nmsThreshold, keep);

            for (int idx : keep)
            {
                finalKeep.push_back(clsOriginalIdx[idx]);
            }
        }

        if (finalKeep.empty())
        {
            return Mat();
        }

        Mat candidates(static_cast<int>(finalKeep.size()), 6, CV_32FC1);

        for (int row = 0; row < static_cast<int>(finalKeep.size()); row++)
        {
            int idx = finalKeep[row];
            const Rect &box = boxesXYWH[idx];

            candidates.at<float>(row, 0) = static_cast<float>(box.x);
            candidates.at<float>(row, 1) = static_cast<float>(box.y);
            candidates.at<float>(row, 2) = static_cast<float>(box.width);
            candidates.at<float>(row, 3) = static_cast<float>(box.height);
            candidates.at<float>(row, 4) = scores[idx];
            candidates.at<float>(row, 5) = static_cast<float>(classIds[idx]);
        }

        return candidates;
    }

    void generateAnchors()
    {
        vector<tuple<int, int, int>> nb;
        int total = 0;

        for (int v : strides)
        {
            int w = inputSize.width / v;
            int h = inputSize.height / v;

            nb.push_back(tuple<int, int, int>(w * h, w, v));
            total += w * h;
        }

        grids = Mat(total, 2, CV_32FC1);
        expandedStrides = Mat(total, 1, CV_32FC1);

        float *ptrGrids = grids.ptr<float>(0);
        float *ptrStrides = expandedStrides.ptr<float>(0);

        int pos = 0;

        for (auto le : nb)
        {
            int r = get<1>(le);

            for (int i = 0; i < get<0>(le); i++, pos++)
            {
                *ptrGrids++ = static_cast<float>(i % r);
                *ptrGrids++ = static_cast<float>(i / r);
                *ptrStrides++ = static_cast<float>(get<2>(le));
            }
        }
    }
};

pair<Mat, double> letterBox(const Mat &srcimg, Size targetSize = Size(640, 640))
{
    Mat paddedImg(targetSize.height, targetSize.width, CV_32FC3, Scalar::all(114.0));
    Mat resizeImg;

    double ratio = min(
        targetSize.height / static_cast<double>(srcimg.rows),
        targetSize.width / static_cast<double>(srcimg.cols));

    int newWidth = static_cast<int>(srcimg.cols * ratio);
    int newHeight = static_cast<int>(srcimg.rows * ratio);

    resize(srcimg, resizeImg, Size(newWidth, newHeight), 0, 0, INTER_LINEAR);

    Mat resizeImg32F;
    resizeImg.convertTo(resizeImg32F, CV_32FC3);

    resizeImg32F.copyTo(paddedImg(Rect(0, 0, newWidth, newHeight)));

    return pair<Mat, double>(paddedImg, ratio);
}

Mat visualize(const Mat &dets, const Mat &srcimg, double letterboxScale, double fps = -1)
{
    Mat resImg = srcimg.clone();

    if (fps > 0)
    {
        putText(
            resImg,
            format("FPS: %.2f", fps),
            Point(10, 25),
            FONT_HERSHEY_SIMPLEX,
            1,
            Scalar(0, 0, 255),
            2);
    }

    if (dets.empty())
    {
        return resImg;
    }

    for (int row = 0; row < dets.rows; row++)
    {
        float x = dets.at<float>(row, 0) / static_cast<float>(letterboxScale);
        float y = dets.at<float>(row, 1) / static_cast<float>(letterboxScale);
        float w = dets.at<float>(row, 2) / static_cast<float>(letterboxScale);
        float h = dets.at<float>(row, 3) / static_cast<float>(letterboxScale);

        int x0 = max(0, cvRound(x));
        int y0 = max(0, cvRound(y));
        int x1 = min(srcimg.cols - 1, cvRound(x + w));
        int y1 = min(srcimg.rows - 1, cvRound(y + h));

        float score = dets.at<float>(row, 4);
        int clsId = static_cast<int>(dets.at<float>(row, 5));

        if (clsId < 0 || clsId >= static_cast<int>(labelYolox.size()))
        {
            continue;
        }

        string text = format("%s : %.2f", labelYolox[clsId].c_str(), score * 100.0f);

        rectangle(resImg, Point(x0, y0), Point(x1, y1), Scalar(0, 255, 0), 2);

        int baseLine = 0;
        Size txtSize = getTextSize(text, FONT_HERSHEY_SIMPLEX, 0.5, 1, &baseLine);

        int textY = max(0, y0 - txtSize.height - 4);

        rectangle(
            resImg,
            Point(x0, textY),
            Point(x0 + txtSize.width + 4, textY + txtSize.height + 4),
            Scalar(255, 255, 255),
            -1);

        putText(
            resImg,
            text,
            Point(x0 + 2, textY + txtSize.height + 1),
            FONT_HERSHEY_SIMPLEX,
            0.5,
            Scalar(0, 0, 0),
            1);
    }

    return resImg;
}

int main()
{
    const string model = "../object_detection_yolox_2022nov.onnx";

    const float confThreshold = 0.5f;
    const float objThreshold = 0.5f;
    const float nmsThreshold = 0.5f;

    YoloX modelNet(
        model,
        confThreshold,
        nmsThreshold,
        objThreshold,
        DNN_BACKEND_OPENCV,
        DNN_TARGET_CPU);

    VideoCapture cap(0, CAP_V4L2);

    if (!cap.isOpened())
    {
        cerr << "카메라를 열 수 없습니다." << endl;
        return -1;
    }

    cap.set(CAP_PROP_FOURCC, VideoWriter::fourcc('M', 'J', 'P', 'G'));
    cap.set(CAP_PROP_FRAME_WIDTH, 640);
    cap.set(CAP_PROP_FRAME_HEIGHT, 480);
    cap.set(CAP_PROP_FPS, 30);

    namedWindow("YOLOX", WINDOW_AUTOSIZE);

    Mat frame;

    while (true)
    {
        cap >> frame;

        if (frame.empty())
        {
            cerr << "프레임을 읽을 수 없습니다." << endl;
            break;
        }

        pair<Mat, double> lb = letterBox(frame);
        Mat inputImage = lb.first;
        double letterboxScale = lb.second;

        TickMeter tm;
        tm.start();

        Mat predictions = modelNet.infer(inputImage);

        tm.stop();

        Mat result = visualize(predictions, frame, letterboxScale, tm.getFPS());

        imshow("YOLOX", result);

        if (waitKey(1) == 27)
            break;
    }

    cap.release();
    destroyAllWindows();

    return 0;
}
// wget https://huggingface.co/camenduru/openpose/resolve/5e17f6ad43ab415a0114537541a8d37d2503424f/models/hand/pose_iter_102000.caffemodel

#include <atomic>
#include <iostream>
#include <mutex>
#include <opencv2/dnn.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <thread>

using namespace std;
using namespace cv;
using namespace cv::dnn;

const int POSE_PAIRS[20][2] =
    {
        {0, 1}, {1, 2}, {2, 3}, {3, 4}, // thumb
        {0, 5},
        {5, 6},
        {6, 7},
        {7, 8}, // index
        {0, 9},
        {9, 10},
        {10, 11},
        {11, 12}, // middle
        {0, 13},
        {13, 14},
        {14, 15},
        {15, 16}, // ring
        {0, 17},
        {17, 18},
        {18, 19},
        {19, 20} // small
};

const String folderPath = "/home/hrd_1_3/study/opencv/data/";

string protoFile = folderPath + "pose_deploy.prototxt";
string weightsFile = folderPath + "pose_iter_102000.caffemodel";

constexpr int nPoints = 21;
constexpr int inputHeight = 224;

int main(int argc, char **argv)
{
    float thresh = 0.01;

    VideoCapture cap(0, CAP_V4L2);

    cap.set(CAP_PROP_FOURCC, VideoWriter::fourcc('M', 'J', 'P', 'G'));
    cap.set(CAP_PROP_FRAME_WIDTH, 640);
    cap.set(CAP_PROP_FRAME_HEIGHT, 480);
    cap.set(CAP_PROP_FPS, 30);
    cap.set(CAP_PROP_BUFFERSIZE, 1);

    if (!cap.isOpened())
    {
        cerr << "Unable to connect to camera" << endl;
        return 1;
    }

    int frameWidth = cap.get(CAP_PROP_FRAME_WIDTH);
    int frameHeight = cap.get(CAP_PROP_FRAME_HEIGHT);
    float aspect_ratio = frameWidth / (float)frameHeight;
    int inHeight = inputHeight;
    int inWidth = cvRound(aspect_ratio * inHeight / 8) * 8;

    cout << "inWidth = " << inWidth << " ; inHeight = " << inHeight << endl;

    Net net = readNetFromCaffe(protoFile, weightsFile);
    net.setPreferableBackend(DNN_BACKEND_OPENCV);
    net.setPreferableTarget(DNN_TARGET_CPU);

    Mat latestFrame;
    mutex frameMutex;
    atomic<bool> captureRunning(true);

    thread captureThread([&]()
                         {
        Mat capturedFrame;
        while (captureRunning)
        {
            if (!cap.read(capturedFrame) || capturedFrame.empty())
                continue;

            lock_guard<mutex> lock(frameMutex);
            capturedFrame.copyTo(latestFrame);
        } });

    while (1)
    {
        Mat frame;
        {
            lock_guard<mutex> lock(frameMutex);
            if (!latestFrame.empty())
                latestFrame.copyTo(frame);
        }

        if (frame.empty())
        {
            if (waitKey(1) == 27)
                break;
            continue;
        }

        double t = (double)getTickCount();
        Mat inpBlob = blobFromImage(frame, 1.0 / 255, Size(inWidth, inHeight), Scalar(0, 0, 0), false, false);

        net.setInput(inpBlob);

        Mat output = net.forward();

        int H = output.size[2];
        int W = output.size[3];

        // find the position of the body parts
        vector<Point> points(nPoints);
        for (int n = 0; n < nPoints; n++)
        {
            // Probability map of corresponding body's part.
            Mat probMap(H, W, CV_32F, output.ptr(0, n));

            Point maxLoc;
            double prob;
            minMaxLoc(probMap, 0, &prob, 0, &maxLoc);
            if (prob > thresh)
            {
                points[n] = Point(
                    cvRound((double)frameWidth * maxLoc.x / W),
                    cvRound((double)frameHeight * maxLoc.y / H)
                );
            }
            else
            {
                points[n] = Point(-1, -1);
            }
        }

        int nPairs = sizeof(POSE_PAIRS) / sizeof(POSE_PAIRS[0]);

        for (int n = 0; n < nPairs; n++)
        {
            // lookup 2 connected body/hand parts
            Point2f partA = points[POSE_PAIRS[n][0]];
            Point2f partB = points[POSE_PAIRS[n][1]];

            if (partA.x <= 0 || partA.y <= 0 || partB.x <= 0 || partB.y <= 0)
                continue;

            line(frame, partA, partB, Scalar(0, 255, 255), 8);
            circle(frame, partA, 8, Scalar(0, 0, 255), -1);
            circle(frame, partB, 8, Scalar(0, 0, 255), -1);
        }

        t = ((double)cv::getTickCount() - t) / cv::getTickFrequency();
        cout << "Time Taken for frame = " << t << endl;
        cv::putText(frame, cv::format("time taken = %.2f sec", t), cv::Point(50, 50), cv::FONT_HERSHEY_COMPLEX, .8, cv::Scalar(255, 50, 0), 2);
        imshow("Output-Skeleton", frame);
        char key = waitKey(1);
        if (key == 27)
            break;
    }

    captureRunning = false;
    captureThread.join();
    cap.release();

    return 0;
}

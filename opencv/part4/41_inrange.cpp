#include "colors.hpp"
#include <iostream>
#include <opencv2/opencv.hpp>
#include <vector>

using namespace std;
using namespace cv;

int main()
{
    VideoCapture cap(0, CAP_V4L2);

    if (!cap.isOpened())
    {
        cerr << "카메라를 열 수 없습니다." << endl;
        return 1;
    }

    cap.set(
        CAP_PROP_FOURCC,
        VideoWriter::fourcc('M', 'J', 'P', 'G')
    );
    cap.set(CAP_PROP_FRAME_WIDTH, 640);
    cap.set(CAP_PROP_FRAME_HEIGHT, 480);
    cap.set(CAP_PROP_FPS, 30);

    // 노란색 검출을 위한 초기 HSV 범위
    int lowerHue = 20;
    int upperHue = 40;
    int lowerSaturation = 80;
    int upperSaturation = 255;
    int lowerValue = 80;
    int upperValue = 255;
    int minimumArea = 1000;

    namedWindow("frame");
    namedWindow("mask");

    createTrackbar("lower H", "mask", &lowerHue, 179);
    createTrackbar("upper H", "mask", &upperHue, 179);
    createTrackbar(
        "lower S",
        "mask",
        &lowerSaturation,
        255
    );
    createTrackbar(
        "upper S",
        "mask",
        &upperSaturation,
        255
    );
    createTrackbar("lower V", "mask", &lowerValue, 255);
    createTrackbar("upper V", "mask", &upperValue, 255);
    createTrackbar("minimum area", "mask", &minimumArea, 20000);

    Mat frame;
    Mat hsv;
    Mat mask;
    const Mat kernel = getStructuringElement(
        MORPH_ELLIPSE,
        Size(5, 5)
    );

    while (true)
    {
        if (!cap.read(frame) || frame.empty())
        {
            cerr << "카메라 frame을 읽을 수 없습니다." << endl;
            break;
        }

        cvtColor(frame, hsv, COLOR_BGR2HSV);

        const int lowH = min(lowerHue, upperHue);
        const int highH = max(lowerHue, upperHue);
        const int lowS = min(lowerSaturation, upperSaturation);
        const int highS = max(lowerSaturation, upperSaturation);
        const int lowV = min(lowerValue, upperValue);
        const int highV = max(lowerValue, upperValue);

        inRange(
            hsv,
            Scalar(lowH, lowS, lowV),
            Scalar(highH, highS, highV),
            mask
        );

        morphologyEx(mask, mask, MORPH_OPEN, kernel);
        morphologyEx(mask, mask, MORPH_CLOSE, kernel);

        vector<vector<Point>> contours;
        findContours(
            mask.clone(),
            contours,
            RETR_EXTERNAL,
            CHAIN_APPROX_SIMPLE
        );

        double largestArea = 0.0;
        Rect targetBox;

        for (const vector<Point> &contour : contours)
        {
            const double area = contourArea(contour);
            if (area > largestArea)
            {
                largestArea = area;
                targetBox = boundingRect(contour);
            }
        }

        const int maskPixelCount = countNonZero(mask);
        if (largestArea >= minimumArea && targetBox.area() > 0)
        {
            rectangle(frame, targetBox, Color::Red, 3, LINE_AA);

            const Point center(
                targetBox.x + targetBox.width / 2,
                targetBox.y + targetBox.height / 2
            );
            drawMarker(
                frame,
                center,
                Color::Green,
                MARKER_CROSS,
                20,
                2,
                LINE_AA
            );
        }

        putText(
            frame,
            "mask pixels: " + to_string(maskPixelCount),
            Point(10, 30),
            FONT_HERSHEY_SIMPLEX,
            0.7,
            Color::Green,
            2,
            LINE_AA
        );
        putText(
            frame,
            "target area: " + to_string(cvRound(largestArea)),
            Point(10, 60),
            FONT_HERSHEY_SIMPLEX,
            0.7,
            Color::Green,
            2,
            LINE_AA
        );

        imshow("frame", frame);
        imshow("mask", mask);

        const int key = waitKey(30);
        if (key == 27 || key == 'q')
            break;
    }

    cap.release();
    destroyAllWindows();
    return 0;
}

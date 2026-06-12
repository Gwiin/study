#include "colors.hpp"
#include <algorithm>
#include <array>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <opencv2/opencv.hpp>
#include <sstream>
#include <vector>

using namespace std;
using namespace cv;

namespace
{
constexpr float POST_IT_WIDTH_MM = 50.0f;
constexpr float POST_IT_HEIGHT_MM = 20.0f;
constexpr double MIN_POST_IT_AREA_PX = 500.0;

struct ThresholdSettings
{
    int yellowLowH = 18;
    int yellowHighH = 42;
    int yellowLowS = 80;
    int yellowLowV = 80;
    int paperMaxS = 90;
    int paperLowV = 100;
};

array<Point2f, 4> orderCorners(const vector<Point> &points)
{
    vector<Point2f> sortedPoints;
    sortedPoints.reserve(points.size());

    Point2f center(0.f, 0.f);
    for (const Point &point : points)
    {
        const Point2f pointFloat(
            static_cast<float>(point.x),
            static_cast<float>(point.y)
        );
        sortedPoints.push_back(pointFloat);
        center += pointFloat;
    }
    center *= 0.25f;

    sort(
        sortedPoints.begin(),
        sortedPoints.end(),
        [&center](const Point2f &a, const Point2f &b)
        {
            return atan2(a.y - center.y, a.x - center.x) <
                atan2(b.y - center.y, b.x - center.x);
        }
    );

    auto firstCorner = min_element(
        sortedPoints.begin(),
        sortedPoints.end(),
        [](const Point2f &a, const Point2f &b)
        {
            return a.x + a.y < b.x + b.y;
        }
    );
    rotate(sortedPoints.begin(), firstCorner, sortedPoints.end());

    array<Point2f, 4> ordered;
    copy(sortedPoints.begin(), sortedPoints.end(), ordered.begin());
    return ordered;
}

bool findPostIt(
    const Mat &mask,
    vector<Point> &postItContour,
    array<Point2f, 4> &postItCorners
)
{
    vector<vector<Point>> contours;
    findContours(
        mask.clone(),
        contours,
        RETR_EXTERNAL,
        CHAIN_APPROX_SIMPLE
    );

    double bestArea = 0.0;
    vector<Point> bestPolygon;
    vector<Point> bestContour;

    for (const vector<Point> &contour : contours)
    {
        const double area = contourArea(contour);
        if (area < MIN_POST_IT_AREA_PX)
            continue;

        vector<Point> polygon;
        approxPolyDP(
            contour,
            polygon,
            arcLength(contour, true) * 0.03,
            true
        );

        if (
            polygon.size() == 4 &&
            isContourConvex(polygon) &&
            area > bestArea
        )
        {
            bestArea = area;
            bestPolygon = polygon;
            bestContour = contour;
        }
    }

    if (bestPolygon.empty())
        return false;

    postItContour = bestContour;
    postItCorners = orderCorners(bestPolygon);
    return true;
}

bool findPaper(
    const Mat &mask,
    const Point2f &postItCenter,
    double postItArea,
    vector<Point> &paperContour,
    vector<Point> &paperPolygon
)
{
    vector<vector<Point>> contours;
    findContours(
        mask.clone(),
        contours,
        RETR_EXTERNAL,
        CHAIN_APPROX_SIMPLE
    );

    double bestScore = 0.0;

    for (const vector<Point> &contour : contours)
    {
        const double area = contourArea(contour);
        if (area < postItArea * 1.2)
            continue;

        const bool containsPostIt =
            pointPolygonTest(contour, postItCenter, false) >= 0;
        const double score = area * (containsPostIt ? 2.0 : 1.0);

        if (score > bestScore)
        {
            bestScore = score;
            paperContour = contour;
        }
    }

    if (paperContour.empty())
        return false;

    approxPolyDP(
        paperContour,
        paperPolygon,
        arcLength(paperContour, true) * 0.01,
        true
    );
    return true;
}

void drawTextLine(
    Mat &image,
    const string &text,
    int lineNumber,
    const Scalar &color = Color::Green
)
{
    const Point position(10, 28 + lineNumber * 27);

    putText(
        image,
        text,
        position,
        FONT_HERSHEY_SIMPLEX,
        0.65,
        Color::Black,
        4,
        LINE_AA
    );
    putText(
        image,
        text,
        position,
        FONT_HERSHEY_SIMPLEX,
        0.65,
        color,
        2,
        LINE_AA
    );
}

string fixedNumber(double value, int precision)
{
    ostringstream stream;
    stream << fixed << setprecision(precision) << value;
    return stream.str();
}
} // namespace

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

    ThresholdSettings settings;
    namedWindow("controls");
    namedWindow("frame");
    namedWindow("yellow mask");
    namedWindow("paper mask");

    createTrackbar(
        "yellow low H",
        "controls",
        &settings.yellowLowH,
        179
    );
    createTrackbar(
        "yellow high H",
        "controls",
        &settings.yellowHighH,
        179
    );
    createTrackbar(
        "yellow low S",
        "controls",
        &settings.yellowLowS,
        255
    );
    createTrackbar(
        "yellow low V",
        "controls",
        &settings.yellowLowV,
        255
    );
    createTrackbar(
        "paper max S",
        "controls",
        &settings.paperMaxS,
        255
    );
    createTrackbar(
        "paper low V",
        "controls",
        &settings.paperLowV,
        255
    );

    const Mat yellowKernel = getStructuringElement(
        MORPH_ELLIPSE,
        Size(5, 5)
    );
    const Mat paperKernel = getStructuringElement(
        MORPH_RECT,
        Size(7, 7)
    );
    const Mat controlImage(1, 500, CV_8UC3, Color::Black);

    Mat frame;
    Mat hsv;
    Mat yellowMask;
    Mat paperMask;

    while (true)
    {
        if (!cap.read(frame) || frame.empty())
        {
            cerr << "카메라 frame을 읽을 수 없습니다." << endl;
            break;
        }

        cvtColor(frame, hsv, COLOR_BGR2HSV);

        const int yellowLowH =
            min(settings.yellowLowH, settings.yellowHighH);
        const int yellowHighH =
            max(settings.yellowLowH, settings.yellowHighH);

        inRange(
            hsv,
            Scalar(
                yellowLowH,
                settings.yellowLowS,
                settings.yellowLowV
            ),
            Scalar(yellowHighH, 255, 255),
            yellowMask
        );
        morphologyEx(
            yellowMask,
            yellowMask,
            MORPH_OPEN,
            yellowKernel
        );
        morphologyEx(
            yellowMask,
            yellowMask,
            MORPH_CLOSE,
            yellowKernel,
            Point(-1, -1),
            2
        );

        // 채도가 낮고 밝은 영역을 흰 종이 후보로 사용한다.
        inRange(
            hsv,
            Scalar(0, 0, settings.paperLowV),
            Scalar(179, settings.paperMaxS, 255),
            paperMask
        );
        morphologyEx(
            paperMask,
            paperMask,
            MORPH_CLOSE,
            paperKernel,
            Point(-1, -1),
            2
        );
        morphologyEx(
            paperMask,
            paperMask,
            MORPH_OPEN,
            paperKernel
        );

        Mat output = frame.clone();
        vector<Point> postItContour;
        array<Point2f, 4> postItCorners;

        bool postItFound = findPostIt(
            yellowMask,
            postItContour,
            postItCorners
        );
        bool paperFound = false;
        double postItAreaPx = 0.0;
        double paperAreaPx = 0.0;
        double areaRatio = 0.0;
        double paperAreaCm2 = 0.0;

        if (postItFound)
        {
            postItAreaPx = contourArea(postItContour);
            vector<Point> postItPolygon;
            postItPolygon.reserve(postItCorners.size());
            for (const Point2f &point : postItCorners)
            {
                postItPolygon.emplace_back(
                    cvRound(point.x),
                    cvRound(point.y)
                );
            }
            polylines(
                output,
                postItPolygon,
                true,
                Color::Yellow,
                3,
                LINE_AA
            );

            Point2f postItCenter(0.f, 0.f);
            for (const Point2f &point : postItCorners)
                postItCenter += point;
            postItCenter *= 0.25f;

            vector<Point> paperContour;
            vector<Point> paperPolygon;
            paperFound = findPaper(
                paperMask,
                postItCenter,
                postItAreaPx,
                paperContour,
                paperPolygon
            );

            if (paperFound)
            {
                paperAreaPx = contourArea(paperContour);
                drawContours(
                    output,
                    vector<vector<Point>>{paperContour},
                    0,
                    Color::Red,
                    2,
                    LINE_AA
                );
                polylines(
                    output,
                    paperPolygon,
                    true,
                    Color::Green,
                    3,
                    LINE_AA
                );

                const array<Point2f, 4> metricCorners = {
                    Point2f(0.f, 0.f),
                    Point2f(POST_IT_WIDTH_MM, 0.f),
                    Point2f(
                        POST_IT_WIDTH_MM,
                        POST_IT_HEIGHT_MM
                    ),
                    Point2f(0.f, POST_IT_HEIGHT_MM)
                };
                const Mat homography = getPerspectiveTransform(
                    postItCorners.data(),
                    metricCorners.data()
                );

                vector<Point2f> paperPoints;
                paperPoints.reserve(paperContour.size());
                for (const Point &point : paperContour)
                    paperPoints.emplace_back(
                        static_cast<float>(point.x),
                        static_cast<float>(point.y)
                    );

                vector<Point2f> metricPaperContour;
                perspectiveTransform(
                    paperPoints,
                    metricPaperContour,
                    homography
                );

                const double paperAreaMm2 =
                    abs(contourArea(metricPaperContour));
                const double postItAreaMm2 =
                    POST_IT_WIDTH_MM * POST_IT_HEIGHT_MM;

                paperAreaCm2 = paperAreaMm2 / 100.0;
                areaRatio = paperAreaMm2 / postItAreaMm2;
            }
        }

        drawTextLine(
            output,
            "Reference: 50 x 20 mm yellow Post-it",
            0
        );
        drawTextLine(
            output,
            "Yellow HSV: H " +
                to_string(yellowLowH) +
                "-" +
                to_string(yellowHighH) +
                " S>=" +
                to_string(settings.yellowLowS) +
                " V>=" +
                to_string(settings.yellowLowV),
            1
        );
        drawTextLine(
            output,
            "Paper HSV: S<=" +
                to_string(settings.paperMaxS) +
                " V>=" +
                to_string(settings.paperLowV),
            2
        );
        drawTextLine(
            output,
            "Post-it: " +
                string(postItFound ? "FOUND" : "NOT FOUND") +
                "  area(px): " +
                fixedNumber(postItAreaPx, 0),
            3,
            postItFound ? Color::Green : Color::Red
        );
        drawTextLine(
            output,
            "Paper: " +
                string(paperFound ? "FOUND" : "NOT FOUND") +
                "  area(px): " +
                fixedNumber(paperAreaPx, 0),
            4,
            paperFound ? Color::Green : Color::Red
        );
        drawTextLine(
            output,
            "Area ratio (paper / Post-it): " +
                fixedNumber(areaRatio, 2),
            5
        );
        drawTextLine(
            output,
            "Estimated paper area: " +
                fixedNumber(paperAreaCm2, 2) +
                " cm^2",
            6,
            Color::Yellow
        );
        drawTextLine(
            output,
            "ESC or q: quit",
            7,
            Color::White
        );

        imshow("controls", controlImage);
        imshow("frame", output);
        imshow("yellow mask", yellowMask);
        imshow("paper mask", paperMask);

        const int key = waitKey(30);
        if (key == 27 || key == 'q')
            break;
    }

    cap.release();
    destroyAllWindows();
    return 0;
}

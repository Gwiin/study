// 요구사항
// 마우스를 따라다니는 사각형 박스를 만드세요.
// 마우스 오른쪽 버튼을 누르면 사각형 박스의 색깔이 랜덤으로 변경되도록 하세요.
// 왼쪽 버튼을 누르고 움직이면 선(사각형 박스의 색깔과 같은) 선이 그어지도록 하세요.
// 휠 버튼을 누르면 (스포이드 기능) 마우스 위치의 픽셀 정보로 사각형 박스의 색깔을 변화 시키세요.

#include "colors.hpp"
#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

String folderPath = "/home/hrd_1_3/study/opencv/data/";

struct MouseData
{
    Mat canvas;
    Mat view;
    Point mousePosition;
    Point previousPosition;
    Scalar boxColor = Color::Red;
    bool leftButtonPressed = false;
};

void printColor(const String &source, const Scalar &color)
{
    cout << "[" << source << "] BGR: ("
         << cvRound(color[0]) << ", "
         << cvRound(color[1]) << ", "
         << cvRound(color[2]) << ")" << endl;
}

void updateView(MouseData &data)
{
    data.view = data.canvas.clone();

    const int halfBoxSize = 25;
    rectangle(data.view,
              Point(data.mousePosition.x - halfBoxSize,
                    data.mousePosition.y - halfBoxSize),
              Point(data.mousePosition.x + halfBoxSize,
                    data.mousePosition.y + halfBoxSize),
              data.boxColor, 2, LINE_AA);
}

void onMouse(int event, int x, int y, int, void *userData)
{
    MouseData &data = *static_cast<MouseData *>(userData);
    Point currentPosition(x, y);
    data.mousePosition = currentPosition;

    switch (event)
    {
    case EVENT_LBUTTONDOWN:
        data.leftButtonPressed = true;
        data.previousPosition = currentPosition;
        circle(data.canvas, currentPosition, 1,
               data.boxColor, FILLED, LINE_AA);
        break;

    case EVENT_LBUTTONUP:
        data.leftButtonPressed = false;
        break;

    case EVENT_MOUSEMOVE:
        if (data.leftButtonPressed)
        {
            line(data.canvas, data.previousPosition, currentPosition,
                 data.boxColor, 2, LINE_AA);
            data.previousPosition = currentPosition;
        }
        break;

    case EVENT_RBUTTONDOWN:
    {
        static RNG rng(getTickCount());
        data.boxColor = Scalar(rng.uniform(0, 256),
                               rng.uniform(0, 256),
                               rng.uniform(0, 256));
        printColor("랜덤 색상", data.boxColor);
        break;
    }

    case EVENT_MBUTTONDOWN:
        if (x >= 0 && x < data.canvas.cols &&
            y >= 0 && y < data.canvas.rows)
        {
            Vec3b pixel = data.canvas.at<Vec3b>(y, x);
            data.boxColor = Scalar(pixel[0], pixel[1], pixel[2]);
            printColor("스포이드", data.boxColor);
        }
        break;
    }

    updateView(data);
}

int main()
{
    MouseData data;
    data.canvas = imread(folderPath + "lenna.bmp");

    if (data.canvas.empty())
    {
        cerr << "이미지를 읽을 수 없습니다." << endl;
        return 1;
    }

    data.mousePosition = Point(data.canvas.cols / 2, data.canvas.rows / 2);
    updateView(data);

    namedWindow("img");
    setMouseCallback("img", onMouse, &data);

    while (true)
    {
        imshow("img", data.view);

        if (waitKey(30) == 27)
            break;
    }

    destroyAllWindows();
    return 0;
}

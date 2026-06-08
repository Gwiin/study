#include "colors.hpp"
#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

int main()
{
    string pipeline =
        "v4l2src device=/dev/video0 ! "
        "image/jpeg,width=640,height=480,framerate=30/1 ! "
        "jpegdec ! "
        "videoconvert ! "
        "appsink drop=true sync=false max-buffers=1";

    VideoCapture cap(pipeline, CAP_GSTREAMER);

    if (!cap.isOpened())
    {
        cerr << "카메라를 열 수 없습니다." << endl;
        return -1;
    }

    Mat frame;

    while (true)
    {
        cap >> frame;

        if (frame.empty())
        {
            cerr << "프레임을 읽을 수 없습니다." << endl;
            break;
        }

        imshow("frame", frame);

        if (waitKey(1) == 27)
            break;
    }

    cap.release();
    destroyAllWindows();

    return 0;
}
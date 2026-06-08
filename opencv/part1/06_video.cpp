#include "colors.hpp"
#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

String folderPath = "/home/aa/kuBig2026/opencv_ex/data/";

int main()
{
    VideoCapture cap(0);
    if (!cap.isOpened())
    {
        cerr << "카메라를 열수 없습니다." << endl;
    }

    //MJPG
    cap.set(CAP_PROP_FOURCC, VideoWriter::fourcc('M','J','P','G'));
    cap.set(CAP_PROP_FRAME_WIDTH, 640);
    cap.set(CAP_PROP_FRAME_HEIGHT, 480);
    cap.set(CAP_PROP_FPS, 30);


    Mat frame;
    for (int i = 0; i < 1000; ++i)
    {
        cap >> frame;
        if(waitKey(30) == 27)
            break;
        imshow("frame", frame);
    }
    cap.release();
    destroyAllWindows();
    return 0;
}
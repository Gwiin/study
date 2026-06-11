#include "colors.hpp"
#include <iostream>
#include <opencv2/opencv.hpp>
#include <vector>

using namespace std;
using namespace cv;

void blur_ex(Mat &img);




int main()
{
    const String folderPath = "/home/hrd_1_3/study/opencv/data/";

    VideoCapture cap(0, CAP_V4L2);

    if (!cap.isOpened())
    {
        cerr << "카메라를 열수 없습니다." << endl;
    }

    // MJPG
    cap.set(CAP_PROP_FOURCC, VideoWriter::fourcc('M', 'J', 'P', 'G'));
    cap.set(CAP_PROP_FRAME_WIDTH, 640);
    cap.set(CAP_PROP_FRAME_HEIGHT, 480);
    cap.set(CAP_PROP_FPS, 30);

    int pos = 1;
    namedWindow("frame");
    createTrackbar("alpha","frame", &pos, 30);

    Mat frame;
    Mat blurM, dst;
    for (int i = 0; i < 1000; ++i)
    {
        cap >> frame;
        if (waitKey(30) == 27)
            break;
        GaussianBlur(frame, blurM, Size(0,0), double(pos));
        dst = (1+(float)pos * 0.1) * frame - (float)pos * 0.1 * blurM;

        imshow("frame", dst);
    }
    cap.release();
    destroyAllWindows();
    return 0;
}



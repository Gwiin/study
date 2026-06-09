#include "colors.hpp"
#include <iostream>
#include <opencv2/freetype.hpp>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

String folderPath = "/home/hrd_1_3/study/opencv/data/";

int main()
{   
    Mat img = imread(folderPath + "lenna.bmp");
    namedWindow("img");
    auto start_tick = getTickCount();
    int fps = 45;
    int keycode;
    int needed_tick_ms;
    while(true)
    {
        start_tick = getTickCount();
        double elapsed_ms = (getTickCount() - start_tick)*1000.0/getTickFrequency();
        needed_tick_ms = cvRound(1000.0/fps-elapsed_ms);
        keycode = waitKey(needed_tick_ms);
        imshow("img", img);
        if(keycode == 27)
            break;
        if(keycode == 'v' || keycode == 'V' )
            img = ~img;
        if(keycode != -1){
            cout << "keycode: " << keycode << endl;
        }
        // cout << "fps: " << getTickFrequency() << endl;
        cout << "fps: " << getTickFrequency()/(getTickCount() - start_tick) << endl;
    }

    destroyAllWindows();
    return 0;
}
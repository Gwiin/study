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
    int fps = 10;
    TickMeter tm1;
    TickMeter tm2;
    int keycode;
    int needed_tick_ms;
    while(true)
    {
        tm1.start();
        tm2.start();
        imshow("img", img);
        tm1.stop();
        double elapsed_ms = tm1.getTimeMilli();
        needed_tick_ms = cvRound(1000.0/fps - elapsed_ms);
        keycode = waitKey(needed_tick_ms);

        if(keycode == 27)
            break;
        if(keycode == 'v' || keycode == 'V' )
            img = ~img;
        if(keycode != -1){
            cout << "keycode: " << keycode << endl;
        }
        // cout << "fps: " << getTickFrequency() << endl;
        cout << "fps: " << getTickFrequency()/(getTickCount() - start_tick) << endl;
        tm1.reset();
        tm2.reset();
    }

    destroyAllWindows();
    return 0;
}
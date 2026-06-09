#include "colors.hpp"
#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

String folderPath = "/home/hrd_1_3/study/opencv/data/";

int main()
{
    Mat img(400, 600, CV_8UC3, Color::White);

    int a = 0;

    while (true)
    {
        img.setTo(Color::White); // 배경 그리기
        putText(img, "SIMPLEX", Point(20 + a, 70),
                FONT_HERSHEY_SIMPLEX, 1.5, Color::Red, 2, LINE_AA);
        putText(img, "SIMPLEX ITALIC", Point(20 + a, 140),
                FONT_HERSHEY_SIMPLEX | FONT_ITALIC,
                1.5, Color::Red, 2, LINE_AA);
        putText(img, "DUPLEX", Point(20 + a, 210),
                FONT_HERSHEY_DUPLEX, 1.5, Color::Blue, 2, LINE_AA);
        putText(img, "PLAIN", Point(20 + a, 280),
                FONT_HERSHEY_PLAIN, 2.0, Color::Black, 2, LINE_AA);

        imshow("img", img);
        if (waitKey(33) == 27)
            break;

        a += 1;
        if (a > img.cols)
            a = -300;
    }

    destroyAllWindows();
    return 0;
}

#include "colors.hpp"
#include <iostream>
#include <opencv2/freetype.hpp>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

String folderPath = "/home/hrd_1_3/study/opencv/data/";

Ptr<cv::freetype::FreeType2> rapperFreeTypeCenterSetup(const String &fontpath)
{
    Ptr<cv::freetype::FreeType2> ft2 = freetype::createFreeType2();
    ft2->loadFontData(fontpath, 0);
    return ft2;
}

void rapperFreeTypeCenter(Mat &img, Ptr<cv::freetype::FreeType2> ft2, const String &text, const int &textHeight, const int &thickness, const int &line_type, const Scalar &color, const Point &textOrg, const bool &withRect)
{
    Size textSize = ft2->getTextSize(text, textHeight, -1, 0) + Size(0, 20);
    // bottom padding을 위해 높이 20 추가
    Point top_left((textOrg.x - textSize.width), (textOrg.y - textSize.height));
    Rect textRect(top_left, textSize);
    if (withRect)
    {
        rectangle(img, textRect, color, 3, line_type); // 텍스트 영역 사각형 그리기
    }

    ft2->putText(img, text, textRect.tl(), textHeight, color, thickness, line_type, false);
}

int main()
{
    Mat img(1000, 1200, CV_8UC3, Color::White);

    int a = 0, b = 0, c = 0;
    auto ft2 = rapperFreeTypeCenterSetup("/home/hrd_1_3/study/opencv/data/NanumPenScript-Regular.ttf");

    String text = "이것은 IOT 수업 입니다.";

    while (true)
    {
        img.setTo(Color::White);                         // 배경 그리기
        circle(img, Point(a, 300), 6, Color::Red, -1); // 빨간색 원 그리기
        rapperFreeTypeCenter(img, ft2, text, 100, 2, LINE_AA, Color::Blue, Point(a, 300), true);
        rapperFreeTypeCenter(img, ft2, "두번째 텍스트입니다.", 50, 2, LINE_AA, Color::Black, Point(b, 400), true);
        rapperFreeTypeCenter(img, ft2, "세번째 텍스트입니다.", 50, 2, LINE_AA, Color::Pink, Point(c, 200), false);

        imshow("img", img);
        if (waitKey(33) == 27)
            break;
        a += 1;
        b += 2;
        c += 3;
    }
    destroyAllWindows();
    return 0;
}
#include <opencv2/opencv.hpp>
#include <vector>

using namespace std;
using namespace cv;

int main()
{
    const String folderPath = "/home/hrd_1_3/study/opencv/data/";
    Mat img = imread(folderPath + "lenna.bmp", IMREAD_GRAYSCALE);
    vector<Mat> images;

    Mat dx, dy;
    Sobel(img, dx, CV_32FC1, 1, 0);
    Sobel(img, dy, CV_32FC1, 0, 1); // 사람 이름은 예외 대문자

    Mat magnitudeM, phaseM;
    magnitude(dx, dy, magnitudeM);
    phase(dx, dy, phaseM, true);

    dx.convertTo(dx, CV_8UC1);
    images.push_back(dx);
    dy.convertTo(dy, CV_8UC1);
    images.push_back(dy);
    magnitudeM.convertTo(magnitudeM, CV_8UC1);
    images.push_back(magnitudeM);
    phaseM.convertTo(phaseM, CV_8UC1);
    images.push_back(phaseM);
    Mat edge = magnitudeM > 150;
    images.push_back(edge);

    // vector img show 코드
    int i = 1;
    for (auto img : images)
    {
        imshow("img" + to_string(i), img);
        ++i;
    }

    waitKey();
    destroyAllWindows();
    return 0;
}
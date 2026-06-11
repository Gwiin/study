#include "colors.hpp"
#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

int main()
{
    const String folderPath = "/home/hrd_1_3/study/opencv/data/";
    Mat img = imread(folderPath + "candies.png");
    vector<Mat> bgr_planes;
    Mat b_planes, g_planes, r_planes;
    Mat empty(img.size(), CV_8UC1, Scalar(0));

    split(img, bgr_planes);
    merge(vector<Mat>({bgr_planes[0], empty, empty}), b_planes);
    merge(vector<Mat>({empty, bgr_planes[1], empty}), g_planes);
    merge(vector<Mat>({empty, empty, bgr_planes[2]}), r_planes);

    imshow("candies", img);
    imshow("b_plane", b_planes);
    imshow("g_plane", g_planes);
    imshow("r_plane", r_planes);
    waitKey();



    return 0;
}
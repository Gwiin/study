#include "colors.hpp"
#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

void on_level_change(int pose, void *data);

int main()
{
    const String folderPath = "/home/hrd_1_3/study/opencv/data/";
    String name;
    int age;
    Point pt1;
    vector<float> scores;
    Mat mat1;

    FileStorage fs;
    fs.open(folderPath + "mydata.yml", FileStorage::READ);
    fs["name"] >> name;
    fs["age"] >> age;
    fs["point"] >> pt1;
    fs["scores"] >> scores;
    fs["data"] >> mat1;

    cout << name << age << pt1 << Mat(scores).t() << mat1 << endl;

    fs.release();

    return 0;
}

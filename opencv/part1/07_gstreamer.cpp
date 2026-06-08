#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

int main()
{
    string info = getBuildInformation();

    size_t pos = info.find("GStreamer");

    if (pos != string::npos)
    {
        size_t lineEnd = info.find('\n', pos);
        string line = info.substr(pos, lineEnd - pos);

        cout << line << endl;

        if (line.find("YES") != string::npos)
        {
            cout << "OpenCV GStreamer 사용 가능" << endl;
        }
        else if (line.find("NO") != string::npos)
        {
            cout << "OpenCV GStreamer 사용 불가" << endl;
        }
        else
        {
            cout << "GStreamer 항목은 찾았지만 YES/NO 판단 불가" << endl;
        }
    }
    else
    {
        cout << "OpenCV build information에서 GStreamer 항목을 찾지 못했습니다." << endl;
    }

    return 0;
}
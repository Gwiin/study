#include <opencv2/opencv.hpp>
#include <array>
#include <cmath>
#include <iostream>

using namespace std;
using namespace cv;

void createVortexMap(
    const Size &size,
    float progress,
    Mat &mapX,
    Mat &mapY
)
{
    const Point2f center(
        static_cast<float>(size.width) / 2.f,
        static_cast<float>(size.height) / 2.f
    );
    const float maxRadius = hypot(center.x, center.y);
    const float scale = 1.f - 0.88f * progress;
    const float twist = progress * 7.f * static_cast<float>(CV_PI);

    mapX.create(size, CV_32FC1);
    mapY.create(size, CV_32FC1);

    for (int y = 0; y < size.height; ++y)
    {
        for (int x = 0; x < size.width; ++x)
        {
            const float dx = static_cast<float>(x) - center.x;
            const float dy = static_cast<float>(y) - center.y;
            const float radius = hypot(dx, dy);
            const float normalizedRadius = radius / maxRadius;

            // 중심에 가까울수록 더 많이 회전하고, 바깥쪽은 천천히 끌려간다.
            const float vortexWeight =
                pow(max(0.f, 1.f - normalizedRadius), 2.f);
            const float sourceAngle =
                atan2(dy, dx) - twist * vortexWeight;

            // 반지름을 일정하게 줄이지 않고 물결을 섞어 찌그러지게 만든다.
            const float ripple =
                1.f +
                0.18f *
                sin(normalizedRadius * 12.f - progress * 18.f) *
                vortexWeight *
                progress;
            const float sourceRadius = radius / scale * ripple;

            mapX.at<float>(y, x) =
                center.x + sourceRadius * cos(sourceAngle);
            mapY.at<float>(y, x) =
                center.y + sourceRadius * sin(sourceAngle);
        }
    }
}

int main()
{
    const String folderPath = "/home/hrd_1_3/study/opencv/data/";
    Mat img = imread(folderPath + "lenna.bmp");

    if (img.empty())
    {
        cerr << "이미지를 읽을 수 없습니다." << endl;
        return 1;
    }

    const float width = static_cast<float>(img.cols);
    const float height = static_cast<float>(img.rows);
    const array<Point2f, 4> srcPts = {
        Point2f(0.f, 0.f),
        Point2f(width - 1.f, 0.f),
        Point2f(width - 1.f, height - 1.f),
        Point2f(0.f, height - 1.f)
    };

    Mat vortex;
    Mat dst;
    Mat mapX;
    Mat mapY;
    int frameCount = 0;
    const int animationFrames = 240;

    namedWindow("dst");
    imshow("img", img);

    while (true)
    {
        const float progress =
            static_cast<float>(frameCount) / animationFrames;
        const float wave = sin(
            progress * 8.f * static_cast<float>(CV_PI)
        );

        createVortexMap(img.size(), progress, mapX, mapY);
        remap(
            img,
            vortex,
            mapX,
            mapY,
            INTER_LINEAR,
            BORDER_CONSTANT,
            Scalar::all(0)
        );

        // 네 모서리를 서로 다르게 움직여 사다리꼴 형태의 왜곡도 추가한다.
        const float bend = 35.f * progress;
        const array<Point2f, 4> dstPts = {
            Point2f(bend * (1.f + wave), bend * 0.3f),
            Point2f(width - 1.f - bend * 0.2f, bend * (1.f - wave)),
            Point2f(
                width - 1.f - bend * (1.f + wave * 0.5f),
                height - 1.f - bend * 0.2f
            ),
            Point2f(
                bend * 0.4f,
                height - 1.f - bend * (1.f - wave * 0.5f)
            )
        };

        Mat perspective = getPerspectiveTransform(
            srcPts.data(),
            dstPts.data()
        );

        warpPerspective(
            vortex,
            dst,
            perspective,
            img.size(),
            INTER_LINEAR,
            BORDER_CONSTANT,
            Scalar::all(0)
        );

        imshow("dst", dst);

        const int key = waitKey(16);
        if (key == 27 || key == 'q')
            break;

        ++frameCount;

        if (frameCount > animationFrames)
            frameCount = 0;
    }

    destroyAllWindows();
    return 0;
}

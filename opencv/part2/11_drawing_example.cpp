// 학습정리에 사용하지 말것.

#include "colors.hpp"
#include <algorithm>
#include <cmath>
#include <opencv2/opencv.hpp>

using namespace cv;

void drawFighter(Mat &img, Point body, bool faceRight, const Scalar &color,
                 double attack, int walk)
{
    int direction = faceRight ? 1 : -1;
    Point head(body.x, body.y - 90);
    Point shoulder(body.x, body.y - 55);
    Point swordHand(body.x + direction * (25 + attack * 20),
                    body.y - 45 - static_cast<int>(attack * 25));
    Point swordTip(swordHand.x + direction * 70,
                   swordHand.y - static_cast<int>(attack * 45));

    // Head, body, arms
    circle(img, head, 22, color, 3, LINE_AA);
    line(img, Point(head.x + direction * 8, head.y - 2),
         Point(head.x + direction * 13, head.y - 2), Color::White, 3, LINE_AA);
    line(img, Point(body.x, body.y - 68), body, color, 5, LINE_AA);
    line(img, shoulder, swordHand, color, 5, LINE_AA);
    line(img, shoulder, Point(body.x - direction * 28, body.y - 25),
         color, 5, LINE_AA);

    // Walking legs
    line(img, body, Point(body.x - 25 + walk, body.y + 65),
         color, 5, LINE_AA);
    line(img, body, Point(body.x + 25 - walk, body.y + 65),
         color, 5, LINE_AA);

    // Sword glow and blade
    line(img, swordHand, swordTip, Color::White, 9, LINE_AA);
    line(img, swordHand, swordTip,
         faceRight ? Color::Cyan : Color::Red, 4, LINE_AA);
    line(img, Point(swordHand.x - direction * 8, swordHand.y - 10),
         Point(swordHand.x + direction * 8, swordHand.y + 10),
         Color::Yellow, 5, LINE_AA);

    if (attack > 0.15)
    {
        int startAngle = faceRight ? 210 : 30;
        int endAngle = startAngle + static_cast<int>(attack * 100);
        ellipse(img, shoulder, Size(95, 95), 0, startAngle, endAngle,
                faceRight ? Color::Cyan : Color::Orange, 3, LINE_AA);
    }
}

void drawImpact(Mat &img, Point center, int power)
{
    circle(img, center, 12 + power * 3, Color::White, 3, LINE_AA);
    circle(img, center, 25 + power * 5, Color::Yellow, 3, LINE_AA);

    for (int i = 0; i < 16; ++i)
    {
        double angle = i * CV_PI / 8.0;
        int inner = 15 + (i % 3) * 5;
        int outer = 45 + power * 8 + (i % 4) * 7;

        Point p1(center.x + static_cast<int>(cos(angle) * inner),
                 center.y + static_cast<int>(sin(angle) * inner));
        Point p2(center.x + static_cast<int>(cos(angle) * outer),
                 center.y + static_cast<int>(sin(angle) * outer));

        line(img, p1, p2, i % 2 == 0 ? Color::Yellow : Color::Orange,
             2 + i % 3, LINE_AA);
        circle(img, p2, 2 + i % 4, Color::White, FILLED, LINE_AA);
    }
}

int main()
{
    Mat background(400, 600, CV_8UC3, Scalar(25, 15, 10));

    // Night battlefield
    circle(background, Point(500, 70), 38, Scalar(210, 220, 230), FILLED, LINE_AA);
    circle(background, Point(485, 60), 38, Scalar(25, 15, 10), FILLED, LINE_AA);
    rectangle(background, Rect(0, 315, 600, 85), Scalar(35, 35, 35), FILLED);
    line(background, Point(0, 315), Point(600, 315), Color::Gray, 2, LINE_AA);

    for (int x = 20; x < 600; x += 55)
    {
        drawMarker(background, Point(x, 40 + (x % 70)),
                   Color::White, MARKER_STAR, 4, 1, LINE_AA);
    }

    while (true)
    {
        for (int frame = 0; frame < 180; ++frame)
        {
            Mat img = background.clone();

            int approach = std::min(frame, 70);
            int retreat = std::max(0, frame - 125);
            int leftX = 80 + approach * 2 - retreat * 2;
            int rightX = 520 - approach * 2 + retreat * 2;

            double attack = 0.0;
            if (frame >= 65 && frame < 95)
                attack = (frame - 65) / 30.0;
            else if (frame >= 95 && frame < 125)
                attack = (125 - frame) / 30.0;

            int walk = static_cast<int>(12 * sin(frame * 0.35));
            bool collision = frame >= 91 && frame <= 103;

            // Small camera shake at the sword collision.
            if (collision)
            {
                int shake = frame % 2 == 0 ? 4 : -4;
                leftX += shake;
                rightX += shake;
            }

            drawFighter(img, Point(leftX, 245), true, Color::Cyan, attack, walk);
            drawFighter(img, Point(rightX, 245), false, Color::Orange,
                        attack, -walk);

            if (collision)
            {
                int power = 6 - std::abs(97 - frame);
                drawImpact(img, Point(300, 150), std::max(1, power));
            }

            putText(img, "STICK FIGHT", Point(18, 35),
                    FONT_HERSHEY_DUPLEX, 0.8, Color::White, 2, LINE_AA);
            putText(img, "ESC : EXIT", Point(465, 385),
                    FONT_HERSHEY_SIMPLEX, 0.45, Color::Gray, 1, LINE_AA);

            imshow("Stickman Battle", img);

            if (waitKey(1000 / 30) == 27)
            {
                destroyAllWindows();
                return 0;
            }
        }
    }
}

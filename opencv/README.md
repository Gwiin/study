# OPENCV 학습노트

## OpenCV를 배우는 이유

OpenCV는 영상 처리와 컴퓨터 비전에서 많이 쓰는 library이다.<br>
Python에서는 `cv2` 모듈로 사용하지만, OpenCV의 핵심 구현은 C/C++ 기반이다.

그래서 Python으로 실습하더라도 내부 자료형이나 함수 이름이 C++ 스타일과 연결되는 경우가 많다.<br>
C++ 예제를 같이 보면 구조를 이해하는 데 도움이 된다.

정리:
- Python에서는 `import cv2`로 사용
- 내부적으로 C/C++ 기반 기능을 Python에서 호출하는 느낌
- 영상처리는 배열, 좌표, 픽셀값을 다루는 과목이다

## 저수준 영상처리와 고수준 영상처리

저수준 영상처리
- 입력도 영상이고, 결과도 보통 영상이다
- 예: 밝기 조절, blur, edge 검출, 이진화, 색 변환

고수준 영상처리
- 영상에서 의미 있는 정보나 특징을 뽑는 쪽이다
- 결과가 꼭 영상일 필요는 없다
- 예: 객체 검출, 얼굴 인식, 문자 인식, 특징점 추출

정리:
- 저수준 -> 이미지를 바꿔서 다시 이미지로 보는 경우가 많다
- 고수준 -> 이미지 안에서 의미나 판단 결과를 얻는 경우가 많다

## 영상 획득 과정

```text
빛 -> 렌즈 -> 이미지 센서 -> ADC -> ISP -> 사진 파일
```

- 빛이 렌즈를 통과해서 이미지 센서에 도달
- 이미지 센서가 빛의 세기를 전기 신호로 바꿈
- ADC가 아날로그 신호를 디지털 값으로 바꿈
- ISP가 색 보정, 노이즈 제거 같은 처리를 함
- 최종적으로 JPG, PNG 같은 파일로 저장될 수 있음

용어:
- ADC -> Analog Digital Converter
- ISP -> Image Signal Processor

정리:
- 카메라가 바로 이미지 파일을 만드는 것이 아니라 여러 단계가 있다
- OpenCV에서는 보통 이미 만들어진 이미지 파일이나 카메라 frame을 배열로 받아서 처리한다

## 영상과 픽셀

영상은 위치값과 밝기값을 가진 화소(pixel)들의 모임으로 볼 수 있다.

```text
grayscale image -> 2차원 배열
color image     -> 3차원 배열처럼 볼 수 있음
```

Python OpenCV에서 이미지는 보통 `numpy.ndarray`로 다룬다.

예:
```python
img = cv2.imread("test.png")
print(type(img))
print(img.shape)
print(img.dtype)
```

확인할 값:
- `type(img)` -> 보통 `numpy.ndarray`
- `img.shape` -> 이미지 크기와 channel 수
- `img.dtype` -> 픽셀값 자료형

주의할 점:
- 이미지 파일을 읽지 못하면 `cv2.imread()`는 예외를 바로 내기보다 `None`을 반환할 수 있다
- 그래서 실습에서는 `img is None` 확인이 필요하다

## 샘플링과 양자화

샘플링
- 연속적인 실제 장면을 일정한 간격의 pixel로 나누는 과정
- 해상도와 관련이 있다
- 예: 640 x 480, 1920 x 1080

양자화
- 밝기나 색 값을 제한된 bit 수의 정수로 표현하는 과정
- 보통 8bit 영상이면 한 channel 값이 `0 ~ 255`

정리:
- 샘플링 -> 공간을 몇 개의 pixel로 나눌 것인가
- 양자화 -> 각 pixel 값을 몇 단계 숫자로 표현할 것인가

## 그레이스케일 영상

그레이스케일 영상은 보통 한 pixel이 밝기값 하나만 가진다.

```text
0   -> 검정
255 -> 흰색
중간값 -> 회색
```

C/C++ 쪽에서는 8bit unsigned 정수로 많이 표현한다.

```c
typedef unsigned char uint8_t;
```

OpenCV에서 8bit 1채널 영상은 `CV_8UC1` 같은 형태로 표현한다.<br>
Python에서는 보통 `dtype=uint8`, `shape=(height, width)` 형태로 확인한다.

정리:
- grayscale은 channel 1개
- 8bit면 값 범위는 보통 0~255
- `uint8_t`는 8bit unsigned char 타입 이름으로 볼 수 있다

## 컬러 영상

일반적으로 컬러 이미지는 RGB 세 개의 색 성분으로 설명하는 경우가 많다.

```text
RGB -> Red, Green, Blue
```

하지만 OpenCV에서 `cv2.imread()`로 읽은 컬러 이미지는 기본적으로 BGR 순서이다.

```text
OpenCV 기본 순서: B, G, R
일반적인 설명 순서: R, G, B
```

그래서 OpenCV 이미지를 matplotlib 같은 다른 library로 보여줄 때 색이 이상하게 보일 수 있다.

```python
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
```

정리:
- 컬러 pixel은 보통 channel 3개
- OpenCV는 기본 BGR 순서를 많이 사용
- RGB가 필요한 library로 넘길 때는 색 공간 변환을 확인해야 한다

## 영상 파일 형식

이미지 파일 형식은 저장 방식과 압축 방식이 다르다.<br>
OpenCV에서는 `cv2.imread()`, `cv2.imwrite()`로 여러 이미지 형식을 읽고 쓸 수 있다.

### BMP

비트맵 이미지 파일 형식이다.

- 보통 압축하지 않거나 단순한 방식이라 용량이 큰 편
- 압축 손실이 거의 없는 형태로 저장할 수 있음
- 알파 채널을 지원할 수 있지만, 실제 지원 여부는 저장 방식과 reader/writer에 따라 확인 필요

### JPG / JPEG

사진 저장에 많이 쓰는 손실 압축 형식이다.

- 파일 크기를 많이 줄일 수 있음
- 대신 압축 과정에서 품질 저하가 생길 수 있음
- 반복 저장하면 화질이 더 나빠질 수 있음

주의:
- "1%보다도 더 적게 압축"처럼 고정된 비율로 외우기보다는 품질 설정에 따라 용량과 화질이 달라진다고 보는 것이 좋다

### GIF

색상 수가 제한된 이미지 형식이다.

- 보통 256색 기반으로 설명함
- 애니메이션 이미지에 많이 사용
- 사진처럼 색이 많은 이미지에는 잘 맞지 않을 수 있음

주의:
- OpenCV 버전과 build 옵션에 따라 GIF 읽기/쓰기 지원이 다를 수 있다
- 학습 초반에는 JPG, PNG, BMP를 먼저 확인하는 것이 편하다

### PNG

무손실 압축 이미지 형식이다.

- 원본 품질을 유지하는 데 좋음
- 투명도(alpha channel)를 저장할 수 있음
- 아이콘, 캡처 이미지, 그래픽 이미지에 자주 사용
- 압축률을 조절할 수 있지만 압축률을 높이면 저장 시간이 더 걸릴 수 있음

정리:
- BMP -> 단순하지만 용량 큼
- JPG -> 손실 압축, 사진에 많이 사용
- GIF -> 256색/애니메이션 이미지에 자주 사용
- PNG -> 무손실 압축, 투명도 가능


## Install(linux)
- sudo apt update
- sudo apt upgrade
- sudo apt install libopencv-dev python3-opencv
- pip install opencv-python

or
- uv add opencv-python (윈도우일때, 권장하지 않음)


pkg-config --modversion opencv4 (버전 확인, 실습당시 4.5.4)

gstreamer패키지
sudo apt install -y \
  gstreamer1.0-tools \
  gstreamer1.0-plugins-base \
  gstreamer1.0-plugins-good \
  gstreamer1.0-plugins-bad \
  gstreamer1.0-plugins-ugly \
  gstreamer1.0-libav

설치확인
pkg-config --modversion opencv4
pkg-config --cflags --libs opencv4

[참고](https://carpal-polonium-c12.notion.site/1-C-OpenCV-375541956f7a81fab32fd726e323eb7b)


---

## C++ OpenCV 실습 구조

현재 실습 파일은 아래처럼 구성했다.

```text
opencv/
├── CMakeLists.txt
├── data/
│   └── view-adorable-kitten.jpg
└── part1/
    ├── 01_helloWorld.cpp
    └── 02_basicOp.cpp
```

- `data/` -> 실습에 사용할 이미지
- `part1/` -> C++ OpenCV 기본 실습 코드
- `CMakeLists.txt` -> 실행 파일 target과 OpenCV library 연결

## CMake로 OpenCV 코드 빌드

```cmake
cmake_minimum_required(VERSION 3.16)
project(opencv_cpp_basic)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(OpenCV REQUIRED)
```

- CMake 최소 버전은 3.16
- C++17 표준을 사용
- `find_package(OpenCV REQUIRED)`로 설치된 OpenCV를 찾음
- OpenCV를 찾지 못하면 configure 단계에서 중단됨

실행 파일마다 target을 따로 만든다.

```cmake
add_executable(01_helloWorld part1/01_helloWorld.cpp)
target_link_libraries(01_helloWorld PRIVATE ${OpenCV_LIBS})

add_executable(02_basicOp part1/02_basicOp.cpp)
target_link_libraries(02_basicOp PRIVATE ${OpenCV_LIBS})
```

- `add_executable()` -> source code로 실행 파일 target 생성
- `target_link_libraries()` -> 해당 target에 OpenCV library 연결
- 두 명령어의 target 이름이 같아야 함

빌드:
```bash
cmake -S opencv -B opencv/build
cmake --build opencv/build --target 01_helloWorld
cmake --build opencv/build --target 02_basicOp
```

실행:
```bash
./opencv/build/01_helloWorld
./opencv/build/02_basicOp
```

주의할 점:
- 저장소 root의 `build/`와 `opencv/build/`는 서로 다른 build directory이다
- OpenCV 실습은 `opencv/CMakeLists.txt`를 source로 사용해야 함
- source를 수정한 뒤에는 실행 파일을 다시 build해야 변경 내용이 반영됨

## 이미지 읽기와 화면 출력

`01_helloWorld.cpp`

```cpp
#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

String folderPath = "/home/hrd_1_3/study/opencv/data/";
```

`opencv2/opencv.hpp`를 include하면 OpenCV의 여러 기능을 한 번에 사용할 수 있다.<br>
`cv::String`은 OpenCV에서 사용하는 문자열 type이고 일반적인 경로 처리에는 `std::string`도 사용할 수 있다.

```cpp
Mat img = imread(folderPath + "view-adorable-kitten.jpg");
```

`imread()`가 이미지 파일을 읽어서 `Mat` 객체로 반환한다.

- 기본 option은 컬러 이미지
- 컬러 channel 순서는 보통 BGR
- 파일을 읽지 못하면 비어 있는 `Mat`이 반환됨

이미지를 사용하기 전에 아래처럼 확인하는 것이 안전하다.

```cpp
if (img.empty())
{
    cerr << "이미지를 읽을 수 없음" << endl;
    return 1;
}
```

## 이미지 크기 변경

```cpp
Size size(640, 480);
resize(img, img, size);
```

`Size`는 너비와 높이를 저장하는 OpenCV type이다.

```text
Size(width, height)
Size(640, 480)
```

`resize()`의 첫 번째 `img`는 원본이고 두 번째 `img`는 결과가 저장될 객체이다.<br>
같은 변수를 입력과 출력에 사용해서 기존 이미지를 변경할 수 있다.

주의할 점:
- 원본 이미지 비율과 `640 x 480` 비율이 다르면 이미지가 늘어나거나 눌릴 수 있음
- 비율을 유지하려면 원본 width, height를 기준으로 새 크기를 계산해야 함

## imshow와 waitKey

```cpp
imshow("lenna", img);
waitKey();
```

- `imshow()` -> 이미지를 GUI 창에 표시
- 첫 번째 argument -> 창 이름
- 두 번째 argument -> 표시할 `Mat`
- `waitKey()` -> 키 입력을 기다리면서 GUI event를 처리

`waitKey()`를 사용하지 않으면 창이 바로 닫히거나 화면이 제대로 그려지지 않을 수 있다.

```cpp
waitKey(0);
```

`0`을 주면 키가 입력될 때까지 계속 기다린다.<br>
현재 코드의 `waitKey()`도 기본 argument가 0이므로 같은 방식으로 동작한다.

정리:
- 터미널의 `cout` 출력과 OpenCV 이미지 창은 서로 다른 결과
- `cout << "hello, world"`가 남아 있으면 이미지를 바꿔도 터미널에는 같은 문장이 나옴
- 이미지를 바꾼 뒤에는 다시 build하고 새 실행 파일을 실행해야 함

## Mat으로 검은 영상 만들기

```cpp
Mat img = Mat::zeros(480, 640, CV_8UC3);
```

모든 pixel 값이 0인 `Mat`을 만든다.

- `480` -> 행 개수, 영상의 height
- `640` -> 열 개수, 영상의 width
- `CV_8U` -> 8bit unsigned 자료형
- `C3` -> channel 3개

모든 BGR channel 값이 0이므로 검은색 영상이 된다.

```text
Mat::zeros(rows, cols, type)
Mat::zeros(height, width, type)
```

`Size`를 사용할 수도 있다.

```cpp
Mat img = Mat::zeros(Size(100, 100), CV_8UC3);
```

주의:
- `Mat::zeros(rows, cols, ...)`는 height, width 순서
- `Size(width, height)`는 width, height 순서
- 순서가 서로 달라서 헷갈릴 수 있음

## Point

`Point`는 영상 안의 2차원 좌표를 표현할 때 사용한다.

```cpp
Point_<int> p1(1, 3);
Point_<float> p2(3.14f, 4.31f);
Point_<int> p3(5, 8);
```

`Point_`는 자료형을 지정할 수 있는 template이다.

```text
Point_<int>   -> 정수 좌표
Point_<float> -> 실수 좌표
```

OpenCV에는 자주 사용하는 type alias가 있다.

```cpp
Point p4(1, 2);
Point2i p5(3, 4);
Point2f p6(3.11f, 2.11f);
```

- `Point`, `Point2i` -> `Point_<int>`
- `Point2f` -> `Point_<float>`
- `Point2d` -> `Point_<double>`

`Point_<int>`를 직접 사용하는 것도 가능하지만 `Point`, `Point2f`처럼 alias를 사용하면 좌표 type을 읽기 쉽다.

좌표끼리 덧셈도 가능하다.

```cpp
cout << p1 + p3 << endl;
```

출력:
```text
[6, 11]
```

## Size

`Size`는 사각형이나 영상의 너비와 높이를 표현한다.

```cpp
Size sz1;
Size2i sz2(10, 20);

sz1.width = 10;
sz1.height = 20;
```

`width`, `height`는 public member라서 직접 접근할 수 있다.

```cpp
cout << sz1.area() << endl;
cout << sz1.aspectRatio() << endl;
```

현재 값:
```text
width  = 10
height = 20
area() = 200
aspectRatio() = 0.5
```

- `area()` -> `width * height`
- `aspectRatio()` -> `width / height`

주의:
- 출력 문장 사이에 공백이나 구분 문자를 넣지 않으면 결과가 붙어서 보임

```cpp
cout << "area: " << sz1.area()
     << ", aspect ratio: " << sz1.aspectRatio()
     << endl;
```

## Rect

`Rect`는 사각형 영역을 표현한다.

```cpp
Rect rc2(10, 10, 20, 20);
```

```text
Rect(x, y, width, height)
```

- `x`, `y` -> 왼쪽 위 좌표
- `width`, `height` -> 사각형 크기

`Size`를 더하면 사각형의 크기가 바뀐다.

```cpp
Rect rc1;
Rect rc3 = rc1 + Size(50, 40);
```

결과:
```text
[50 x 40 from (0, 0)]
```

`Point`를 더하면 사각형의 위치가 이동한다.

```cpp
Rect rc4 = rc2 + Point(10, 10);
```

결과:
```text
[20 x 20 from (20, 20)]
```

사각형의 교집합과 합집합 영역도 구할 수 있다.

```cpp
Rect rc5 = rc3 & rc4;
Rect rc6 = rc3 | rc4;
```

- `&` -> 두 사각형이 겹치는 교집합 영역
- `|` -> 두 사각형을 모두 포함하는 최소 bounding rectangle

현재 실행 결과:
```text
rc3: [50 x 40 from (0, 0)]
rc4: [20 x 20 from (20, 20)]
rc5: [20 x 20 from (20, 20)]
rc6: [50 x 40 from (0, 0)]
```

점이 사각형 안에 있는지 확인할 수 있다.

```cpp
cout << rc6.contains(p1);
```

현재 `p1`은 `(1, 3)`이고 `rc6` 안에 있으므로 `1`이 출력된다.

주의:
- `contains()`는 왼쪽/위쪽 경계는 포함하고 오른쪽/아래쪽 끝 경계는 포함하지 않는 방식으로 판단함

## rectangle로 사각형 그리기

```cpp
Mat img = Mat::zeros(Size(100, 100), CV_8UC3);
rectangle(img, rc3, Scalar(255, 255, 255));
```

`rectangle()`은 `Mat` 위에 사각형을 그린다.

```text
rectangle(image, rect, color)
```

OpenCV의 컬러 순서는 BGR이다.

```cpp
Scalar(255, 255, 255) // 흰색
Scalar(255, 0, 0)     // 파란색
Scalar(0, 255, 0)     // 초록색
Scalar(0, 0, 255)     // 빨간색
```

현재 코드에는 아래처럼 작성된 부분이 있다.

```cpp
rectangle(img, rc3, (255, 255, 255));
```

C++에서 `(255, 255, 255)`는 색상 tuple이 아니다.<br>
comma operator에 의해 마지막 값 하나만 남기 때문에 원하는 BGR 색을 정확하게 전달하려면 `Scalar`를 사용해야 한다.

```cpp
rectangle(img, rc3, Scalar(255, 255, 255));
rectangle(img, rc4, Scalar(255, 255, 255));
rectangle(img, rc5, Scalar(255, 0, 0));
rectangle(img, rc6, Scalar(0, 255, 255));
```

주의할 점:
- 뒤에 그린 큰 사각형이 앞에서 그린 선을 덮을 수 있음
- 기본 thickness는 1
- 내부를 채우려면 thickness에 `FILLED`를 사용할 수 있음

```cpp
rectangle(img, rc5, Scalar(255, 0, 0), FILLED);
```

정리:
- `Point` -> 위치, 좌표
- `Size` -> 너비와 높이
- `Rect` -> 위치와 크기를 가진 사각형 영역
- `Mat` -> 영상 데이터를 저장하는 기본 객체
- 색상은 `(B, G, R)`처럼 보이더라도 C++에서는 `Scalar(B, G, R)`로 전달해야 함

## Mat 기본 생성

`03_matOp.cpp`에서는 `Mat`을 여러 방식으로 생성해보았다.

```cpp
Mat img;
Mat img2(100, 200, CV_8UC1);
Mat img3(100, 200, CV_8UC3, Scalar(0, 0, 255));
Mat img4(Size(600, 600), CV_8UC3);
```

`Mat img;`
- 비어 있는 `Mat`
- 아직 실제 pixel data를 가지고 있지 않음

`Mat img2(100, 200, CV_8UC1);`
- height 100, width 200 영상
- `CV_8UC1` -> 8bit unsigned, channel 1개
- grayscale 영상처럼 볼 수 있음

`Mat img3(100, 200, CV_8UC3, Scalar(0, 0, 255));`
- height 100, width 200 영상
- `CV_8UC3` -> 8bit unsigned, channel 3개
- `Scalar(0, 0, 255)`로 초기화
- OpenCV는 BGR 순서라서 빨간색이다

`Mat img4(Size(600, 600), CV_8UC3);`
- `Size(width, height)`를 사용해서 생성
- 이 경우에는 600 x 600 크기

주의:
- `Mat(rows, cols, type)`은 `height, width` 순서
- `Mat(Size(width, height), type)`은 `width, height` 순서
- 같은 크기라도 생성자 모양에 따라 순서가 다르게 보일 수 있음

정리:
- `Mat`은 OpenCV에서 영상 데이터를 담는 기본 type
- type 이름에서 깊이와 channel 수를 같이 확인한다
- `CV_8UC1`, `CV_8UC3`, `CV_32FC1` 같은 표현을 자주 본다

## Mat type 읽기

```text
CV_8UC1
CV_8UC3
CV_32FC1
```

대략 이렇게 나눠서 보면 된다.

```text
CV_8U   -> 8bit unsigned integer
CV_32F  -> 32bit float
C1      -> channel 1개
C3      -> channel 3개
```

예:
- `CV_8UC1` -> 8bit unsigned, 1 channel
- `CV_8UC3` -> 8bit unsigned, 3 channel
- `CV_32FC1` -> 32bit float, 1 channel

정리:
- grayscale image는 보통 `CV_8UC1`
- color image는 보통 `CV_8UC3`
- 실수 계산용 행렬은 `CV_32FC1` 같은 type을 사용할 수 있음

## 외부 배열로 Mat 만들기

```cpp
float data[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
Mat mat5(2, 5, CV_32FC1, data);
```

외부에 이미 있는 배열을 `Mat`이 사용하게 만들 수 있다.

```text
Mat(rows, cols, type, data_pointer)
```

현재 코드는 `float` 값 10개를 2행 5열 행렬로 본다.

실행 결과:
```text
mat5 : [1, 2, 3, 4, 5;
 6, 7, 8, 9, 10]
```

확인한 점:
- `Mat` 출력에서 `;`는 행이 바뀌는 느낌이다
- 1~5는 첫 번째 row
- 6~10은 두 번째 row

주의:
- 이 방식은 `Mat`이 data를 복사해서 새로 소유하는 것이 아니라 외부 메모리를 참조하는 방식으로 볼 수 있다
- 원본 배열의 lifetime이 `Mat`보다 짧으면 문제가 생길 수 있음
- 지역 배열은 함수가 끝나면 사라지므로 함수 밖에서 오래 쓰면 위험할 수 있다

## 동적 할당 배열과 Mat

```cpp
float *data2 = new float[10];

vector<float> data3(10);
int i = 0;
for (auto x : data3)
{
    data2[i++] = 100;
}

Mat mat6(2, 5, CV_32FC1, data2);
```

`new float[10]`으로 float 10개를 동적 할당했다.<br>
그 다음 모든 값을 `100`으로 넣고, 이 메모리를 `Mat`에 연결했다.

실행 결과:
```text
mat6 : [100, 100, 100, 100, 100;
 100, 100, 100, 100, 100]
```

주의할 점:
- `new[]`로 만든 메모리는 직접 `delete[]` 해야 함
- `Mat`이 외부 포인터로 받은 메모리를 자동으로 해제해주지 않는다고 생각하는 것이 안전하다

```cpp
delete[] data2;
```

현재 코드의 반복문:
```cpp
for (auto x : data3)
{
    data2[i++] = 100;
}
```

`x` 값 자체는 사용하지 않고, `data3`의 길이만큼 반복하기 위해 사용하고 있다.<br>
학습용으로는 동작하지만, 실제로는 아래처럼 쓰는 편이 더 직접적이다.

```cpp
for (int i = 0; i < 10; i++)
{
    data2[i] = 100.0f;
}
```

또는 `vector`를 쓸 거면 처음부터 `vector`의 data를 사용하는 방식도 가능하다.

```cpp
vector<float> data2(10, 100.0f);
Mat mat6(2, 5, CV_32FC1, data2.data());
```

주의:
- `vector`를 이용해도 `Mat`이 그 메모리를 참조하고 있으면 `vector`가 살아 있어야 한다
- `Mat`만 남기고 `vector`가 먼저 사라지면 위험할 수 있음

## std::span 에러

처음에 아래처럼 작성하면 에러가 날 수 있다.

```cpp
#include <span>

for (auto x : span<float>(data, 10))
{
    x = 100;
}
```

에러:
```text
‘span’ was not declared in this scope
```

이유:
- `std::span`은 C++20 기능이다
- 현재 CMake는 C++17로 설정되어 있다

```cmake
set(CMAKE_CXX_STANDARD 17)
```

그래서 GCC가 `<span>` header를 제대로 사용할 수 없는 상황이 된다.

해결 방법 1: C++17 방식으로 작성
```cpp
for (int i = 0; i < 10; i++)
{
    data2[i] = 100.0f;
}
```

해결 방법 2: CMake를 C++20으로 변경
```cmake
set(CMAKE_CXX_STANDARD 20)
```

정리:
- 수업 초반에는 C++17 기준 일반 `for`문으로 쓰는 것이 덜 헷갈림
- `span`을 쓰려면 C++20 설정이 필요하다
- 표준 library 기능은 CMake의 C++ 표준 설정과 같이 봐야 함

## colors.hpp로 색상 이름 정리

`colors.hpp` 파일을 만들어 자주 쓰는 색을 이름으로 정리했다.

```cpp
#pragma once
#include <opencv2/opencv.hpp>

namespace Color {
    inline const cv::Scalar Black{0, 0, 0};
    inline const cv::Scalar White{255, 255, 255};

    inline const cv::Scalar Red{0, 0, 255};
    inline const cv::Scalar Green{0, 255, 0};
    inline const cv::Scalar Blue{255, 0, 0};
}
```

OpenCV 색상은 BGR 순서이다.

```cpp
Color::Red   // Scalar{0, 0, 255}
Color::Green // Scalar{0, 255, 0}
Color::Blue  // Scalar{255, 0, 0}
```

`inline const`를 사용하면 header에 상수를 정의해도 여러 cpp 파일에서 include할 때 중복 정의 문제가 줄어든다.

사용 예:
```cpp
rectangle(img, rc, Color::Red);
```

정리:
- 숫자로 `Scalar(0, 0, 255)`를 계속 쓰면 색을 헷갈리기 쉽다
- `Color::Red`처럼 이름으로 쓰면 읽기 좋다
- 그래도 내부 값은 RGB가 아니라 BGR 순서임을 기억해야 한다

## 03_matOp 빌드와 실행

CMake에 `03_matOp` target을 추가했다.

```cmake
add_executable(03_matOp part1/03_matOp.cpp)
target_link_libraries(03_matOp PRIVATE ${OpenCV_LIBS})
```

빌드:
```bash
cmake --build opencv/build --target 03_matOp
```

실행:
```bash
./opencv/build/03_matOp
```

실행 결과:
```text
mat5 : [1, 2, 3, 4, 5;
 6, 7, 8, 9, 10]
mat6 : [100, 100, 100, 100, 100;
 100, 100, 100, 100, 100]
```

정리:
- `Mat`은 이미지뿐 아니라 일반 행렬처럼 사용할 수도 있다
- 외부 메모리를 연결할 수 있지만 메모리 lifetime을 조심해야 한다
- `new[]`를 사용하면 `delete[]`까지 직접 책임져야 한다

## smart pointer와 vector를 이용한 외부 메모리

`03_matOp.cpp`의 동적 할당 부분을 `unique_ptr`과 `vector`를 사용하는 형태로 바꿨다.

```cpp
auto data2 = make_unique<vector<float>>(10);
```

- `make_unique` -> 객체를 동적 생성하고 `unique_ptr`로 관리
- `vector<float>(10)` -> float 원소 10개 생성
- float 원소들은 기본적으로 `0.0f`로 초기화됨
- `unique_ptr`가 scope를 벗어나면 vector도 자동으로 해제됨

기존 `new[]`, `delete[]` 방식과 비교:

```cpp
float* data2 = new float[10];
delete[] data2;
```

`unique_ptr`를 사용하면 직접 `delete`를 호출하지 않아도 된다.<br>
다만 현재처럼 `make_unique`를 사용하려면 `<memory>`를 직접 include하는 것이 좋다.

```cpp
#include <memory>
#include <vector>
```

정리:
- raw pointer는 메모리 해제를 직접 관리
- smart pointer는 소유권과 해제를 객체로 관리
- 가능하면 `make_unique`를 사용하면 메모리 누수를 줄이기 좋다

## range-based for와 값 복사

처음에는 아래처럼 작성했다.

```cpp
for (auto x : *data2)
{
    x = 100.0;
}
```

`auto x`는 vector의 각 원소를 복사해서 받는다.<br>
그래서 `x`를 100으로 바꿔도 vector 안의 실제 원소는 바뀌지 않는다.

실제 실행 결과:

```text
mat6 : [0, 0, 0, 0, 0;
 0, 0, 0, 0, 0]
```

vector의 실제 원소를 수정하려면 reference로 받아야 한다.<br>
현재 `03_matOp.cpp`는 아래 형태로 수정되어 있다.

```cpp
for (auto& x : *data2)
{
    x = 100.0f;
}
```

수정 후 실행 결과:

```text
mat6 : [100, 100, 100, 100, 100;
 100, 100, 100, 100, 100]
```

정리:
- `auto x` -> 원소를 복사해서 사용
- `auto& x` -> 실제 원소를 reference로 사용
- container의 원소를 변경할 때는 `&`가 필요한지 확인해야 함

## vector data와 Mat 연결

```cpp
Mat mat6(2, 5, CV_32FC1, data2->data());
```

`vector::data()`는 vector가 관리하는 연속된 메모리의 시작 주소를 반환한다.<br>
이 주소를 `Mat` 생성자에 전달해서 2행 5열 행렬로 사용한다.

주의할 점:
- `Mat`이 vector의 데이터를 복사하는 것이 아니라 같은 메모리를 참조함
- `Mat`을 사용하는 동안 vector가 살아 있어야 함
- vector의 크기를 변경해서 재할당이 발생하면 기존 data pointer가 무효가 될 수 있음

현재 코드에서는 `data2`가 `mat6`보다 나중까지 살아 있으므로 `cout`으로 출력하는 동안에는 사용할 수 있다.

## InputArray와 OutputArray

`04_inputArray.cpp`에서는 OpenCV 함수의 입력과 출력을 받는 공용 interface를 실습했다.

```cpp
void printMat(InputArray _mat, OutputArray _output);
```

- `InputArray` -> 입력 데이터를 받는 read-only proxy
- `OutputArray` -> 결과를 저장할 대상을 받는 output proxy
- 실제 호출할 때는 보통 `Mat`을 그대로 전달함

```cpp
Mat img = Mat(10, 20, CV_8UC1, Scalar(125));

Mat mat2;
printMat(img, mat2);
```

`img`는 `InputArray`로 전달되고 `mat2`는 `OutputArray`로 전달된다.

OpenCV에서는 `InputArray`를 사용하면 함수 하나가 `Mat`, `vector`, `Matx` 등 여러 형태의 입력을 받을 수 있다.<br>
일반 변수로 저장하기 위한 type이라기보다 함수 argument용 proxy로 보는 것이 좋다.

## InputArray에서 Mat 얻기

```cpp
void printMat(InputArray _mat, OutputArray _output)
{
    Mat img = _mat.getMat();
}
```

`getMat()`으로 입력 데이터를 `Mat` header 형태로 가져온다.<br>
이 과정은 보통 pixel data 전체를 깊은 복사하는 것이 아니라 기존 데이터를 참조하는 형태이다.

주의:
- 입력값을 읽는 용도로 사용
- 입력 데이터를 독립적으로 보관해야 한다면 `clone()` 같은 깊은 복사를 고려

## Mat 전체 값 연산

```cpp
Mat img2 = img + 3;
```

`img`의 각 원소에 3을 더한 결과를 새 `Mat`으로 만든다.

기존 `img` 값:
```text
125
```

연산 결과:
```text
128
```

현재 영상은 `CV_8UC1`이므로 한 channel의 범위는 `0 ~ 255`이다.<br>
OpenCV의 일반적인 영상 산술 연산은 범위를 넘어갈 때 type 범위에 맞게 포화 연산되는 경우가 많다.

정리:
- `img + 3` -> 모든 pixel에 3 더하기
- 원본 `img`는 125 유지
- 결과 `img2`는 128

## OutputArray로 결과 전달

```cpp
img2.copyTo(_output);
```

`copyTo()`를 사용해서 계산 결과를 호출한 쪽의 `mat2`에 복사한다.

```cpp
Mat mat2;
printMat(img, mat2);
cout << mat2 << endl;
```

실행 흐름:

```text
img 생성: 모든 값 125
-> printMat(img, mat2)
-> InputArray에서 Mat 얻기
-> 각 원소에 3을 더해서 img2 생성
-> img2.copyTo(_output)
-> mat2에 모든 값 128 저장
```

실행 결과에서 확인한 점:
- 함수 내부에서 출력한 `img`는 모두 125
- 함수 호출 후 출력한 `mat2`는 모두 128

## Mat의 얕은 복사

`05_matOp2.cpp`에서는 `Mat`의 얕은 복사와 깊은 복사를 비교했다.

```cpp
Mat img1 = imread(folderPath + "dog.bmp");
Mat img2 = img1;

Mat img3;
img3 = img1;
```

`Mat`을 단순 대입하면 pixel data 전체를 새로 복사하지 않는다.<br>
새로운 `Mat` header가 같은 pixel data를 공유하는 얕은 복사가 된다.

```text
img1 ─┐
img2 ─┼─> 같은 pixel data
img3 ─┘
```

그래서 아래처럼 `img1`의 전체 값을 바꾸면 같은 데이터를 공유하는 `img2`, `img3`도 영향을 받는다.

```cpp
img1.setTo(Color::Yellow);
```

정리:
- `Mat img2 = img1` -> 얕은 복사
- `img3 = img1` -> 얕은 복사
- header는 다르지만 실제 pixel data는 공유
- OpenCV `Mat`은 내부적으로 reference count를 관리함

## Mat의 깊은 복사

독립된 pixel data가 필요하면 `clone()` 또는 `copyTo()`를 사용한다.

```cpp
Mat img4 = img1.clone();

Mat img5;
img1.copyTo(img5);
```

```text
img1 -> 원본 pixel data
img4 -> 별도로 복사된 pixel data
img5 -> 별도로 복사된 pixel data
```

이후 `img1.setTo(Color::Yellow)`를 호출해도 `img4`, `img5`에는 원래 강아지 이미지가 남아 있다.

정리:
- `clone()` -> 새로운 `Mat`을 반환하는 깊은 복사
- `copyTo()` -> 지정한 출력 `Mat`으로 깊은 복사
- 원본과 독립적으로 수정해야 할 때 사용

## setTo로 Mat 값 변경

```cpp
img1.setTo(Color::Yellow);
```

`setTo()`는 `Mat`의 모든 원소를 지정한 값으로 바꾼다.

```cpp
Color::Yellow
```

`colors.hpp` 기준:

```cpp
inline const cv::Scalar Yellow{0, 255, 255};
```

OpenCV는 BGR 순서이므로 `(0, 255, 255)`는 노란색이다.

주의:
- 얕은 복사된 `Mat`이 있으면 같은 pixel data가 함께 변경됨
- 깊은 복사된 `Mat`에는 영향을 주지 않음

## ROI와 부분 영상

ROI는 Region Of Interest의 약자이다.<br>
전체 영상 중에서 처리할 특정 영역을 선택하는 데 사용한다.

```cpp
Rect roi(220, 120, 200, 200);
Mat img6 = img4(roi);
```

```text
Rect(x, y, width, height)
Rect(220, 120, 200, 200)
```

- 시작 위치 -> `(220, 120)`
- 영역 크기 -> `200 x 200`

`img4(roi)`는 해당 부분을 가리키는 새로운 `Mat` header를 만든다.<br>
pixel data를 따로 복사하지 않으므로 `img6`는 `img4`의 일부 데이터를 공유한다.

```cpp
img6.setTo(Color::Black);
```

`img6`를 검은색으로 바꾸면 원본 역할을 하는 `img4`의 ROI 부분도 검은색으로 바뀐다.

정리:
- ROI 추출은 기본적으로 얕은 복사
- ROI를 수정하면 원본의 해당 영역도 수정됨
- 독립된 ROI가 필요하면 `clone()` 사용

```cpp
Mat img6 = img4(roi).clone();
```

## ROI 범위 주의

ROI는 반드시 원본 영상 범위 안에 있어야 한다.

```cpp
Rect roi(220, 120, 200, 200);
```

확인할 조건:

```text
x >= 0
y >= 0
x + width  <= image width
y + height <= image height
```

범위를 벗어나면 OpenCV assertion error가 발생할 수 있다.

이미지를 읽지 못한 경우도 먼저 확인하는 것이 좋다.

```cpp
if (img1.empty())
{
    cerr << "이미지를 읽을 수 없음" << endl;
    return 1;
}
```

## 여러 창 표시와 종료

```cpp
imshow("img1", img1);
imshow("img2", img2);
imshow("img3", img3);
imshow("img4", img4);
imshow("img5", img5);
imshow("img6", img6);

waitKey();
destroyAllWindows();
```

- `imshow()`를 여러 번 호출하면 이름이 다른 창을 여러 개 만들 수 있음
- `waitKey()`로 키 입력과 GUI event를 기다림
- 키를 누르면 `waitKey()` 다음 코드로 이동
- `destroyAllWindows()`로 OpenCV가 만든 창을 모두 닫음

현재 화면에서 예상되는 결과:
- `img1`, `img2`, `img3` -> 노란색 영상
- `img4` -> 원본 강아지 영상에서 ROI 부분만 검은색
- `img5` -> 원본 강아지 영상 유지
- `img6` -> 검은색으로 변경된 200 x 200 ROI

## 04, 05 실습 target

CMake에 실행 target을 추가했다.

```cmake
add_executable(04_inputArray part1/04_inputArray.cpp)
target_link_libraries(04_inputArray PRIVATE ${OpenCV_LIBS})

add_executable(05_matOp2 part1/05_matOp2.cpp)
target_link_libraries(05_matOp2 PRIVATE ${OpenCV_LIBS})
```

빌드:

```bash
cmake --build opencv/build --target 04_inputArray
cmake --build opencv/build --target 05_matOp2
```

실행:

```bash
./opencv/build/04_inputArray
./opencv/build/05_matOp2
```

정리:
- `InputArray`, `OutputArray`는 OpenCV 함수 argument를 유연하게 만드는 proxy
- 단순 `Mat` 대입은 얕은 복사
- `clone()`, `copyTo()`는 깊은 복사
- ROI는 원본의 일부 data를 공유
- 공유된 data를 수정하면 연결된 다른 `Mat`에도 변화가 보임

## 카메라 영상 입력

`06_video.cpp`

카메라나 동영상 파일에서 frame을 읽을 때는 `VideoCapture`를 사용한다.

```cpp
VideoCapture cap(0);
if (!cap.isOpened())
{
    cerr << "카메라를 열수 없습니다." << endl;
}
```

- `VideoCapture cap(0)` -> 기본 카메라 장치 열기
- 보통 Linux에서는 `/dev/video0` 같은 장치와 연결됨
- `isOpened()`로 카메라가 정상적으로 열렸는지 확인

주의:
- 지금 코드는 카메라를 열지 못해도 바로 종료하지 않고 계속 진행한다
- 실제 코드에서는 `return 1;`로 중단하는 것이 더 안전하다

```cpp
if (!cap.isOpened())
{
    cerr << "카메라를 열수 없습니다." << endl;
    return 1;
}
```

## 카메라 속성 설정

카메라 frame 형식, 크기, FPS를 설정했다.

```cpp
cap.set(CAP_PROP_FOURCC, VideoWriter::fourcc('M','J','P','G'));
cap.set(CAP_PROP_FRAME_WIDTH, 640);
cap.set(CAP_PROP_FRAME_HEIGHT, 480);
cap.set(CAP_PROP_FPS, 30);
```

확인한 점:
- `CAP_PROP_FOURCC` -> 영상 압축/전송 형식 설정
- `MJPG` -> Motion JPEG 형식
- `CAP_PROP_FRAME_WIDTH` -> frame width
- `CAP_PROP_FRAME_HEIGHT` -> frame height
- `CAP_PROP_FPS` -> 초당 frame 수

주의:
- `set()`은 요청한 값을 카메라에 전달하는 것이다
- 실제 적용 여부는 카메라, driver, WSL/리눅스 환경에 따라 다를 수 있다
- 필요하면 `cap.get()`으로 실제 적용된 값을 확인하는 것이 좋다

예:
```cpp
cout << cap.get(CAP_PROP_FRAME_WIDTH) << endl;
cout << cap.get(CAP_PROP_FRAME_HEIGHT) << endl;
cout << cap.get(CAP_PROP_FPS) << endl;
```

## frame 읽기와 화면 출력

```cpp
Mat frame;
for (int i = 0; i < 1000; ++i)
{
    cap >> frame;
    if(waitKey(30) == 27)
        break;
    imshow("frame", frame);
}
```

`cap >> frame`으로 카메라에서 한 장의 frame을 읽는다.<br>
동영상은 결국 이미지를 계속 읽어서 빠르게 보여주는 방식으로 생각하면 된다.

- `frame` -> 현재 카메라에서 읽은 한 장의 영상
- `imshow("frame", frame)` -> frame 창에 출력
- `waitKey(30)` -> 약 30ms 기다리면서 키 입력 확인
- `27` -> ESC key 값

주의:
- `cap >> frame` 이후 `frame.empty()`도 확인하는 것이 안전하다
- 카메라 연결이 끊기거나 frame을 못 읽으면 빈 `Mat`이 될 수 있다

```cpp
cap >> frame;
if (frame.empty())
{
    cerr << "frame을 읽을 수 없습니다." << endl;
    break;
}
```

정리:
- 이미지 파일은 `imread()`로 한 번 읽음
- 카메라는 `VideoCapture`로 열고 frame을 반복해서 읽음
- `waitKey()`는 화면 갱신과 키 입력 처리에 필요함
- ESC를 누르면 loop를 빠져나오게 만들 수 있음

## 카메라 장치 권한 문제

GStreamer로 먼저 카메라 입력을 확인했다.

```bash
gst-launch-1.0 v4l2src device=/dev/video0 ! \
  video/x-h264,width=1280,height=720,framerate=30/1 ! \
  h264parse ! avdec_h264 ! videoconvert ! autovideosink sync=false
```

처음에는 아래 에러가 났다.

```text
Could not open device '/dev/video0' for reading and writing.
system error: Permission denied
```

`/dev/video0` 권한을 확인했다.

```bash
ls -l /dev/video0
id
```

확인한 내용:
```text
/dev/video0 -> root video
현재 user -> video group에 없음
```

원인:
- `/dev/video0`는 `root` 또는 `video` group 사용자만 읽고 쓸 수 있었다
- 현재 사용자가 `video` group에 없어서 permission denied가 발생했다

해결:
```bash
sudo usermod -aG video $USER
```

WSL에서는 group 변경 후 세션을 다시 시작해야 적용된다.

```powershell
wsl --shutdown
```

다시 확인:
```bash
id
```

`video` group이 보이면 정상이다.

정리:
- 카메라 코드가 안 될 때는 OpenCV 코드보다 장치 권한을 먼저 확인할 수 있다
- `/dev/video0`가 `root video`이고 내 계정이 `video` group에 있어야 함
- 권한을 준 뒤에는 GStreamer pipeline과 OpenCV `VideoCapture`가 정상 동작했다

## 06 실습 target

CMake에 `06_video` target을 추가했다.

```cmake
add_executable(06_video part1/06_video.cpp)
target_link_libraries(06_video PRIVATE ${OpenCV_LIBS})
```

빌드:

```bash
cmake --build opencv/build --target 06_video
```

실행:

```bash
./opencv/build/06_video
```

빌드 확인:
```text
[100%] Built target 06_video
```

## 카메라 영상 파일로 저장

`09_videoSave.cpp`

카메라에서 읽은 frame을 화면에 보여주는 것뿐만 아니라 동영상 파일로 저장해보았다.

```cpp
int w = 640;
int h = 480;
double fps = 30.0;
int fourcc = VideoWriter::fourcc('D','I','V','X');

VideoWriter outVideo(
    folderPath + "flip_roi_inverse.avi",
    fourcc,
    fps,
    Size(w, h)
);
```

동영상 저장에는 `VideoWriter`를 사용한다.

```text
VideoWriter(파일 경로, codec, FPS, frame 크기)
```

- 파일 경로 -> 저장할 동영상 이름과 위치
- `fourcc` -> 동영상 압축 codec
- `fps` -> 초당 저장할 frame 수
- `Size(w, h)` -> 저장할 frame 크기

현재 코드는 AVI 파일에 `DIVX` codec을 사용하도록 요청했다.

```cpp
VideoWriter::fourcc('D', 'I', 'V', 'X');
```

FourCC는 4개의 문자로 codec을 표현하는 방식이다.

주의할 점:
- 사용할 수 있는 codec은 OpenCV build, 운영체제, 설치된 codec에 따라 다를 수 있음
- 파일 확장자와 codec 조합도 확인해야 함
- `VideoWriter`가 정상적으로 열렸는지 확인하는 것이 안전함

```cpp
if (!outVideo.isOpened())
{
    cerr << "동영상 파일을 열 수 없습니다." << endl;
    return 1;
}
```

## frame 저장

카메라에서 frame을 읽고 처리한 다음 `VideoWriter`에 전달한다.

```cpp
cap >> frame;

outVideo << frame;
```

`outVideo << frame`을 loop 안에서 반복하면 각 이미지가 동영상의 frame으로 저장된다.

주의할 점:
- 저장하는 `frame`의 크기는 `VideoWriter`를 만들 때 전달한 크기와 같아야 함
- 카메라에 `640 x 480`을 요청해도 실제 적용된 크기는 다를 수 있음
- `frame.empty()`를 확인한 다음 저장하는 것이 안전함

```cpp
cap >> frame;

if (frame.empty())
{
    cerr << "frame을 읽을 수 없습니다." << endl;
    break;
}

outVideo << frame;
```

카메라의 실제 크기는 `get()`으로 확인할 수 있다.

```cpp
int w = static_cast<int>(cap.get(CAP_PROP_FRAME_WIDTH));
int h = static_cast<int>(cap.get(CAP_PROP_FRAME_HEIGHT));
double fps = cap.get(CAP_PROP_FPS);
```

환경에 따라 카메라가 반환하는 FPS가 정확하지 않거나 0일 수도 있어서 확인이 필요하다.

## 영상 좌우 반전

```cpp
flip(frame, frame, 1);
```

`flip()`은 영상을 뒤집는 함수이다.

```text
flip(source, destination, flipCode)
```

`flipCode`에 따라 반전 방향이 달라진다.

- `0` -> 위아래 반전
- 양수 -> 좌우 반전
- 음수 -> 위아래와 좌우 모두 반전

현재 코드의 `1`은 좌우 반전이다.<br>
카메라 화면을 거울처럼 보이게 만들 때 사용할 수 있다.

## 움직이는 ROI

가로로 이동하는 `200 x 200` ROI를 만들었다.

```cpp
int y = (480 - 200) / 2;
int move_x = 0;

Mat roi = frame(Rect(move_x, y, 200, 200));
```

- `move_x` -> ROI의 시작 x 좌표
- `y` -> ROI의 시작 y 좌표
- `200, 200` -> ROI의 width와 height

loop가 한 번 실행될 때마다 x 좌표를 증가시킨다.

```cpp
move_x += 1;

if (move_x > 340)
{
    move_x = 0;
}
```

frame width가 640이고 ROI width가 200이므로 시작 x 좌표의 최댓값은 440이다.

```text
640 - 200 = 440
```

현재 코드는 `340`에서 처음으로 돌아가므로 화면 오른쪽 끝까지 이동하지는 않는다.<br>
오른쪽 끝까지 이동하려면 frame width를 기준으로 범위를 계산할 수 있다.

```cpp
if (move_x > frame.cols - 200)
{
    move_x = 0;
}
```

정리:
- `frame.cols` -> frame width
- `frame.rows` -> frame height
- ROI의 오른쪽과 아래쪽이 frame 범위를 벗어나면 assertion error가 날 수 있음

## ROI 색상 반전

```cpp
Mat roi = frame(Rect(move_x, y, 200, 200));
roi = ~roi;
```

`~` 연산은 각 pixel의 bit를 반전한다.

8bit 영상에서는 아래처럼 생각할 수 있다.

```text
결과 pixel = 255 - 원래 pixel
```

예:

```text
0   -> 255
50  -> 205
255 -> 0
```

ROI는 원본 frame의 일부를 가리키므로 ROI에 연산 결과를 저장하면 frame의 해당 영역에서 변화가 보인다.

의도를 더 명확하게 쓰려면 `bitwise_not()`을 사용할 수도 있다.

```cpp
bitwise_not(roi, roi);
```

ROI 주위에는 빨간색 사각형을 그렸다.

```cpp
rectangle(
    frame,
    Rect(move_x, y, 200, 200),
    Color::Red,
    2
);
```

- `Color::Red` -> BGR `(0, 0, 255)`
- `2` -> 선 두께

현재 처리 순서에서는 좌우 반전, ROI 색상 반전, 사각형 그리기가 끝난 frame이 파일에 저장된다.

## VideoCapture와 VideoWriter 해제

```cpp
cap.release();
outVideo.release();
destroyAllWindows();
```

- `cap.release()` -> 카메라 장치 해제
- `outVideo.release()` -> 동영상 파일 저장 종료
- `destroyAllWindows()` -> OpenCV 창 닫기

`VideoWriter`는 해제될 때 파일의 마무리 정보를 기록할 수 있다.<br>
프로그램이 비정상 종료되면 동영상 파일이 제대로 재생되지 않을 수도 있다.

정리:
- `VideoCapture` -> frame 입력
- 영상 처리 -> `flip`, ROI 반전, `rectangle`
- `VideoWriter` -> 처리된 frame 저장
- ESC를 누르면 loop를 종료하고 장치와 파일을 해제

## 기본 도형 그리기

`10_drawing.cpp`

빈 영상 위에 선, 화살표, marker를 그려보았다.

```cpp
Mat img(400, 600, CV_8UC3, Color::White);
```

```text
Mat(rows, cols, type, color)
Mat(height, width, type, color)
```

- height -> 400
- width -> 600
- channel -> 3
- 초기 색상 -> 흰색

주의:
- `Mat(400, 600, ...)`은 height, width 순서
- `Point(x, y)`는 width 방향, height 방향 순서

## clone으로 매 frame 초기화

```cpp
while (true)
{
    Mat img2 = img.clone();

    // 도형 그리기
}
```

반복문 안에서 원본 흰색 영상 `img`를 깊은 복사한다.

매 frame마다 새로운 흰색 배경에서 도형을 다시 그리기 때문에 이전 위치의 선이 계속 남지 않는다.

```text
clone() 사용     -> 현재 위치의 도형만 보임
같은 Mat에 계속 그림 -> 이동 경로가 누적되어 보일 수 있음
```

정리:
- `img` -> 변하지 않는 기본 배경
- `img2` -> 현재 frame에 사용할 복사본
- 애니메이션처럼 위치만 바꾸고 싶을 때 매번 배경을 복사할 수 있음

## line으로 선 그리기

```cpp
line(
    img2,
    Point(50, 50),
    Point(200 + a, 100 + b),
    Color::Blue,
    3
);
```

```text
line(image, startPoint, endPoint, color, thickness)
```

- 시작점 -> `(50, 50)`
- 끝점 -> `(200 + a, 100 + b)`
- 색상 -> 파란색
- 선 두께 -> 3

`a`, `b`가 계속 증가하므로 시작점은 고정되고 끝점은 오른쪽 아래 방향으로 이동한다.

```cpp
a += 1;
b += 2;
```

x는 한 번에 1씩, y는 한 번에 2씩 증가한다.

## arrowedLine으로 화살표 그리기

```cpp
arrowedLine(
    img2,
    Point(50, 100),
    Point(200, 50),
    Color::Orange,
    3,
    LINE_8
);
```

`arrowedLine()`은 끝부분에 화살표 모양이 있는 선을 그린다.

- 시작점 -> `(50, 100)`
- 끝점 -> `(200, 50)`
- 색상 -> 주황색
- 두께 -> 3
- `LINE_8` -> 8-connected line 방식

현재 화살표 좌표는 `a`, `b`를 사용하지 않으므로 움직이지 않는다.

## drawMarker로 marker 그리기

```cpp
drawMarker(
    img2,
    Point(400 - a, 600 - b),
    Color::Red,
    MARKER_STAR
);
```

`drawMarker()`는 지정한 좌표에 marker 모양을 그린다.

- 위치 -> `Point(x, y)`
- 색상 -> 빨간색
- 모양 -> 별 모양

현재 영상 크기는 width 600, height 400이다.

```text
x 범위: 0 ~ 599
y 범위: 0 ~ 399
```

하지만 marker의 처음 좌표는 `(400, 600)`이다.<br>
x는 범위 안이지만 y가 영상 높이보다 커서 marker가 화면에 보이지 않는다.

화면 안에서 시작하려면 y 좌표를 400보다 작은 값으로 잡아야 한다.

```cpp
drawMarker(
    img2,
    Point(400 - a, 300 - b),
    Color::Red,
    MARKER_STAR
);
```

`a`, `b`가 계속 증가하면 나중에는 x나 y가 음수가 될 수 있다.<br>
계속 반복할 경우 좌표를 초기화하거나 화면 범위를 확인하는 처리가 필요하다.

## waitKey로 애니메이션 속도 조절

```cpp
if (waitKey(1000 / 30) == 27)
    break;
```

초당 약 30번 화면을 갱신하도록 약 33ms를 기다린다.

```text
1000ms / 30fps = 약 33ms
```

주의:
- `waitKey()`의 시간은 정확한 FPS를 보장하는 값은 아님
- 도형 처리 시간과 운영체제 scheduling에 따라 실제 속도는 달라질 수 있음
- ESC key 값 `27`을 확인해서 loop를 종료함

정리:
- `line()` -> 일반 선
- `arrowedLine()` -> 화살표 선
- `drawMarker()` -> 지정한 모양의 marker
- `Point(x, y)`에서 x는 가로, y는 세로 좌표
- 영상 밖의 좌표는 도형이 잘리거나 보이지 않을 수 있음
- `clone()`으로 매 frame 배경을 초기화하면 도형의 이동 흔적이 남지 않음

## rectangle 옵션 추가 확인

`10_drawing.cpp`

사각형을 그릴 때 선 종류까지 전달해보았다.

```cpp
rectangle(
    img2,
    Rect(300, 50, 50 + c, 50 + c),
    Color::Red,
    2,
    LINE_AA
);
```

```text
rectangle(image, rect, color, thickness, lineType)
```

- `Rect(300, 50, ...)` -> 사각형의 왼쪽 위 좌표
- `50 + c` -> width와 height
- `Color::Red` -> 빨간색
- `2` -> 선 두께
- `LINE_AA` -> 경계선을 부드럽게 그리는 anti-aliasing 방식

현재 코드에서는 `c`의 초기값이 0이고 loop 안에서 증가시키지 않는다.

```cpp
int a = 0, b = 0, c = 0;
```

그래서 현재 사각형 크기는 계속 `50 x 50`이다.<br>
크기가 커지는 모습을 보려면 loop 안에서 `c`를 변경해야 한다.

```cpp
c += 1;
```

주의:
- `c`가 계속 증가하면 사각형이 영상 범위를 넘어갈 수 있음
- 반복 애니메이션으로 만들려면 일정 크기에서 다시 0으로 초기화할 수 있음

## circle로 원 그리기

```cpp
circle(
    img2,
    Point(350, 150),
    20,
    Color::Yellow,
    2,
    LINE_AA
);
```

```text
circle(image, center, radius, color, thickness, lineType)
```

- 중심 좌표 -> `(350, 150)`
- 반지름 -> 20
- 색상 -> 노란색
- 두께 -> 2
- 선 종류 -> `LINE_AA`

원의 내부를 채우려면 두께에 `FILLED` 또는 `-1`을 사용할 수 있다.

```cpp
circle(img2, Point(350, 150), 20, Color::Yellow, FILLED, LINE_AA);
```

정리:
- `Point`는 원의 중심 좌표
- 크기는 width, height가 아니라 반지름으로 지정
- 양수 thickness는 외곽선, `FILLED`는 내부 채우기

## ellipse로 타원과 호 그리기

```cpp
ellipse(
    img2,
    Point(500, 50),
    Size(60, 30),
    20,
    0,
    0 + c,
    Color::Cyan,
    FILLED,
    LINE_AA
);
```

```text
ellipse(image, center, axes, angle,
        startAngle, endAngle, color, thickness, lineType)
```

- 중심 좌표 -> `(500, 50)`
- `Size(60, 30)` -> 가로와 세로 반지름
- `20` -> 타원 자체의 회전 각도
- `0` -> 호의 시작 각도
- `c` -> 호의 끝 각도
- `FILLED` -> 내부 채우기

`Size(60, 30)`은 전체 크기 `60 x 30`이 아니라 타원의 반지름 크기이다.<br>
그래서 전체 폭과 높이는 대략 `120 x 60`으로 생각할 수 있다.

현재 코드에서는 `c`가 0이므로 시작 각도와 끝 각도가 둘 다 0이다.<br>
이 상태에서는 그려지는 호의 범위가 없어서 타원이 보이지 않을 수 있다.

전체 타원을 그리려면 아래처럼 끝 각도를 360으로 준다.

```cpp
ellipse(
    img2,
    Point(500, 50),
    Size(60, 30),
    20,
    0,
    360,
    Color::Cyan,
    FILLED,
    LINE_AA
);
```

`c`를 증가시키면 타원이 조금씩 채워지는 애니메이션도 만들 수 있다.

```cpp
c += 3;

if (c > 360)
    c = 0;
```

정리:
- `angle` -> 타원 전체의 기울기
- `startAngle`, `endAngle` -> 어느 범위의 호를 그릴지 결정
- 전체 타원은 보통 `0 ~ 360`
- `LINE_AA`를 사용하면 곡선 경계가 조금 더 부드럽게 보임

## putText로 영문 출력

`13_font_.cpp`

OpenCV 기본 font를 사용해서 영상 위에 문자열을 출력했다.

```cpp
putText(
    img,
    "SIMPLEX",
    Point(20 + a, 70),
    FONT_HERSHEY_SIMPLEX,
    1.5,
    Color::Red,
    2,
    LINE_AA
);
```

```text
putText(image, text, origin, fontFace,
        fontScale, color, thickness, lineType)
```

- `text` -> 출력할 문자열
- `origin` -> 문자열 기준 좌표
- `fontFace` -> 글꼴 종류
- `fontScale` -> 글자 크기 배율
- `color` -> 글자 색
- `thickness` -> 획 두께
- `lineType` -> 선을 그리는 방식

`Point(20 + a, 70)`은 글자의 왼쪽 아래 기준점으로 사용된다.<br>
일반적인 사각형의 왼쪽 위 좌표와 기준이 달라서 y 좌표를 정할 때 주의해야 한다.

## Hershey font 종류

```cpp
FONT_HERSHEY_SIMPLEX
FONT_HERSHEY_DUPLEX
FONT_HERSHEY_PLAIN
```

OpenCV 기본 `putText()`는 Hershey stroke font를 제공한다.

- `FONT_HERSHEY_SIMPLEX` -> 기본적인 글꼴
- `FONT_HERSHEY_DUPLEX` -> SIMPLEX보다 획 표현이 조금 더 복잡함
- `FONT_HERSHEY_PLAIN` -> 비교적 단순하고 작은 글꼴

font에 italic flag를 추가할 수도 있다.

```cpp
FONT_HERSHEY_SIMPLEX | FONT_ITALIC
```

`FONT_ITALIC`은 단독 font 종류로 사용하기보다 기존 Hershey font와 bit OR 연산으로 결합한다.

```cpp
putText(
    img,
    "SIMPLEX ITALIC",
    Point(20 + a, 140),
    FONT_HERSHEY_SIMPLEX | FONT_ITALIC,
    1.5,
    Color::Red,
    2,
    LINE_AA
);
```

정리:
- OpenCV 기본 `putText()`는 간단한 영문과 숫자 표시에 편리함
- font 크기는 pixel 높이를 직접 지정하는 것이 아니라 `fontScale` 배율로 조절
- 한글 같은 UTF-8 문자는 기본 Hershey font로 제대로 표시되지 않을 수 있음

## 움직이는 문자열

문자열의 x 좌표에 변수 `a`를 더했다.

```cpp
Point(20 + a, 70)
```

loop가 한 번 실행될 때마다 `a`를 증가시킨다.

```cpp
a += 1;
```

그래서 문자열이 왼쪽에서 오른쪽으로 이동한다.

화면 오른쪽을 지나면 다시 왼쪽에서 시작하도록 값을 변경했다.

```cpp
if (a > img.cols)
    a = -300;
```

- `img.cols` -> 영상 width
- `-300` -> 문자열이 화면 왼쪽 바깥에서 다시 들어오게 하기 위한 값

주의:
- 문자열마다 실제 width가 다르므로 `-300`은 대략 정한 값
- 정확한 문자열 width는 `getTextSize()`로 구할 수 있음

## colors.hpp namespace 오류

처음 코드에서는 색상을 아래처럼 사용했다.

```cpp
Mat img(400, 600, CV_8UC3, white);
putText(img, "TEXT", Point(20, 50),
        FONT_HERSHEY_SIMPLEX, 2, red);
```

빌드할 때 색상 이름을 찾을 수 없다는 에러가 발생했다.

```text
error: 'white' was not declared in this scope
error: 'red' was not declared in this scope
```

`colors.hpp`의 색상은 `Color` namespace 안에 있고 이름도 대문자로 시작한다.

```cpp
namespace Color
{
    inline const cv::Scalar White{255, 255, 255};
    inline const cv::Scalar Red{0, 0, 255};
}
```

그래서 아래처럼 사용해야 한다.

```cpp
Color::White
Color::Red
Color::Blue
Color::Black
```

header include도 컴퓨터의 전체 경로보다 현재 project 기준 경로를 사용하는 것이 좋다.

```cpp
#include "colors.hpp"
```

정리:
- namespace 안의 값은 `namespace이름::값` 형태로 접근
- C++은 대문자와 소문자를 구분
- 절대경로 include는 project 위치가 바뀌면 깨질 수 있음

## FreeType으로 한글 출력

`14_freetype.cpp`

OpenCV 기본 `putText()` 대신 FreeType module과 TTF font 파일을 사용해서 한글을 출력했다.

```cpp
#include <opencv2/freetype.hpp>
```

현재 실습 환경에서는 `opencv_freetype` module을 사용할 수 있고 아래 font 파일도 존재한다.

```text
opencv/data/NanumPenScript-Regular.ttf
```

FreeType 객체를 만들고 font 파일을 불러온다.

```cpp
Ptr<cv::freetype::FreeType2> ft2 =
    freetype::createFreeType2();

ft2->loadFontData(fontpath, 0);
```

- `createFreeType2()` -> FreeType 객체 생성
- `loadFontData()` -> TTF 또는 지원되는 font 파일 읽기
- 두 번째 argument `0` -> font collection 안에서 사용할 face index

현재 코드는 이 과정을 함수로 묶었다.

```cpp
Ptr<cv::freetype::FreeType2>
rapperFreeTypeCenterSetup(const String &fontpath)
{
    Ptr<cv::freetype::FreeType2> ft2 =
        freetype::createFreeType2();

    ft2->loadFontData(fontpath, 0);
    return ft2;
}
```

`Ptr`은 OpenCV에서 사용하는 smart pointer이다.<br>
FreeType 객체의 수명을 직접 `delete`하지 않아도 관리할 수 있다.

## FreeType putText

```cpp
ft2->putText(
    img,
    text,
    textRect.tl(),
    textHeight,
    color,
    thickness,
    line_type,
    false
);
```

기본 `cv::putText()`와 argument 구성이 조금 다르다.

```text
FreeType putText(image, text, origin, fontHeight,
                 color, thickness, lineType, bottomLeftOrigin)
```

- `fontHeight` -> pixel 단위의 font 높이
- `thickness`가 음수 -> glyph 내부를 채움
- `thickness`가 양수 -> 지정한 두께의 외곽선으로 그림
- `bottomLeftOrigin=false` -> 영상 원점을 왼쪽 위 기준으로 사용

현재 코드는 `thickness=2`를 전달하므로 글자가 외곽선 형태로 그려진다.<br>
채워진 글자를 원하면 음수를 사용할 수 있다.

```cpp
ft2->putText(
    img,
    text,
    textOrg,
    textHeight,
    color,
    -1,
    LINE_AA,
    false
);
```

주의:
- 입력 영상은 현재 FreeType module 기준으로 `CV_8UC3` 형식을 사용하는 것이 안전함
- font 경로가 틀리면 font data를 불러올 수 없음
- 다른 컴퓨터에서는 OpenCV가 FreeType module과 함께 build되었는지 확인 필요

## getTextSize로 문자열 영역 구하기

문자열을 그리기 전에 차지할 영역을 계산했다.

```cpp
Size textSize =
    ft2->getTextSize(text, textHeight, -1, 0)
    + Size(0, 20);
```

```text
getTextSize(text, fontHeight, thickness, baseline)
```

- 반환값 -> 문자열을 감싸는 대략적인 width와 height
- `-1` -> 채워진 glyph 기준 두께
- 마지막 `0` -> baseline 결과를 따로 받지 않음
- `Size(0, 20)` -> 아래쪽 여백을 위해 height에 20 추가

현재 크기 계산은 `thickness=-1`을 사용하지만 실제 출력 함수에는 `thickness=2`를 전달한다.<br>
계산 기준과 출력 기준이 달라서 사각형과 글자 외곽선 크기가 조금 다르게 보일 수 있다.

정확하게 맞추려면 같은 thickness 값을 사용한다.

```cpp
Size textSize =
    ft2->getTextSize(text, textHeight, thickness, 0)
    + Size(0, 20);
```

계산한 크기로 `Rect`를 만든다.

```cpp
Point top_left(
    textOrg.x - textSize.width,
    textOrg.y - textSize.height
);

Rect textRect(top_left, textSize);
```

현재 계산 방식에서는 `textOrg`가 사각형의 중앙점은 아니다.<br>
사각형의 오른쪽 아래를 기준으로 왼쪽 위 좌표를 구하는 형태에 가깝다.

```text
textRect 오른쪽 아래 위치 ~= textOrg
```

함수 이름에는 `Center`가 들어가 있지만 실제 중앙 정렬을 하려면 width와 height의 절반을 사용해야 한다.

```cpp
Point topLeft(
    textOrg.x - textSize.width / 2,
    textOrg.y - textSize.height / 2
);
```

정렬 기준은 원하는 결과에 따라 직접 정해야 한다.

## 텍스트 영역 사각형 표시

```cpp
if (withRect)
{
    rectangle(img, textRect, color, 3, line_type);
}
```

`withRect`가 `true`이면 계산한 문자열 영역 주위에 사각형을 그린다.

확인할 수 있는 점:
- 문자열의 예상 width와 height
- 문자열 이동에 따라 `Rect`도 같이 이동하는지
- 기준 좌표와 실제 문자열 위치가 맞는지

현재 실습에서는 기준 위치를 확인하기 위해 빨간색 원도 같이 그렸다.

```cpp
circle(img, Point(a, 300), 6, Color::Red, -1);
```

`-1`은 원 내부를 채우는 의미이다.<br>
`FILLED`를 사용해도 같은 목적이다.

## 여러 한글 문자열 이동

```cpp
rapperFreeTypeCenter(
    img,
    ft2,
    text,
    100,
    2,
    LINE_AA,
    Color::Blue,
    Point(a, 300),
    true
);
```

세 문자열에 서로 다른 위치 변수와 증가값을 사용했다.

```cpp
a += 1;
b += 2;
c += 3;
```

- 첫 번째 문자열 -> 한 frame마다 1 pixel 이동
- 두 번째 문자열 -> 한 frame마다 2 pixel 이동
- 세 번째 문자열 -> 한 frame마다 3 pixel 이동

그래서 같은 loop 안에서도 서로 다른 속도로 움직인다.

주의:
- 현재 코드에는 좌표를 초기화하는 부분이 없음
- 문자열이 화면 오른쪽을 지나면 계속 영상 범위 밖으로 이동함
- 반복해서 보이게 하려면 각 좌표를 `img.cols`와 비교해서 초기화해야 함

정리:
- 기본 `putText()` -> Hershey font를 사용하는 간단한 영문 출력
- FreeType `putText()` -> TTF font를 불러와 UTF-8 한글 출력 가능
- `getTextSize()` -> 문자열이 차지할 영역 계산
- `Rect`를 같이 그리면 텍스트 좌표와 영역을 확인하기 편함
- font 파일 경로와 OpenCV FreeType module 지원 여부를 확인해야 함

## waitKey로 키보드 입력 받기

`15_keyboard.cpp`

`waitKey()`의 반환값을 저장해서 어떤 키가 눌렸는지 확인했다.

```cpp
int keycode = waitKey(needed_tick_ms);

if (keycode == 27)
    break;

if (keycode == 'v' || keycode == 'V')
    img = ~img;

if (keycode != -1)
    cout << "keycode: " << keycode << endl;
```

- 키 입력이 없으면 보통 `-1`
- ESC key -> 27
- 소문자 `v`와 대문자 `V`를 각각 비교할 수 있음

`v`를 누르면 영상의 pixel 값을 반전한다.

```cpp
img = ~img;
```

8bit 영상에서는 각 channel 값이 아래처럼 바뀐다.

```text
결과값 = 255 - 원래값
```

같은 영상을 다시 반전하면 원래 색에 가까운 상태로 돌아온다.

주의:
- `waitKey()`는 키보드 입력뿐 아니라 OpenCV 창의 GUI event 처리에도 필요함
- 특수 key 값은 운영체제와 backend에 따라 다르게 들어올 수 있음
- 현재 실습처럼 일반 문자와 ESC를 처리할 때는 반환값을 직접 출력해보는 것이 편함

## getTickCount로 시간 측정

OpenCV에서는 tick 값을 이용해서 코드 실행 시간을 계산할 수 있다.

```cpp
auto start_tick = getTickCount();

double elapsed_ms =
    (getTickCount() - start_tick)
    * 1000.0
    / getTickFrequency();
```

- `getTickCount()` -> 현재 tick count
- `getTickFrequency()` -> 1초에 해당하는 tick 수
- 두 tick의 차이를 frequency로 나누면 초 단위 시간
- `1000.0`을 곱하면 millisecond 단위 시간

현재 `15_keyboard.cpp`에서는 loop 시작 직후 start tick을 저장하고 바로 elapsed time을 계산한다.

```cpp
start_tick = getTickCount();
double elapsed_ms =
    (getTickCount() - start_tick) * 1000.0
    / getTickFrequency();
```

사이에 처리하는 코드가 거의 없어서 `elapsed_ms`도 거의 0에 가깝다.<br>
실제 영상 처리 시간을 빼고 남은 시간만 기다리려면 처리할 코드를 두 tick 사이에 넣어야 한다.

```cpp
int64 startTick = getTickCount();

// 영상 처리
imshow("img", img);

double elapsedMs =
    (getTickCount() - startTick)
    * 1000.0
    / getTickFrequency();
```

## 목표 FPS에 맞춰 기다리기

```cpp
int fps = 45;
int needed_tick_ms =
    cvRound(1000.0 / fps - elapsed_ms);

int keycode = waitKey(needed_tick_ms);
```

45 FPS에서 한 frame에 사용할 수 있는 시간은 약 22.2ms이다.

```text
1000ms / 45fps = 약 22.2ms
```

처리 시간을 제외한 나머지 시간을 `waitKey()`에 전달하면 목표 FPS에 가깝게 조절할 수 있다.

주의:
- 처리 시간이 frame 시간보다 길면 계산 결과가 0 이하가 될 수 있음
- `waitKey(0)` 또는 음수 delay는 key가 입력될 때까지 기다릴 수 있음
- 최소 delay를 보장하는 것이 안전함

```cpp
int delay = std::max(1, cvRound(1000.0 / fps - elapsedMs));
int keycode = waitKey(delay);
```

정확한 실시간 FPS를 보장하는 것은 아니고, 간단한 화면 갱신 속도 조절로 생각하면 된다.

## TickMeter

`16_tickmeter.cpp`

tick 계산을 직접 하지 않고 `TickMeter`로 실행 시간을 측정해보았다.

```cpp
TickMeter tm1;

tm1.start();
imshow("img", img);
tm1.stop();

double elapsed_ms = tm1.getTimeMilli();
tm1.reset();
```

- `start()` -> 측정 시작
- `stop()` -> 측정 종료
- `getTimeMilli()` -> 누적 시간을 ms 단위로 반환
- `reset()` -> 측정값 초기화

`start()`와 `stop()` 사이의 코드만 측정한다.

현재 코드는 `imshow()` 호출 시간을 측정하고, 목표 10 FPS에서 남은 시간을 계산한다.

```cpp
int fps = 10;
int needed_tick_ms =
    cvRound(1000.0 / fps - elapsed_ms);
```

현재 코드에는 `tm2`도 있지만 `start()`만 호출하고 측정값을 사용하지 않는다.

```cpp
TickMeter tm2;
tm2.start();
```

사용하지 않는 측정기는 제거하거나 loop 전체 시간을 측정하는 용도로 `stop()`과 출력 코드를 추가할 수 있다.

정리:
- 짧은 구간 측정 -> `getTickCount()`
- start/stop 형태의 측정 -> `TickMeter`
- 여러 번 start/stop하면 시간이 누적될 수 있으므로 frame별 측정은 `reset()` 필요

## 마우스 callback 등록

`17_mouse.cpp`

OpenCV 창에서 발생한 mouse event를 처리할 때 `setMouseCallback()`을 사용한다.

```cpp
namedWindow("img");
setMouseCallback("img", on_mouse, (void *)&img);
```

```text
setMouseCallback(windowName, callback, userData)
```

- `windowName` -> mouse event를 받을 창 이름
- `callback` -> event가 생길 때 실행할 함수
- `userData` -> callback에 전달할 사용자 data

callback 함수 형태:

```cpp
void on_mouse(
    int event,
    int x,
    int y,
    int flags,
    void *data
);
```

- `event` -> click, button up, mouse move 같은 event 종류
- `x`, `y` -> 현재 mouse 좌표
- `flags` -> 눌린 button이나 modifier key 상태
- `data` -> 등록할 때 전달한 사용자 data

## void pointer로 Mat 전달

등록할 때 `Mat` 주소를 `void*`로 전달했다.

```cpp
setMouseCallback("img", on_mouse, (void *)&img);
```

callback 안에서는 다시 `Mat*`로 변환한다.

```cpp
Mat *img = (Mat *)data;
```

현재 코드 방식으로 동작하지만 C++에서는 `static_cast`를 사용하면 의도가 더 명확하다.

```cpp
Mat *img = static_cast<Mat *>(data);
```

callback이 실행되는 동안 전달한 객체가 살아 있어야 한다.<br>
현재 `img`는 `main()`이 끝날 때까지 유지되므로 callback에서 사용할 수 있다.

## 왼쪽 drag로 선 그리기

```cpp
static Point ptOld;
static bool pushed;
```

callback 호출이 끝난 뒤에도 이전 위치와 button 상태를 유지하기 위해 `static` 지역 변수를 사용했다.

```cpp
case EVENT_LBUTTONDOWN:
    ptOld = Point(x, y);
    pushed = true;
    break;

case EVENT_LBUTTONUP:
    pushed = false;
    break;
```

mouse가 움직일 때 button이 눌린 상태라면 이전 위치와 현재 위치를 선으로 연결한다.

```cpp
case EVENT_MOUSEMOVE:
    if (pushed)
    {
        line(*img, ptOld, Point(x, y), Color::Red, 2);
        ptOld = Point(x, y);
    }
    break;
```

점들을 따로 찍는 것이 아니라 짧은 선분을 계속 연결하기 때문에 부드러운 drag 선처럼 보인다.

정리:
- button down -> drawing 시작
- mouse move -> 이전 좌표에서 현재 좌표까지 선 그리기
- button up -> drawing 종료

## mouse event data 구조체로 관리

`18_mouse_example.cpp`

이미지뿐 아니라 mouse 위치, 이전 위치, 현재 색상, button 상태가 필요해서 구조체로 묶었다.

```cpp
struct MouseData
{
    Mat canvas;
    Mat view;
    Point mousePosition;
    Point previousPosition;
    Scalar boxColor = Color::Red;
    bool leftButtonPressed = false;
};
```

- `canvas` -> 실제 선이 계속 저장되는 영상
- `view` -> mouse box까지 합쳐서 화면에 보여줄 영상
- `mousePosition` -> 현재 mouse 좌표
- `previousPosition` -> 이전 drawing 좌표
- `boxColor` -> box와 선의 현재 색상
- `leftButtonPressed` -> 왼쪽 button 상태

callback에는 구조체 주소를 전달한다.

```cpp
setMouseCallback("img", onMouse, &data);
```

```cpp
MouseData &data =
    *static_cast<MouseData *>(userData);
```

여러 상태를 전역 변수로 따로 만들지 않고 하나의 data로 관리할 수 있었다.

## 화면용 Mat과 drawing Mat 분리

mouse를 따라가는 사각형은 이전 위치에 흔적을 남기면 안 된다.<br>
그래서 실제 drawing이 저장되는 `canvas`를 복사해서 `view`를 만든다.

```cpp
void updateView(MouseData &data)
{
    data.view = data.canvas.clone();

    rectangle(
        data.view,
        Point(data.mousePosition.x - 25,
              data.mousePosition.y - 25),
        Point(data.mousePosition.x + 25,
              data.mousePosition.y + 25),
        data.boxColor,
        2,
        LINE_AA
    );
}
```

```text
canvas -> 선이 실제로 누적되는 원본
view   -> canvas 복사본 + 현재 위치의 사각형
```

mouse가 움직일 때마다 `view`를 새로 만들기 때문에 이전 사각형은 사라지고 현재 위치에만 보인다.

## 오른쪽 click으로 랜덤 색상 만들기

```cpp
case EVENT_RBUTTONDOWN:
{
    static RNG rng(getTickCount());

    data.boxColor = Scalar(
        rng.uniform(0, 256),
        rng.uniform(0, 256),
        rng.uniform(0, 256)
    );

    printColor("랜덤 색상", data.boxColor);
    break;
}
```

`RNG`는 OpenCV의 난수 생성기이다.

- `uniform(0, 256)` -> 0 이상 256 미만의 정수
- B, G, R channel에 각각 난수 생성
- 오른쪽 button을 누를 때 box와 drawing 색상이 같이 변경됨

출력 예:

```text
[랜덤 색상] BGR: (34, 182, 91)
```

OpenCV 색상 순서이므로 출력도 RGB가 아니라 BGR이다.

## 휠 button으로 스포이드 만들기

mouse wheel을 누르는 동작은 `EVENT_MBUTTONDOWN`으로 처리했다.

```cpp
case EVENT_MBUTTONDOWN:
    if (x >= 0 && x < data.canvas.cols &&
        y >= 0 && y < data.canvas.rows)
    {
        Vec3b pixel = data.canvas.at<Vec3b>(y, x);

        data.boxColor =
            Scalar(pixel[0], pixel[1], pixel[2]);

        printColor("스포이드", data.boxColor);
    }
    break;
```

컬러 `CV_8UC3` 영상의 pixel 하나는 `Vec3b`로 읽을 수 있다.

```text
pixel[0] -> B
pixel[1] -> G
pixel[2] -> R
```

Mat의 pixel 접근 순서는 `(y, x)`이다.

```cpp
data.canvas.at<Vec3b>(y, x);
```

`Point(x, y)` 순서와 반대처럼 보여서 헷갈릴 수 있다.

출력 예:

```text
[스포이드] BGR: (120, 88, 203)
```

주의:
- pixel에 접근하기 전에 x, y가 영상 범위 안인지 확인해야 함
- grayscale 영상이라면 `Vec3b`가 아니라 `uchar` 같은 1channel type을 사용해야 함

## 트랙바 만들기

`19_trackbar.cpp`

OpenCV 창에 값을 조절할 수 있는 trackbar를 추가했다.

```cpp
int pos = 0;

createTrackbar(
    "level",
    "img",
    &pos,
    255,
    on_level_change,
    (void *)&img
);
```

```text
createTrackbar(name, windowName, value,
               maxValue, callback, userData)
```

- trackbar 이름 -> `level`
- 붙일 창 이름 -> `img`
- 현재 값을 저장할 변수 -> `pos`
- 최댓값 -> 255
- 값이 변경될 때 호출할 함수 -> `on_level_change`
- callback에 전달할 data -> `img`

callback:

```cpp
void on_level_change(int pos, void *data)
{
    Mat *img = (Mat *)data;
    img->setTo(Scalar(pos, 0, 0));
}
```

trackbar 값이 바뀌면 영상 전체 pixel을 `(pos, 0, 0)`으로 변경한다.

OpenCV는 BGR 순서이므로 `pos`가 증가할수록 파란색 channel이 강해진다.

주의:
- 원본 lenna 영상이 밝아지는 것이 아니라 영상 전체를 같은 색으로 덮어씀
- 밝기 조절을 하려면 원본을 따로 보관하고 pixel 연산 결과를 출력해야 함
- loop에서 `cout << pos`를 계속 실행하므로 값이 바뀌지 않아도 매 frame 출력됨

## FileStorage로 YAML 저장

`20_filestorage.cpp`

OpenCV의 `FileStorage`를 사용해서 여러 자료형을 YAML 파일에 저장했다.

```cpp
FileStorage fs;
fs.open(
    folderPath + "mydata.yml",
    FileStorage::WRITE
);
```

- `FileStorage::WRITE` -> 새 파일을 쓰는 mode
- 같은 파일이 있으면 기존 내용이 바뀔 수 있음
- 확장자에 따라 YAML, XML, JSON 형식을 사용할 수 있음

값은 `<<` 연산자로 key와 value를 차례대로 전달한다.

```cpp
fs << "name" << name;
fs << "age" << age;
fs << "point" << pt1;
fs << "scores" << scores;
fs << "data" << mat1;
```

저장한 type:

```text
name   -> String
age    -> int
point  -> Point
scores -> vector<float>
data   -> Mat, 2 x 2 float
```

사용이 끝나면 파일을 닫는다.

```cpp
fs.release();
```

## YAML 저장 결과

실제 `mydata.yml` 일부:

```yaml
%YAML:1.0
---
name: Kim Chan Ho
age: 33
point: [ 100, 200 ]
scores: [ 3.14000010e+00, 6.65999985e+00, 9.14000034e+00 ]
data: !!opencv-matrix
   rows: 2
   cols: 2
   dt: f
   data: [ 1., 1.50000000e+00, 2., 3.20000005e+00 ]
```

Mat에는 크기와 자료형 정보도 같이 저장된다.

- `rows` -> 2
- `cols` -> 2
- `dt: f` -> float type
- `data` -> 실제 원소 값

float 값은 YAML에서 소수 표현이 조금 길게 보일 수 있다.<br>
이것은 이진 부동소수점 표현과 출력 정밀도 때문이고 저장 실패는 아니다.

## FileStorage에서 YAML 읽기

`21_filestorage2.cpp`

읽을 때는 `FileStorage::READ` mode를 사용한다.

```cpp
FileStorage fs;
fs.open(
    folderPath + "mydata.yml",
    FileStorage::READ
);
```

key로 node를 선택하고 `>>` 연산자로 변수에 저장한다.

```cpp
fs["name"] >> name;
fs["age"] >> age;
fs["point"] >> pt1;
fs["scores"] >> scores;
fs["data"] >> mat1;
```

저장할 때 사용한 type과 읽을 변수 type을 맞추는 것이 좋다.

실행 결과:

```text
Kim Chan Ho33[100, 200][3.1400001, 6.6599998, 9.1400003][1, 1.5;
 2, 3.2]
```

값은 정상적으로 읽혔지만 출력 사이에 공백이나 label을 넣지 않아서 붙어서 보인다.

```cpp
cout << "name: " << name << '\n'
     << "age: " << age << '\n'
     << "point: " << pt1 << '\n'
     << "scores: " << Mat(scores).t() << '\n'
     << "data:\n" << mat1 << endl;
```

주의:
- 파일이 열렸는지 `fs.isOpened()`로 확인하는 것이 안전함
- key가 없거나 type이 다르면 원하는 값이 들어오지 않을 수 있음
- 읽기가 끝나면 `release()`로 닫음

## mask를 이용한 부분 변경

`22_mask.cpp`

`setTo()`의 두 번째 argument에 mask를 전달했다.

```cpp
Mat img1 =
    imread(folderPath + "lenna.bmp");

Mat img2 =
    imread(
        folderPath + "mask_smile.bmp",
        IMREAD_GRAYSCALE
    );

img1.setTo(Color::Yellow, img2);
```

mask에서 값이 0이 아닌 pixel 위치만 노란색으로 변경된다.

```text
mask pixel == 0 -> 원본 유지
mask pixel != 0 -> Color::Yellow로 변경
```

mask는 보통 8bit 1channel 영상으로 사용한다.

```cpp
IMREAD_GRAYSCALE
```

현재 `lenna.bmp`와 `mask_smile.bmp`는 둘 다 `512 x 512`라서 같은 위치에 mask를 적용할 수 있다.

주의:
- mask 크기는 대상 영상 크기와 같아야 함
- mask는 보통 `CV_8UC1`
- grayscale 값이 꼭 255일 필요는 없고 0이 아니면 선택된 위치로 처리됨

## copyTo와 mask로 영상 합성

비행기 영상에서 mask가 선택한 부분만 배경 ROI에 복사했다.

```cpp
Mat roi = frame(roiRect);
airplane.copyTo(roi, maskAirPlane);
```

```text
source.copyTo(destination, mask)
```

- `airplane` -> 복사할 원본
- `roi` -> 결과가 들어갈 배경의 일부 영역
- `maskAirPlane` -> 복사할 pixel 위치

mask 값이 0인 위치는 배경이 그대로 남고, 0이 아닌 위치에는 비행기 pixel이 복사된다.

정리:
- `setTo(value, mask)` -> 선택된 위치를 같은 값으로 변경
- `copyTo(destination, mask)` -> 선택된 위치에 source pixel 복사

## 합성 영상 크기 맞추기

원본 비행기와 mask를 같은 비율로 줄였다.

```cpp
resize(
    airplane,
    airplane,
    Size(),
    0.5,
    0.5,
    INTER_AREA
);

resize(
    maskAirPlane,
    maskAirPlane,
    Size(),
    0.5,
    0.5,
    INTER_NEAREST
);
```

원본 크기는 `600 x 400`이고 0.5배 resize 후에는 `300 x 200`이 된다.

- 일반 컬러 영상 축소 -> `INTER_AREA`
- mask 축소 -> `INTER_NEAREST`

mask에 `INTER_NEAREST`를 사용하면 중간 grayscale 값이 새로 생기는 것을 줄일 수 있다.<br>
이진 mask의 경계를 유지할 때 자주 사용한다.

주의:
- source 영상과 mask는 resize 후에도 같은 크기여야 함
- mask를 일반 보간으로 resize하면 경계에 중간값이 생길 수 있음
- OpenCV mask는 0이 아닌 값을 모두 선택하므로 중간값도 선택된 pixel로 처리됨

## ROI 위에서 비행기 이동

매 frame마다 배경을 깊은 복사하고 현재 x 좌표에 ROI를 만든다.

```cpp
Mat frame = sky.clone();
Rect roiRect(
    x,
    y,
    airplane.cols,
    airplane.rows
);

Mat roi = frame(roiRect);
airplane.copyTo(roi, maskAirPlane);
```

배경 원본 `sky`를 직접 수정하지 않기 때문에 이전 위치의 비행기가 남지 않는다.

```text
sky   -> 변하지 않는 배경
frame -> 현재 화면을 만들기 위한 복사본
roi   -> 비행기가 들어갈 현재 영역
```

x 좌표는 `dx`만큼 이동한다.

```cpp
x += dx;
```

경계에 도달하면 이동 방향을 반대로 바꾼다.

```cpp
if (x <= 0 ||
    x + airplane.cols >= sky.cols)
{
    dx = -dx;
    flip(airplane, airplane, 1);
    flip(maskAirPlane, maskAirPlane, 1);
}
```

비행기와 mask를 둘 다 좌우 반전해서 이동 방향에 맞는 모습으로 바꾼다.

현재 크기:

```text
배경 width       = 600
비행기 width     = 300
가능한 x 좌표 범위 = 0 ~ 300
```

정리:
- ROI는 반드시 배경 범위 안에 있어야 함
- source와 mask를 함께 flip해야 모양과 선택 영역이 일치함
- 매 frame 배경을 clone하면 이동 흔적이 남지 않음
- mask를 이용하면 사각형 전체가 아니라 원하는 모양만 합성할 수 있음

---

## 영상의 밝기 조절

`23_brightness.cpp`에서는 grayscale 영상의 모든 pixel에 같은 값을 더해서 밝기를 조절했다.

```cpp
Mat img = imread(
    folderPath + "lenna.bmp",
    IMREAD_GRAYSCALE
);

Mat img2;
add(img, 100, img2);

Mat img3 = img + 100;
```

- 양수를 더하면 영상이 밝아짐
- 음수를 더하면 영상이 어두워짐
- `add()`와 `Mat + scalar` 연산은 결과를 영상 type의 범위에 맞게 포화시킴

현재 영상은 `CV_8UC1`이므로 pixel 값의 범위는 `0 ~ 255`이다.

```text
200 + 100 -> 255
```

300을 저장하지 않고 최댓값인 255가 된다.

### pixel에 직접 더하기

```cpp
Mat img4(img.rows, img.cols, img.type());

for (int j = 0; j < img.rows; j++)
{
    for (int i = 0; i < img.cols; i++)
    {
        img4.at<uchar>(j, i)
            = img.at<uchar>(j, i) + 100;
    }
}
```

- `j` -> row, y 좌표
- `i` -> column, x 좌표
- `at<uchar>(j, i)` -> grayscale pixel 하나에 접근

주의할 점:
- 위 코드는 `uchar`에 직접 대입하므로 값이 255를 넘으면 포화되지 않고 overflow가 발생할 수 있음
- 예를 들어 200에 100을 더한 300은 `uchar` 범위에서 다시 작은 값으로 돌아갈 수 있음
- 직접 pixel을 계산할 때는 `saturate_cast<uchar>()`를 사용하는 것이 안전하다

```cpp
img4.at<uchar>(j, i) =
    saturate_cast<uchar>(
        img.at<uchar>(j, i) + 100
    );
```

정리:
- 밝기 조절은 모든 pixel에 같은 값을 더하거나 빼는 연산
- OpenCV 산술 함수는 보통 포화 연산을 사용
- `uchar`에 직접 계산 결과를 넣을 때는 overflow를 확인해야 함

## 명암비 조절

명암비는 밝은 부분과 어두운 부분의 차이를 조절하는 것이다.

```cpp
Mat img = imread(
    folderPath + "hawkes.bmp",
    IMREAD_GRAYSCALE
);

Mat img2 = 2.f * img;
```

모든 pixel 값에 2를 곱한다.

- 어두운 값도 커짐
- 밝은 값은 더 빠르게 255에 도달함
- 전체 밝기도 같이 올라갈 수 있음

중간 밝기 128을 기준으로 명암비를 조절할 수도 있다.

```cpp
Mat img3 = img + (img - 128) * 1.f;
```

수식으로 보면 아래와 같다.

```text
dst = src + (src - 128) * alpha
```

- 128보다 밝은 pixel -> 더 밝아짐
- 128보다 어두운 pixel -> 더 어두워짐
- 128 근처의 pixel -> 변화가 작음

현재 `alpha`는 `1.f`이므로 128을 기준으로 차이를 두 배로 만든다.

## 명암비 스트레칭

영상에서 실제로 사용 중인 최솟값과 최댓값을 `0 ~ 255` 범위로 늘릴 수 있다.

```cpp
double min, max;
minMaxLoc(img, &min, &max);

Mat img4 =
    (img - min) * 255 / (max - min);
```

```text
원본 최솟값 -> 0
원본 최댓값 -> 255
```

좁은 범위에 모여 있던 밝기값을 넓게 사용하므로 명암비가 좋아질 수 있다.

주의할 점:
- 모든 pixel 값이 같으면 `max - min`이 0이 됨
- 일반화해서 함수로 만들 때는 0으로 나누는 경우를 확인해야 함

## 히스토그램 평활화

```cpp
Mat img5;
equalizeHist(img, img5);
```

`equalizeHist()`는 grayscale 영상의 밝기 분포가 더 넓게 사용되도록 변환한다.

- 입력 영상은 8bit 1 channel이어야 함
- 단순히 최솟값과 최댓값만 늘리는 방식과는 다름
- 누적 히스토그램을 이용해 밝기값을 다시 배치함

정리:
- 곱셈 -> 간단한 명암비 증가, 밝기도 같이 변할 수 있음
- 중심 기준 조절 -> 기준 밝기를 중심으로 차이를 조절
- stretching -> 현재 min, max를 전체 범위로 확장
- equalization -> 밝기 분포를 기준으로 다시 배치

## grayscale 히스토그램 계산

히스토그램은 각 밝기값을 가진 pixel이 몇 개인지 나타낸다.

```cpp
Mat calcGrayHist(const Mat &img)
{
    CV_Assert(img.type() == CV_8UC1);

    Mat hist;
    int channel[] = {0};
    int dims = 1;
    const int histSize[] = {256};
    float graylevel[] = {0, 256};
    const float *ranges[] = {graylevel};

    calcHist(
        &img,
        1,
        channel,
        noArray(),
        hist,
        dims,
        histSize,
        ranges
    );

    return hist;
}
```

설정값:

```text
channel  = 0
dims     = 1
histSize = 256
range    = [0, 256)
```

- grayscale은 channel이 1개라서 0번 channel 사용
- 밝기값 `0 ~ 255`를 256개의 구간으로 계산
- range의 마지막 256은 포함되지 않는 끝값
- mask 자리에 `noArray()`를 전달해서 전체 영상을 계산

`calcHist()` 결과는 현재 설정에서 보통 `CV_32FC1`이고 `256 x 1` 형태이다.

```cpp
CV_Assert(hist.type() == CV_32FC1);
CV_Assert(hist.size() == Size(1, 256));
```

`Size(width, height)` 순서이므로 `Size(1, 256)`은 1열 256행이다.

## 히스토그램 영상으로 표시

```cpp
double histMax;
minMaxLoc(hist, 0, &histMax);

Mat imgHist(
    100,
    256,
    CV_8UC1,
    Scalar(255)
);
```

- width 256 -> 밝기값 0부터 255까지 표시
- height 100 -> 막대 높이를 100 pixel 안으로 정규화
- 배경은 흰색

각 밝기값의 빈도에 따라 검은 선을 그린다.

```cpp
for (int i = 0; i < 256; ++i)
{
    int height = cvRound(
        hist.at<float>(i, 0)
        / histMax
        * 100
    );

    line(
        imgHist,
        Point(i, 100),
        Point(i, 100 - height),
        Color::Black
    );
}
```

OpenCV 영상 좌표는 아래로 갈수록 y가 커진다.<br>
그래서 histogram 막대를 위쪽으로 그리려면 `100 - height`로 계산한다.

주의할 점:
- 원본 코드의 괄호 위치로는 `cvRound()`가 빈도값에 먼저 적용됨
- 위처럼 비율 계산 전체를 반올림하면 계산 의도가 더 분명함
- `histMax`가 0인 경우에는 나눗셈을 하지 않도록 확인 필요

정리:
- histogram의 x축 -> 밝기값
- histogram의 y축 -> 해당 밝기값의 pixel 개수
- 밝기와 명암비를 바꾼 뒤 histogram 모양도 같이 비교할 수 있음

## 영상의 비트 연산

`26_arithmetic.cpp`에서는 같은 크기의 두 grayscale 영상에 비트 연산을 적용했다.

```cpp
Mat img = imread(
    folderPath + "lenna256.bmp",
    IMREAD_GRAYSCALE
);

Mat img2 = imread(
    folderPath + "square.bmp",
    IMREAD_GRAYSCALE
);
```

```cpp
bitwise_and(img, img2, dst1);
bitwise_or(img, img2, dst2);
bitwise_xor(img, img2, dst3);
bitwise_not(img, dst4);
```

- `bitwise_and()` -> 두 pixel의 bit가 모두 1인 부분
- `bitwise_or()` -> 하나라도 1인 부분
- `bitwise_xor()` -> 두 bit가 서로 다른 부분
- `bitwise_not()` -> 각 bit를 반전

이진 mask 영상에서는 선택 영역을 합치거나 빼는 동작으로 이해하기 쉽다.<br>
일반 grayscale 영상에서는 각 pixel의 8bit 값에 그대로 연산된다.

## 영상의 산술 연산

```cpp
add(img, img2, dst5);
addWeighted(img, 0.9, img2, 0.1, 0, dst6);
subtract(img, img2, dst7);
absdiff(img, img2, dst8);
```

`addWeighted()` 계산:

```text
dst = img * 0.9 + img2 * 0.1 + 0
```

두 영상을 서로 다른 비율로 섞을 수 있다.

- `add()` -> 두 영상의 pixel 값을 더함
- `subtract()` -> 첫 번째 영상에서 두 번째 영상을 뺌
- `absdiff()` -> 두 영상 pixel 차이의 절댓값

주의할 점:
- 입력 영상의 크기와 channel 수가 같아야 함
- 일반적인 8bit 영상의 `add()`, `subtract()`는 범위를 벗어나면 포화됨
- `subtract()`는 음수가 0으로 포화되지만 `absdiff()`는 방향 없이 차이의 크기를 보여줌

여러 영상을 `vector<pair<string, Mat>>`로 묶어서 반복 출력했다.

```cpp
vector<pair<string, Mat>> images = {
    {"lenna", img},
    {"square", img2},
    {"and", dst1},
    {"or", dst2},
    {"xor", dst3},
    {"not", dst4},
    {"add", dst5},
    {"addWeighted", dst6},
    {"subtract", dst7},
    {"absdiff", dst8},
};

for (auto [name, image] : images)
{
    imshow(name, image);
}
```

`auto [name, image]`는 C++17의 structured binding이다.<br>
`pair`의 첫 번째 값과 두 번째 값을 이름으로 나누어 받을 수 있다.

## 공간 필터와 kernel

공간 필터링은 현재 pixel과 주변 pixel을 함께 사용해서 새 값을 계산한다.

```text
입력 영상의 주변 영역
        *
      kernel
        =
출력 영상의 한 pixel
```

kernel은 어떤 주변 값을 어느 정도 사용할지 정하는 작은 행렬이다.

`filter2D()` 기본 형태:

```cpp
filter2D(
    src,
    dst,
    ddepth,
    kernel,
    anchor,
    delta,
    borderType
);
```

- `ddepth = -1` -> 입력 영상과 같은 depth로 출력
- `anchor = Point(-1, -1)` -> kernel 중심을 anchor로 사용
- `delta = 0` -> 계산 결과에 추가할 값 없음
- `BORDER_REPLICATE` -> 가장자리 pixel을 복제해서 바깥 영역 처리

## 엠보싱 필터

엠보싱은 밝기 변화가 있는 경계를 이용해서 영상이 돌출된 것처럼 보이게 한다.

3 x 3 kernel 예:

```cpp
float data[] = {
    -1, -1, 0,
    -1,  0, 1,
     0,  1, 1
};

Mat emboss(3, 3, CV_32FC1, data);
filter2D(
    img,
    img,
    -1,
    emboss,
    Point(-1, -1),
    128,
    BORDER_REPLICATE
);
```

`delta`에 128을 더하면 음수 방향의 경계도 중간 회색을 기준으로 표현하기 쉽다.

현재 파일에는 아래 부분을 확인해야 한다.

```text
opencv/part3/27_embossing,cpp
```

- 확장자가 `.cpp`가 아니라 `,cpp`라서 CMake의 `"*.cpp"` 검색에 포함되지 않음
- 현재 kernel의 `-1.-1`은 쉼표가 빠져 `-2` 계산식 하나가 됨
- 배열 값도 8개만 명시되어 마지막 한 칸은 0으로 초기화됨

정리:
- 파일명을 `27_embossing.cpp`로 바꿔야 자동 build 대상이 됨
- kernel은 3 x 3에 맞게 9개 값을 구분해서 작성해야 함
- 엠보싱 결과가 너무 어두우면 `delta` 값도 확인

## 평균값 blur

평균값 filter는 주변 pixel의 평균을 사용해서 영상을 부드럽게 만든다.

```cpp
float data[] = {
    1, 1, 1,
    1, 1, 1,
    1, 1, 1
};

Mat kernel(3, 3, CV_32FC1, data);
kernel = kernel / 9.0;

filter2D(
    img,
    img,
    -1,
    kernel,
    Point(-1, -1),
    0,
    BORDER_REPLICATE
);
```

3 x 3의 9개 값을 모두 더한 뒤 9로 나누는 것과 같다.

OpenCV의 `blur()`를 사용하면 같은 형태를 더 간단하게 작성할 수 있다.

```cpp
blur(
    frame,
    frame,
    Size(pos * 2 + 1, pos * 2 + 1)
);
```

kernel 크기를 홀수로 만드는 이유는 중심 pixel을 정하기 쉽기 때문이다.

```text
pos = 1 -> 3 x 3
pos = 2 -> 5 x 5
pos = 3 -> 7 x 7
```

## Gaussian blur와 trackbar

현재 실습에서는 카메라 frame에 Gaussian blur를 적용했다.

```cpp
int pos = 1;
namedWindow("frame");
createTrackbar("blur", "frame", &pos, 30);

GaussianBlur(
    frame,
    frame,
    Size(0, 0),
    double(pos)
);
```

`Size(0, 0)`을 주면 sigma 값을 기준으로 kernel 크기를 OpenCV가 계산한다.

- `pos`가 커짐
- sigma가 커짐
- 더 넓은 주변 pixel이 섞임
- 영상이 더 흐려짐

주의할 점:
- trackbar를 0으로 옮기면 `sigmaX = 0`이고 kernel 크기도 비어 있어 assertion error가 날 수 있음
- 최소 sigma가 1 이상이 되도록 보정하는 것이 안전함

```cpp
double sigma = max(pos, 1);
GaussianBlur(
    frame,
    frame,
    Size(0, 0),
    sigma
);
```

평균값 blur는 주변 pixel을 같은 비중으로 사용하고, Gaussian blur는 중심에 가까운 pixel에 더 큰 가중치를 준다.

## unsharp mask를 이용한 sharpening

`29_sharpening.cpp`에서는 원본 영상과 blur 영상을 이용해 선명도를 높였다.

```cpp
GaussianBlur(
    frame,
    blurM,
    Size(0, 0),
    double(pos)
);

dst =
    (1 + (float)pos * 0.1) * frame
    - (float)pos * 0.1 * blurM;
```

수식:

```text
dst = (1 + alpha) * src - alpha * blurred
```

다시 정리하면 아래와 비슷하다.

```text
detail = src - blurred
dst = src + alpha * detail
```

blur 영상과 원본의 차이를 detail로 보고 원본에 더한다.

확인한 점:
- `alpha`가 커질수록 경계가 더 강조됨
- 너무 크게 적용하면 noise도 같이 강조될 수 있음
- 밝은 경계나 어두운 경계 주변에 부자연스러운 halo가 생길 수 있음

현재 코드는 `pos`를 Gaussian sigma와 sharpening 강도에 동시에 사용한다.<br>
두 값의 역할이 다르므로 나중에는 trackbar를 따로 만들 수도 있다.

## Gaussian noise 만들기

`30_Bilateral.cpp`에서는 원본 grayscale 영상에 정규분포 noise를 추가했다.

```cpp
Mat noise(img.size(), CV_32SC1);
randn(noise, 0, 15);
add(img, noise, img, Mat(), CV_8U);
```

- `randn()` -> 정규분포 난수 생성
- 평균 0
- 표준편차 15
- noise는 음수와 양수를 모두 가지므로 `CV_32SC1` 사용
- 최종 출력 type은 `CV_8U`

`add()`가 결과를 `CV_8U` 범위인 `0 ~ 255`로 포화시킨다.

원본은 먼저 깊은 복사해두었다.

```cpp
images.push_back(img.clone());
```

이후 `img`에 noise를 직접 더해도 vector에 저장한 원본 영상은 변하지 않는다.

## Gaussian filter와 bilateral filter 비교

```cpp
GaussianBlur(
    img,
    images[2],
    Size(),
    5
);

bilateralFilter(
    img,
    images[3],
    -1,
    10,
    5
);
```

Gaussian filter:
- noise를 줄이고 영상을 부드럽게 만듦
- 경계도 같이 흐려질 수 있음

bilateral filter:
- 공간적으로 가까운 pixel을 확인
- 밝기값이 비슷한 pixel에 더 큰 가중치를 줌
- 경계를 비교적 유지하면서 noise를 줄일 수 있음

`bilateralFilter()` argument:

```text
d          = -1
sigmaColor = 10
sigmaSpace = 5
```

- `d = -1` -> `sigmaSpace`를 기준으로 filter 크기 계산
- `sigmaColor` -> 밝기값 차이를 어느 정도까지 비슷하다고 볼지 결정
- `sigmaSpace` -> 공간적으로 어느 정도 거리까지 볼지 결정

주의:
- bilateral filter는 Gaussian blur보다 계산량이 큰 편
- `sigmaColor`가 너무 작으면 noise 제거 효과가 약할 수 있음
- `sigmaColor`가 커지면 밝기 차이가 큰 pixel도 더 많이 섞일 수 있음

## 어파인 변환

어파인 변환은 직선의 성질을 유지하면서 영상을 이동, 확대/축소, 회전, 전단할 수 있는 변환이다.

2차원 어파인 변환 행렬은 2 x 3 형태로 사용한다.

```text
[ a  b  tx ]
[ c  d  ty ]
```

좌표 계산:

```text
x' = a*x + b*y + tx
y' = c*x + d*y + ty
```

OpenCV에서는 `warpAffine()`으로 변환을 적용한다.

```cpp
warpAffine(
    src,
    dst,
    M,
    outputSize
);
```

## 이동 변환

```cpp
Mat M = Mat_<double>(
    {2, 3},
    {
        1, 0, 150,
        0, 1, 100
    }
);

warpAffine(
    img,
    images[1],
    M,
    img.size() + Size(150, 100)
);
```

변환 행렬:

```text
[ 1  0  150 ]
[ 0  1  100 ]
```

- x 방향으로 150 pixel 이동
- y 방향으로 100 pixel 이동
- 출력 크기도 늘려서 이동한 영상이 잘리지 않게 함

주의:
- 출력 영상 크기를 원본과 같게 두면 오른쪽과 아래쪽으로 이동한 부분이 잘릴 수 있음

## 전단 변환

```cpp
double mx = 0.3;
double my = 0.2;

M = Mat_<double>(
    {2, 3},
    {
        1,  mx, 0,
        my, 1,  0
    }
);

warpAffine(
    img,
    images[2],
    M,
    Size()
);
```

전단 변환은 한 축의 좌표에 다른 축의 값을 섞어서 영상을 기울인다.

```text
x' = x + mx*y
y' = my*x + y
```

주의할 점:
- 현재 OpenCV 4.5.4 환경에서 빈 `Size()`를 전달하면 출력 크기가 원본 크기로 결정됨
- 전단된 영상이 원본 크기 밖으로 나가면 해당 부분은 잘릴 수 있음
- 전체 결과를 보려면 변환 후 필요한 출력 크기를 직접 계산해서 전달해야 함

```cpp
warpAffine(
    img,
    images[2],
    M,
    img.size()
);
```

## 세 점으로 어파인 행렬 구하기

어파인 변환은 서로 일직선 위에 있지 않은 세 점의 변환 관계로 행렬을 구할 수 있다.

```cpp
Point2f srcPts[3];
Point2f dstPts[3];

srcPts[0] = Point2f(0, 0);
srcPts[1] = Point2f(1, 0);
srcPts[2] = Point2f(1, 1);

dstPts[0] = Point2f(0, 0);
dstPts[1] = Point2f(2, 1);
dstPts[2] = Point2f(1.5, 1.3);

M = getAffineTransform(srcPts, dstPts);
```

```cpp
warpAffine(
    img,
    images[3],
    M,
    img.size() + Size(500, 500)
);
```

`getAffineTransform()`이 세 source 좌표와 세 destination 좌표의 관계를 만족하는 2 x 3 행렬을 반환한다.

현재 좌표는 0과 1을 사용하는 단위 좌표 형태이다.<br>
영상의 실제 모서리를 기준으로 변형하려면 `img.cols`, `img.rows`를 이용해 점을 정할 수 있다.

```cpp
Point2f srcPts[3] = {
    Point2f(0, 0),
    Point2f(img.cols - 1.f, 0),
    Point2f(0, img.rows - 1.f)
};
```

정리:
- `warpAffine()` -> 2 x 3 변환 행렬을 영상에 적용
- 이동값은 행렬의 마지막 열에 들어감
- 전단은 x와 y 좌표를 서로 섞음
- 세 점의 이동 관계로 어파인 행렬을 계산할 수 있음
- 변환 후 영상이 잘리지 않도록 출력 크기를 같이 확인해야 함

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

# C++ 학습 정리

## 저장소 구성

- `practice/chap01`: C++ 첫 프로그램과 표준 출력
- `practice/chap02`: namespace, 문자열, 함수 분리, C에서 C++로 전환
- `practice/chap03`: class와 객체 기초
- `practice/chap04`: 생성자, 멤버 접근, 객체 사용
- `practice/chap05`: reference, pointer, 동적 메모리, 복사 생성자
- `practice/chap06`: static member와 공유 상태
- `practice/chap07`: 상속 기초
- `practice/ctocpp`: C 스타일 코드를 C++ 스타일로 바꾸는 연습

## C에서 C++로 넘어가는 관점

C에서는 data와 function이 따로 존재함. C++에서는 관련 data와 function을 class 안에 묶어 객체로 다룸.

```text
C: 함수가 데이터를 처리한다.
C++: 객체가 자신의 상태와 동작을 가진다.
```

이 차이 때문에 C++에서는 “어떤 함수가 어떤 data를 바꾸는가”보다 “어떤 객체가 어떤 책임을 가지는가”를 더 많이 생각함.

## `iostream`과 stream 입출력

C의 `printf`, `scanf`는 format string을 사용함. C++의 `cout`, `cin`은 stream 연산자 `<<`, `>>`를 사용함.

[00_hello_world.cpp](./practice/chap01/00_hello_world.cpp)의 기본 형태는 다음과 같음.

```cpp
#include <iostream>

int main()
{
    std::cout << "Hello World" << std::endl;
    return 0;
}
```

`std::cout`은 표준 출력 stream이고, `std::endl`은 줄바꿈과 flush를 의미함. `using namespace std;`를 쓰면 짧게 쓸 수 있지만, 이름이 어디서 왔는지 흐려질 수 있음.

## namespace

namespace는 이름 충돌을 막기 위한 범위임. `practice/chap02/namespace` 예제처럼 여러 사람이 같은 함수 이름을 써도 namespace가 다르면 구분할 수 있음.

```cpp
namespace mike {
    void foo();
}

namespace kitae {
    void foo();
}
```

이 구조는 큰 프로젝트에서 중요함. C의 header/source 분리와 비슷하지만, C++에서는 namespace와 class까지 함께 사용해 이름의 소속을 더 분명히 함.

## reference

reference는 기존 변수에 붙는 별칭임. pointer처럼 주소를 다루는 효과가 있지만 문법은 일반 변수처럼 씀.

```cpp
int n = 10;
int& ref = n;
ref = 20;
```

`ref`를 바꾸면 실제로는 `n`이 바뀜. reference는 선언할 때 반드시 초기화해야 하고, 다른 대상을 다시 가리키게 바꿀 수 없음. 함수 인자로 원본을 바꾸고 싶지만 pointer 문법을 덜 노출하고 싶을 때 유용함.

## pointer와 reference 비교

pointer는 주소를 저장하는 변수이고 `nullptr`일 수 있음. reference는 반드시 어떤 대상의 별칭이어야 함.

- pointer: `int *p = &n;`, `*p`, `p->member`
- reference: `int &r = n;`, 일반 변수처럼 사용

`chap05`의 주소/reference 실습은 C에서 배운 포인터 개념을 C++의 reference와 비교하는 단계임.

## class

class는 data와 function을 하나로 묶는 사용자 정의 타입임. 멤버 변수는 객체의 상태를 저장하고, 멤버 함수는 그 상태를 사용하는 동작임.

```cpp
class Circle {
private:
    int radius;

public:
    double getArea();
};
```

`private`는 class 내부에서만 접근할 수 있고, `public`은 외부에서 사용할 수 있는 interface임. 좋은 class는 내부 data를 직접 열어두기보다 필요한 동작만 public 함수로 제공함.

## 생성자와 소멸자

생성자는 객체가 만들어질 때 자동으로 호출되어 초기화를 담당함. 소멸자는 객체 수명이 끝날 때 자동으로 호출되어 정리를 담당함.

```text
객체 생성 -> 생성자 호출 -> 객체 사용 -> 객체 소멸 -> 소멸자 호출
```

동적 메모리나 파일 같은 자원을 class가 소유하면 생성자와 소멸자가 더 중요해짐. 생성자에서 확보한 자원은 소멸자에서 정리해야 함.

## 복사 생성자와 깊은 복사

`ex_book.cpp`는 C++에서 특히 중요한 복사 문제를 보여줌. 객체 안에 `char *`처럼 동적 메모리를 가리키는 멤버가 있으면 단순 복사는 주소만 복사함. 그러면 두 객체가 같은 메모리를 공유하게 됨.

```cpp
Book::Book(const Book& b)
{
    title = new char[strlen(b.title) + 1];
    strcpy(title, b.title);
    price = b.price;
}
```

이런 식으로 새 메모리를 만들고 내용을 복사해야 깊은 복사가 됨. 그렇지 않으면 한 객체가 메모리를 해제한 뒤 다른 객체가 같은 주소를 다시 사용하거나 해제하는 문제가 생길 수 있음.

## 동적 할당과 `new`/`delete`

C의 `malloc/free`와 달리 C++에서는 `new/delete`를 사용함. 객체를 `new`로 만들면 생성자가 호출되고, `delete`하면 소멸자가 호출됨. 배열을 만들었으면 `delete[]`로 해제해야 함.

현대 C++에서는 직접 `new/delete`를 많이 쓰기보다 `std::string`, `std::vector`, smart pointer를 사용해 소유권 문제를 줄임. 하지만 실습 단계에서는 raw pointer로 문제를 직접 겪어봐야 왜 이런 도구가 필요한지 이해됨.

## static member

일반 멤버 변수는 객체마다 따로 존재함. static 멤버는 class 차원에 하나만 존재하고 모든 객체가 공유함.

```text
일반 member: 객체마다 따로 존재
static member: class에 하나만 존재
```

생성된 객체 수, 공통 설정값, 전체 합계처럼 모든 객체가 함께 봐야 하는 값에 static을 사용할 수 있음.

## 상속

상속은 기존 class의 특징을 물려받아 새 class를 만드는 기능임. `chap07`은 객체지향의 재사용 구조로 넘어가는 단계임. 상속을 쓰면 공통 코드를 부모 class에 두고, 다른 부분만 자식 class에서 확장할 수 있음.

다만 상속은 관계를 강하게 묶음. 단순히 코드가 비슷하다는 이유만으로 상속을 쓰기보다 “자식이 부모의 한 종류인가”를 생각해야 함.

## C 스타일에서 C++ 스타일로

`ctocpp` 실습은 C에서 배운 배열, 문자열, 함수 중심 코드를 C++스럽게 바꾸는 연습임. 핵심은 문법을 바꾸는 것이 아니라 책임을 옮기는 것임.

- 문자열: `char[]`에서 `std::string` 사고로 이동
- 배열: 직접 크기 관리에서 container 사고로 이동
- 함수 묶음: 관련 data와 함께 class로 이동

이 전환을 이해하면 C++이 단순히 C에 문법을 더한 언어가 아니라, program을 조직하는 방식이 달라지는 언어라는 점이 보임.

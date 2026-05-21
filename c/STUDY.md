# C 학습 정리

## 저장소 구성

- `basics/part1`: 출력, 자료형, 문자, 연산자, 기본 입출력
- `basics/part2`: 조건문, 반복문, 배열, 난수, 기초 알고리즘
- `basics/part3`: 함수, 포인터, 배열과 포인터, 정렬, 함수 포인터
- `basics/part4`: 여러 파일로 나눈 작은 프로그램
- `basics/part5`: 문자열, 구조체, enum, union, 문자 파일 입출력
- `basics/part6`: 동적 메모리, 파일 포인터, file descriptor
- `ds`: stack, queue, list
- `projects/bowlingGame`: 규칙 기반 점수 계산 프로젝트

## C 프로그램의 기본 형태

C는 source file을 compiler가 기계어에 가까운 실행 파일로 바꾸는 언어임. 가장 기본적인 구조는 `#include`, `main()`, 문장, `return`임. `#include <stdio.h>`는 `printf`, `scanf` 같은 표준 입출력 함수의 선언을 compiler에게 알려줌.

[hello.c](./basics/part1/hello.c)에서 보듯 `main()`은 프로그램 시작점임.

```c
#include <stdio.h>

int main(void)
{
    printf("Hello, world \n");
    return 0;
}
```

여기서 `int main(void)`는 “인자를 받지 않고 정수를 반환하는 시작 함수”라는 뜻임. `return 0`은 운영체제에 정상 종료를 알리는 관습적인 값임.

## 자료형과 메모리 크기

C에서 변수는 정해진 크기의 메모리 공간임. `char`, `int`, `double`은 값의 종류뿐 아니라 차지하는 byte 수와 표현 가능한 범위가 다름. `sizeof` 실습은 “변수는 메모리에 저장된다”는 관점을 잡기 위한 코드임.

문자도 내부적으로는 숫자임. [charNumber.c](./basics/part1/charNumber.c)처럼 `%c`와 `%d`를 함께 출력하면 같은 값이 문자와 정수로 다르게 해석되는 것을 볼 수 있음.

```c
char ch1 = 'A';
char ch2 = 64;
printf("ch1: %c Number: %d\n", ch1, ch1);
printf("ch2: %c Number: %d\n", ch2, ch2);
```

`'A'`는 문자 literal이지만 ASCII 값으로는 정수임. 이 감각이 있어야 대소문자 변환, 알파벳 판별, 문자열 처리 코드를 이해하기 쉬움.

## 입력과 주소 연산자

`scanf()`는 값을 저장할 위치를 알아야 하므로 변수의 주소를 넘겨야 함. 그래서 `scanf("%d", &num)`처럼 `&`를 붙임. `&num`은 “num이라는 변수의 주소”임.

이 개념은 뒤에서 포인터로 이어짐. 초반에는 `scanf` 때문에 `&`를 외우는 것처럼 보이지만, 실제로는 함수가 호출된 곳의 변수 값을 바꾸기 위한 주소 전달임.

## 조건문과 삼항 연산자

조건문은 값을 분류하는 도구임. `if`, `else if`, `else`는 조건이 참인지 거짓인지에 따라 다른 문장을 실행함. `compare.c`, `passFail.c`, `scoreGrade.c`, `oddEven.c` 같은 예제는 모두 입력값을 조건식으로 나누는 연습임.

삼항 연산자 `조건 ? 참값 : 거짓값`은 간단한 조건 결과를 값으로 만들 때 사용함.

```c
printf("%c는 %s\n", ch, isAlphabet ? "알파벳입니다" : "알파벳이 아닙니다");
```

이 코드는 `isAlphabet`이 참이면 앞 문자열, 거짓이면 뒤 문자열을 선택함. 조건문이 “실행 흐름”을 나눈다면, 삼항 연산자는 “값 선택”에 가깝음.

## 반복문과 누적

반복문은 같은 규칙을 여러 번 적용함. `for`는 반복 횟수가 비교적 명확할 때, `while`은 조건이 계속 참인 동안 반복할 때 자주 씀. `oneToTenFor.c`, `one2TenSum.c`, `a2bSum.c`는 loop 변수와 누적 변수의 변화를 보는 실습임.

```c
int sum = 0;
for (int i = 1; i <= 10; i++) {
    sum += i;
}
```

여기서 중요한 값은 `i`와 `sum`임. `i`는 반복 위치를 나타내고, `sum`은 이전 결과를 계속 쌓음. `star.c`, `xstar.c`, `sumMatrix.c`처럼 중첩 반복문이 나오면 바깥 반복과 안쪽 반복이 각각 어떤 차원을 담당하는지 나누어 보면 됨.

## 배열과 문자열

배열은 같은 타입의 값을 연속된 메모리에 저장함. `arrayInit.c`, `sumArray.c`, `findMax.c`, `sumMatrix.c`는 index로 여러 값을 순회하는 감각을 익히기 위한 코드임.

문자열은 `char` 배열로 볼 수 있고, 끝에는 null 문자 `'\0'`이 있어야 함. `stringCopy.c`, `stringExample.c`, `string3.c`에서는 문자 하나씩 복사하거나 길이를 확인하는 방식이 나옴.

문자열을 다룰 때는 두 가지를 계속 봐야 함.

- 배열의 크기를 넘지 않는가
- 문자열 끝을 나타내는 `'\0'`을 처리했는가

## 함수와 값 전달

함수는 반복되는 코드를 이름 붙여 분리하는 도구임. C에서 함수 인자는 기본적으로 값이 복사되어 전달됨. 그래서 함수 안에서 인자 값을 바꿔도 호출한 쪽의 원본 변수는 그대로임.

`add.c` 같은 단순 함수는 return 값을 이해하기 좋고, `swap.c`는 값 전달의 한계를 보여줌. 두 변수의 값을 함수 안에서 바꾸려면 변수 값이 아니라 주소를 넘겨야 함.

## 포인터

포인터는 주소를 저장하는 변수임. C에서 포인터가 중요한 이유는 함수 밖의 값을 바꾸고, 배열과 문자열을 효율적으로 넘기고, 동적 메모리와 자료구조를 직접 연결하기 위해서임.

[swap.c](./basics/part3/swap.c)의 핵심은 다음 패턴임.

```c
void swap(int *pa, int *pb)
{
    int temp = *pa;
    *pa = *pb;
    *pb = temp;
}
```

`pa`와 `pb`는 `int` 값이 아니라 `int`가 저장된 위치를 가리킴. `*pa`는 그 주소에 들어 있는 실제 값임. 이 구조를 이해하면 `scanf`에서 `&`를 쓰는 이유도 자연스럽게 연결됨.

배열 이름은 많은 상황에서 첫 번째 요소의 주소처럼 동작함. 그래서 배열을 함수로 넘길 때 전체 배열이 복사되는 것이 아니라 시작 주소가 전달됨. 이 때문에 함수 안에서는 배열 크기를 따로 넘기거나, 문자열처럼 종료 조건을 정해야 함.

## 함수 포인터와 `void *`

`pointer5_functionpointer.c`는 함수도 주소를 가질 수 있다는 점을 보여줌. 함수 포인터는 “어떤 함수를 나중에 호출할지”를 변수처럼 넘길 수 있게 함. `qsort.c`에서 비교 함수를 넘기는 방식과 연결됨.

`void *`는 특정 타입이 정해지지 않은 주소임. 어떤 타입이든 받을 수 있지만, 사용할 때는 원래 타입으로 해석해야 하므로 더 조심해야 함.

## 정렬

`bubbleSorting.c`, `selectionSorting.c`, `qsort.c`는 배열 안의 값을 비교하고 위치를 바꾸는 실습임. 선택 정렬은 현재 위치에 들어갈 값을 찾고, 버블 정렬은 인접한 값을 비교하며 큰 값을 뒤로 보냄.

`qsort()`는 표준 library 정렬 함수임. 정렬 기준은 data type마다 다르기 때문에 비교 함수를 인자로 받음. 이 지점에서 배열, 포인터, 함수 포인터가 한 번에 연결됨.

## 구조체

구조체는 서로 관련 있는 값을 하나의 타입으로 묶음. `struct.c`, `structArray.c`, `date/`, `twoDouble/` 실습은 “여러 변수를 의미 있는 단위로 묶는 법”을 보여줌.

```c
typedef struct {
    int year;
    int month;
    int day;
} Date;
```

구조체를 쓰면 `year`, `month`, `day`가 따로 떠다니지 않고 `Date`라는 하나의 값으로 묶임. 자료구조로 넘어가면 구조체 안에 다음 node의 주소를 넣어 연결 리스트를 만들 수 있음.

## enum과 union

`enum`은 이름 있는 정수 상수 묶음임. 상태값이나 선택지를 숫자로만 쓰는 것보다 의미가 분명해짐. `union`은 여러 멤버가 같은 메모리 공간을 공유함. 동시에 여러 값을 보관하는 구조체와 달리, union은 한 번에 하나의 해석만 의미가 있음.

## 파일 입출력

`charGetPut*.c`, `filePointer.c`, `fileDescriptor.c`, `scoreProcess/`는 프로그램 밖의 데이터를 다루는 실습임. `FILE *` 기반 입출력은 C 표준 library의 추상화이고, file descriptor는 운영체제에 더 가까운 낮은 수준의 파일 식별자임.

파일은 열고, 읽거나 쓰고, 닫는 흐름이 중요함. 닫지 않으면 buffer가 남거나 자원이 해제되지 않을 수 있음.

## 동적 메모리

`dynamicAllocation*.c`는 실행 중 필요한 크기의 메모리를 heap에서 확보하는 실습임. `malloc()`으로 받은 메모리는 직접 `free()`해야 함.

```c
int *arr = malloc(sizeof(int) * count);
if (arr == NULL) {
    return 1;
}
free(arr);
```

동적 메모리에서 중요한 것은 소유권임. 누가 할당했고, 누가 해제할지 정해지지 않으면 memory leak이나 잘못된 접근이 생김.

## 자료구조

stack은 마지막에 넣은 값이 먼저 나오는 LIFO 구조임. queue는 먼저 넣은 값이 먼저 나오는 FIFO 구조임. list는 node들이 pointer로 연결된 구조임.

배열 기반 stack/queue는 index 관리가 중요하고, list는 node 생성과 연결 변경이 중요함. `struct`는 data 묶음, pointer는 연결, header file은 외부에 공개할 함수 목록을 담당함.

## 프로젝트 구성

`bowlingGame`은 문법 실습을 넘어 규칙 기반 프로그램을 구성하는 단계임. `main.c`는 실행 흐름, `bowling.c`는 점수 계산 구현, `bowling.h`는 외부에 공개할 함수와 타입을 맡음. 이 구조는 이후 C++, embedded, Flask에서도 계속 반복되는 “interface와 구현 분리”의 시작점임.

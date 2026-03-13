# kuhrd 개발자 교육


## [2026-03-09]

    - 구글 슬라이드 자기소개
    - wsl 설치
    - vscode, git 설치
    - os (리눅스 wsl 사용)

- Ubuntu install
```bash
wsl --install -d Ubuntu-22.04
wsl --set-default-version 2
wsl --set-version Ubuntu-22.04 2
wsl -l -v
```

- 터미널에서 유저 정보 입력
```bash
git config --global user.email freshmea@gmail.com
git config --global user.name freshmea
```


### 1. hello.c 작성<br>
`#` -> 전처리 지시자<br>
`main` 함수 -> 엔트리 포인트<br>
함수의 리턴값의 타입과 함수이름앞의 타입은 같아야함

### 2. literal.c 작성
| 변환문자 |  |
|---|---|
| `%d` | 10진수로 표현 |
| `0%o` | 8진수로 표현 |
| `0x%x` | 16진수로 표현 |
| `%c` | 문자 |
| `%s` | 문자열(포인터) |


### 3. limit.c 작성<br>
최대 비트수 확인 ( `<limits.h>` )<br>
` #define END_HELLO "end of file\n"` => `END_HELLO`를 `"end of file\n"` 로 치환


[실습폴더](./c_example/)


---

## [2026-03-10]



### makefile
```makefile
TARGET = target1 target2 ...

all: ${TARGET} # make all을 명시해야하지만 처음에 명시하면 make만 했을때도 가능

target1 : $@ #앞의 hello를 찾아.c를 붙임
target2 : $@
...
# cc -o hello hello.c 실행파일과 c파일의 이름이 같으면 생략가능
# 파일이 수정된 날짜와 시간을 체크하기때문에 수정하고 바로 make 해도 적용이 된다
clean : 
	rm ${TARGET}
```
```makefile
SRCS = ${wildcard *.c}
TARGET = ${SRCS:.c=} # 확장자를 가지지 않게 함

all: ${TARGET} 

clean : 
	rm ${TARGET}
```




### 연산자
|산술연산자||
|---|---|
|`+`|더하기|
|`-`|빼기|
|`/`|나누기|
|`%`|나머지|

|증감연산자||
|---|---|
|`++`|+1|
|`--`|-1|

`전위 후위에 따라 계산 순서가 다름`

대입연산자 : `=`

관계연산자(return, true, false) : `< > <= >= == !=`<br>
`True = 1 , False = 0`

|논리연산자||
|---|---|
|`&&`|AND|
|`\|\|`|OR|
|`!`|NOT|


- 연산자 오버로딩 : 연산자를 재정의
    - 사용자정의 Type -> 구조체

삼항연산자 :  `?`

```C
printf("1 <= %d <= 9 : %s\n" ,num, (1<=num)&&(num<=9) ? "true" : "false");
// '?' 삼항 연산자 ( [조건식] ? [참] : [거짓] )
```

[compare실습](./c_example/compare.c)<br>
```c
#include <stdbool.h> <=c에서 true false 를 명시적으로 쓸때 stdbool헤더를 쓴다
```

형 변환 연산자 : `(자료형)피연산자 <= 해당 줄 이후에 다시 원래 자료형으로 돌아옴`

sizeof 연산자 : <br>
c는 메모리를 다루는 언어이기때문에 sizeof는 자주 쓰인다.<br>
피연산자의 크기를 바이트 단위로 알려줌 (1byte = 8bit)

|비트연산자|||
|---|---|---|
|`&`|AND연산자|두비트가 모두 1인 경우만 1로 계산|
|`^`|XOR연산자|두 비트가 서로다른 경우 1로 계산|
|`\|`|OR연산자|두 비트 중 하나라도 참이면 1로 계산|
|`~`|NOT연산자|1은 0으로 0은 1로 바꿈|
|`<<`|왼쪽비트이동연산자|비트를 왼쪽으로 이동|
|`>>`|오른쪽비트이동연산자|비트를 오른쪽으로 이동|


*\*tip `ctrl+h` -> 같은 글자 한번에 치환*   


---
## [2026-03-11]

### 조건문

#### if - else
```c
if(조건식)
{
    실행문;
}else if(조건식){
    실행문;
}else{
    실행문;
}
```

 - 난수생성
    - srand() `<stdlib.h>`
    - time(NULL) `<time.h>`

#### switch
```c
switch(조건식)
{
    case 상수식:
        실행문;
        break;
        :
        :
    defalt:
        실행문;
        break;
}
```

### 반복문

#### for

```c
for(초기식;조건식;증감식)
{
    실행문;
}
//Flow : 초기식 -> 조건식 -(참)-> 실행문 -> 증감식 -> 조건식 -(거짓)-> 종료
```
`for문은 반복횟수가 정해져 있을 때 사용`
`초기식에서 선언한 변수 =  지역변수`

#### while

```c
while(조건문)
{
    실행문;
} // Flow : 조건문 -(참)-> 실행문 -> 조건문 -(거짓)-> 종료
```
`한번은 꼭 실행문을 실행하고자 할때 do-while 사용`

#### do-while
```c
do
{
    실행문;
}while(조건문);
//Flow : 실행문 -> 조건문 -(참)-> 실행문 -> 조건문 -(거짓)-> 종료
```
`break` -> 블록 탈출(강제로 조건 False)<br>
`continue` -> 다음 루프로 이동

### 배열

`array` = 타입의 묶음(ex. int char float ... *사용자 정의 타입*)<br>
`변수명[n]` 
 - 메모리의 범위를 넘어서면 안된다(0~n-1 까지만 접근 가능)
 - 선언과 대입을 따로 할 수 있다
    - for문을 쓰게되면 번거롭기때문에 `{ , , , }`를 통해 대입을 한다


```c
int nums1[5] = {1,2,3,4,5};
int nums2[] = {1,2,3,4,5}; //입력한 만큼의 메모리 확보
int nums3[10] = {1,2,3,4,5}; //채워지지 않은 공간은 0으로 초기화
int nums4[50]; //랜덤한 값이 채워져 있음
int nums5[50] = {0}; //모든 값을 0으로 초기화, 효율성이 떨어짐
```


## [2026-03-12]

### 정렬(sorting)
`빅데이터에서는 한번을 순회하더라도 많은 시간이 걸리기에 어떤 알고리즘을 사용하는지가 중요`
- 데이터의 순서 변경(swap)
- swap 함수 작성
- info 함수 작성

#### 버블정렬
 : 인접한 두 원소를 비교하여 스왑하는 정렬방식<br>
`if(arr[j] > arr[j+1])`

#### 선택정렬
 : 전체에서 가장 작은 값을 찾아 앞쪽 위치와 교환하며 정렬하는 방식<br>


#### 퀵정렬
`stdlib.h`
```c
qsort(정렬할 배열의 시작주소, 배열원소개수, 원소의 크기, 비교함수이름(compare))

int compare(const void *a, const void *b){
    return (*(int *)a - *(int *)b);
}
```
 - `void *` -> 자료형이 정해지지않은 포인터 (qsort는 범용)
 - `const` -> 값을 바꾸지 않음, 비교만
 - `(int *)a` -> a를 int형 포인터로 형변환
 - `*(int *)a` -> a가 가리키는 주소의 값


### 포인터(Pointer)
`주소값을 저장하는 변수` <br>
선언 : ` int *pValue `<br>
`pValue` -> 주소<br>
`*pValue` -> pValue주소안의 값<br>
`*` -> 참조 연산자
`&` -> 역참조 연산자
 *선언이 된 변수의 주소만 저장 및 역참조 가능*

```c    
int *p;     //1.포인터 변수 선언
int Value;
p = &Value; //2.주소 저장
*p = 200;   //3.참조 사용
```

### 포인터 사용한 구조(C)
1. 함수 함수포인터 함수명 = 포인터
```c
int (*fp)(int,int); //함수 포인터 선언 (타입이 같아야함)
fp = add; //함수 포인터에 add 함수의 주소를 할당
//fp = &add; 가능
int re = (*fp)(4,3); 
// int re = fp(4,3); 가능
```
<br>

함수의 인자로 참조 연산자(*) 쓰는 5가지 상황
 - 호출 당하는 쪽에서 호출한 쪽의 변수를 변경할 때
 - 배열을 인자로 넘길때(필수)
 - 구조체를 인자로 넘길때(선택)
 - 사용자 정의 연산(함수)을 인자로 넘길때
 - 임의의 자료 넘길때(void *)
 
<br>
2. 배열 abc[ ] 배열명 = 포인터

```c
int nums[] = {1,2,3,4,5};
int *p;
p=nums; //배열명을 넣으면 첫번째 자리의 주소값
p=&nums[0];
// p+1 -> nums[1]
```


`sudo apt install build-essential`
`sudo apt install gdb`

## [2026-03-13]

### 분할 컴파일


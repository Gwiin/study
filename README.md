# kuhrd 개발자 교육
학습정리

---

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


*\*tip ctrl+h -> 같은 글자 한번에 치환*   

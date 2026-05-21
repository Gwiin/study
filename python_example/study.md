# Python

## 2026-05-21

- conda 사용하는 이유 : 가상환경을 사용하기 위해서
> 1. dependency(의존성)<br>
`.venv/` => 프로젝트 마다 라이브러리 관리<br>
.venv 를 만들어도 root 의 바이너리를 공유하지만<br>
conda로 가상환경을 만들면 가상환경내에 바이너리를 만들어서 사용한다

> ! conda로 가상환경을 만들어도 커널은 공유한다 커널까지 가상화를 위해서 WSL 같은것을 사용한다

> 커널 상위의 가상환경 => VM머신


```
C
main() 필수 
컴파일 언어
코드 완성이 전제
전처리 -> 어셈블리 -> 바이너리(기계어)
```

```
Python
1번 라인
built-in varialbe 이 있다
인더액티브셀로 실행
인터프리터(C언어 프로그램) 언어
```
[C로 만든 인터프리터 예제](https://github.com/Gwiin/study/blob/main/python_example/basic/interpreter.c)


---

### Python

1. 인터프리터 언어
    - 코드를 한줄씩 실행 -> 빠르게 테스트 가능
2. 문법의 간결함
    - 가독성 높음
3. 동적 타이핑
    - 변수 타입을 미리 선언하지 않음<br>
    - 파이썬에서는 primitive type 이 없다
    - type -> class(구조체 함수로 구현)
    - 파이썬에서는 변수를 heap메모리에서 다룸
4. 객체지향 지원
    - 클래스와 객체 기반 설계 가능
5. 라이브러리가 풍부
    - 웹, 데이터, AI, 자동화, IoT까지 확장 가능

---

>`frame` <- 변수 scope

frame
-
|       C           |       python                          |
|       ---         |       ---                             |
|       &&          |       and                             |
|       조건        |       assert                          |
|       throw       |       raise                           |
|       thread      |       async(비동기)    await          |
|       struct      |       class                           |
|       free        |       del(객체 삭제)                  |
|       try-catch   |       try-except(예외처리)-finally    |
|       #include    |       import from(소스를 불러옴)      |
|       ==          |       is                              |
|       inline      |       lambda                          |
|       return      |       return                          |


indexing, slicing
-
[a08.str_indexing](/home/hrd_1_3/study/python_example/basic/a08.str_indexing.py)


for, enumerate, zip
-
[a19_range_enumerate.py](/home/hrd_1_3/study/python_example/basic/a19_range_enumerate.py)



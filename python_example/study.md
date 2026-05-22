# Python 학습 정리

## 저장소 구성

- `basic/hello.py`: Python script 실행과 `__name__`
- `basic/variable.py`: 변수와 객체 참조
- `basic/a00_default.py`: 기본 실행 틀
- `basic/a02_keyward.py`: Python keyword와 C 문법 비교
- `basic/a04_print.py`: `print`, literal, 출력 option
- `basic/a08.str_indexing.py`: 문자열 indexing/slicing
- `basic/a13_comparison.py`: 비교 연산
- `basic/a19_range_enumerate.py`: `range`, `enumerate`, `zip`
- `basic/frame.py`: scope와 frame
- `basic/interpreter.c`: C로 보는 interpreter 개념

## 가상환경

Python은 project마다 필요한 package와 version이 달라질 수 있음. 그래서 project별로 실행 환경을 분리함.

- `.venv`: Python 표준 가상환경임. 가볍고 project 폴더 안에서 관리하기 좋음.
- `conda`: Python interpreter와 package 환경을 함께 관리하기 좋음.
- Docker: OS 수준에 가까운 container로 실행 환경 전체를 재현하기 좋음.

가상환경은 kernel까지 완전히 분리하는 VM과는 다름. Python 실행 파일과 package 의존성을 project별로 관리하는 도구로 이해하면 됨.

```bash
conda create -n iot1 python=3.12
conda activate iot1
python basic/hello.py
```

## interpreter 언어

C는 source code를 compiler가 실행 파일로 바꾼 뒤 실행함. Python은 interpreter가 source를 읽고 실행함.

```text
C: source -> compile -> binary -> execute
Python: source -> interpreter -> execute
```

Python도 내부적으로 bytecode 변환 같은 과정이 있지만, 학습 초반에는 “코드를 작성하고 바로 실행해 확인하기 쉽다”는 점이 중요함.

## `__name__`과 실행 진입점

Python은 C처럼 `main()`이 반드시 필요하지 않음. 파일 위에서 아래로 실행됨. 그래도 script의 시작점을 분명히 하려면 다음 패턴을 사용함.

```python
def main():
    print("hello, world")

if __name__ == "__main__":
    main()
```

파일을 직접 실행하면 `__name__`이 `"__main__"`임. 다른 파일에서 import되면 `__name__`은 파일 이름이 됨. 그래서 import할 때 실행되면 안 되는 코드를 이 조건 안에 둠.

## 변수와 객체 참조

Python 변수는 값을 담는 상자라기보다 객체를 가리키는 이름에 가깝음.

```python
x = 10
y = x
```

`x`와 `y`는 같은 정수 객체를 참조함. Python에서는 기본 자료형도 객체처럼 다뤄짐. C의 primitive type처럼 stack에 정해진 크기의 값을 직접 둔다고만 생각하면 Python의 동작을 오해하기 쉬움.

## `print`

`print()`는 여러 값을 출력할 수 있고, 구분자와 끝 문자를 바꿀 수 있음.

```python
print("this is", "python", "class", sep="-")
print("next", end="")
```

`sep`는 여러 인자 사이에 들어갈 문자열이고, `end`는 출력 끝에 붙을 문자열임. 기본 `end`는 줄바꿈임.

## keyword

keyword는 Python 문법에서 이미 의미가 정해진 단어임. 변수 이름으로 사용할 수 없음. `a02_keyward.py`에서는 `keyword.kwlist`로 현재 Python이 예약어로 쓰는 단어 목록을 확인함.

Python의 `and`, `or`, `not`은 C의 `&&`, `||`, `!`와 비슷한 역할임. Python에서는 기호보다 영어 단어에 가까운 논리 연산자를 사용함.

## 비교 연산과 `is`

`==`는 값이 같은지 비교함. `is`는 두 이름이 같은 객체를 가리키는지 비교함.

```python
print(10 == 100)
print(10 != 100)
```

초반에는 값 비교에는 `==`를 쓴다고 기억하는 것이 안전함. `is`는 `None` 비교나 객체 동일성을 확인할 때 의미가 있음.

## 문자열 indexing

문자열은 순서가 있는 sequence임. index로 한 글자를 가져올 수 있음.

```python
str_var = "안녕하세요"
print(str_var[0])
print(str_var[-1])
```

index는 0부터 시작함. 음수 index는 뒤에서부터 접근함. `-1`은 마지막 글자임.

## slicing

slicing은 sequence의 일부 구간을 잘라냄.

```python
str_var = "안녕하세요" * 3
print(str_var[5:10])
print(str_var[5:10:2])
print(str_var[-1::-1])
```

`[start:end]`에서 `end`는 포함되지 않음. 세 번째 값은 step임. `[::-1]`은 문자열을 뒤집는 대표적인 slicing 패턴임.

## 반복문과 Pythonic 순회

Python에서는 index가 꼭 필요하지 않으면 직접 요소를 순회하는 편이 좋음.

```python
for ele in list1:
    print(ele)

for i, ele in enumerate(list1):
    print(i, ele)

for ele1, ele2 in zip(list1, list2):
    print(ele1, ele2)
```

- 단순히 값만 필요하면 `for ele in list1`
- index도 필요하면 `enumerate`
- 두 sequence를 같이 돌면 `zip`

`range(len(list1))`는 C 스타일 index 반복에 가깝음. Python에서는 상황에 맞는 반복 도구를 고르는 것이 중요함.

## scope와 frame

함수가 호출되면 새로운 frame이 생김. frame은 그 함수 호출 중의 local variable, 실행 위치, global 참조 정보를 담음.

```python
main_frame = sys._getframe()
print(main_frame.f_code.co_name)
print(main_frame.f_locals)
print(main_frame.f_globals)
```

`frame.py`는 이 내부 구조를 직접 확인하는 실습임. C의 stack frame과 비교하면 함수 호출마다 독립된 지역 공간이 생긴다는 점을 이해하기 쉬움.

## C로 보는 interpreter

`interpreter.c`는 Python interpreter를 완전히 구현한 코드는 아니지만, interpreter가 source text를 읽고 해석한 뒤 실행한다는 감각을 잡기 위한 비교 예제임.

```c
fgets(source, sizeof(source), stdin);
Instruction inst = parse(source);
execute(inst);
```

입력 문자열을 읽고, `parse`로 명령 형태로 바꾸고, `execute`로 실행함. Python이 C보다 “즉시 실행되는 느낌”을 주는 이유를 이해하는 데 도움이 됨.

---

## 함수(function)

c
>type 식별자(매개변수)<Br>
>return 객체<br>
- return -> 에러코드
- argument -> 정보전달, 받을 변수, 옵션


python
>def 식별자(매개변수)
>return 객체(python type)
- 받을 변수 여러개를 보낼 수 있다


```python
def print_n_time(value : str, n : int): #type hint
    #doc string 
    """_summary_
    교육용 테스트 함수
    Args:
        value (str): _description_
        n (int): _description_

    Returns:
        str: 에러 반환

    """    
    for i in range(n):
        print(value)
    return "ok"

def main():
    print("첫번째 함수 콜")
    print_3_time()
    print("두번째 함수 콜")
    print_3_time()
    print("세번째 함수 콜")
    print_3_time()

    print_n_time("안녕하세요",3)

if __name__ == "__main__":
    main()
```

리턴 타입에 대한 타입 힌트를 주면 좋다.
```
(function) def print_n_time(<br>
    value: str,<br>
    n: int<br>
) -> None
```

doc string으로 함수에 대한 정보를 주는 것도 필요.
```
"""_summary_<br>
교육용 테스트 함수<br>
Args:<br>
    value (str): _description_<br>
    n (int): _description_<br>

Returns:<br>
    str: 에러 반환
"""    
```

```python
def print_n_time(*value : str, n : int):
```
`*`를 매개변수 앞에 붙이면 가변 매개변수로 여러개를 받을 수 있지만 앞에 있는 매개변수에 붙이게 되면 어디까지 패킹을 해야하는지 알수 없다.
```python
def print_n_time(n : int, *value : str):
```
위와 같이 사용할 수 있다.


패킹을 해서 받고 언팩해서 출력하면 결과값으로 tuple이 나오게 된다.
```
('abc', 'def', 'ghi')
```

>컨테이너<br>
tuple 시스템인 활용 <Br> 
list 시스템인 활용 <br>
dict<br>
set<br>
...

언팩을 할때
`temp1, temp2, temp3 = value`
로 하게 되면 갯수에 따라 에러가 발생할 수 있음
```python
for v in value:
    print(v,end=" ")
```
for문을 활용하는 것이 좋다.

```python
#함수의 리턴
return "ok",n

#리턴값 저장, 리턴값 타입
return_var = print_n_time(3,'abc','def','ghi','ddd')
print(type(return_var))
print(*return_var)
```
리턴값이 튜플로 나오기 때문에 출력할때 `*`으로 언팩을 해서 하면된다.

---

## 기본 매개변수(default argument), 키워드 매개변수

```python
def print_n_time(
    *value: str,
    n: int = 2,
    i_var: int = 4,
) -> str:
```

`*value`로 여러개의 값을 받을 수 있다.<br>
이렇게 받은 값은 tuple로 패킹된다.

```python
print(type(value))
```

출력결과
```
<class 'tuple'>
```

`n: int = 2` 처럼 쓰면 type hint와 default argument를 같이 사용할 수 있다.

```python
n: int = 2
i_var: int = 4
```

- `n` 값을 안보내면 기본값 2를 사용
- `i_var` 값을 안보내면 기본값 4를 사용
- 값을 보내면 보낸 값으로 변경됨

```python
return_var = print_n_time("abc", "def", "ghi", "ddd")
return_var = print_n_time("abc", "def", "ghi", "ddd", n=4)
return_var = print_n_time("abc", "def", "ghi", "ddd", n=4, i_var=8)
return_var = print_n_time("abc", "def", "ghi", "ddd", i_var=8, n=4)
```

키워드 매개변수는 이름을 지정해서 값을 넣을 수 있다.

```python
n=4
i_var=8
```

이름을 지정하면 순서가 바뀌어도 동작한다.
```python
print_n_time("abc", "def", "ghi", "ddd", i_var=8, n=4)
```

`*value` 뒤에 있는 `n`, `i_var`는 그냥 위치로 넣는 것이 아니라 키워드로 넣어야 한다.<br>
왜냐하면 앞의 값들은 `*value`가 계속 받아가기 때문이다.

```python
for i in range(n):
    print(value)
    for v in value:
        print(v, end=" ")
```

`print(value)`를 하면 tuple 자체가 출력된다.
```
('abc', 'def', 'ghi', 'ddd')
```

for문으로 하나씩 꺼내면 언팩해서 출력하는 것처럼 사용할 수 있다.
```
abc def ghi ddd
```

```python
def print_keyward_arguemnt(a, b, c, d=5, *e):
    print(a, b, c, d, e)
```

앞에서부터 `a`, `b`, `c`, `d`에 값이 들어가고 남는 값은 `*e`로 패킹된다.

```python
print_keyward_arguemnt(1, 2, 3, 4, 5, 6, 7)
```

출력결과
```
1 2 3 4 (5, 6, 7)
```

```python
print_keyward_arguemnt(1, 2, 3)
```

출력결과
```
1 2 3 5 ()
```

`d`는 값을 안주면 기본값 5가 들어간다.<br>
남는 값이 없으면 `e`는 빈 tuple이 된다.

주의할 점
```python
return "ok"

print(*return_var)
```

`return_var`가 문자열이면 `*`로 언팩할 때 문자열이 한 글자씩 나누어진다.
```
o k
```

리턴값이 tuple일 때와 str일 때 언팩 결과가 다르게 나온다.

---

## 가변 매개변수 args, keyword argument

```python
def print_n_times(*args, **kargs):
```

`*args`는 위치 인자를 여러개 받을 때 사용한다.<br>
받은 값은 tuple이다.

```python
# args -> tuple
for value in args:
    print("args")
    print(value)
```

함수 호출
```python
print_n_times(1, 2, 3, 4, 5, 6, a=1, b=2, c=3)
```

위치 인자 부분
```
1, 2, 3, 4, 5, 6
```

이 값들이 `args`로 들어간다.

출력결과
```
args
1
args
2
args
3
args
4
args
5
args
6
```

`**kargs`는 키워드 인자를 여러개 받을 때 사용한다.<br>
받은 값은 dict이다.

```python
# kargs -> dict {key: value, ...}
```

키워드 인자 부분
```
a=1, b=2, c=3
```

이 값들이 dict 형태로 들어간다.

```python
for value in kargs:
    print("keyward_argument")
    print(value, kargs[value])
```

dict는 반복문을 돌리면 기본적으로 key가 나온다.

출력결과
```
keyward_argument
a 1
keyward_argument
b 2
keyward_argument
c 3
```

하지만 python에서는 dict를 출력할 때 `.items()`를 더 많이 사용한다.

```python
for key, value in kargs.items():
    print(key, value)
```

`kargs.items()`는 `(key, value)` tuple을 하나씩 꺼내준다.<br>
그래서 아래처럼 받을 수 있다.

```python
for key, value in kargs.items():
```

출력결과
```
a 1
b 2
c 3
```

정리:
- `*args` -> 여러개의 위치 인자 받기, tuple
- `**kargs` -> 여러개의 키워드 인자 받기, dict
- dict를 for문으로 돌리면 key가 나온다
- key와 value를 같이 쓰고 싶으면 `.items()`를 사용한다

---

## list

python에서 여러개의 값을 묶어서 사용할 때 list를 사용할 수 있다.

```python
import datetime

def main():
    #list 선언
    list_a = [] #아래줄보다 이방식을 주로 사용
    list_b = list()
    list_c = [1, 2, 3, 4, 5, 6] # 선언과 동시에 입력
```

list 선언 방법
```python
list_a = []
list_b = list()
list_c = [1, 2, 3, 4, 5, 6]
```

- `[]` -> 빈 list 생성
- `list()` -> list 생성자 사용
- `[1, 2, 3]` -> 선언하면서 값을 같이 넣음

보통 빈 list를 만들 때는 `[]`를 많이 사용한다.

```python
print(list_a, list_b, list_c)
print(type(list_a),type(list_b), type(list_c))
```

출력결과
```text
[] [] [1, 2, 3, 4, 5, 6]
<class 'list'> <class 'list'> <class 'list'>
```

`[]`로 만든 것도 list이고, `list()`로 만든 것도 list이다.<br>
값을 넣어서 만든 `list_c`도 type은 list이다.

```python
ptime = datetime.datetime.now()
list_d = [1,2,3.141582, "padak", ptime]
print(list_d)
```

list에는 서로 다른 type의 객체를 같이 넣을 수 있다.

```text
[1, 2, 3.141582, 'padak', datetime.datetime(2026, 5, 22, 10, 50, 59, 835072)]
```

위 list에는 아래 값들이 같이 들어가 있다.

- `1`, `2` -> int
- `3.141582` -> float
- `"padak"` -> str
- `ptime` -> datetime 객체

>컨테이너<br>
list는 여러 객체를 담을 수 있는 container로 볼 수 있다.

C 배열과 비교하면 Python list는 조금 다르게 생각해야 한다.

c
>int arr[3] = {1, 2, 3};<br>
>같은 type의 값을 정해진 크기로 저장하는 느낌<br>

python
>list_a = [1, 2, "padak"]<br>
>여러 객체를 순서대로 담는 container 느낌<br>

정리:
- list는 여러 값을 순서대로 저장하는 container이다
- 빈 list는 `[]`로 만들 수 있다
- `list()`로도 만들 수 있지만 `[]`를 더 자주 사용한다
- list 안에는 서로 다른 type의 객체도 같이 넣을 수 있다
- `type()`으로 확인하면 `<class 'list'>`가 나온다



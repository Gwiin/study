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

---

## list indexing, 값 변경

list는 순서가 있기 때문에 index로 접근할 수 있다.

```python
ptime = datetime.datetime.now()
list_d = [1,2,3.141582, "padak", ptime]
print(list_d)
print(list_d[3])
```

`list_d[3]`은 4번째 원소를 의미한다.<br>
index는 0부터 시작한다.

출력결과
```text
[1, 2, 3.141582, 'padak', datetime.datetime(2026, 5, 22, 11, 46, 18, 582159)]
padak
```

list는 값을 변경할 수 있다.

```python
list_d[3] = "agu"
print(list_d[3])
```

출력결과
```text
agu
```

문자열은 한 글자만 바꾸는 것이 안되지만, list는 index 위치의 값을 바꿀 수 있다.

```python
list_e = [ [1, 2, 3] , [4, 5, 6] , [7, 8, 9] ]
print(list_e)
print(list_e[1][1])
```

list 안에 list를 넣을 수 있다.<br>
2차원 배열 같은 느낌으로 사용할 수 있다.

출력결과
```text
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
5
```

`list_e[1]`은 `[4, 5, 6]`이고,<br>
`list_e[1][1]`은 그 안의 1번 index라서 `5`가 나온다.

정리:
- list는 index로 접근할 수 있다
- index는 0부터 시작한다
- list는 원소 값을 변경할 수 있다
- list 안에 list를 넣으면 2차원 list처럼 사용할 수 있다

---

## list와 함수

```python
def make_20(var_a_b):
    # global var_a
    var_a_b[0] = 20
```

함수 안에서 list의 0번 값을 바꾸고 있다.

```python
def main():
    var_a = 10
    wrapper_list = [var_a] #list로 가두어서
    make_20(wrapper_list)  #함수로 보냄 
    var_a = wrapper_list[0]
    print(var_a) # 20
```

출력결과
```text
20
```

`var_a` 자체를 함수에 보내면 정수 객체를 바로 바꾸는 느낌으로 사용하기 어렵다.<br>
그래서 list로 감싸서 보내고, 함수 안에서 list 원소를 수정한다.

```python
wrapper_list = [var_a]
make_20(wrapper_list)
var_a = wrapper_list[0]
```

list는 함수로 보냈을 때 내부 원소를 바꾸면 바깥에서도 확인된다.

```python
list_a = [1, 2, 3]
list_b = [4, 5, 6, list_a] # 값의 복사가 아니고 메모리 참조

print(list_b)
list_a[2] = 30
print(list_b)
```

출력결과
```text
[4, 5, 6, [1, 2, 3]]
[4, 5, 6, [1, 2, 30]]
```

`list_b` 안에 들어간 `list_a`는 값이 복사된 것이 아니라 같은 list를 참조하는 느낌이다.<br>
그래서 `list_a[2]`를 바꾸면 `list_b` 안쪽에 들어있는 list도 바뀐 것처럼 보인다.

>리스트의 이름은 값이 아니라 메모리를 다룬다.

정리:
- list를 함수에 보내면 내부 원소를 수정할 수 있다
- list 안에 다른 list를 넣으면 참조 관계를 조심해야 한다
- 단순 값 복사인지 같은 객체를 가리키는지 확인해야 한다

---

## list method

list는 연산자와 method를 사용할 수 있다.

```python
list_a = [1,2,3]
list_b = [4,5,6]
print(list_a + list_b)
print(list_a.__add__(list_b)) # 스페셜 메소드 (c++ 오버라이딩)
```

출력결과
```text
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
```

`+` 연산은 list를 이어붙인 새로운 결과를 만든다.<br>
내부적으로는 `__add__()` 같은 special method와 연결해서 생각할 수 있다.

```python
print(list_a := list_a.__add__(list_b))
```

`:=` 는 elephant sign이라고 적어둠.<br>
정확히는 walrus operator라고 부르고, 대입하면서 값을 사용할 수 있다.

출력결과
```text
[1, 2, 3, 4, 5, 6]
```

```python
print(list_a.extend(list_b))
print(list_a)
```

`extend()`는 list 자체를 수정한다.<br>
return 값은 `None`이다.

출력결과
```text
None
[1, 2, 3, 4, 5, 6, 4, 5, 6]
```

`+`는 결과를 만들어주고, `extend()`는 원본 list를 수정하는 차이가 있다.

```python
print(list_a * 4)
print(list_a.__mul__(4))
```

list에 `*`를 사용하면 반복된 list가 만들어진다.

```text
[1, 2, 3, 4, 5, 6, 4, 5, 6, 1, 2, 3, 4, 5, 6, 4, 5, 6, 1, 2, 3, 4, 5, 6, 4, 5, 6, 1, 2, 3, 4, 5, 6, 4, 5, 6]
```

### append, insert

```python
list_b.append("추가 원소")
print(list_b)
```

`append()`는 list의 마지막에 원소 하나를 추가한다.

출력결과
```text
[4, 5, 6, '추가 원소']
```

```python
list_b.insert(3,7)
print(list_b)
```

`insert(index, value)`는 원하는 위치에 값을 넣는다.

출력결과
```text
[4, 5, 6, 7, '추가 원소']
```

### pop, remove

```python
print(list_b.pop())
print(list_b)
```

`pop()`은 마지막 값을 꺼내고 list에서 제거한다.

출력결과
```text
추가 원소
[4, 5, 6, 7]
```

```python
print(list_b.pop(0))
print(list_b)
```

`pop(0)`처럼 index를 주면 해당 위치의 값을 꺼내고 제거한다.

출력결과
```text
4
[5, 6, 7]
```

```python
list_b.remove(6)
print(list_b)
```

`remove(값)`은 해당 값을 찾아서 삭제한다.

출력결과
```text
[5, 7]
```

### index, len, in

```python
print(list_b.index(7)) # 인수의 인덱스 위치
```

`index()`는 값의 index 위치를 반환한다.

출력결과
```text
1
```

```python
list_b = ['a','b','c','d','e','f']
list_e = [*str("abcdef padak mon")] # 리스트에 문자열 입력 (공백까지)
print(list_b.index("e"))
print(list_e)
```

문자열을 `[*str(...)]` 형태로 list에 넣으면 한 글자씩 나누어 들어간다.<br>
공백도 하나의 문자라서 list에 들어간다.

출력결과
```text
4
['a', 'b', 'c', 'd', 'e', 'f', ' ', 'p', 'a', 'd', 'a', 'k', ' ', 'm', 'o', 'n']
```

```python
print(list_e.__len__()) # 리스트 길이
print(len(list_e))
```

`len()`은 list의 길이를 구할 때 사용한다.<br>
`__len__()` special method를 직접 호출해도 같은 값이 나온다.

출력결과
```text
16
16
```

```python
print("k" in list_e)
print("g" in list_e)
```

`in`은 list 안에 값이 있는지 확인한다.<br>
return은 bool이다.

출력결과
```text
True
False
```

정리:
- `+` -> list를 합친 결과를 만든다
- `extend()` -> list 자체를 수정하고 return은 `None`
- `*` -> list를 반복한 결과를 만든다
- `append()` -> 마지막에 원소 추가
- `insert()` -> 원하는 index에 원소 추가
- `pop()` -> 값을 꺼내면서 삭제
- `remove()` -> 값을 찾아서 삭제
- `index()` -> 값의 위치 확인
- `len()` -> list 길이 확인
- `in` -> 값이 list 안에 있는지 확인

### list 삭제와 실행 순서 주의

```python
del list_e[4]
```

`del`은 list의 특정 index 원소를 삭제할 때 사용할 수 있다.

다만 변수는 사용하기 전에 먼저 만들어져 있어야 한다.<br>
`list_e`를 만들기 전에 `del list_e[4]`를 실행하면 `NameError`가 발생한다.

```python
list_e = [*str("abcdef padak mon")]
del list_e[4]
print(list_e)
```

위처럼 먼저 list를 만든 뒤 삭제해야 한다.

```python
ptime = datetime.datetime.now()
list_e.append(ptime)
print(list_e[16])
del list_e[16]
print(list_e)
```

list에는 문자열, 숫자뿐 아니라 `datetime` 객체 같은 사용자 정의 또는 library 객체도 넣을 수 있다.<br>
`append()`로 객체를 추가하고, `del`로 해당 index의 객체를 삭제할 수 있다.

## list comprehension

`basic/a30_list_comprehension.py`에서는 list comprehension으로 반복문과 조건문을 한 줄에 사용한다.

```python
li = [i**2 for i in range(100) if i % 2 == 0]
```

구조:

```python
[결과 for 변수 in 컨테이너 if 조건]
```

위 코드는 `0`부터 `99`까지 반복하면서 짝수만 골라 제곱한 값을 list로 만든다.

일반 반복문으로 쓰면 다음과 비슷하다.

```python
li = []
for i in range(100):
    if i % 2 == 0:
        li.append(i**2)
```

list comprehension은 짧고 읽기 좋게 list를 만들 때 사용한다.<br>
조건이 너무 복잡해지면 일반 `for`문으로 풀어 쓰는 것이 더 좋다.

### random.shuffle

```python
random.shuffle(li)
```

`random.shuffle()`은 list의 순서를 무작위로 섞는다.<br>
주의할 점은 원본 list 자체를 수정하고, return 값은 `None`이라는 것이다.

```python
print(min(li), max(li), sum(li))
```

- `min(li)`: list에서 가장 작은 값
- `max(li)`: list에서 가장 큰 값
- `sum(li)`: list 안 숫자의 합계

### sort

```python
li.sort()
print(li)

li.sort(reverse=True)
print(li)
```

`sort()`는 list 자체를 오름차순으로 정렬한다.<br>
`reverse=True`를 주면 내림차순으로 정렬한다.

정리:
- list comprehension -> list를 짧게 생성
- `random.shuffle()` -> list 순서를 무작위로 섞음
- `min()` -> 최솟값
- `max()` -> 최댓값
- `sum()` -> 합계
- `sort()` -> list 자체를 정렬

## module import

`basic/hello_use_module.py`에서는 다른 Python file에 있는 변수를 가져와 사용한다.

```python
from test_package.module_b import module_var_b
from test_package.module_a import module_var_a
```

`from 패키지.모듈 import 이름` 형식이다.

- `test_package`: package 폴더
- `module_a`, `module_b`: Python module file
- `module_var_a`, `module_var_b`: module 안에 정의된 변수

가져온 변수는 현재 file에서 바로 사용할 수 있다.

```python
def main():
    print(module_var_a)
    print(module_var_b)
```

module을 import하면 다른 file에 작성한 함수, 변수, class를 재사용할 수 있다.<br>
코드를 기능별 file로 나누고 필요할 때 가져와 쓰는 것이 module 사용의 기본 목적이다.

직접 실행할 때는 기존과 같이 진입점 패턴을 사용한다.

```python
if __name__ == "__main__":
    main()
```

정리:
- module -> Python file 하나
- package -> module들을 담는 폴더
- `import` -> 다른 module의 코드를 가져오는 문법
- `from ... import ...` -> module 안의 특정 이름만 가져옴
- `__name__ == "__main__"` -> 직접 실행할 때만 `main()` 호출

## package import와 `__init__.py`

`basic/a90_package_import.py`에서는 package 자체를 import해서 사용하는 방법을 확인한다.

```python
import test_package
from test_package import *
```

`import test_package`는 package 자체를 가져온다.<br>
이 방식으로 가져오면 package 안의 이름을 사용할 때 package 이름을 붙여 접근한다.

```python
print(test_package.module_var_a)
test_package.module_b_func()
print(test_package.Module_A())
test_package.package_func()
```

`test_package.module_var_a`처럼 `패키지이름.이름` 형태로 사용한다.<br>
이 방식은 어디에서 가져온 이름인지 코드에서 분명하게 보인다.

### `from test_package import *`

```python
from test_package import *
```

`*` import는 package에서 공개된 이름들을 현재 file로 바로 가져온다.

그래서 아래처럼 package 이름 없이 사용할 수 있다.

```python
print(module_var_a)
print(module_var_b)
```

다만 `*` import는 어떤 이름이 현재 namespace에 들어오는지 한눈에 보기 어렵다.<br>
학습용으로는 동작을 이해하기 좋지만, 실제 코드에서는 필요한 이름만 명시해서 import하는 편이 더 안전하다.

### `__init__.py`

`basic/test_package/__init__.py`는 package가 import될 때 실행되는 file이다.

```python
from .module_a import module_var_a, module_a_func, Module_A
from .module_b import module_var_b, module_b_func, Module_B
```

`.`은 현재 package를 뜻하는 상대 import이다.<br>
즉 `test_package` 안에서 `module_a`, `module_b`를 가져온다는 의미이다.

위 코드를 통해 `module_a.py`, `module_b.py` 안에 있던 변수, 함수, class를 package 수준으로 끌어올릴 수 있다.

예를 들어 원래는 다음처럼 쓸 수 있는 이름을

```python
from test_package.module_a import Module_A
```

`__init__.py`에서 import해두면 다음처럼 package를 통해 접근할 수 있다.

```python
import test_package

print(test_package.Module_A())
```

### `__all__`

```python
__all__ = ["module_var_a", "module_var_b"]
```

`__all__`은 `from test_package import *`를 했을 때 어떤 이름을 가져올지 정하는 list이다.

현재 설정에서는 `*` import를 하면 `module_var_a`, `module_var_b`만 직접 가져온다.<br>
그래서 `a90_package_import.py`에서 다음 코드는 package 이름 없이 사용할 수 있다.

```python
print(module_var_a)
print(module_var_b)
```

하지만 `Module_A`, `module_b_func`, `package_func`는 `__all__`에 없기 때문에 `*` import로 직접 들어오지 않는다.<br>
이 이름들은 `test_package.Module_A`, `test_package.module_b_func`, `test_package.package_func`처럼 package 이름을 붙여 사용한다.

### package import 시 실행되는 코드

```python
print("test_package 패키지에서 실행되는 프린트다.")
```

`__init__.py`의 맨 아래에 있는 이 코드는 package를 import할 때 실행된다.<br>
그래서 `import test_package`를 하면 이 print가 실행될 수 있다.

일반적으로 import할 때 불필요한 출력이나 실행이 생기지 않도록 주의해야 한다.<br>
테스트용 코드는 보통 아래처럼 `main()` 진입점 안에 넣는 것이 좋다.

```python
if __name__ == "__main__":
    main()
```

현재 `__init__.py`에는 `main()` 함수가 정의되어 있지만 직접 호출하지는 않는다.<br>
대신 file 맨 아래의 `print()`는 import 시 바로 실행된다.

정리:
- package를 import하면 package의 `__init__.py`가 실행된다
- `import test_package` -> `test_package.이름` 형태로 접근
- `from test_package import *` -> `__all__`에 적힌 이름을 직접 가져옴
- `.` import -> 현재 package 기준 상대 import
- `__init__.py`는 package의 공개 interface를 정리하는 역할을 할 수 있음
- import 시 실행될 코드는 신중히 작성해야 함

## dictionary

`dict`는 key와 value를 묶어서 저장하는 container이다.

c에서 배열은 index가 숫자로 정해져 있는 느낌이라면,<br>
python의 dict는 내가 정한 key로 value를 찾을 수 있다.

```python
dict_a = {}
dict_b = dict()
print(type(dict_a))
print(type(dict_b))
```

출력 결과
```text
<class 'dict'>
<class 'dict'>
```

`{}`는 비어있는 dict이다.<br>
`dict()`를 사용해도 빈 dict를 만들 수 있다.

### set과 헷갈릴 수 있음

```python
set_a = {1,2}
print(type(set_a))
```

출력 결과
```text
<class 'set'>
```

중괄호를 사용한다고 무조건 dict는 아니다.

```python
{}        # 빈 dict
{1, 2}    # set
{"a": 1}  # dict
```

`key: value` 형태가 있으면 dict이다.<br>
값만 있으면 set이다.

### dict key

```python
class A():
    pass

a = A()
dict_c = {"a":1234, "b":897, "c":876, 1234: 5678, 3.14:1.111, a:4.444}
print(type(dict_c))
print(dict_c)
```

출력 결과
```text
<class 'dict'>
{'a': 1234, 'b': 897, 'c': 876, 1234: 5678, 3.14: 1.111, <__main__.main.<locals>.A object at ...>: 4.444}
```

dict의 key는 문자열만 되는 것이 아니다.

```python
"a"     # str key
1234    # int key
3.14    # float key
a       # object key
```

이런 값들도 key로 사용할 수 있다.

단, key로 쓰려면 내부적으로 hash가 가능해야 한다.<br>
list처럼 바뀔 수 있는 객체는 보통 key로 쓰기 어렵다.

### key로 value 가져오기

```python
print(dict_c[a])
print(dict_c[3.14])
print(dict_c["c"])
```

출력 결과
```text
4.444
1.111
876
```

dict는 key를 넣으면 value가 나온다.

```python
dict_c["c"]
```

이 코드는 `"c"`라는 key에 연결된 value를 가져온다.

### 숫자 key와 문자열 key는 다름

```python
print(dict_c["1234"])
```

실행 결과
```text
KeyError: '1234'
```

`dict_c`에는 `1234`라는 int key는 있다.

```python
1234: 5678
```

하지만 `"1234"`라는 str key는 없다.

```python
1234    # int
"1234"  # str
```

두 개는 출력했을 때 비슷해 보여도 type이 다르다.<br>
그래서 dict에서는 다른 key로 본다.

없는 key를 `dict_c["1234"]`처럼 바로 접근하면 `KeyError`가 발생한다.

정리:
- dict는 `key: value` 구조이다
- `{}`는 빈 dict이다
- `{1, 2}`는 set이다
- key는 문자열만 되는 것이 아니라 int, float, object도 가능하다
- `1234`와 `"1234"`는 다른 key이다
- 없는 key를 `[]`로 접근하면 `KeyError`가 난다


### set()

`set`은 집합 자료형이다.

`set()`은 hash 기반으로 값을 저장한다.<br>
그래서 list처럼 `set_a[0]` 이런 식의 인덱싱은 불가능하다.

정확히는 많은 양의 데이터를 무조건 잘 다룬다기보다는,<br>
중복 제거와 포함 여부 확인에 효과적이다.

```python
set_a = {1, 2, 3}
```

주의할 점
```python
set_a[0]
```

이런 식으로 접근하면 에러가 난다.<br>
set은 순서로 값을 꺼내는 container가 아니다.

`in`으로 값이 있는지 확인할 때 list보다 빠르게 동작하는 경우가 많다.

```python
2 in set_a
```

set은 중복을 허용하지 않는다.

```python
{1, 1, 2, 2, 3}
```

결과적으로는 `{1, 2, 3}`처럼 중복이 제거된다.

집합 연산도 가능하다.

```python
a | b  # 합집합
a & b  # 교집합
a - b  # 차집합
```

정리:
- set은 중복 없는 값들의 모음이다
- hash 기반이라 포함 여부 확인에 유리하다
- index가 없어서 `set_a[0]`은 안된다
- 순서가 중요하면 list나 tuple을 사용해야 한다
- 중복 제거, 집합 연산에 사용하기 좋다

### tuple()

`tuple`은 여러 값을 묶어서 저장하는 container이다.

list와 비슷하게 순서가 있고 인덱싱도 가능하다.<br>
하지만 list와 다르게 한 번 만들면 값을 바꿀 수 없다.

```python
tuple_a = (1, 2, 3)
```

`tuple_a[0]`처럼 인덱싱은 가능하다.

```python
tuple_a[0]
```

하지만 값을 바꾸는 것은 안된다.

```python
tuple_a[0] = 10
```

tuple은 immutable 객체이다.<br>
immutable은 생성된 뒤 내부 값을 바꿀 수 없다는 뜻이다.

함수에서 여러 값을 return하면 tuple로 묶여서 나오는 경우가 많다.

```python
return "ok", n
```

이런 return은 실제로는 tuple을 return하는 것과 비슷하다.

```python
("ok", n)
```

그리고 가변 매개변수 `*args`로 받은 값도 tuple이다.

```python
def func(*args):
    pass
```

여기서 `args`는 tuple로 패킹된다.

tuple은 packing, unpacking에서 자주 나온다.

```python
a, b, c = (1, 2, 3)
```

오른쪽 tuple의 값이 왼쪽 변수들로 unpacking된다.

주의할 점
```python
a, b = (1, 2, 3)
```

값의 개수가 맞지 않으면 에러가 난다.

값이 1개인 tuple은 쉼표가 중요하다.

```python
(1)   # int
(1,)  # tuple
```

괄호보다 쉼표가 tuple을 만든다고 생각하면 좋다.

정리:
- tuple은 순서가 있는 container이다
- indexing 가능하다
- 한 번 만들면 값을 바꿀 수 없다
- 함수 return 값 여러개, `*args`, packing/unpacking에서 자주 사용된다
- 값 1개짜리 tuple은 `(1,)`처럼 쉼표가 필요하다



## 환경세팅

1. 가상 환경 세팅

2. requirments.txt
```bash
$ pip freeze >> requirments.txt
```

.venv
uv -> 빠르다

### UV

`uv`는 python package/project 관리 도구이다.<br>
pip, venv, pyproject.toml 관리 쪽을 빠르게 처리해주는 도구라고 보면 된다.

#### 설치방법
```bash
pip install uv
```

환경에 따라 `pip` 명령이 바로 안될 수 있으므로 아래처럼 실행할 수도 있다.

```bash
python3 -m pip install uv
```

#### 활용방법

프로젝트 생성
```bash
python3 -m uv init
```

`uv init`을 하면 기본적으로 이런 파일들이 생긴다.

```text
pyproject.toml
.python-version
README.md
main.py
```

`pyproject.toml`은 project 설정 파일이다.

```toml
[project]
name = "uv-test"
version = "0.1.0"
requires-python = ">=3.13"
dependencies = []
```

`requires-python`은 이 project에서 사용할 python version 조건이다.

```toml
requires-python = ">=3.13"
```

이렇게 되어 있으면 python 3.13 이상이 필요하다는 뜻이다.

`.python-version` 파일도 python version을 알려주는 역할을 한다.

```text
3.13
```

가상환경과 package 맞추기
```bash
python3 -m uv sync
```

`uv sync`는 `pyproject.toml`, `uv.lock`을 기준으로 package와 가상환경을 맞춘다.<br>
보통 project 안에 `.venv`가 만들어진다.

package 설치
```bash
python3 -m uv add numpy
```

설치하면 `pyproject.toml`의 `dependencies`에 자동으로 추가된다.

```toml
dependencies = [
    "numpy>=2.4.6",
]
```

package 제거
```bash
python3 -m uv remove numpy
```

실행
```bash
python3 -m uv run python main.py
```

또는
```bash
python3 -m uv run main.py
```

python version 확인
```bash
python3 -m uv run python --version
```

이 명령으로 uv project 안에서 어떤 python이 실행되는지 확인할 수 있다.

가상환경 삭제
```bash
rm -rf .venv
```

`.venv` 폴더를 지우면 가상환경이 삭제된다.<br>
다시 만들고 싶으면 `uv sync`를 하면 된다.

주의할 점
- `pyproject.toml`은 project 설정 파일이라 함부로 지우지 않는다
- `uv.lock`은 설치된 package version을 고정하는 파일이다
- `.venv`는 가상환경 폴더라 지워도 다시 만들 수 있다
- `uv` 명령이 안되면 `python3 -m uv`로 실행해본다
- python version을 3.13으로 적어두면 실제로 3.13을 사용할 수 있어야 한다

정리:
- `pip install uv` 또는 `python3 -m pip install uv`로 설치
- `python3 -m uv init`으로 project 생성
- `python3 -m uv add package명`으로 package 설치
- `python3 -m uv sync`로 가상환경/package 동기화
- `python3 -m uv run ...`으로 project 환경에서 실행
- `.venv`를 지우면 가상환경 삭제, 다시 만들려면 `uv sync`


#### 패키지 배포

pyproject.toml 파일에 아래 내용 추가
```toml
[project.scripts]
test_package_main = "test_package.__init__:main"

[build-system]
requires = ["setuptools>=42","wheel"]
build-backend = "setuptools.build_meta"
```
.whl 파일 생성
```bash
uv build --no-sources
```


## 객체지향(object oriented programming)

클래스, 객체
- 클래스는 설계도
- 객체는 설계도로 만든 인스턴스

c++
>class 클래스명 { ... }<br>
>객체를 만들면 this로 자기 자신을 가리킬 수 있음<br>

python
>class 클래스명:<br>
>def 메서드(self):<br>

```python
class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"이름: {self.name}, 나이: {self.age}")


student1 = Student("kim", 20)
student1.introduce()
```

출력 결과
```text
이름: kim, 나이: 20
```

`Student`가 클래스이고 `student1`이 객체이다.<br>
`Student("kim", 20)`처럼 호출하면 객체가 생성된다.

### special method

special method는 Python이 특정 상황에서 자동으로 호출하는 메서드이다.<br>
이름 앞뒤에 `__`가 붙어서 dunder method라고도 한다.

```python
class Student:
    def __init__(self, name: str):
        self.name = name
```

`__init__`은 객체가 생성된 뒤 초기값을 넣을 때 사용한다.<br>
생성자 느낌으로 이해하면 된다.

주의할 점
- `__init__`은 객체를 직접 만드는 함수라기보다, 만들어진 객체를 초기화하는 메서드이다
- return 값을 직접 쓰지 않는다
- `self.name = name`처럼 객체 안에 값을 저장한다

### self

`self`는 메서드 내부에서 현재 객체 자체를 가리키는 이름이다.<br>
C++의 `this`와 비슷하게 생각할 수 있다.

```python
class Counter:
    def __init__(self):
        self.count = 0

    def up(self):
        self.count += 1
        print(self.count)


c1 = Counter()
c2 = Counter()

c1.up()
c1.up()
c2.up()
```

출력 결과
```text
1
2
1
```

`c1`과 `c2`는 서로 다른 객체이다.<br>
그래서 `self.count`도 객체마다 따로 관리된다.

정리:
- `self`는 현재 객체
- 메서드를 정의할 때 첫 번째 매개변수로 적는다
- 메서드를 호출할 때는 `c1.up()`처럼 쓰고, `self`는 자동으로 전달된다

### cls

`cls`는 class 자체를 가리킬 때 사용하는 이름이다.<br>
보통 `@classmethod`와 같이 사용한다.

```python
class Student:
    school = "python school"

    def __init__(self, name: str):
        self.name = name

    @classmethod
    def print_school(cls):
        print(cls.school)


Student.print_school()
```

출력 결과
```text
python school
```

`self`는 객체를 가리키고, `cls`는 클래스를 가리킨다.

정리:
- class -> 객체를 만들기 위한 설계도
- object(instance) -> class로 실제 만든 것
- `__init__` -> 객체 초기화에 많이 사용
- `self` -> 현재 객체
- `cls` -> 현재 class
- 객체마다 따로 가져야 하는 값은 `self.변수명`
- class 전체가 공유하는 값은 class 변수로 둘 수 있다

### Student class 예제

`Student` class 안에 학생 이름과 점수를 저장하고,<br>
총합과 평균을 구하는 메서드를 추가했다.

```python
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def to_string(self):
        return f"{self.name}\t {self.korean}\t {self.math}\t {self.english}\t {self.science}\t {self.get_sum()}\t {self.get_average()}"

    def __repr__(self):
        return f"{self.name}\t {self.korean}\t {self.math}\t {self.english}\t {self.science}\t {self.get_sum()}\t {self.get_average()}"
```

`get_sum()`은 객체 안에 저장된 점수를 더해서 return한다.<br>
`get_average()`는 `self.get_sum()`을 다시 사용해서 평균을 구한다.

```python
def get_average(self):
    return self.get_sum() / 4
```

메서드 안에서 같은 객체의 다른 메서드를 부를 때도 `self.메서드명()`으로 호출한다.

### 객체 리스트

```python
students = [
    Student('abc', 34, 65, 35, 94),
    Student('gdf', 34, 45, 45, 50),
    Student('wtr', 36, 75, 63, 94),
]
```

`students`는 list이고, list 안에 `Student` 객체들이 들어간다.

주의할 점
```python
print(Student[0])
```

`Student`는 class 자체이기 때문에 index로 접근할 수 없다.<br>
첫 번째 학생 객체를 가져오려면 list 이름인 `students`를 사용해야 한다.

```python
print(students[0])
```

정리:
- `Student` -> class
- `students` -> Student 객체들을 담은 list
- `students[0]` -> 첫 번째 Student 객체
- `students[0].name` -> 첫 번째 Student 객체의 name

### 객체 출력과 `__repr__`

객체를 그냥 출력하면 원래는 주소처럼 보인다.

```python
print(students[0])
```

기본 출력 느낌
```text
<__main__.Student object at 0x...>
```

그래서 객체를 출력했을 때 어떤 문자열로 보일지 정하려면 special method를 사용할 수 있다.

```python
def __repr__(self):
    return f"{self.name}\t {self.korean}\t {self.math}\t {self.english}\t {self.science}\t {self.get_sum()}\t {self.get_average()}"
```

`print(student)`를 하면 내부적으로 문자열 표현이 필요하다.<br>
이때 `__repr__`이 정의되어 있으면 이 return 값이 출력된다.

```python
print("이름\t 국어\t 수학\t 영어\t 과학\t 총합\t 평균")
for student in students:
    print(student)
```

출력 결과
```text
이름	 국어	 수학	 영어	 과학	 총합	 평균
abc	 34	 65	 35	 94	 228	 57.0
gdf	 34	 45	 45	 50	 174	 43.5
wtr	 36	 75	 63	 94	 268	 67.0
nbd	 47	 65	 85	 70	 267	 66.75
ujd	 88	 95	 75	 33	 291	 72.75
efg	 64	 65	 55	 40	 224	 56.0
dgd	 33	 25	 75	 93	 226	 56.5
```

정리:
- 점수 데이터는 `self.korean` 같은 instance variable에 저장한다
- 계산은 `get_sum()`, `get_average()` 같은 method로 분리할 수 있다
- 객체 여러 개는 list에 담아서 for문으로 순회하면 된다
- 객체를 보기 좋게 출력하고 싶으면 `__repr__` 또는 `__str__`을 사용할 수 있다
- 사용자가 보기 위한 출력은 보통 `__str__`, 개발자가 확인하기 위한 표현은 보통 `__repr__` 느낌으로 사용한다

### isinstance

객체가 어떤 class로 만들어졌는지 확인할 때 `isinstance()`를 사용할 수 있다.

```python
class Student(object): # 상속 문법, object가 이미 숨겨져 있다
    def study(self):
        print("studying")


class Teacher:
    def teach(self):
        print("teaching")
```

Python class는 기본적으로 `object`를 상속받는다.<br>
그래서 `class Student(object)`라고 적어도 되고, 그냥 `class Student`라고 적어도 된다.

```python
student = Student()

print(isinstance(student, Student))
print(isinstance(student, int))
print(isinstance(student, object))

print(isinstance(1, object))
print(isinstance([1, 2, 3, student], object))
```

출력 결과
```text
True
False
True
True
True
```

`student`는 `Student` 객체라서 `Student` 검사 결과는 `True`이다.<br>
`int` 객체는 아니기 때문에 `False`가 나온다.

주의할 점:
- Python의 거의 모든 값은 객체이다
- 숫자 `1`, list도 object로 볼 수 있다
- 그래서 `isinstance(1, object)`도 `True`이다

### isinstance로 타입에 따라 다르게 실행

```python
classroom = [Student(), Student(), Teacher(), Student(), Student()]

for person in classroom:
    if isinstance(person, Student):
        person.study()
    if isinstance(person, Teacher):
        person.teach()
```

출력 결과
```text
studying
studying
teaching
studying
studying
```

`classroom` list 안에는 `Student` 객체와 `Teacher` 객체가 섞여 있다.<br>
그냥 `person.study()`를 호출하면 `Teacher` 객체에서는 에러가 날 수 있다.

그래서 `isinstance()`로 먼저 확인하고,<br>
해당 객체가 가지고 있는 method만 호출한다.

정리:
- `isinstance(객체, 클래스)` -> 객체가 그 class의 instance인지 확인
- 결과는 `True` 또는 `False`
- 여러 종류의 객체가 섞여 있을 때 안전하게 method 호출 가능

### special method로 연산자 사용

기본 `Student` class에 special method를 추가하면 객체끼리 연산자를 사용할 수 있다.

```python
def __add__(self, other):
    return self.get_sum() + other.get_sum()

def __sub__(self, other):
    return self.get_sum() - other.get_sum()

def __mul__(self, other):
    return self.get_sum() * other.get_sum()

def __truediv__(self, other):
    return self.get_sum() / other.get_sum()
```

`students[0] + students[1]`처럼 객체끼리 더해도,<br>
내부적으로는 `__add__`가 호출된다.

```python
print("students[0] + students[1]", students[0] + students[1])
print("students[0] - students[1]", students[0] - students[1])
print("students[0] * students[1]", students[0] * students[1])
print("students[0] / students[1]", students[0] / students[1])
```

출력 결과
```text
students[0] + students[1] 402
students[0] - students[1] 54
students[0] * students[1] 39672
students[0] / students[1] 1.3103448275862069
```

여기서는 객체 자체를 더하는 것이 아니라,<br>
각 객체의 총점 `get_sum()` 결과를 가지고 계산하게 만든 것이다.

연산자와 special method
- `+` -> `__add__`
- `-` -> `__sub__`
- `*` -> `__mul__`
- `/` -> `__truediv__`
- `>` -> `__gt__`
- `<` -> `__lt__`
- `==` -> `__eq__`
- `!=` -> `__ne__`
- `>=` -> `__ge__`
- `<=` -> `__le__`

주의할 점:
- `/`는 `__truediv__`이다
- `divmod()`에 대응되는 것은 `__divmod__`이다

### 비교 연산자와 타입 검사

```python
def __gt__(self, other):
    if isinstance(other, Student):
        return self.get_sum() > other.get_sum()
    else:
        return "error"
```

`>` 연산자를 사용하면 `__gt__`가 호출된다.

```python
print("students[0] > students[1]", students[0] > students[1])
print("students[0] > students[1]", students[0] > 90)
```

출력 결과
```text
students[0] > students[1] True
students[0] > students[1] error
```

첫 번째는 `Student` 객체끼리 비교하므로 총점을 비교할 수 있다.<br>
두 번째는 `90`이 `Student`가 아니므로 `"error"`가 return된다.

다만 실제 코드에서는 `"error"` 문자열을 return하는 것보다,<br>
예외를 발생시키거나 `NotImplemented`를 return하는 방식이 더 자연스럽다.

```python
def __gt__(self, other):
    if isinstance(other, Student):
        return self.get_sum() > other.get_sum()
    return NotImplemented
```

정리:
- special method를 만들면 객체에 연산자 의미를 줄 수 있다
- 연산 기준은 직접 정해야 한다
- `Student` 예제에서는 총점을 기준으로 연산/비교했다
- 비교 대상이 맞는 타입인지 `isinstance()`로 확인할 수 있다

### class variable

객체마다 따로 가지는 값은 instance variable이고,<br>
class 전체가 공유하는 값은 class variable이다.

```python
class Student:
    count = int()
    students = list()
```

`count`와 `students`는 class 변수이다.<br>
모든 `Student` 객체가 같이 공유한다.

```python
def __init__(self, name, korean, math, english, science):
    self.name = name
    self.korean = korean
    self.math = math
    self.english = english
    self.science = science

    Student.count += 1
    Student.students.append(self)
```

객체가 생성될 때마다 `Student.count`가 1씩 증가한다.<br>
그리고 생성된 객체 자신을 `Student.students` list에 추가한다.

```python
Student("abc", 34, 65, 35, 94)
Student("gdf", 34, 45, 45, 50)

print(Student.count)
```

`Student.count`는 class 변수라서 전체 학생 수를 세기에 좋다.

### Student.count와 self.count 차이

```python
Student.count += 1
```

이 코드는 class 변수 `count`를 직접 증가시킨다.<br>
전체 `Student` 객체가 공유하는 값이 바뀐다.

```python
self.count += 1
```

이렇게 쓰면 먼저 객체 안에서 `count`를 찾는다.<br>
없으면 class 변수에서 값을 읽을 수는 있지만, 대입되는 순간 `self.count`라는 instance variable이 따로 생길 수 있다.

정리:
- 전체 학생 수처럼 공유해야 하는 값 -> `Student.count`
- 학생 한 명마다 따로 가져야 하는 값 -> `self.name`, `self.korean`
- class 변수는 `클래스명.변수명`으로 접근하면 의도가 더 분명하다

### classmethod

class variable을 다룰 때는 `@classmethod`를 사용할 수 있다.

```python
@classmethod
def print(cls):
    print(f"등록된 학생 수는 {Student.count}")
    print("이름\t 국어\t 수학\t 영어\t 과학\t 총점\t 평균")

    for student in Student.students:
        print(student)
```

이 method는 객체 하나에 대한 동작이라기보다,<br>
`Student` class 전체에 대한 동작이다.

```python
Student.print()
```

출력 결과
```text
등록된 학생 수는 7
이름	 국어	 수학	 영어	 과학	 총점	 평균

--------------------학생 목록--------------------------
abc	 34	 65	 35	 94	 228	 57.0
gdf	 34	 45	 45	 50	 174	 43.5
wtr	 36	 75	 63	 94	 268	 67.0
nbd	 47	 65	 85	 70	 267	 66.75
ujd	 88	 95	 75	 33	 291	 72.75
efg	 64	 65	 55	 40	 224	 56.0
dgd	 33	 25	 75	 93	 226	 56.5
-------------------------------------------------------
```

주의할 점:
- `cls`를 받지만 코드 안에서 `Student.count`처럼 직접 class 이름을 써도 동작은 한다
- 다만 상속까지 생각하면 `cls.count`, `cls.students`를 쓰는 편이 더 확장하기 좋다
- `print`는 Python 내장 함수 이름이기도 해서 method 이름으로 쓰면 헷갈릴 수 있다

### name mangling

```python
self.__aa = "secret key"
```

변수 이름 앞에 `__`를 붙이면 외부에서 바로 접근하기 어렵게 이름이 바뀐다.<br>
이것을 name mangling이라고 한다.

완전히 보안 처리가 되는 것은 아니고,<br>
class 내부용 변수라는 의미를 강하게 주는 문법에 가깝다.

정리:
- `_name` -> 내부용이라는 약한 표시
- `__name` -> name mangling 적용
- Python은 완전한 private보다는 약속과 관례를 많이 사용한다

### destructor `__del__`

객체가 생성될 때는 `__init__`이 호출되고,<br>
객체가 사라질 때는 `__del__`이 호출될 수 있다.

```python
class Test:
    def __init__(self, name):
        self.name = name
        print(f"{self.name}이 생성 되었습니다.")

    def __del__(self):
        print(f"{self.name}이 파괴 되었습니다.")
```

```python
def main():
    a = Test("a")
    b = Test("b")
    c = Test("c")
    print(a, b, c)
    del c
```

실행 결과
```text
a이 생성 되었습니다.
b이 생성 되었습니다.
c이 생성 되었습니다.
<__main__.Test object at 0x...> <__main__.Test object at 0x...> <__main__.Test object at 0x...>
c이 파괴 되었습니다.
a이 파괴 되었습니다.
b이 파괴 되었습니다.
```

`del c`를 하면 이름 `c`가 객체를 더 이상 가리키지 않는다.<br>
그 객체를 참조하는 이름이 없어지면 객체가 정리되면서 `__del__`이 호출될 수 있다.

`a`, `b`는 `main()`이 끝날 때 지역변수가 사라지므로 그 뒤에 파괴된다.

주의할 점:
- `del 변수`는 객체를 바로 삭제한다기보다, 그 이름의 참조를 제거하는 것에 가깝다
- 객체를 참조하는 이름이 더 있으면 바로 파괴되지 않을 수 있다
- `__del__` 호출 시점은 항상 직접 제어하기 어렵다

정리:
- `__init__` -> 객체 초기화
- `__del__` -> 객체가 정리될 때 호출될 수 있는 special method
- 파일 닫기 같은 자원 정리는 보통 `with` 문을 더 많이 사용한다

### property

`@property`를 사용하면 method를 instance variable처럼 사용할 수 있다.

```python
class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius
```

겉으로 사용할 때는 함수 호출처럼 `circle.radius()`가 아니라,<br>
변수 접근처럼 `circle.radius`로 사용한다.

```python
circle = Circle(10)
print(circle.radius)
```

### getter, setter

```python
@radius.getter
def radius(self):
    print("getter")
    return self.__radius

@radius.setter
def radius(self, value):
    print("setter")
    if isinstance(value, int) and value > 0:
        self.__radius = value
    else:
        print("양의 정수만 넣으시오.")
```

`circle.radius`처럼 값을 읽으면 getter가 호출된다.<br>
`circle.radius = 20`처럼 값을 넣으면 setter가 호출된다.

```python
circle = Circle(10)
print(circle.radius)
circle.radius = 20
circle.radius = 3.14
circle.radius = -5
print(circle.get_area())
```

실행 결과
```text
getter
10
setter
setter
양의 정수만 넣으시오.
setter
양의 정수만 넣으시오.
1256.6370614359173
```

처음 `print(circle.radius)`에서 getter가 호출된다.<br>
`circle.radius = 20`은 양의 정수라서 radius 값이 20으로 바뀐다.

`3.14`는 float라서 실패한다.<br>
`-5`는 int이지만 양수가 아니라서 실패한다.

그래서 마지막 넓이는 반지름 20 기준으로 계산된다.

```python
math.pi * (20 ** 2)
```

정리:
- 값을 읽을 때 -> getter
- 값을 대입할 때 -> setter
- setter에서 값 검사를 할 수 있다
- 잘못된 값이면 객체 내부 값을 바꾸지 않게 막을 수 있다

### `__radius`와 `__dict__`

```python
self.__radius = radius
```

`__radius`처럼 앞에 `__`가 붙으면 name mangling이 적용된다.<br>
실제로 객체 내부 dict를 보면 이름이 바뀌어 있다.

```python
print(circle.__dict__)
print(vars(circle))
```

실행 결과
```text
{'_Circle__radius': 20}
{'_Circle__radius': 20}
```

`__radius`가 그대로 저장되는 것이 아니라 `_Circle__radius`라는 이름으로 저장된다.

`vars(circle)`도 객체의 `__dict__`를 보여주는 것과 비슷하다.

정리:
- `circle.__dict__` -> 객체가 가진 instance variable 확인
- `vars(circle)` -> 객체의 변수 dict 확인
- `__radius` -> 내부적으로 `_Circle__radius` 형태로 바뀜

### getattr

`getattr()`은 객체에서 이름으로 attribute를 가져온다.

```python
print(getattr(circle, "get_area"))
print(getattr(circle, "get_area")())
print(getattr(circle, "get_area2", None))
```

실행 결과
```text
<bound method Circle.get_area of <__main__.Circle object at 0x...>>
1256.6370614359173
None
```

`getattr(circle, "get_area")`는 method 자체를 가져온다.<br>
아직 호출한 것은 아니기 때문에 bound method라고 출력된다.

```python
getattr(circle, "get_area")()
```

뒤에 `()`를 붙이면 가져온 method를 호출한다.

```python
getattr(circle, "get_area2", None)
```

없는 이름을 가져오려고 할 때 세 번째 값으로 기본값을 줄 수 있다.<br>
그래서 에러가 아니라 `None`이 나온다.

정리:
- `getattr(객체, "이름")` -> 이름으로 attribute 가져오기
- method를 가져온 뒤 호출하려면 뒤에 `()`를 붙인다
- `getattr(객체, "없는이름", 기본값)` 형태로 에러 대신 기본값을 받을 수 있다

### class inheritance

상속은 부모 class의 attribute와 method를 자식 class가 이어받는 것이다.

```python
class Parent:
    def __init__(self, value):
        self.value = "테스트"
        self.value2 = value
        print("Parent 클래스의 __init__ 메소드가 호출 되었다.")

    def test(self, *args):
        print("Parent 클래스의 test 메소드 입니다.")
```

```python
class Child(Parent):
    def __init__(self, value):
        super().__init__(value)
        print("Child 클래스의 __init__ 메소드가 호출 되었다.")

    def test(self, *args):
        print("Child 클래스의 test 메소드 입니다.")
```

`class Child(Parent)`처럼 적으면 `Child`가 `Parent`를 상속받는다.<br>
자식 class에서 부모의 `__init__`을 실행하고 싶으면 `super().__init__()`을 사용한다.

```python
child = Child("자식 자료")
child.test()
print(child.value)
print(child.value2)
```

실행 결과
```text
Parent 클래스의 __init__ 메소드가 호출 되었다.
Child 클래스의 __init__ 메소드가 호출 되었다.
Child 클래스의 test 메소드 입니다.
테스트
자식 자료
```

`Child` 객체를 만들 때 `Child.__init__`이 실행된다.<br>
그 안에서 `super().__init__(value)`를 호출했기 때문에 부모의 `__init__`도 실행된다.

그래서 부모 쪽에서 만든 `self.value`, `self.value2`를 자식 객체에서도 사용할 수 있다.

정리:
- 부모 class -> 공통 기능을 가지고 있음
- 자식 class -> 부모 기능을 이어받고 필요한 것을 추가/수정
- `super()` -> 부모 class 쪽 method 호출
- 부모 `__init__`을 호출하지 않으면 부모에서 초기화한 값이 없을 수 있다

### overriding

부모 class와 자식 class에 같은 이름의 method가 있으면,<br>
자식 class의 method가 우선 사용된다.

```python
class Parent:
    def test(self, *args):
        print("Parent 클래스의 test 메소드 입니다.")


class Child(Parent):
    def test(self, *args):
        print("Child 클래스의 test 메소드 입니다.")
```

```python
pObject = Parent("부모 자료")
pObject.test()

child = Child("자식 자료")
child.test()
```

실행 결과
```text
Parent 클래스의 test 메소드 입니다.
Child 클래스의 test 메소드 입니다.
```

이렇게 부모 method를 자식 쪽에서 다시 정의하는 것을 overriding이라고 한다.

주의할 점:
- Python에서는 같은 이름의 함수를 여러 개 만들어서 구분하는 overloading이 기본적으로 없다
- 같은 이름으로 다시 정의하면 마지막 정의가 사용된다
- 상속에서는 부모 method를 자식 method가 덮어쓰는 overriding을 많이 사용한다

### multiple inheritance

Python은 여러 부모 class를 상속받을 수 있다.

```python
class Person:
    def __init__(self, b):
        self.b = b

    def greeting(self):
        print("안녕하세요!")


class University:
    def __init__(self, a):
        self.a = a

    def message_credit(self):
        print("학점관리")
```

```python
class Undergraduate(Person, University):
    def __init__(self):
        Person.__init__(self, 1)
        University.__init__(self, 2)

    def study(self):
        print("공부하기")
```

`Undergraduate`는 `Person`과 `University`를 둘 다 상속받는다.<br>
그래서 `greeting()`, `message_credit()` 둘 다 사용할 수 있다.

```python
james = Undergraduate()
james.greeting()
james.message_credit()
james.study()
print(james.a, james.b)
```

실행 결과
```text
안녕하세요!
학점관리
공부하기
2 1
```

`Person.__init__(self, 1)`에서 `self.b = 1`이 만들어진다.<br>
`University.__init__(self, 2)`에서 `self.a = 2`가 만들어진다.

그래서 `print(james.a, james.b)` 결과가 `2 1`이다.

### MRO

MRO는 Method Resolution Order이다.<br>
method나 attribute를 찾을 때 어떤 class 순서로 찾는지 보여준다.

```python
print(Undergraduate.__mro__)
```

실행 결과
```text
(<class '__main__.Undergraduate'>, <class '__main__.Person'>, <class '__main__.University'>, <class 'object'>)
```

찾는 순서:
- `Undergraduate`
- `Person`
- `University`
- `object`

다중 상속에서 같은 이름의 method가 여러 부모에 있으면,<br>
이 MRO 순서에 따라 먼저 찾은 method가 사용된다.

주의할 점:
- 다중 상속에서는 부모 class의 `__init__` 호출 순서를 신경써야 한다
- 예제처럼 `Person.__init__(self, 1)` 형태로 직접 호출할 수 있다
- `super()`도 MRO를 기준으로 움직인다
- 다중 상속은 편하지만 구조가 복잡해질 수 있어서 조심해서 사용한다

정리:
- 단일 상속: `class Child(Parent)`
- 다중 상속: `class Undergraduate(Person, University)`
- overriding: 부모 method를 자식에서 다시 정의
- MRO: method를 찾는 class 순서
- 다중 상속에서 같은 이름이 겹치면 MRO 순서가 중요하다

### dataclass

데이터를 담는 class를 만들 때 `dataclass`를 사용할 수 있다.<br>
반복해서 작성하던 `__init__`, `__repr__` 같은 코드를 자동으로 만들어준다.

```python
from dataclasses import dataclass


@dataclass
class Student:
    name: str
    korean: int
    math: int
    english: int
    science: int

    def get_sum(self):
        return self.korean + self.math + self.english + self.science
```

일반 class에서는 보통 이렇게 직접 적었다.

```python
def __init__(self, name, korean, math, english, science):
    self.name = name
    self.korean = korean
    self.math = math
    self.english = english
    self.science = science
```

`@dataclass`를 쓰면 위와 같은 초기화 코드를 직접 안 적어도 된다.<br>
class 안에 type hint로 field를 적어두면 자동으로 `__init__`이 만들어진다.

```python
student = Student("abc", 34, 65, 35, 94)
print(student)
print(student.get_sum())
```

실행 결과
```text
Student(name='abc', korean=34, math=65, english=35, science=94)
228
```

`print(student)`를 했을 때도 주소가 아니라 내용이 보기 좋게 나온다.<br>
이것은 dataclass가 `__repr__`도 자동으로 만들어주기 때문이다.

정리:
- `@dataclass` -> 데이터 저장용 class를 짧게 만들 수 있음
- type hint로 field를 적으면 `__init__`이 자동 생성된다
- `print()` 했을 때 보기 좋은 `__repr__`도 자동 생성된다
- `get_sum()` 같은 일반 method는 그대로 추가할 수 있다
- 점수 데이터처럼 단순히 값을 묶어서 다룰 때 편하다

주의할 점:
- `dataclass`를 쓰려면 `from dataclasses import dataclass`가 필요하다
- type hint를 적어야 field로 인식된다
- 복잡한 동작보다 데이터 저장이 중심인 class에 잘 맞는다

## file write

파일을 쓸 때는 `open()`을 사용한다.<br>
파일 경로는 문자열로 직접 써도 되지만, `pathlib.Path`를 사용하면 경로를 다루기 편하다.

```python
from pathlib import Path


def main():
    path = Path(r"/home/hrd_1_3/study/python_example/data")

    with open(path / "text.txt", "a") as f:
        f.write("hello!!!")
```

`path / "text.txt"`는 경로를 합치는 표현이다.<br>
문자열을 `+`로 이어붙이는 것보다 OS 경로를 다룰 때 자연스럽다.

파일 모드:
- `"w"` -> write, 새로 쓰기. 기존 내용이 지워질 수 있다
- `"a"` -> append, 기존 내용 뒤에 추가
- `"r"` -> read, 읽기

`with open(...) as f:`를 사용하면 파일을 사용한 뒤 자동으로 닫힌다.<br>
그래서 `f.close()`를 직접 호출하지 않아도 된다.

주의할 점:
- `"a"` 모드는 뒤에 이어붙인다
- `f.write("hello!!!")`에는 줄바꿈이 없어서 기존 내용 바로 뒤에 붙을 수 있다
- 줄을 바꾸고 싶으면 `"hello!!!\n"`처럼 `\n`을 넣어야 한다

## file read

파일을 읽을 때도 `with open()`을 사용할 수 있다.

```python
from pathlib import Path
import sys


def main():
    path = Path(r"/home/hrd_1_3/study/python_example/data")

    with open(path / "text.txt", "r") as f:
        while data := f.readline():
            print(data)
```

`readlines()`는 파일 전체 줄을 list로 가져온다.<br>
`read()`는 파일 전체 내용을 문자열로 가져온다.

파일이 크면 한 번에 전부 읽는 것보다,<br>
`readline()`으로 한 줄씩 읽는 방식이 메모리 사용에 좋다.

```python
while data := f.readline():
    print(data)
```

16번 줄의 `:=`는 walrus operator이다.<br>
이미 앞에서 [list method 정리 부분](/home/hrd_1_3/study/python_example/study.md:726)에 한 번 적어두었다.

여기서는 `f.readline()` 결과를 `data`에 대입하면서,<br>
그 값이 비어있는지 아닌지를 `while` 조건으로 같이 확인한다.

풀어서 쓰면 이런 느낌이다.

```python
while True:
    data = f.readline()
    if not data:
        break
    print(data)
```

`readline()`은 더 읽을 줄이 없으면 빈 문자열 `""`을 return한다.<br>
빈 문자열은 조건식에서 `False`처럼 동작하므로 while문이 끝난다.

주의할 점:
- `print(data)`는 기본적으로 줄바꿈을 한 번 더 한다
- `data` 안에도 파일에서 읽은 `\n`이 들어있을 수 있다
- 그래서 출력할 때 줄이 한 줄씩 더 비어 보일 수 있다

### standard stream

```python
print(sys.stdin.fileno())
print(sys.stdout.fileno())
print(sys.stderr.fileno())
print("error message", file=sys.stderr)
```

표준 입출력도 파일처럼 다룰 수 있다.

정리:
- `sys.stdin` -> 표준 입력
- `sys.stdout` -> 표준 출력
- `sys.stderr` -> 표준 에러
- `print(..., file=sys.stderr)` -> 에러 출력 쪽으로 출력

```python
with open(path / "text.txt", "a", encoding="utf-8") as f:
    print("이것은 프린트로 파일을 쓴 데이터이다.", file=f)
```

`print()`도 `file=` 옵션을 주면 화면이 아니라 파일에 쓸 수 있다.<br>
`print()`는 기본적으로 끝에 줄바꿈을 붙이므로 `f.write()`와 차이가 있다.

## JSON serialization

JSON 파일은 Python에서 `json` module로 읽을 수 있다.

```python
import json
from pathlib import Path


def main():
    path = Path(r"/home/hrd_1_3/study/python_example/data/test.json")

    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
        print(data)
        print(type(data))
```

`json.load(f)`는 파일 객체에서 JSON 데이터를 읽어서 Python 객체로 바꾼다.<br>
예제에서는 JSON object가 Python `dict`로 변환된다.

실행 결과
```text
{'abc': 123, 'name': 'son', 'subject': {'korean': 99, 'math': 83}}
<class 'dict'>
```

정리:
- JSON object -> Python dict
- JSON string -> Python str
- JSON number -> Python int 또는 float
- JSON array -> Python list
- `json.load(f)` -> 파일에서 읽기

## YAML serialization

YAML 파일은 `yaml` module을 사용해서 읽을 수 있다.<br>
실습에서는 `pyyaml` package가 필요하다.

```python
# python3.10 -m pip install pyyaml

from pathlib import Path

import yaml


def main():
    path = Path(r"/home/hrd_1_3/study/python_example/data/test.yaml")

    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
        print(data)
        print(type(data))
        print(data["abc"])
        print(data["subject"]["korean"])
```

`yaml.safe_load(f)`는 YAML 파일을 Python 객체로 바꾼다.<br>
예제에서는 YAML 내용도 Python `dict`로 바뀐다.

실행 결과
```text
{'abc': 123, 'name': 'son', 'subject': {'korean': 99, 'math': 83}}
<class 'dict'>
123
99
```

YAML 원본
```yaml
abc: 123
name: son
subject:
  korean: 99
  math: 83
```

중첩된 값은 dict 안의 dict처럼 접근한다.

```python
data["subject"]["korean"]
```

정리:
- YAML도 Python에서 dict/list 형태로 읽을 수 있다
- `yaml.safe_load()`를 사용하는 것이 일반적으로 안전하다
- 설정 파일은 JSON보다 YAML이 더 읽기 편할 때가 있다
- 들여쓰기로 구조를 표현하므로 indentation을 조심해야 한다

JSON과 YAML 비교:
- JSON은 문법이 엄격하고 다른 언어와 주고받기 좋다
- YAML은 사람이 읽고 쓰기 편해서 설정 파일에 자주 사용한다
- Python으로 읽으면 둘 다 dict/list 같은 객체로 다룰 수 있다

## pickle serialization

`pickle`은 Python 객체를 파일에 저장하고 다시 불러올 때 사용할 수 있다.<br>
JSON/YAML은 dict, list, str 같은 데이터 교환용 느낌이고,<br>
pickle은 Python 객체 자체를 저장하는 느낌에 가깝다.

```python
import random
from pathlib import Path
import pickle
```

`student_model.py`에서는 `Student` 객체 100개를 만들고 list에 담는다.

```python
students = [
    Student(
        random.choice(hanguls) + "".join(random.choices(hanguls2, k=2)),
        random.randint(65, 100),
        random.randint(65, 100),
        random.randint(65, 100),
        random.randint(65, 100)
    )
    for _ in range(100)
]
```

list comprehension으로 `Student` 객체를 100개 생성한다.<br>
`random.choice()`는 하나를 고르고, `random.choices(..., k=2)`는 여러 개를 뽑는다.

```python
with path.open("wb") as f:
    pickle.dump(students, f)
```

`pickle.dump(students, f)`는 `students` list 전체를 파일에 저장한다.<br>
`"wb"`는 write binary 모드이다.

정리:
- `pickle.dump(객체, 파일)` -> 객체를 파일에 저장
- pickle은 binary 형태로 저장하므로 `"wb"` 사용
- list 안에 들어있는 `Student` 객체들도 같이 저장된다

### pickle load

저장한 pickle 파일은 `pickle.load()`로 다시 읽을 수 있다.

```python
from pathlib import Path
import pickle
from student_model import Student


def main():
    students = []
    path = Path(r"/home/hrd_1_3/study/python_example/data/test.pickle")

    with path.open("rb") as f:
        students = pickle.load(f)

    Student.students = students
    Student.print()
```

`"rb"`는 read binary 모드이다.<br>
저장할 때 `pickle.dump(students, f)`로 list 전체를 한 번에 저장했으므로,<br>
읽을 때도 `pickle.load(f)` 한 번으로 list 전체를 가져온다.

주의할 점:
```python
while data := pickle.load(f):
    students.append(data)
```

이 방식은 객체를 여러 번 나눠서 dump했을 때 생각해볼 수 있다.<br>
지금 파일은 list 하나를 통째로 dump했기 때문에 while로 반복해서 읽는 구조와 맞지 않는다.

파일 끝까지 읽으면 `EOFError`가 날 수 있어서 이전 코드에서는 이렇게 처리하려고 했다.

```python
try:
    while data := pickle.load(f):
        students.append(data)
except EOFError:
    pass
```

하지만 현재 예제에서는 list 하나를 저장했으므로 아래처럼 읽는 것이 더 단순하다.

```python
students = pickle.load(f)
```

### pickle load와 class variable

로드한 뒤에 이렇게 넣어준다.

```python
Student.students = students
Student.print()
```

pickle로 객체를 복원할 때는 `Student.__init__()`이 다시 실행되지 않는다.<br>
그래서 `__init__` 안에 있던 아래 코드도 자동으로 다시 실행되지 않는다.

```python
Student.count += 1
Student.students.append(self)
```

그래서 로드한 학생 목록을 `Student.students`에 직접 넣어준 것이다.

실행 결과에서 학생 목록은 나오지만,

```text
등록된 학생 수는 0
```

처럼 count가 0으로 나올 수 있다.

이유는 `Student.students = students`만 했고,<br>
`Student.count`는 다시 설정하지 않았기 때문이다.

```python
Student.students = students
Student.count = len(students)
```

이렇게 하면 학생 수까지 맞출 수 있다.

정리:
- pickle load는 저장된 객체를 복원한다
- 복원할 때 `__init__`이 다시 호출되지 않는다
- class variable은 필요하면 직접 다시 맞춰줘야 한다
- `Student.students = students` -> 목록 복원
- `Student.count = len(students)` -> 개수 복원

주의할 점:
- pickle은 Python 전용에 가깝다
- 모르는 사람이 만든 pickle 파일은 함부로 열면 위험할 수 있다
- class가 저장될 때의 module/class 이름과 load할 때의 구조가 맞아야 한다

## try except

예외가 날 수 있는 코드는 `try` 안에 넣고,<br>
예외가 발생했을 때 처리할 코드는 `except`에 적는다.

```python
import math


def main():
    user_input = input("정수 입력")
    try:
        number_input = int(user_input)
        if number_input < 0:
            raise NagativeError
        print("원의 반지름: ", number_input)
        print("원의 둘레: ", 2 * math.pi * number_input)
        print("원의 넓이: ", math.pi * number_input * number_input)
    except ValueError as e:
        print("정수를 입력하지 않았습니다.\n", e)
    except NagativeError as e:
        print("양의 정수를 입력하세요.\n", e)
    finally:
        print("--------------- 프로그램이 끝났습니다. ------------------")
```

`input()`은 무조건 str을 return한다.<br>
그래서 숫자로 계산하려면 `int(user_input)`처럼 변환해야 한다.

정상 입력
```text
정수 입력원의 반지름:  10
원의 둘레:  62.83185307179586
원의 넓이:  314.1592653589793
--------------- 프로그램이 끝났습니다. ------------------
```

문자 입력
```text
정수 입력정수를 입력하지 않았습니다.
 invalid literal for int() with base 10: 'abc'
--------------- 프로그램이 끝났습니다. ------------------
```

`abc`는 정수로 바꿀 수 없어서 `ValueError`가 발생한다.<br>
그래서 `except ValueError as e:` 부분이 실행된다.

### custom exception

직접 예외 class를 만들 수도 있다.

```python
class NagativeError(Exception):
    def __init__(self, *args):
        super().__init__(*args)
        self.args = ["이것은 내가 만든 네가티브 에러이다."]
```

`Exception`을 상속받으면 사용자 정의 예외를 만들 수 있다.<br>
예제에서는 음수가 들어오면 직접 예외를 발생시킨다.

```python
if number_input < 0:
    raise NagativeError
```

음수 입력
```text
정수 입력양의 정수를 입력하세요.
 이것은 내가 만든 네가티브 에러이다.
--------------- 프로그램이 끝났습니다. ------------------
```

`raise`는 예외를 직접 발생시키는 문법이다.<br>
음수는 `int()` 변환 자체는 가능하지만, 프로그램 규칙상 허용하지 않기 때문에 직접 예외를 발생시킨다.

정리:
- `try` -> 예외가 날 수 있는 코드
- `except ValueError as e` -> ValueError 처리
- `raise` -> 예외를 직접 발생
- `finally` -> 예외 발생 여부와 상관없이 마지막에 실행
- custom exception은 `Exception`을 상속해서 만든다

주의할 점:
- `NagativeError`는 철자가 `NegativeError`가 더 자연스럽다
- `raise NagativeError`보다 `raise NagativeError()`처럼 객체를 만들어 던지는 형태가 더 명확하다
- 모든 예외를 `except Exception`으로 크게 잡으면 원인을 놓칠 수 있다

## main argument

C에서는 main 함수에서 실행 인자를 받을 때 이런 형태를 사용한다.

```c
int main(int argc, char *argv[])
```

python에서는 `sys.argv`로 실행 인자를 확인할 수 있다.

```python
import sys


def main():
    if len(sys.argv) < 2:
        print("사용법: 로드할 파일을 명시하시오!")
        sys.exit()

    print("정상작동")
```

`sys.argv`는 list이다.<br>
첫 번째 값 `sys.argv[0]`에는 실행한 파일 이름이 들어간다.

```python
# print(sys.argv[0])
# print(sys.argv[1])
```

명령행에서 파일 뒤에 적은 값들이 그 다음 index에 들어간다.

```bash
python3 basic/a103_main_argument.py abc 123 hello
```

이런 식으로 실행하면 대략 이런 구조가 된다.

```python
sys.argv[0] # basic/a103_main_argument.py
sys.argv[1] # abc
sys.argv[2] # 123
sys.argv[3] # hello
```

주의할 점:
- command line argument는 기본적으로 str이다
- 숫자로 쓰고 싶으면 `int(sys.argv[1])`처럼 변환해야 한다
- 인자가 없는 상태에서 `sys.argv[1]`에 접근하면 index error가 날 수 있다

그래서 먼저 길이를 확인한다.

```python
if len(sys.argv) < 2:
    print("사용법: 로드할 파일을 명시하시오!")
    sys.exit()
```

인자가 없으면 사용법을 출력하고 `sys.exit()`로 프로그램을 끝낸다.

인자 없이 실행
```bash
python3 basic/a103_main_argument.py
```

실행 결과
```text
사용법: 로드할 파일을 명시하시오!
```

인자를 넣고 실행
```bash
python3 basic/a103_main_argument.py abc 123 hello
```

실행 결과
```text
정상작동
```

정리:
- `sys.argv` -> command line argument list
- `sys.argv[0]` -> 실행한 script 이름
- `sys.argv[1]`부터 사용자가 넘긴 argument
- `len(sys.argv)`로 argument 개수를 확인한다
- `sys.exit()`는 프로그램을 종료할 때 사용한다
- argument가 많아지고 option 처리가 필요하면 `argparse` library를 사용하면 좋다



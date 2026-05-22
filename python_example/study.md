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



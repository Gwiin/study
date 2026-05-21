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

# 머신러닝 학습 정리

## 학습 목적

이 폴더는 NumPy부터 시작해 데이터 분석과 머신러닝으로 이어지는 과정을 정리한다.

실습 코드만 모아두는 것이 아니라 다음 내용을 함께 기록한다.

- 개념을 왜 사용하는지
- 코드의 입력값과 결과
- 배열이나 데이터의 `shape`, `dtype`
- 실행 중 발생한 오류와 원인
- 머신러닝 과정에서 주의할 데이터 누수와 평가 방법
- 공식 문서와 실제 실행 결과를 기준으로 확인한 내용

학습 내용은 교재를 그대로 옮기기보다 직접 실습하면서 이해한 흐름으로 작성한다.

## 폴더 구조

```text
ML/
├─ README.md
├─ prompt.md
├─ pyproject.toml
├─ uv.lock
├─ .venv/
├─ references/
│  ├─ 1_넘파이_KarL.pdf
│  └─ 2_맷플롯립_KarL.pdf
├─ numpy/
│  └─ ex_01.ipynb
└─ matplot/
   └─ ex_01.ipynb
```

- `README.md`: ML 과정 전체 학습 정리
- `prompt.md`: 학습 내용을 README에 정리할 때 사용하는 공통 프롬프트
- `pyproject.toml`, `uv.lock`: ML 과정에서 공유하는 Python 환경
- `.venv/`: `uv`가 생성하는 가상환경이며 Git에는 포함하지 않음
- `references/`: 수업에서 제공된 강의 자료와 참고 문서
- `numpy/`: NumPy 실습 노트북과 예제 코드
- `matplot/`: Matplotlib 실습 노트북과 예제 코드

NumPy, pandas, matplotlib, scikit-learn은 서로 연계되므로 우선 `ML`에서 하나의 가상환경을 공유한다. 특정 과정에서 의존성 충돌이 생길 때만 별도 프로젝트로 분리한다.

## 강의 자료

- `references/1_넘파이_KarL.pdf`: NumPy 수업 참고 자료
- `references/2_맷플롯립_KarL.pdf`: Matplotlib 수업 참고 자료

README를 정리할 때 강의 자료의 설명 순서와 수업 맥락을 참고한다. 다만 강의 자료의 내용을 그대로 옮기거나 무조건 정답으로 취급하지 않는다. 코드의 실제 실행 결과와 현재 NumPy 공식 문서를 함께 확인하여 잘못되었거나 버전에 따라 달라진 내용은 바로잡는다.

## 개발 환경

- IDE: PyCharm
- 패키지 및 가상환경 관리: `uv`
- Python: 3.13.x
- 실습 형식: Jupyter Notebook과 Python 코드

### 환경 생성 및 동기화

저장소 최상위 폴더에서 실행한다.

```powershell
uv sync --project ML
```

또는 `ML` 폴더로 이동해서 실행한다.

```powershell
cd ML
uv sync
```

PyCharm 인터프리터는 다음 경로를 선택한다.

```text
ML\.venv\Scripts\python.exe
```

패키지를 추가할 때는 `ML` 프로젝트에 추가한다.

```powershell
uv add --project ML pandas
uv add --project ML matplotlib
uv add --project ML scikit-learn
```

## 학습 정리 원칙

- 코드에서 직접 확인할 수 있는 내용은 실행 결과와 함께 기록한다.
- 배열은 가능한 경우 `shape`, `ndim`, `dtype`을 함께 확인한다.
- `axis`, broadcasting, view와 copy처럼 혼동하기 쉬운 내용은 입력과 출력 모양을 같이 적는다.
- 수학식은 기호만 나열하지 않고 코드에서 어떤 계산으로 연결되는지 설명한다.
- 머신러닝 실습은 데이터 분리, 전처리, 학습, 예측, 평가 순서를 구분한다.
- 정확도 하나만 보고 모델을 판단하지 않는다. 문제에 맞는 평가 지표와 기준 모델을 확인한다.
- 데이터 누수를 막기 위해 테스트 데이터에서 얻은 정보를 학습 과정에 사용하지 않는다.
- 기존 내용과 중복되면 반복 설명을 줄이고 새로 배운 차이점만 추가한다.
- 확실하지 않은 내용은 단정하지 않고 확인이 필요한 부분으로 표시한다.

---

## NumPy

NumPy는 다차원 배열인 `ndarray`를 중심으로 수치 계산을 수행하는 Python 라이브러리다.

이번 학습은 다음 자료를 기준으로 확인했다.

- 실습 파일: `numpy/ex_01.ipynb`
- 강의 자료: `references/1_넘파이_KarL.pdf` 4~26페이지
- 실행 환경: Python 3.13.13, NumPy 2.4.5

### Python `list`와 NumPy 배열

Python `list`의 `+` 연산은 두 리스트를 이어 붙인다.

```python
list_a = [10, 20, 30]
list_b = [20, 30, 40]

print(list_a + list_b)
```

실행 결과:

```text
[10, 20, 30, 20, 30, 40]
```

NumPy 배열의 `+` 연산은 같은 위치의 원소끼리 더한다.

```python
import numpy as np

array_a = np.array([10, 20, 30])
array_b = np.array([20, 30, 40])

print(array_a + array_b)
```

실행 결과:

```text
[30 50 70]
```

정리:

- Python `list + list`는 연결 연산이다.
- `ndarray + ndarray`는 조건에 맞는 배열끼리 원소별 덧셈을 수행한다.
- NumPy 배열은 보통 하나의 `dtype`으로 원소를 관리한다.
- NumPy가 항상 빠른 것은 아니다. 반복적인 수치 계산을 벡터화할 수 있을 때 장점이 크다.

### 배열 생성과 `dtype` 결정

`np.array()`에 Python 리스트를 전달하면 `ndarray`를 만들 수 있다.

```python
values = [1, 2, 3, 4, 5.0]
array = np.array(values)

print(array)
print(array.dtype)
```

실행 결과:

```text
[1. 2. 3. 4. 5.]
float64
```

정수와 실수가 섞여 있으므로 모든 원소를 함께 표현할 수 있는 `float64` 배열이 생성되었다. 이러한 자료형 변환을 type promotion이라고 한다.

### 배열의 기본 속성

```python
array = np.array([[1, 2, 3], [4, 5, 6]])

print(array.shape)
print(array.ndim)
print(array.dtype)
print(array.size)
```

확인할 내용:

- `shape`: 각 축의 원소 수를 튜플로 나타냄
- `ndim`: 축의 개수, 즉 배열의 차원 수
- `dtype`: 배열 원소의 자료형 확인
- `size`: 배열 전체 원소 수

위 배열의 `shape`는 `(2, 3)`이다. 첫 번째 축의 크기가 2이고 두 번째 축의 크기가 3이라는 뜻이다.

1차원 배열의 `shape`는 `(3,)`처럼 표시한다. `(3)`은 정수지만 `(3,)`은 원소가 하나인 튜플이므로 쉼표가 필요하다.

### 원소별 사칙연산

```python
array_a = np.array([10, 20, 30])
array_b = np.array([1, 2, 3])

print(array_a + array_b)
print(array_a - array_b)
print(array_a * array_b)
print(array_a / array_b)
```

실행 결과:

```text
[11 22 33]
[ 9 18 27]
[10 40 90]
[10. 10. 10.]
```

연산은 같은 위치의 원소끼리 수행된다. `/`의 결과는 정수로 정확히 나누어지더라도 실수 배열이 된다.

주의할 점:

- `*`는 원소별 곱셈이다.
- 행렬곱에는 `@` 또는 `np.matmul()`을 사용한다.
- 두 배열의 모양이 다르면 broadcasting 규칙을 만족해야 한다.

### Broadcasting

Broadcasting은 서로 다른 `shape`의 배열을 일정한 규칙에 따라 원소별 연산이 가능한 모양으로 맞추는 기능이다.

```python
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
])
row = np.array([2, 3, 4])

print(matrix + row)
print(matrix * row)
```

실행 결과:

```text
[[12 23 34]
 [42 53 64]]

[[ 20  60 120]
 [ 80 150 240]]
```

`matrix.shape`는 `(2, 3)`이고 `row.shape`는 `(3,)`이다. 뒤쪽 축의 크기 `3`이 같으므로 `row`가 각 행에 적용된다.

Broadcasting 규칙:

- 두 배열의 뒤쪽 축부터 크기를 비교한다.
- 축의 크기가 서로 같거나 한쪽이 `1`이면 호환된다.
- 축의 개수가 부족하면 앞쪽에 크기 `1`인 축이 있다고 간주한다.
- 호환되지 않으면 `ValueError`가 발생한다.

강의 자료에서는 작은 배열이 큰 배열 크기로 확장된다고 설명한다. 이는 연산을 이해하기 위한 개념적인 표현이며, 일반적으로 실제 데이터를 반복 복사하여 큰 배열을 만드는 것은 아니다.

### 특정 값으로 배열 생성

```python
zeros = np.zeros((2, 3))
ones = np.ones((2, 3))
full = np.full((2, 3), 255)
identity = np.eye(3)
```

| 함수 | 생성 결과 | 기본 `dtype` |
|---|---|---|
| `np.zeros(shape)` | 모든 값이 0인 배열 | `float64` |
| `np.ones(shape)` | 모든 값이 1인 배열 | `float64` |
| `np.full(shape, value)` | 지정한 값으로 채운 배열 | `value`에서 추론 |
| `np.eye(n)` | 주대각선이 1인 2차원 배열 | `float64` |

실습에서 `np.ones((100, 100)) * 255`는 `float64` 배열을 만들지만 `np.full((100, 100), 255)`는 정수 배열을 만든다. 필요한 자료형이 정해져 있다면 `dtype`을 명시하는 편이 분명하다.

```python
image = np.full((100, 100), 255, dtype=np.uint8)
```

### 연속적인 값 생성

#### `np.arange()`

```python
print(np.arange(0, 5, 0.2))
```

`np.arange(start, stop, step)`은 `start`부터 `stop` 미만까지 `step` 간격의 값을 만든다. Python의 `range()`와 달리 실수 간격도 사용할 수 있다.

실수는 이진 부동소수점으로 정확히 표현되지 않을 수 있다.

```text
0.6000000000000001
1.2000000000000002
```

따라서 실수 구간에서 원소 개수나 마지막 값이 중요하면 `arange()`보다 `linspace()`가 더 적합하다.

#### `np.linspace()`

```python
print(np.linspace(0, 10, 5))
```

실행 결과:

```text
[ 0.   2.5  5.   7.5 10. ]
```

`np.linspace(start, stop, num)`은 기본적으로 시작값과 끝값을 모두 포함하여 `num`개의 일정한 간격 값을 만든다.

#### `np.logspace()`

```python
print(np.logspace(0, 5, 6))
```

실행 결과:

```text
[1.e+00 1.e+01 1.e+02 1.e+03 1.e+04 1.e+05]
```

기본 밑은 10이므로 `10**0`부터 `10**5`까지 로그 간격으로 6개의 값을 만든다. 밑은 `base` 매개변수로 변경할 수 있다.

### NumPy 수학 함수와 근사값

NumPy 수학 함수는 배열 전체에 원소별로 적용할 수 있다.

```python
angles = np.linspace(0, np.pi, 11)
print(np.sin(angles))
```

마지막 값인 `sin(pi)`는 수학적으로 0이지만 실행 결과는 다음과 같은 매우 작은 값이다.

```text
1.2246467991473532e-16
```

이는 계산 오류라기보다 부동소수점 근사 표현에서 발생하는 정상적인 오차다. 실수 결과를 비교할 때는 `==`보다 `np.isclose()` 또는 `np.allclose()`를 사용하는 것이 안전하다.

정리:

- NumPy 배열은 같은 `dtype`의 원소를 다차원 구조로 관리한다.
- 배열 연산자는 대부분 원소별로 동작한다.
- 서로 다른 `shape`의 연산은 broadcasting 규칙을 확인한다.
- `zeros`, `ones`, `full`, `eye`로 목적에 맞는 배열을 생성할 수 있다.
- 일정한 간격은 `arange`, 일정한 개수는 `linspace`, 로그 간격은 `logspace`를 사용한다.
- 부동소수점 계산 결과는 정확한 0이나 소수 표현과 조금 다를 수 있다.

### 배열 조작 추가 실습

이번 추가 실습에서는 배열의 삽입, 뒤집기, 슬라이싱, 조건 선택, 전치, 정렬, 결합을 확인했다.

#### `np.insert()`

```python
a = np.array([[1, 1], [2, 2], [3, 3]])
b = np.insert(a, 1, 4, axis=0)
c = np.insert(a, 1, 4, axis=1)

print(a.shape)
print(b.shape)
print(c.shape)
```

확인할 내용:

```text
(3, 2)
(4, 2)
(3, 3)
```

`axis=0`으로 삽입하면 첫 번째 축의 길이가 늘어나고, `axis=1`로 삽입하면 두 번째 축의 길이가 늘어난다. `axis`는 어느 방향으로 보이는지가 아니라 어느 축의 크기가 바뀌는지로 확인하는 편이 안전하다.

#### `np.flip()`

```python
c = np.array([[1, 2, 3], [4, 5, 6]])

print(np.flip(c, axis=1))
print(np.flip(c, axis=0))
```

실행 결과:

```text
[[3 2 1]
 [6 5 4]]
[[4 5 6]
 [1 2 3]]
```

`axis=1`은 두 번째 축의 원소 순서를 뒤집고, `axis=0`은 첫 번째 축의 원소 순서를 뒤집는다. 두 축을 모두 뒤집으면 배열 전체를 반대 방향으로 읽는 결과가 된다.

#### 슬라이싱과 조건 선택

```python
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [0, 1, 2]])
print(arr_2d[1:, 0:2])
```

실행 결과:

```text
[[4 5]
 [7 8]
 [0 1]]
```

슬라이싱은 범위를 잘라오지만 차원을 자동으로 줄이지 않는다. 위 결과는 2차원 배열로 유지된다.

조건식은 배열과 같은 모양의 `bool` 배열을 만든다.

```python
x = np.arange(1, 17).reshape(4, 4)
result = x % 2 == 0

print(result)
print(x[result])
```

실행 결과:

```text
[[False  True False  True]
 [False  True False  True]
 [False  True False  True]
 [False  True False  True]]
[ 2  4  6  8 10 12 14 16]
```

`x[result]`처럼 Boolean indexing을 사용하면 조건이 `True`인 원소만 1차원 배열로 선택된다.

#### 전치와 정렬

```python
x = np.arange(1, 17).reshape(4, 4)

print(x.T)
print(np.transpose(x))
```

두 코드는 2차원 배열에서 같은 전치 결과를 만든다. 행과 열로 보이는 축이 서로 바뀐다.

정렬은 `axis`에 따라 정렬 기준이 달라진다.

```python
d = np.array([[35, 24, 55], [69, 19, 9], [4, 1, 11]])
d.sort(axis=1)
print(d)
```

실행 결과:

```text
[[24 35 55]
 [ 9 19 69]
 [ 1  4 11]]
```

`ndarray.sort()`는 배열 자체를 제자리에서 바꾼다. 원본을 유지해야 한다면 `np.sort()`를 사용해 새 결과를 받는 편이 안전하다.

#### 난수와 데이터 분리

```python
a = np.arange(10)
np.random.shuffle(a)
print(a)
```

`np.random.shuffle()`은 배열의 순서를 제자리에서 섞는다. seed를 고정하지 않으면 실행할 때마다 결과가 달라질 수 있다.

실습에서는 간단한 `train_test_split()` 함수를 만들어 섞은 데이터를 앞쪽 80%와 뒤쪽 20%로 나눴다.

```python
def train_test_split(a):
    divisor = int(len(a) * 0.8)
    train_data = a[:divisor]
    test_data = a[divisor:]
    return train_data, test_data
```

머신러닝에서는 데이터를 먼저 섞은 뒤 학습용과 테스트용으로 나누는 흐름이 중요하다. 다만 실제 프로젝트에서는 재현성을 위해 random seed를 관리하고, 문제 유형에 따라 계층적 분할 같은 방법도 고려해야 한다.

#### 벡터화 연산과 선형대수

같은 원소별 곱셈을 Python 반복문과 NumPy 배열 연산으로 비교했다.

```python
arr_a = np.random.rand(1000)
arr_b = np.random.rand(1000)

result = arr_a * arr_b
```

배열끼리 직접 곱하면 각 위치의 원소가 한 번에 곱해진다. 실습 출력에서는 반복문보다 배열 연산 시간이 더 짧게 나왔지만, 실행 시간은 환경과 데이터 크기에 따라 달라질 수 있으므로 일반적인 성능 결론으로 단정하지 않는다.

연립방정식은 `np.linalg.solve()`로 풀 수 있다.

```python
a = np.array([[1, 1, -1], [2, -1, 3], [1, 2, 1]])
b = np.array([0, 9, 8])
s = np.linalg.solve(a, b)

print(s)
```

실행 결과:

```text
[1. 2. 3.]
```

`a`는 계수 행렬이고 `b`는 우변 벡터다. `np.linalg.solve(a, b)`는 `a @ s == b`를 만족하는 해 `s`를 계산한다.

#### 배열 결합

```python
a = np.arange(10, 18).reshape(2, -1)
b = np.arange(12).reshape(-1, 4)

print(np.concatenate((a, b)))
print(np.vstack((a, b)))
```

두 배열 모두 두 번째 축의 크기가 4이므로 첫 번째 축 방향으로 결합할 수 있다. 이 예제에서는 `np.concatenate((a, b))`와 `np.vstack((a, b))`가 같은 결과를 만든다.

정리:

- `axis`는 결과에서 어떤 축의 크기나 순서가 바뀌는지로 확인한다.
- 슬라이싱은 차원을 유지할 수 있고, Boolean indexing은 조건에 맞는 원소만 뽑아 1차원 결과를 만들 수 있다.
- `ndarray.sort()`와 `np.random.shuffle()`처럼 원본을 직접 바꾸는 함수는 사용 전에 원본 보존 여부를 확인한다.
- 머신러닝 데이터 분리는 섞기, 학습/테스트 분리, 재현성 관리가 함께 고려되어야 한다.
- NumPy 배열 연산은 반복문보다 간결하게 원소별 계산을 표현할 수 있다.

### 공식 참고 문서

- [NumPy absolute basics for beginners](https://numpy.org/doc/stable/user/absolute_beginners.html)
- [Array creation](https://numpy.org/doc/stable/user/basics.creation.html)
- [Broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html)
- [`numpy.arange`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html)
- [`numpy.linspace`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)
- [`numpy.logspace`](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html)
- [`numpy.insert`](https://numpy.org/doc/stable/reference/generated/numpy.insert.html)
- [`numpy.flip`](https://numpy.org/doc/stable/reference/generated/numpy.flip.html)
- [`numpy.transpose`](https://numpy.org/doc/stable/reference/generated/numpy.transpose.html)
- [`numpy.sort`](https://numpy.org/doc/stable/reference/generated/numpy.sort.html)
- [`numpy.linalg.solve`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html)

## Matplotlib

Matplotlib은 데이터를 그래프로 시각화할 때 사용하는 Python 라이브러리다. 이번 실습에서는 `matplotlib.pyplot`을 `plt`라는 이름으로 가져와 선 그래프를 그렸다.

이번 학습은 다음 자료를 기준으로 확인했다.

- 실습 파일: `matplot/ex_01.ipynb`
- 강의 자료: `references/2_맷플롯립_KarL.pdf`
- 실행 환경: Python 3.13.13, NumPy 2.4.5, Matplotlib 3.10.9

### 기본 선 그래프

`plt.plot(x, y)`는 x축 값과 y축 값을 받아 선 그래프를 그린다.

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [1, 2, 3, 4])
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()
```

실행 결과:

```text
Figure size 640x480 with 1 Axes
```

노트북에는 PNG 이미지 출력이 함께 저장되어 있다. x값과 y값이 모두 `[1, 2, 3, 4]`이므로 왼쪽 아래에서 오른쪽 위로 올라가는 직선 그래프가 그려진다.

확인할 내용:

- 첫 번째 리스트는 x축 값이다.
- 두 번째 리스트는 y축 값이다.
- 두 리스트의 길이가 같아야 각 위치의 값이 하나의 점으로 연결된다.
- `xlabel()`과 `ylabel()`은 축 이름을 지정한다.
- `show()`는 지금까지 만든 그래프를 화면에 표시한다.

### NumPy 배열을 이용한 그래프

NumPy로 x값을 만들고, 각 x값을 제곱해 y값을 만든 뒤 그래프로 확인했다.

```python
import numpy as np

x = np.arange(-10, 11)
y = np.square(x)

plt.plot(x, y)
plt.show()
```

실행 결과:

```text
Figure size 640x480 with 1 Axes
```

`np.arange(-10, 11)`은 -10부터 10까지의 정수 배열을 만든다. `stop` 값인 11은 포함되지 않는다.

```python
print(x.shape)
print(y.shape)
print(x.dtype)
print(y.dtype)
```

확인할 내용:

```text
(21,)
(21,)
int64
int64
```

`x`와 `y`는 모두 길이가 21인 1차원 배열이다. `y = np.square(x)`는 각 원소를 제곱하므로 `x`가 음수여도 `y`는 0 이상의 값이 된다. 그래프는 x가 0일 때 가장 낮고 양쪽으로 갈수록 커지는 포물선 모양이다.

노트북에는 같은 계산을 다음처럼 작성할 수 있다는 주석도 있다.

```python
y = x ** 2
```

이번 예제에서는 `np.square(x)`와 `x ** 2`가 같은 제곱 결과를 만든다. 둘 다 배열 전체에 원소별로 적용된다.

주의할 점:

- `plot()`에 전달하는 x와 y의 길이가 다르면 값의 짝을 맞출 수 없어 오류가 발생한다.
- `np.arange(start, stop)`에서 `stop`은 포함되지 않는다.
- 노트북의 저장된 출력은 그래프 이미지이므로 텍스트 숫자 결과가 필요한 경우에는 `print()`로 별도 확인해야 한다.

정리:

- Matplotlib의 기본 사용 흐름은 `import`, `plot()`, 축 설정, `show()` 순서다.
- NumPy 배열로 계산한 결과를 바로 Matplotlib에 전달해 시각화할 수 있다.
- 그래프를 해석할 때는 입력 배열의 범위, 길이, 자료형을 함께 확인한다.
- 시각화는 계산 결과를 이해하는 보조 수단이며, 정확한 값 확인은 배열 출력이나 통계 계산으로 따로 확인한다.

### 공식 참고 문서

- [Pyplot tutorial](https://matplotlib.org/stable/tutorials/pyplot.html)
- [`matplotlib.pyplot.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)
- [`matplotlib.pyplot.xlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html)
- [`matplotlib.pyplot.ylabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html)
- [`matplotlib.pyplot.show`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html)

## 다음 정리 항목

실습 진행에 따라 아래 주제를 순서대로 추가한다.

- 인덱싱과 슬라이싱
- 배열 형태 변경
- 축과 집계 연산
- view와 copy
- 난수 생성
- 선형대수 기초
- pandas와 데이터 전처리
- Matplotlib 그래프 세부 설정
- 머신러닝 기본 과정

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
│  ├─ 2_맷플롯립_KarL.pdf
│  └─ 4_팬다스_KarL.pdf
├─ csv/
│  ├─ README.md
│  ├─ vehicle_prod.csv
│  └─ ...
├─ numpy/
│  └─ ex_01.ipynb
├─ matplot/
│  ├─ ex_01.ipynb
│  └─ Sine-Cosine.png
└─ pandas/
   └─ ex_01.ipynb
```

- `README.md`: ML 과정 전체 학습 정리
- `prompt.md`: 학습 내용을 README에 정리할 때 사용하는 공통 프롬프트
- `pyproject.toml`, `uv.lock`: ML 과정에서 공유하는 Python 환경
- `.venv/`: `uv`가 생성하는 가상환경이며 Git에는 포함하지 않음
- `references/`: 수업에서 제공된 강의 자료와 참고 문서
- `csv/`: pandas와 시각화 실습에서 사용하는 CSV 데이터
- `numpy/`: NumPy 실습 노트북과 예제 코드
- `matplot/`: Matplotlib 실습 노트북과 예제 코드
- `pandas/`: pandas 실습 노트북과 예제 코드

NumPy, pandas, matplotlib, scikit-learn은 서로 연계되므로 우선 `ML`에서 하나의 가상환경을 공유한다. 특정 과정에서 의존성 충돌이 생길 때만 별도 프로젝트로 분리한다.

## 강의 자료

- `references/1_넘파이_KarL.pdf`: NumPy 수업 참고 자료
- `references/2_맷플롯립_KarL.pdf`: Matplotlib 수업 참고 자료
- `references/4_팬다스_KarL.pdf`: pandas 수업 참고 자료

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

### 축 범위와 선 스타일

그래프의 x축, y축 범위는 `plt.axis([xmin, xmax, ymin, ymax])`로 지정할 수 있다.

```python
x = np.arange(-10, 11)
y = np.square(x)

plt.plot(x, y)
plt.axis([-100, 100, 0, 100])
plt.show()
```

`x`는 -10부터 10까지지만, 화면에 표시되는 축 범위는 -100부터 100까지로 넓어진다. 축 범위를 넓히면 실제 데이터가 차지하는 위치를 더 큰 좌표계 안에서 볼 수 있다.

여러 그래프를 한 그림에 겹쳐 그릴 수도 있다.

```python
x = np.arange(-20, 21)
y1 = x * 2
y2 = (1 / 3) * np.square(x) + 5
y3 = -(x ** 2) - 5

plt.plot(x, y1, 'g--')
plt.plot(x, y2, 'b-*')
plt.plot(x, y3, 'r.:')
plt.axis([-30, 30, -30, 30])
plt.show()
```

세 번째 인자는 색, 마커, 선 모양을 짧게 지정하는 형식 문자열이다. 예를 들어 `g--`는 초록색 점선, `b-*`는 파란색 선과 별표 마커, `r.:`는 빨간색 점 마커와 점선을 뜻한다.

주의할 점:

- 스타일 문자열은 그래프를 구분하기 위한 표시 방법이다.
- 선 모양이 달라져도 원본 데이터 값이 바뀌는 것은 아니다.
- 축 범위를 너무 좁게 잡으면 일부 데이터가 화면에서 잘릴 수 있다.

### 범례, 축 이름, 이미지 저장

`label`을 지정하고 `legend()`를 호출하면 그래프에 범례를 표시할 수 있다.

```python
x = np.linspace(0, 2 * np.pi, 1000)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, 'b--', label='Sine wave')
plt.plot(x, y2, 'r--', label='Cosine wave')
plt.legend()
plt.xlabel('time')
plt.ylabel('magnitude')
plt.savefig('Sine-Cosine.png')
plt.show()
```

확인할 내용:

- `np.linspace(0, 2 * np.pi, 1000)`은 0부터 `2π`까지 1000개의 값을 만든다.
- `np.sin(x)`와 `np.cos(x)`는 각 x값에 대해 사인, 코사인 값을 계산한다.
- `legend()`는 `label` 값을 읽어 범례를 만든다.
- `savefig()`는 현재 figure를 이미지 파일로 저장한다.

이번 실습에서는 `matplot/Sine-Cosine.png` 파일이 생성되었다. 노트북에서 `savefig('Sine-Cosine.png')`처럼 상대 경로를 사용하면 실행 위치에 따라 저장 위치가 달라질 수 있으므로, 필요한 경우 저장 경로를 명확히 지정한다.

### 여러 그래프 배치

`plt.subplots()`를 사용하면 하나의 figure 안에 여러 axes를 만들 수 있다.

```python
fig, ax = plt.subplots(2, 2)

X = np.random.randn(100)
Y = np.random.randn(100)
ax[0, 0].scatter(X, Y)

X = np.arange(10)
Y = np.random.uniform(1, 10, 10)
ax[0, 1].bar(X, Y)

X = np.linspace(0, 10, 100)
Y = np.cos(X)
ax[1, 0].plot(X, Y)

Z = np.random.uniform(0, 1, (5, 5))
ax[1, 1].imshow(Z)
```

확인할 내용:

- `fig`는 전체 그림이다.
- `ax`는 각 subplot의 좌표축 배열이다.
- `ax[0, 0]`, `ax[0, 1]`처럼 위치를 지정해 각 칸에 다른 그래프를 그린다.
- `scatter`, `bar`, `plot`, `imshow`는 데이터의 성격에 따라 다른 시각화 방식을 제공한다.

더 복잡한 배치는 `GridSpec`으로 만들 수 있다.

```python
fig = plt.figure(figsize=(7, 5), constrained_layout=True)
grid = plt.GridSpec(3, 3, figure=fig)

ax1 = fig.add_subplot(grid[0, :])
ax2 = fig.add_subplot(grid[1, 0:2])
ax3 = fig.add_subplot(grid[2, 0])
ax4 = fig.add_subplot(grid[2, 1])
ax5 = fig.add_subplot(grid[1:, 2])
```

`grid[0, :]`는 첫 번째 행 전체를 사용하고, `grid[1:, 2]`는 두 번째 행부터 마지막 행까지의 세 번째 열을 사용한다. 단순한 격자는 `subplots()`가 편하고, 서로 다른 크기의 영역이 필요하면 `GridSpec`이 더 적합하다.

### 비율과 분포 시각화

비율 데이터는 pie chart로 볼 수 있다.

```python
data = [5, 4, 6, 11]
clist = ['cyan', 'gray', 'orange', 'red']
explode = [.06, .07, .08, .09]

plt.pie(data, autopct='%.2f%%', colors=clist, labels=clist, explode=explode)
plt.show()
```

`autopct='%.2f%%'`는 각 조각의 비율을 소수 둘째 자리까지 표시한다. `explode`는 각 조각을 중심에서 조금씩 떨어뜨려 강조한다.

분포는 histogram으로 확인할 수 있다.

```python
heights = np.array(np.random.randint(150, 180, 30))
plt.hist(heights, bins=6)
plt.xlabel('height')
plt.ylabel('frequency')
```

`bins`는 값을 몇 개의 구간으로 나눌지 정한다. 같은 데이터라도 `bins` 값이 달라지면 분포가 다르게 보일 수 있다.

누적 histogram은 다음처럼 그릴 수 있다.

```python
plt.hist(heights, bins=6, label='cumulative=True', cumulative=True)
plt.hist(heights, bins=6, label='cumulative=False', cumulative=False)
plt.legend(loc='upper left')
```

정규분포 형태의 난수도 histogram으로 확인했다.

```python
f1 = np.random.normal(loc=0, scale=1, size=100000)
f2 = np.random.normal(loc=3, scale=1, size=100000)

plt.hist(f1, bins=200, color='red', alpha=.4, label='avg = 0, std = 1')
plt.hist(f2, bins=200, color='green', alpha=.4, label='avg = 3, std = 1')
plt.axis([-8, 8, -2, 2500])
plt.legend()
```

`loc`는 평균, `scale`은 표준편차에 해당한다. `alpha`를 낮추면 두 histogram이 겹치는 부분을 더 쉽게 볼 수 있다.

정리:

- `axis()`는 그래프의 표시 범위를 조절한다.
- `label`과 `legend()`는 여러 그래프를 구분할 때 사용한다.
- `subplots()`와 `GridSpec`은 여러 그래프를 한 figure에 배치할 때 사용한다.
- `pie()`는 비율, `hist()`는 값의 분포를 볼 때 사용한다.
- 난수 기반 예제는 실행할 때마다 모양이 달라질 수 있으므로 정확한 수치 결론으로 단정하지 않는다.

### 공식 참고 문서

- [Pyplot tutorial](https://matplotlib.org/stable/tutorials/pyplot.html)
- [`matplotlib.pyplot.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)
- [`matplotlib.pyplot.xlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html)
- [`matplotlib.pyplot.ylabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html)
- [`matplotlib.pyplot.show`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html)

## pandas

pandas는 표 형태의 데이터를 다루기 위한 Python 라이브러리다. NumPy 배열이 같은 `dtype`의 다차원 수치 계산에 강하다면, pandas는 행과 열 이름을 가진 데이터 분석 흐름에 적합하다.

이번 학습은 다음 자료를 기준으로 확인했다.

- 실습 파일: `pandas/ex_01.ipynb`
- 데이터 파일: `csv/vehicle_prod.csv`
- 강의 자료: `references/4_팬다스_KarL.pdf`
- 실행 환경: Python 3.13.13, NumPy 2.4.5, pandas 3.0.3

### `Series`와 결측치

`Series`는 1차원 데이터에 index를 붙인 자료구조다.

```python
import pandas as pd
import numpy as np

se = pd.Series([1, 2, np.nan, 4])
se
```

실행 결과:

```text
0    1.0
1    2.0
2    NaN
3    4.0
dtype: float64
```

`np.nan`은 결측치를 나타낸다. 정수처럼 보이는 값과 `NaN`이 함께 들어가면서 `dtype`은 `float64`가 되었다.

결측치 여부는 `isna()`로 확인할 수 있다.

```python
se.isna()
```

실행 결과:

```text
0    False
1    False
2     True
3    False
dtype: bool
```

`None`을 넣어도 숫자형 `Series`에서는 결측치로 처리될 수 있다.

```python
list1 = [1, 2, None, 4]
se = pd.Series(list1, index=['A', 'B', 'C', 'D'])
print(se)
```

실행 결과:

```text
A    1.0
B    2.0
C    NaN
D    4.0
dtype: float64
```

index를 지정하면 기본 정수 index 대신 이름으로 값을 조회할 수 있다.

```python
se['A']
```

실행 결과:

```text
1.0
```

정리:

- `Series`는 값과 index를 함께 가진다.
- `NaN`은 결측치이며, `isna()`로 위치를 확인할 수 있다.
- 결측치가 섞인 숫자 데이터는 실수형으로 변환될 수 있다.

### `DataFrame` 생성과 열 선택

`DataFrame`은 행과 열을 가진 2차원 표 형태의 자료구조다.

```python
month_se = pd.Series(['1월', '2월', '3월', '4월'])
income_se = pd.Series([9500, 6200, 6050, 7000])
expenses_se = pd.Series([5040, 2350, 2300, 4800])

df = pd.DataFrame({
    '월': month_se,
    '수익': income_se,
    '지출': expenses_se,
})
df
```

실행 결과:

```text
    월    수익    지출
0  1월  9500  5040
1  2월  6200  2350
2  3월  6050  2300
3  4월  7000  4800
```

열 이름은 `columns`로 확인할 수 있다.

```python
(df.columns)[0]
```

실행 결과:

```text
'월'
```

특정 열은 딕셔너리처럼 선택할 수 있다.

```python
df['수익'][0]
```

실행 결과:

```text
9500
```

실습에서는 `np.argmax()`로 `수익`이 가장 큰 위치를 찾고 해당 값을 조회했다.

```python
np.argmax(df['수익'])
df['수익'][np.argmax(df['수익'])]
```

실행 결과:

```text
0
9500
```

주의할 점:

- `np.argmax(df['수익'])`는 가장 큰 값 자체가 아니라 가장 큰 값의 위치를 반환한다.
- 이 예제에서는 index가 0부터 순서대로 붙어 있어 위치와 label이 같지만, index가 달라지면 더 명확한 선택 방법이 필요하다.
- pandas에서는 위치 기반 선택은 `iloc`, label 기반 선택은 `loc`를 구분해서 사용하는 편이 안전하다.

### 기본 통계

`Series`는 기본 통계 메서드를 제공한다.

```python
income_se.max()
income_se.min()
income_se.mean()
```

실행 결과:

```text
9500
6050
7187.5
```

`max()`는 최댓값, `min()`은 최솟값, `mean()`은 평균을 구한다. 평균은 전체 수익 합을 데이터 개수로 나눈 값이다.

정리:

- pandas는 열 단위로 데이터를 선택하고 계산할 수 있다.
- 통계 메서드는 `Series`나 `DataFrame`에 바로 적용할 수 있다.
- 통계값만 보고 결론을 내리기보다 데이터 개수, 결측치, 단위, 기간을 함께 확인해야 한다.

### CSV 파일 읽기

CSV 파일은 `pd.read_csv()`로 읽을 수 있다.

```python
file = '../csv/vehicle_prod.csv'
df = pd.read_csv(file)
df
```

실행 결과:

```text
  Unnamed: 0   2007   2008   2009   2010   2011
0      China   7.71   7.95  11.96  15.84  16.33
1         EU  19.02  17.71  15.00  16.70  17.48
2         US  10.47   8.45   5.58   7.60   8.40
3      Japan  10.87  10.83   7.55   9.09   7.88
4      Korea   4.04   3.78   3.45   4.20   4.62
5     Mexico   2.01   2.05   1.50   2.25   2.54
```

`vehicle_prod.csv`의 첫 번째 열에는 별도 열 이름이 없어서 pandas가 `Unnamed: 0`이라는 열 이름을 붙였다. 이 열은 국가나 지역 이름을 담고 있다.

확인한 구조:

```text
shape: (6, 6)
columns: ['Unnamed: 0', '2007', '2008', '2009', '2010', '2011']
```

주의할 점:

- CSV의 첫 행이 열 이름으로 해석된다.
- 열 이름이 비어 있으면 `Unnamed: 0` 같은 이름이 자동으로 붙을 수 있다.
- 상대 경로는 노트북 실행 위치에 따라 달라질 수 있다.
- 파일 인코딩이 다르면 한글 데이터가 깨질 수 있으므로 필요하면 `encoding`을 지정한다.

정리:

- pandas 학습의 기본 흐름은 `Series`, `DataFrame`, 열 선택, 통계, 파일 읽기 순서로 시작한다.
- CSV를 읽은 뒤에는 `shape`, `columns`, 앞부분 데이터, 결측치 여부를 먼저 확인한다.
- 데이터 분석에서는 표가 읽혔다는 사실보다 각 열이 무엇을 의미하는지 파악하는 것이 중요하다.

### 공식 참고 문서

- [pandas Intro to data structures](https://pandas.pydata.org/docs/user_guide/dsintro.html)
- [`pandas.Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html)
- [`pandas.DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- [`pandas.isna`](https://pandas.pydata.org/docs/reference/api/pandas.isna.html)
- [`pandas.read_csv`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

## 다음 정리 항목

실습 진행에 따라 아래 주제를 순서대로 추가한다.

- 인덱싱과 슬라이싱
- 배열 형태 변경
- 축과 집계 연산
- view와 copy
- 난수 생성
- 선형대수 기초
- pandas 인덱싱과 CSV 전처리
- Matplotlib 그래프 세부 설정 심화
- 머신러닝 기본 과정

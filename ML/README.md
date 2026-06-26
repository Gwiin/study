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
│  ├─ 4_팬다스_KarL.pdf
│  └─ 고려대학교_Machin_Learning_강의자료.pdf
├─ numpy/
│  └─ ex_01.ipynb
├─ matplot/
│  ├─ ex_01.ipynb
│  └─ Sine-Cosine.png
├─ pandas/
│  └─ ex_01.ipynb
└─ ml/
   ├─ ex_01.ipynb
   ├─ ex_02.ipynb
   ├─ ex_03.ipynb
   ├─ ex_04.ipynb
   ├─ ex_05.ipynb
   ├─ ex_06.ipynb
   ├─ ex_07.ipynb
   ├─ ex_08.ipynb
   ├─ project01.ipynb
   ├─ titanic.csv
   ├─ MNIST_20260626_15_30.keras
   ├─ digit3.png
   ├─ digit4.png
   ├─ digit4_2.png
   ├─ digit5.png
   └─ digit9.png
```

- `README.md`: ML 과정 전체 학습 정리
- `prompt.md`: 학습 내용을 README에 정리할 때 사용하는 공통 프롬프트
- `pyproject.toml`, `uv.lock`: ML 과정에서 공유하는 Python 환경
- `.venv/`: `uv`가 생성하는 가상환경이며 Git에는 포함하지 않음
- `references/`: 수업에서 제공된 강의 자료와 참고 문서
- `numpy/`: NumPy 실습 노트북과 예제 코드
- `matplot/`: Matplotlib 실습 노트북과 예제 코드
- `pandas/`: pandas 실습 노트북과 예제 코드
- `ml/`: 머신러닝 기본 실습 노트북, 예제 데이터, 저장된 모델, 직접 그린 숫자 이미지

NumPy, pandas, matplotlib, scikit-learn은 서로 연계되므로 우선 `ML`에서 하나의 가상환경을 공유한다. 특정 과정에서 의존성 충돌이 생길 때만 별도 프로젝트로 분리한다.

## 강의 자료

- `references/1_넘파이_KarL.pdf`: NumPy 수업 참고 자료
- `references/2_맷플롯립_KarL.pdf`: Matplotlib 수업 참고 자료
- `references/4_팬다스_KarL.pdf`: pandas 수업 참고 자료
- `references/고려대학교_Machin_Learning_강의자료.pdf`: 머신러닝 수업 참고 자료

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
uv add --project ML seaborn
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

### 행과 열 기준 집계

`axis=1`을 사용하면 각 행에서 여러 열을 가로로 계산할 수 있다.

```python
df = pd.DataFrame(
    {
        'A': [10, 20, 30],
        'B': [1, 2, 3],
    },
    index=['x', 'y', 'z'],
)

df['total'] = df.sum(axis=1)
df['mean'] = df[['A', 'B']].mean(axis=1)
print(df)
```

실행 결과:

```text
    A  B  total  mean
x  10  1     11   5.5
y  20  2     22  11.0
z  30  3     33  16.5
```

`sum(axis=1)`은 각 행의 값을 더한다. `mean(axis=1)`은 각 행의 평균을 구한다. 특정 열만 계산에 포함하려면 열 목록을 명시하는 편이 안전하다.

열이나 행은 `drop()`으로 제거할 수 있다.

```python
df_without_a = df.drop('A', axis=1)
df_without_x = df.drop('x', axis=0)
```

`axis=1`은 열 삭제, `axis=0`은 행 삭제다. `inplace=True`를 사용하면 원본 `DataFrame`이 직접 바뀐다. 원본을 보존해야 하는 경우에는 새 변수로 결과를 받는다.

`loc`를 사용하면 label 기준으로 새 행을 추가할 수도 있다.

```python
df.loc['total'] = df.select_dtypes(include='number').sum()
```

정리:

- `axis=0`은 행 index 방향으로 내려가며 열별 계산을 만든다.
- `axis=1`은 열 방향으로 가로 계산을 하며 행별 결과를 만든다.
- 원본이 바뀌는 연산인지, 새 `DataFrame`을 반환하는 연산인지 확인한다.

### pandas 시각화

pandas `DataFrame`과 `Series`는 Matplotlib 기반의 간단한 그래프를 바로 그릴 수 있다.

```python
df['A'].plot(kind='bar')
```

`Series.plot(kind='bar')`는 index를 x축으로, 값을 y축으로 사용한다.

```python
df[['A', 'B']].plot.area()
```

`DataFrame.plot.area()`는 여러 열의 값을 누적 영역 그래프로 보여준다. 값이 누적되어 보이므로 개별 값 비교에는 막대그래프나 선 그래프가 더 적합할 수 있다.

### 행 선택: slicing, `loc`, `iloc`

앞부분 일부는 `head()`로 확인한다.

```python
df.head()
```

행 범위는 slicing으로 선택할 수 있다.

```python
df[2:4]
```

`loc`는 label 기반 선택이다.

```python
df.loc['x']
df.loc[['x', 'z']]
```

`iloc`는 위치 기반 선택이다.

```python
df.iloc[0]
```

이 예제에서는 `x`가 첫 번째 행이므로 `df.loc['x']`와 `df.iloc[0]`가 같은 값을 보여준다. 하지만 index 순서가 바뀌거나 label이 숫자일 때는 두 방식의 의미가 달라질 수 있다.

정리:

- `loc`는 index label을 기준으로 선택한다.
- `iloc`는 정수 위치를 기준으로 선택한다.
- `df[2:4]` 같은 slicing은 행 위치 범위를 가져오지만, 명확한 코드를 위해 `loc`와 `iloc`를 구분해 쓰는 편이 좋다.

### 결측치 처리

결측치가 있는 행은 `isna()`와 `any(axis=1)`로 찾을 수 있다.

```python
df_missing = pd.DataFrame({
    'A': [1, 2, np.nan],
    'B': [10, np.nan, 30],
})

print(df_missing[df_missing.isna().any(axis=1)])
```

결측치가 하나라도 있는 행을 제거하려면 `dropna()`를 사용한다.

```python
clean_df = df_missing.dropna(how='any', axis=0, inplace=False)
```

주의할 점:

- `dropna(how='any')`는 결측치가 하나라도 있는 행을 제거한다.
- 결측치 제거는 간단하지만 데이터가 줄어든다.
- 머신러닝에서는 결측치를 제거할지, 대체할지, 별도 표시할지 문제와 데이터 양에 따라 결정해야 한다.

### 날짜 변환과 월별 집계

여러 형식의 날짜 문자열은 `DatetimeIndex`로 변환할 수 있다.

```python
d_list = ['2018-01-11', '2018/01/11', '01/11/2018', '01-11-2018']
new_d_index = pd.DatetimeIndex(d_list)

print(new_d_index.year)
print(new_d_index.month)
print(new_d_index.day)
```

날짜와 시간이 함께 있으면 시, 분도 꺼낼 수 있다.

```python
dt_list = ['01,03,2018 11:12:13', '01-03-2018 11:22:13']
pd.DatetimeIndex(dt_list).hour
pd.DatetimeIndex(dt_list).minute
```

날짜 열에서 월 정보를 뽑아 월별 평균을 계산할 수 있다.

```python
df_time = pd.DataFrame({
    'date': ['2018-01-03', '2018-01-06', '2018-02-01'],
    'value': [10, 20, 30],
})

df_time['month'] = pd.DatetimeIndex(df_time['date']).month
group1 = df_time.groupby('month')['value'].mean()
print(group1)
```

같은 결과를 반복문으로 월별 subset을 만든 뒤 평균을 구할 수도 있지만, pandas에서는 `groupby()`가 더 직접적이다.

```python
monthly_mean = df_time.groupby('month')['value'].mean()
monthly_mean.plot(kind='bar')
```

정리:

- 날짜 문자열은 `DatetimeIndex`로 변환하면 `year`, `month`, `day`, `hour`, `minute` 같은 속성을 꺼낼 수 있다.
- `groupby('month')`는 월별로 데이터를 묶은 뒤 평균 같은 집계를 적용할 수 있다.
- 반복문으로 직접 나누는 방식보다 `groupby()`가 의도가 더 분명하다.
- 날짜 형식이 섞여 있으면 pandas가 해석할 수 있는지 확인하고, 애매한 형식은 `format`이나 전처리를 명시하는 것이 안전하다.

### 공식 참고 문서

- [pandas Intro to data structures](https://pandas.pydata.org/docs/user_guide/dsintro.html)
- [`pandas.Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html)
- [`pandas.DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- [`pandas.isna`](https://pandas.pydata.org/docs/reference/api/pandas.isna.html)
- [Indexing and selecting data](https://pandas.pydata.org/docs/user_guide/indexing.html)
- [`pandas.DataFrame.drop`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html)
- [`pandas.DataFrame.dropna`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html)
- [`pandas.DataFrame.groupby`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html)
- [`pandas.DatetimeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html)

## 머신러닝 기본 실습

이번 실습은 Titanic 데이터를 사용해 결측치 처리, 조건별 집계, 시각화, 상관계수 계산을 확인했다. 아직 모델 학습 단계는 아니며, 머신러닝 전에 데이터를 이해하고 정리하는 탐색 단계다.

이번 학습은 다음 자료를 기준으로 확인했다.

- 실습 파일: `ml/ex_01.ipynb`
- 데이터 파일: `ml/titanic.csv`
- 강의 자료: `references/고려대학교_Machin_Learning_강의자료.pdf`
- 실행 환경: Python 3.13.13, pandas 3.0.3, NumPy 2.4.5, Matplotlib 3.10.9, seaborn 0.13.2

### Titanic 데이터 불러오기와 저장

Seaborn은 예제 데이터셋을 제공한다. Titanic 데이터는 다음처럼 불러왔다.

```python
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

titanic = sns.load_dataset("titanic")
titanic.to_csv(path_or_buf="titanic.csv", index=False)
```

확인한 구조:

```text
shape: (891, 15)
columns: survived, pclass, sex, age, sibsp, parch, fare, embarked, class, who, adult_male, deck, embark_town, alive, alone
```

`survived`는 생존 여부를 0과 1로 나타낸 target에 해당한다. `pclass`, `sex`, `age`, `fare` 같은 열은 생존 여부를 설명하는 feature 후보로 볼 수 있다.

### 결측치 확인과 대체

먼저 열별 결측치 개수를 확인했다.

```python
print(titanic.isnull().sum())
```

실행 결과 중 결측치가 있는 열:

```text
age            177
embarked         2
deck           688
embark_town      2
```

실습에서는 `age`의 결측치를 중앙값으로 채웠다.

```python
titanic['age'] = titanic['age'].fillna(value=titanic['age'].median())
print(titanic['age'].isnull().sum())
```

실행 결과:

```text
0
```

`embarked`는 가장 많이 나온 값인 `S`로 채웠다.

```python
titanic['embarked'].value_counts()
titanic['embarked'] = titanic['embarked'].fillna(value='S')
```

`deck`은 결측치가 688개로 매우 많았다. 실습에서는 최빈값인 `C`로 채웠지만, 결측치 비율이 큰 열은 단순 대체가 분석 결과를 크게 왜곡할 수 있다.

```python
titanic['deck'].value_counts()
titanic['deck'] = titanic['deck'].fillna(value='C')
```

`embark_town`도 결측치를 채웠다.

```python
titanic['embark_town'].value_counts()
titanic['embark_town'] = titanic['embark_town'].fillna(value='Cherbourg')
```

주의할 점:

- 결측치를 평균, 중앙값, 최빈값으로 채우는 것은 편리하지만 항상 정답은 아니다.
- `deck`처럼 결측치가 대부분인 열은 대체보다 제거하거나 별도 범주로 다루는 방법도 고려해야 한다.
- 머신러닝에서는 전처리 기준을 학습 데이터에서만 정하고 테스트 데이터에 적용해야 데이터 누수를 막을 수 있다.

### 성별에 따른 생존 여부 확인

조건식으로 남성과 여성 데이터를 나누고 생존 여부를 집계했다.

```python
titanic['survived'][titanic['sex'] == 'male'].value_counts()
```

실행 결과:

```text
survived
0    468
1    109
Name: count, dtype: int64
```

여성 데이터는 다음처럼 확인했다.

```python
titanic[titanic['sex'] == 'female']['survived'].value_counts(ascending=True)
```

실행 결과:

```text
survived
0     81
1    233
Name: count, dtype: int64
```

이 데이터에서는 남성보다 여성의 생존 비율이 높게 나타난다. 다만 이는 Titanic 데이터 안에서의 관찰 결과이며, 일반적인 결론으로 확장해서는 안 된다.

### 생존 비율과 객실 등급 시각화

성별 생존 비율은 pie chart로 비교했다.

```python
(_, ax) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

titanic['survived'][titanic['sex'] == 'male'].value_counts().plot.pie(
    explode=[0, 0.1],
    autopct='%1.1f%%',
    ax=ax[0],
    shadow=True,
)

titanic['survived'][titanic['sex'] == 'female'].value_counts(ascending=True).plot.pie(
    explode=[0, 0.1],
    autopct='%1.1f%%',
    ax=ax[1],
    shadow=True,
)

ax[0].set_title('Survived(Male)')
ax[1].set_title('Survived(Female)')
plt.show()
```

객실 등급과 생존 여부는 count plot으로 확인했다.

```python
sns.countplot(x='pclass', hue='survived', data=titanic)
plt.show()
```

`pclass`는 객실 등급이고 `hue='survived'`는 생존 여부별로 막대를 나누어 보여준다. 이런 시각화는 모델을 만들기 전에 feature와 target의 관계를 눈으로 확인하는 데 도움이 된다.

### 상관계수 계산과 문자열 컬럼 오류

상관계수는 두 수치형 변수의 선형 관계를 확인하는 방법이다. 실습에서는 전체 `DataFrame`에 바로 `corr()`를 적용하면서 오류가 발생했다.

```python
titanic_correlation_analysis = titanic.corr(method='pearson')
```

오류 핵심:

```text
ValueError: could not convert string to float: 'male'
```

원인은 `sex`, `embarked`, `class`, `who`, `alive`처럼 문자열이나 범주형 값이 들어 있는 열까지 상관계수 계산에 포함되었기 때문이다. pandas 3.0.3에서 `DataFrame.corr()`의 기본값은 `numeric_only=False`이므로 문자열 열을 숫자로 변환하려다 실패한다.

숫자형 열만 대상으로 계산하면 된다.

```python
titanic_correlation_analysis = titanic.corr(
    method='pearson',
    numeric_only=True,
)
```

또는 명시적으로 숫자 열만 고를 수 있다.

```python
numeric_titanic = titanic.select_dtypes(include='number')
titanic_correlation_analysis = numeric_titanic.corr(method='pearson')
```

개별 열끼리의 상관계수도 확인했다.

```python
titanic['survived'].corr(other=titanic['adult_male'], method='pearson')
```

실행 결과:

```text
-0.5570800422053258
```

`survived`와 `adult_male`은 음의 상관관계를 보였다. 이 값은 `adult_male`이 `True`인 경우 생존 값이 낮아지는 경향이 있다는 뜻이다.

```python
titanic['survived'].corr(other=titanic['fare'], method='pearson')
```

실행 결과:

```text
0.2573065223849622
```

`fare`와 `survived`는 약한 양의 상관관계를 보였다. 요금이 높을수록 생존 값이 커지는 경향이 있지만, 상관계수만으로 원인이라고 단정할 수는 없다.

정리:

- `corr()`는 숫자형 데이터에 대해 계산해야 한다.
- 문자열 범주형 feature는 그대로 상관계수 계산에 넣을 수 없다.
- `numeric_only=True` 또는 `select_dtypes(include='number')`로 숫자 열만 고른다.
- 상관관계는 선형 관계의 정도이지 인과관계를 증명하지 않는다.

### Pair plot

`pairplot()`은 여러 수치형 변수 간 관계를 한 번에 확인하는 시각화다.

```python
sns.pairplot(data=titanic, hue='survived')
plt.show()
```

`hue='survived'`를 지정하면 생존 여부에 따라 색을 나누어 표시한다. 변수 간 분포와 대략적인 구분 가능성을 빠르게 볼 수 있지만, feature가 많으면 그래프가 커지고 해석이 복잡해진다.

정리:

- Titanic 실습은 분류 문제의 탐색 단계로 볼 수 있다.
- target은 `survived`이고, 나머지 열은 feature 후보가 된다.
- 결측치 처리, 범주형 데이터 처리, 시각화, 상관관계 확인은 모델 학습 전 중요한 준비 과정이다.
- 실제 모델 학습 전에는 train/test 분리와 전처리 기준의 데이터 누수 여부를 반드시 확인해야 한다.

### 공식 참고 문서

- [seaborn.load_dataset](https://seaborn.pydata.org/generated/seaborn.load_dataset.html)
- [seaborn.countplot](https://seaborn.pydata.org/generated/seaborn.countplot.html)
- [seaborn.pairplot](https://seaborn.pydata.org/generated/seaborn.pairplot.html)
- [`pandas.DataFrame.corr`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html)
- [`pandas.Series.corr`](https://pandas.pydata.org/docs/reference/api/pandas.Series.corr.html)

## 선형회귀와 모델 학습

이번 실습은 scikit-learn의 `LinearRegression`으로 입력값과 target 사이의 직선 관계를 학습하는 흐름을 확인했다. 앞의 Titanic 실습이 모델 학습 전 탐색 단계였다면, 이번 내용은 실제 모델을 만들고 예측값을 확인하는 첫 단계다.

이번 학습은 다음 자료를 기준으로 확인했다.

- 실습 파일: `ml/ex_02.ipynb`, `ml/ex_03.ipynb`
- 데이터 파일: scikit-learn `load_diabetes()` 예제 데이터
- 실행 환경: Python 3.13.13, scikit-learn 1.8.0, NumPy 2.4.5, Matplotlib 3.10.9

### 가장 단순한 선형회귀

`LinearRegression`은 feature와 target의 관계를 직선 형태로 학습한다. 입력 `X`는 2차원 형태로 전달하고, `y`는 예측하려는 값이다.

```python
from sklearn import linear_model

reg = linear_model.LinearRegression()

X = [[0], [1], [2]]
y = [[3], [4], [5]]

reg.fit(X, y)
print(reg.coef_)
print(reg.intercept_)
print(reg.predict([[-4]]))
print(reg.predict([[5]]))
```

실행 결과:

```text
coef: [[1.]]
intercept: [3.]
predict([[-4]]): [[-1.]]
predict([[5]]): [[8.]]
```

이 예제에서 모델은 `y = 1 * x + 3` 형태의 관계를 학습했다. 그래서 `x=-4`이면 `-1`, `x=5`이면 `8`을 예측한다.

정리:

- `fit(X, y)`는 feature와 target의 관계를 학습한다.
- `coef_`는 기울기, `intercept_`는 절편이다.
- `predict()`에는 학습 때와 같은 2차원 입력 형태를 맞춰야 한다.
- 학습 데이터가 3개뿐이므로 이 결과를 일반화된 성능으로 해석하면 안 된다.

### 키와 몸무게 예측 예제

키를 feature, 몸무게를 target으로 두고 단순 선형회귀를 적용했다.

```python
X = [[174], [152], [138], [128], [186]]
y = [71, 55, 46, 38, 88]

reg.fit(X, y)
print(reg.predict([[165]]))
print(reg.coef_)
print(reg.intercept_)
```

실행 결과:

```text
predict([[165]]): [67.30998637]
coef: [0.82021132]
intercept: -68.0248807089298
```

학습된 직선은 대략 `몸무게 = 0.8202 * 키 - 68.0249`로 볼 수 있다. 이 모델은 키가 165일 때 몸무게를 약 `67.31`로 예측했다.

주의할 점:

- 표본이 5개뿐이라 예측값은 학습 흐름을 확인하는 용도로만 봐야 한다.
- 키 하나만으로 몸무게를 설명한다고 단정할 수 없다.
- `ex_02.ipynb`의 `y1 = 0.82 * x - 68.02` 셀은 현재 노트북을 처음부터 다시 실행하면 `x`가 정의되어 있지 않아 오류가 날 수 있다. 앞에서 만든 `x1`을 사용하려면 `y1 = 0.82 * x1 - 68.02`처럼 맞춰야 한다.

### Diabetes 데이터와 train/test 분리

`load_diabetes()` 데이터는 442명의 환자에 대해 10개 feature와 1년 뒤 질병 진행 정도를 나타내는 target을 제공한다. target이 연속적인 수치이므로 회귀 문제다.

```python
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

diabete = datasets.load_diabetes()

X = diabete['data']
y = diabete['target']

print(X.shape)
print(y.shape)
```

실행 결과:

```text
X: (442, 10)
y: (442,)
```

전체 feature 중 세 번째 열인 `bmi`만 꺼내 단순 회귀 입력으로 사용했다.

```python
bmi = X[:, 2]
X_new = X[:, np.newaxis, 2]

print(bmi.shape)
print(X_new.shape)
```

확인 결과:

```text
bmi: (442,)
X_new: (442, 1)
```

`bmi`는 1차원 배열이고, `X_new`는 scikit-learn 모델 입력에 맞춘 2차원 배열이다. `np.newaxis`를 사용해 sample 수는 유지하고 feature 축을 하나 추가했다.

학습 데이터와 테스트 데이터를 나눴다.

```python
X_train, X_test, y_train, y_test = train_test_split(
    X_new,
    y,
    test_size=0.1,
    random_state=0,
)

print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)
```

실행 결과:

```text
X_train: (397, 1)
y_train: (397,)
X_test: (45, 1)
y_test: (45,)
```

`test_size=0.1`은 전체 데이터의 10%를 테스트 데이터로 분리한다. `random_state=0`은 같은 분할을 재현하기 위한 값이며, 성능을 보장하는 값은 아니다.

### 학습과 예측값 비교

분리한 학습 데이터로 모델을 학습하고 테스트 데이터에 대해 예측했다.

```python
regression = LinearRegression()
regression.fit(X_train, y_train)

y_pred = regression.predict(X_test)

print(regression.coef_)
print(regression.intercept_)
print(y_pred[:5])
print(y_test[:5])
```

실행 결과:

```text
coef: [966.7269242]
intercept: 151.20933147606175
pred_first5: [252.53071348 209.81076549 159.79716784 128.53866931 195.22346617]
y_first5: [321. 215. 127.  64. 175.]
```

예측값과 실제값을 나란히 보면 완전히 같지 않다. 이 실습에서는 train/test 분리와 예측 흐름을 확인했지만, 아직 MAE, MSE, RMSE, R² 같은 평가 지표를 계산하지 않았다. 따라서 모델 성능이 좋다고 말할 수는 없다.

정리:

- `load_diabetes()` 실습은 회귀 문제다.
- feature는 `X`, target은 `y`로 분리한다.
- scikit-learn의 입력 `X`는 보통 `(sample 수, feature 수)` 형태의 2차원 배열이어야 한다.
- `train_test_split()`으로 학습 데이터와 테스트 데이터를 나누고, 모델은 학습 데이터에만 `fit()`한다.
- 테스트 데이터는 학습에 사용하지 않고, 학습 후 예측과 평가에 사용한다.
- 평가 지표를 계산하기 전에는 예측값 몇 개만 보고 성능을 단정하면 안 된다.

### 공식 참고 문서

- [`sklearn.linear_model.LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
- [`sklearn.datasets.load_diabetes`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html)
- [`sklearn.model_selection.train_test_split`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)

## KNN 분류와 모델 평가

이번 실습은 회귀가 아니라 분류 문제를 다뤘다. `KNeighborsClassifier`를 사용해 Iris 품종, 손글씨 숫자, 강아지 품종을 예측했고, 예측 결과를 `accuracy_score`, `confusion_matrix`, `classification_report`로 확인했다.

이번 학습은 다음 자료를 기준으로 확인했다.

- 실습 파일: `ml/ex_04.ipynb`, `ml/ex_05.ipynb`, `ml/project01.ipynb`
- 데이터 파일: scikit-learn `load_iris()`, `load_digits()` 예제 데이터, 직접 만든 닥스훈트/사모예드 길이와 키 데이터
- 실행 환경: Python 3.13.13, scikit-learn 1.8.0, NumPy 2.4.5, Matplotlib 3.10.9

### Iris 데이터와 KNN 분류

`load_iris()` 데이터는 붓꽃 150개 sample에 대해 꽃받침과 꽃잎의 길이, 너비 4개 feature를 제공한다. target은 `setosa`, `versicolor`, `virginica` 세 품종이다.

```python
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

iris = datasets.load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=4,
)

print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)
```

실행 결과:

```text
X_train: (120, 4)
y_train: (120,)
X_test: (30, 4)
y_test: (30,)
```

전체 150개 중 80%인 120개는 학습에 사용하고, 20%인 30개는 테스트에 사용했다. feature가 4개이므로 `X_train`의 shape는 `(120, 4)`가 된다.

```python
knn = KNeighborsClassifier(n_neighbors=6)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)
score = metrics.accuracy_score(y_test, y_pred)
print(score)
```

실행 결과:

```text
0.9666666666666667
```

이 정확도는 테스트 데이터 30개 중 약 96.7%를 맞췄다는 뜻이다. 테스트 데이터가 30개뿐이므로 1개를 틀리면 정확도는 약 `0.0333`씩 변한다.

새로운 입력 2개도 예측했다.

```python
classes = {
    0: 'setosa',
    1: 'versicolor',
    2: 'virginica',
}

x_new = [[3, 4, 5, 2], [5, 4, 2, 2]]
y_predict = knn.predict(x_new)

print(classes[y_predict[0]])
print(classes[y_predict[1]])
```

실행 결과:

```text
versicolor
setosa
```

분류 결과를 더 자세히 보기 위해 confusion matrix도 확인했다.

```python
from sklearn.metrics import confusion_matrix

confusion = confusion_matrix(y_test, y_pred)
print(confusion)
```

실행 결과:

```text
[[16  0  0]
 [ 0  4  1]
 [ 0  0  9]]
```

첫 번째 품종은 16개를 모두 맞췄고, 두 번째 품종은 5개 중 1개를 세 번째 품종으로 잘못 예측했다. 세 번째 품종은 9개를 모두 맞췄다.

정리:

- Iris 데이터는 3개 품종을 맞히는 다중 분류 문제다.
- `KNeighborsClassifier(n_neighbors=6)`은 가까운 이웃 6개를 기준으로 class를 결정한다.
- `accuracy_score`는 전체 테스트 데이터 중 맞춘 비율을 보여준다.
- `confusion_matrix`는 어떤 class를 어떤 class로 잘못 예측했는지 확인하는 데 유용하다.

### Digits 손글씨 숫자 분류

`load_digits()` 데이터는 8x8 손글씨 숫자 이미지와 정답 숫자를 제공한다. 각 이미지는 8x8 픽셀이고, 모델 입력에는 64개 feature로 펼쳐진 `digits.data`를 사용한다.

```python
from sklearn import datasets, metrics
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

digits = datasets.load_digits()

data = digits.data
target = digits.target

print(data.shape)
print(target.shape)
```

실행 결과:

```text
data: (1797, 64)
target: (1797,)
```

`digits.images`는 이미지 형태인 `(8, 8)` 배열이고, `digits.data`는 모델에 넣기 쉽게 64개 값으로 펼친 데이터다.

```python
plt.imshow(digits['images'][0], cmap=plt.cm.gray_r)
```

첫 번째 이미지를 보면 숫자 하나가 8x8 밝기 값으로 표현되어 있다. 밝기 값 배열은 이미지로 볼 수도 있고, 64개 feature로 펼쳐 KNN에 넣을 수도 있다.

```python
X_train, X_test, y_train, y_test = train_test_split(
    data,
    target,
    train_size=0.8,
)

knn = KNeighborsClassifier()
knn.fit(X_train, y_train)

y_predict = knn.predict(X_test)

print(y_predict[:10])
print(y_test[:10])
```

저장된 실행 결과:

```text
y_predict[:10]: [3 9 0 4 2 3 1 9 4 7]
y_test[:10]:    [3 9 0 4 2 3 1 9 4 7]
```

앞의 10개 예측은 실제값과 같았다. 전체 테스트 정확도도 계산했다.

```python
score = accuracy_score(y_test, y_predict)
print(score)
```

저장된 실행 결과:

```text
0.9833333333333333
```

`train_test_split()`에 `random_state`를 지정하지 않았으므로 실행할 때마다 학습/테스트 데이터가 달라지고 정확도도 달라질 수 있다. 이 실습에서는 그 변동을 직접 확인할 수 있다.

특정 테스트 이미지를 다시 8x8로 바꿔 확인했다.

```python
plt.imshow(X_test[10].reshape(8, -1), cmap=plt.cm.gray_r)
plt.show()

print(y_test[10])
```

실행 결과:

```text
7
```

`X_test[10]`은 64개 feature로 펼쳐진 상태이므로, 이미지를 보려면 `reshape(8, -1)`로 다시 8x8 형태를 만들어야 한다.

분류 결과는 confusion matrix와 classification report로도 확인했다.

```python
from sklearn.metrics import ConfusionMatrixDisplay

ConfusionMatrixDisplay.from_estimator(knn, X_test, y_test)
plt.show()

print(metrics.classification_report(y_test, knn.predict(X_test)))
```

정리:

- Digits 데이터는 0부터 9까지 숫자를 맞히는 다중 분류 문제다.
- 이미지 데이터도 모델 입력에는 숫자 feature 배열로 들어간다.
- `digits.images`는 시각화에 좋고, `digits.data`는 모델 학습에 바로 쓰기 좋다.
- `classification_report`는 class별 precision, recall, f1-score를 함께 보여준다.

### 닥스훈트와 사모예드 분류 프로젝트

`project01.ipynb`는 직접 만든 닥스훈트와 사모예드 데이터를 사용한 KNN 분류 실습이다. 길이와 키를 feature로 사용하고, 닥스훈트는 `0`, 사모예드는 `1`로 라벨을 만들었다.

```python
dach_length = [77, 78, 85, 83, 73, 77, 73, 80]
dach_height = [25, 28, 29, 30, 21, 22, 17, 35]

samo_length = [75, 77, 86, 86, 79, 83, 83, 88]
samo_height = [56, 57, 50, 53, 60, 53, 49, 61]
```

각 품종은 길이 8개, 키 8개를 가진다. 두 feature를 하나의 2차원 배열로 묶었다.

```python
dach_data = np.column_stack((dach_length, dach_height))
samo_data = np.column_stack((samo_length, samo_height))

dach_target = [0] * 8
samo_target = [1] * 8

dogs = np.concatenate((dach_data, samo_data))
labels = np.concatenate((dach_target, samo_target))

print(dogs.shape)
print(labels.shape)
```

실행 결과:

```text
dogs: (16, 2)
labels: (16,)
```

처음에는 원본 16개 데이터만으로 KNN을 학습했다.

```python
knn = KNeighborsClassifier(3)
knn.fit(dogs, labels)

unknown_dog = [[79, 35]]
print(knn.predict(unknown_dog))
```

실행 결과:

```text
[0]
```

`[79, 35]`는 닥스훈트 class인 `0`으로 예측되었다.

이후에는 각 품종의 길이와 키 평균을 기준으로 정규분포 난수 데이터를 만들었다.

```python
dach_length_mean = sum(dach_length) / len(dach_length)
dach_height_mean = sum(dach_height) / len(dach_height)
samo_length_mean = sum(samo_length) / len(samo_length)
samo_height_mean = sum(samo_height) / len(samo_height)

print(dach_length_mean)
print(dach_height_mean)
print(samo_length_mean)
print(samo_height_mean)
```

실행 결과:

```text
78.25
25.875
82.125
54.875
```

평균값을 `loc`으로 두고, 표준편차는 `scale=5.0`으로 두어 품종별 200개 데이터를 생성했다.

```python
new_dach_length = np.random.normal(loc=78.25, scale=5.0, size=(200,))
new_dach_height = np.random.normal(loc=25.875, scale=5.0, size=(200,))

new_samo_length = np.random.normal(loc=82.125, scale=5.0, size=(200,))
new_samo_height = np.random.normal(loc=54.875, scale=5.0, size=(200,))

new_dach_data = np.column_stack((new_dach_length, new_dach_height))
new_samo_data = np.column_stack((new_samo_length, new_samo_height))

print(new_dach_data.shape)
print(new_samo_data.shape)
```

실행 결과:

```text
new_dach_data: (200, 2)
new_samo_data: (200, 2)
```

두 품종 데이터를 합치면 총 400개 sample이 된다.

```python
new_dogs = np.concatenate((new_dach_data, new_samo_data))

new_dach_target = [0] * 200
new_samo_target = [1] * 200
new_labels = np.concatenate((new_dach_target, new_samo_target))

print(new_dogs.shape)
print(new_labels.shape)
```

실행 결과:

```text
new_dogs: (400, 2)
new_labels: (400,)
```

전체 데이터의 80%를 학습에 사용하고 20%를 테스트에 사용했다.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    new_dogs,
    new_labels,
    train_size=0.8,
)

print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)
```

실행 결과:

```text
X_train: (320, 2)
y_train: (320,)
X_test: (80, 2)
y_test: (80,)
```

KNN으로 학습하고 테스트 데이터의 정확도를 확인했다.

```python
knn = KNeighborsClassifier(5)
knn.fit(X_train, y_train)

y_predict = knn.predict(X_test)

score = accuracy_score(y_test, y_predict)
print(score)
```

저장된 실행 결과:

```text
1.0
```

다시 실행했을 때는 난수 데이터와 train/test 분할이 달라질 수 있으므로 정확도도 달라진다. 실제 재검증에서는 `0.9875`가 나왔다. 이는 seed를 고정하지 않고 매번 새 데이터를 만들도록 한 의도된 동작이다.

정리:

- 길이와 키 2개 feature로 닥스훈트와 사모예드를 분류했다.
- 원본 데이터는 품종별 8개씩 총 16개다.
- 평균을 기준으로 `np.random.normal()`을 사용해 품종별 200개 synthetic data를 만들었다.
- 전체 400개 중 320개는 학습, 80개는 테스트에 사용했다.
- `random_state`를 고정하지 않았기 때문에 실행할 때마다 정확도는 달라질 수 있다.
- 이 프로젝트는 데이터 생성, 라벨 생성, train/test 분리, KNN 학습, 정확도 확인까지 분류 모델의 기본 흐름을 한 번에 확인하는 실습이다.

### 공식 참고 문서

- [`sklearn.datasets.load_iris`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html)
- [`sklearn.datasets.load_digits`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html)
- [`sklearn.neighbors.KNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)
- [`sklearn.metrics.accuracy_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html)
- [`sklearn.metrics.confusion_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html)
- [`sklearn.metrics.classification_report`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html)
- [`numpy.random.normal`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html)

## 퍼셉트론과 신경망 기초

이번 실습은 퍼셉트론의 가중치 갱신 과정을 직접 구현하고, scikit-learn과 Keras로 같은 흐름을 더 높은 수준의 API에서 확인했다. 앞의 KNN은 이웃 데이터와의 거리로 분류했다면, 이번 내용은 입력값과 가중치의 곱을 이용해 예측값을 만들고 오차에 따라 가중치를 조정하는 방식이다.

이번 학습은 다음 자료를 기준으로 확인했다.

- 실습 파일: `ml/ex_06.ipynb`, `ml/ex_07.ipynb`
- 실행 환경: Python 3.13.13, NumPy 2.4.5, scikit-learn 1.8.0, TensorFlow 2.20.0

### AND 문제와 직접 구현한 퍼셉트론

`ex_06.ipynb`에서는 AND 연산을 분류 문제로 만들었다. 입력 두 개에 bias 역할을 하는 `1`을 붙여 3개 feature로 사용했다.

```python
X = np.array([
    [0, 0, 1],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
])

y = np.array([0, 0, 0, 1])
W = np.zeros(len(X[0]))
```

확인할 내용:

- `X.shape`는 `(4, 3)`으로 볼 수 있다.
- 앞의 두 값은 실제 입력이고, 마지막 `1`은 bias를 가중치 안에서 함께 학습하기 위한 상수 입력이다.
- `y`는 AND의 정답이므로 두 입력이 모두 1일 때만 `1`이다.
- `W`는 입력 feature 수와 같은 길이의 가중치 벡터다.

퍼셉트론은 입력과 가중치의 내적을 계산한 뒤, 계단 함수로 0 또는 1을 출력한다.

```python
epsilon = 0.0000001

def step_func(t):
    if t > epsilon:
        return 1
    else:
        return 0
```

학습에서는 예측값과 정답의 차이를 `error`로 계산하고, 학습률 `eta`를 곱해 가중치를 수정했다.

```python
def perceptron_fit(X, Y, epochs=10):
    global W
    eta = 0.2

    for t in range(epochs):
        for i in range(len(X)):
            predict = step_func(np.dot(X[i], W))
            error = Y[i] - predict
            W += eta * error * X[i]
```

저장된 출력에서는 처음에는 `[1, 1, 1]`도 `0`으로 예측하지만, epoch가 진행되면서 가중치가 바뀌고 마지막에는 AND 결과를 맞히는 흐름을 확인했다. 예를 들어 학습 중 가중치는 `[0.4, 0.2, -0.4]` 같은 값으로 변했다.

주의할 점:

- 이 구현은 `global W`를 사용하므로 같은 노트북에서 다시 학습하면 이전 가중치 상태의 영향을 받을 수 있다.
- 입력 데이터 순서와 초기 가중치, 학습률에 따라 중간 가중치 변화는 달라질 수 있다.
- 단층 퍼셉트론은 AND처럼 선형 분리 가능한 문제에는 적합하지만 XOR처럼 선형 분리되지 않는 문제는 한 층만으로 해결하기 어렵다.

같은 AND 문제를 scikit-learn의 `Perceptron`으로도 확인했다.

```python
from sklearn.linear_model import Perceptron

X = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [0, 0, 0, 1]

ann = Perceptron()
ann.fit(X, y)
print(ann.predict(X))
```

실행 결과:

```text
[0 0 0 1]
```

정리:

- 퍼셉트론은 `입력과 가중치의 내적 -> 활성화 함수 -> 예측` 순서로 동작한다.
- 오차가 있으면 `W += 학습률 * 오차 * 입력` 형태로 가중치를 갱신한다.
- bias를 별도 절편으로 두지 않고 입력에 항상 `1`인 값을 추가해 함께 학습할 수 있다.
- scikit-learn의 `Perceptron`은 직접 작성한 학습 루프를 API로 감싼 형태로 이해할 수 있다.

### Keras MLP와 XOR 학습

`ex_07.ipynb`에서는 TensorFlow/Keras를 사용해 작은 다층 퍼셉트론을 만들었다. 입력층은 2개 값을 받고, 은닉층은 32개 뉴런, 출력층은 1개 뉴런으로 구성했다.

```python
import keras

mlp = keras.models.Sequential()
mlp.add(keras.layers.Input(shape=(2,)))
mlp.add(keras.layers.Dense(32, activation='sigmoid'))
mlp.add(keras.layers.Dense(1, activation='sigmoid'))
mlp.summary()
```

저장된 모델 요약:

```text
Total params: 129
Trainable params: 129
```

입력 데이터는 XOR에 가까운 형태다.

```python
x = tf.constant([[0, 0], [0, 1], [0, 1], [1, 1]])
y = tf.constant([0, 1, 1, 0])

mlp.compile(loss='mse', optimizer='adam')
mlp.fit(x, y, epochs=1000)
print(mlp.predict(x))
```

저장된 예측 결과:

```text
[[0.0651931 ]
 [0.93118113]
 [0.93118113]
 [0.07185799]]
```

출력층의 activation이 `sigmoid`이므로 결과는 0과 1 사이의 확률처럼 해석할 수 있다. 위 결과는 `[0, 1, 1, 0]`에 가까워졌으므로 작은 데이터에 대해서는 학습이 된 상태로 볼 수 있다.

주의할 점:

- `x`에는 `[1, 0]` 입력이 없고 `[0, 1]`이 두 번 들어 있다. 일반적인 XOR 전체 입력을 모두 확인하려면 `[[0, 0], [0, 1], [1, 0], [1, 1]]`로 구성해야 한다.
- `epochs=1000`은 같은 작은 데이터에 여러 번 반복 학습하는 설정이다. 학습 데이터에 잘 맞는다는 것과 새로운 데이터에 일반화된다는 것은 다르다.
- 이진 분류에서는 `mse`도 동작은 하지만, 보통은 출력 activation과 target 형태에 맞춰 `binary_crossentropy` 같은 손실도 함께 검토한다.

정리:

- 단층 퍼셉트론으로 어려운 문제도 은닉층을 추가한 MLP로 학습할 수 있다.
- `Input(shape=(2,))`는 sample 하나가 feature 2개를 가진다는 뜻이다.
- `Dense(32)`의 parameter 수는 입력 2개와 bias 1개가 32개 뉴런에 연결되어 `3 * 32 = 96`개가 된다.
- 마지막 `Dense(1)`은 은닉층 32개 출력과 bias 1개가 연결되어 `33`개 parameter를 가진다.

## MNIST 숫자 분류와 저장 모델 사용

이번 실습은 TensorFlow/Keras의 MNIST 데이터셋으로 손글씨 숫자 분류 모델을 학습하고, 저장한 모델과 직접 만든 숫자 이미지로 예측 흐름을 확인했다.

이번 학습은 다음 자료를 기준으로 확인했다.

- 실습 파일: `ml/ex_08.ipynb`
- 데이터 파일: Keras MNIST 데이터셋, `ml/digit3.png`, `ml/digit4.png`, `ml/digit4_2.png`, `ml/digit5.png`, `ml/digit9.png`
- 저장 모델: `ml/MNIST_20260626_15_30.keras`
- 실행 환경: Python 3.13.13, TensorFlow 2.20.0, OpenCV 4.13.0.92

### MNIST 데이터 구조

Keras의 MNIST 데이터는 학습 데이터와 테스트 데이터로 이미 나뉘어 제공된다.

```python
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)
```

실행 결과:

```text
(60000, 28, 28)
(60000,)
(10000, 28, 28)
(10000,)
```

확인할 내용:

- 학습 이미지는 60,000개이고 테스트 이미지는 10,000개다.
- 각 이미지는 `28 x 28` 크기의 흑백 이미지다.
- label은 0부터 9까지의 숫자 class다.
- 원본 이미지 값은 `uint8` 범위의 픽셀 값이므로 모델에 넣기 전에 정규화했다.

### Dense 모델 입력으로 바꾸기

이번 모델은 합성곱층이 아니라 `Dense` 층만 사용한다. 그래서 2차원 이미지 `(28, 28)`을 1차원 feature 784개로 펼쳤다.

```python
X_images = X_train.reshape((60000, 28 * 28))
X_images_norm = (X_images / 255).astype('float32')

X_images_test = X_test.reshape((10000, 28 * 28))
X_images_test_norm = (X_images_test / 255).astype('float32')
```

정규화 전에는 픽셀 값이 0부터 255 사이지만, `/ 255`를 하면 0부터 1 사이 값으로 바뀐다. 이후 `astype('float32')`를 사용해 TensorFlow 학습에 적합한 실수형 배열로 맞췄다.

주의할 점:

- `reshape((60000, 28 * 28))`은 sample 수 60,000개를 유지하고 각 이미지만 784개 feature로 펼친다.
- 학습 데이터와 테스트 데이터에 같은 방식의 정규화를 적용해야 한다.
- 테스트 데이터의 정답 `y_test`는 전처리 기준을 정하는 데 사용하지 않고 평가에만 사용한다.

### 모델 구조와 학습

모델은 입력 784개, 은닉층 512개, 은닉층 256개, 출력층 10개로 구성했다.

```python
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Input(shape=(28 * 28,)))
model.add(tf.keras.layers.Dense(units=512, activation='relu', name='Hidden1'))
model.add(tf.keras.layers.Dense(units=256, activation='relu', name='Hidden2'))
model.add(tf.keras.layers.Dense(units=10, activation='softmax', name='OutputLayer'))
model.summary()
```

저장된 모델 요약:

```text
Total params: 535,818
Trainable params: 535,818
```

출력층은 숫자 0부터 9까지 10개 class 중 하나를 고르는 문제이므로 `softmax`를 사용했다. label이 one-hot 벡터가 아니라 정수 label이므로 손실 함수는 `sparse_categorical_crossentropy`를 사용했다.

```python
model.compile(
    loss='sparse_categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy'],
)

model.fit(X_images_norm, y_train, epochs=40)
model.save("MNIST_20260626_15_30.keras")
```

저장된 학습 로그에서는 epoch가 진행되며 학습 정확도가 0.99 이상까지 올라갔다. 다만 학습 정확도는 모델이 본 데이터에 대한 결과이므로 일반화 성능은 테스트 데이터로 따로 확인해야 한다.

### 테스트 데이터 평가

학습 후 테스트 데이터로 평가했다.

```python
model.evaluate(X_images_test_norm, y_test)
```

실행 결과:

```text
[0.18221096694469452, 0.982200026512146]
```

테스트 정확도는 약 `0.9822`다. 이 값은 MNIST 테스트 데이터 10,000개 기준으로 계산된 결과다. 학습 정확도보다 낮을 수 있으며, 그 차이는 과적합 여부를 살펴볼 때 중요한 신호가 된다.

### 직접 그린 숫자 이미지 예측

OpenCV로 직접 만든 PNG 이미지를 읽고, MNIST와 같은 입력 형태로 맞춘 뒤 예측했다.

```python
import cv2

img = cv2.imread("digit9.png", cv2.IMREAD_GRAYSCALE)
resize_img = cv2.resize(img, (28, 28))
resize_img = resize_img.astype('float32')
inverse_img = 255 - resize_img
inverse_img_norm = inverse_img / 255

result = model.predict(inverse_img_norm.reshape((1, 28 * 28)))
print(result.argmax())
```

저장된 예측 결과:

```text
9
```

직접 그린 이미지의 배경과 글자 색이 MNIST와 반대일 수 있어 `255 - resize_img`로 흑백을 반전했다. 그 뒤 0부터 1 사이로 정규화하고, sample 하나를 의미하는 `(1, 784)` 형태로 바꿔 모델에 넣었다.

저장된 예측 결과:

| 파일 | 예측 결과 |
|---|---:|
| `digit4.png` | `8` |
| `digit9.png` | `9` |
| `digit5.png` | `5` |
| `digit3.png` | `3` |
| `digit4_2.png` | `4` |

`digit4.png`는 4를 의도했지만 8로 예측되었다. 반면 `digit4_2.png`는 4로 예측되었다. 이는 모델 정확도가 높아도 입력 이미지의 선 굵기, 위치, 크기, 전처리 방식이 MNIST 분포와 다르면 오답이 나올 수 있음을 보여준다.

정리:

- MNIST 원본 이미지는 `(sample 수, 28, 28)`이고, Dense 모델에는 `(sample 수, 784)`로 펼쳐 넣었다.
- 픽셀 값은 `/ 255`로 정규화하고 `float32`로 변환했다.
- 정수 label을 사용할 때 `sparse_categorical_crossentropy`를 사용할 수 있다.
- `softmax` 출력의 `argmax()`는 가장 점수가 높은 class 번호를 반환한다.
- 테스트 정확도와 직접 만든 이미지 예측 결과는 다를 수 있다. 직접 만든 이미지는 학습 데이터 분포와 다르기 때문이다.
- 저장 모델은 같은 구조와 가중치를 다시 사용할 수 있게 해 주지만, 입력 전처리는 학습 때와 동일하게 맞춰야 한다.

### 공식 참고 문서

- [Keras MNIST dataset](https://keras.io/api/datasets/mnist/)
- [Keras Sequential model](https://keras.io/guides/sequential_model/)
- [Keras Dense layer](https://keras.io/api/layers/core_layers/dense/)
- [Keras model training APIs](https://keras.io/api/models/model_training_apis/)
- [OpenCV image file reading and writing](https://docs.opencv.org/4.x/d4/da8/group__imgcodecs.html)

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
- 회귀 모델 평가 지표
- 범주형 데이터 인코딩
- 분류 모델의 `n_neighbors` 변화 비교
- 학습 데이터 크기와 정확도 변화 비교
- 퍼셉트론 수렴 조건과 선형 분리 가능성
- 이진 분류 손실 함수 비교
- MNIST 모델의 과적합 확인과 validation 데이터 사용
- 저장 모델 불러오기와 추론 전처리 함수화

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
│  └─ 1_넘파이_KarL.pdf
└─ numpy/
   └─ ex_01.ipynb
```

- `README.md`: ML 과정 전체 학습 정리
- `prompt.md`: 학습 내용을 README에 정리할 때 사용하는 공통 프롬프트
- `pyproject.toml`, `uv.lock`: ML 과정에서 공유하는 Python 환경
- `.venv/`: `uv`가 생성하는 가상환경이며 Git에는 포함하지 않음
- `references/`: 수업에서 제공된 강의 자료와 참고 문서
- `numpy/`: NumPy 실습 노트북과 예제 코드

NumPy, pandas, matplotlib, scikit-learn은 서로 연계되므로 우선 `ML`에서 하나의 가상환경을 공유한다. 특정 과정에서 의존성 충돌이 생길 때만 별도 프로젝트로 분리한다.

## 강의 자료

- `references/1_넘파이_KarL.pdf`: NumPy 수업 참고 자료

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

### 공식 참고 문서

- [NumPy absolute basics for beginners](https://numpy.org/doc/stable/user/absolute_beginners.html)
- [Array creation](https://numpy.org/doc/stable/user/basics.creation.html)
- [Broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html)
- [`numpy.arange`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html)
- [`numpy.linspace`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)
- [`numpy.logspace`](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html)

## 다음 정리 항목

실습 진행에 따라 아래 주제를 순서대로 추가한다.

- 인덱싱과 슬라이싱
- 배열 형태 변경
- 축과 집계 연산
- view와 copy
- 난수 생성
- 선형대수 기초
- pandas와 데이터 전처리
- 데이터 시각화
- 머신러닝 기본 과정

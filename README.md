# NumPy 학습 정리

## 2026-06-15

Python의 수치 계산 라이브러리인 **NumPy**의 기본 개념과 배열 연산을
정리한 학습 기록입니다.

### 주요 학습 내용

- Python 리스트와 `ndarray`의 차이
- 배열 생성: `array()`, `zeros()`, `ones()`, `full()`, `eye()`
- 배열 정보 확인: `shape`, `ndim`, `dtype`, `size`
- 데이터 생성: `arange()`, `linspace()`, `logspace()`
- 배열 사칙연산과 브로드캐스팅

```python
import numpy as np

data = np.array([[1, 2, 3], [4, 5, 6]])
print(data.shape)  # (2, 3)
print(data * 2)
print(data + np.array([10, 20, 30]))
print(np.linspace(0, 1, 5))
```

## 2026-06-16

PDF 30페이지부터 마지막까지는 다차원 배열 처리, 난수, 벡터화 연산,
리덕션, 선형대수, 배열 결합을 중심으로 학습했습니다.

### 주요 학습 내용

- `np.insert()`와 `axis`를 이용한 행/열 방향 값 삽입
- `np.flip()`으로 지정한 축 방향의 배열 뒤집기
- 다차원 배열 인덱싱, 슬라이싱, 논리 인덱싱
- `max()`, `min()`, `mean()`, `astype()`, `sort()` 활용
- `append()`, `reshape()`, `flatten()`으로 배열 형태 변경
- `random` 모듈을 활용한 난수 생성과 평균, 분산, 표준편차 이해
- 벡터화 연산과 리덕션(`sum`, `mean`, `min`, `max`)의 성능 장점
- `numpy.linalg`를 활용한 선형방정식 풀이와 행렬식 계산
- `concatenate()`, `vstack()`, `hstack()`, `r_`, `c_`, `column_stack()` 결합

### 예시

```python
import numpy as np

a = np.array([[1, 1], [2, 2], [3, 3]])
print(np.insert(a, 1, 4, axis=0))  # 행 삽입
print(np.insert(a, 1, 4, axis=1))  # 열 삽입

b = np.arange(1, 17).reshape(4, 4)
print(b[1:3, 1:3])   # 부분 행렬 추출
print(b[b % 2 == 0]) # 짝수만 추출

scores = np.array([[80, 90], [70, 100], [85, 95]])
print(scores.mean(axis=0)) # 열별 평균
print(scores.flatten())    # 1차원 변환

x = np.array([[2, 1], [1, 3]])
y = np.array([8, 13])
print(np.linalg.solve(x, y)) # 연립방정식 해

left = np.array([[1, 2], [3, 4]])
right = np.array([[5, 6], [7, 8]])
print(np.vstack((left, right)))
print(np.hstack((left, right)))
```

### 학습 목표

NumPy의 핵심은 배열을 직접 반복문으로 하나씩 처리하기보다, 축과 벡터화
연산을 활용해 더 간결하고 빠르게 데이터를 다루는 것입니다.


---------------------------------------------------------------------------------------------------
## 2026 - 06 - 17
# Matplotlib 학습 정리

이 폴더는 `ex_01.ipynb` 노트북과 `2_맷플롯립_KarL.pdf` 자료를 참고하여 Matplotlib의 기본 그래프 작성법을 실습한 내용이다. 주요 목표는 `matplotlib.pyplot`과 `numpy`를 이용해 선 그래프, 막대그래프, 히스토그램, 서브 플롯을 그리는 방법을 익히는 것이다.

## 파일 구성

| 파일 | 내용 |
| --- | --- |
| `ex_01.ipynb` | Matplotlib 실습 노트북 |
| `2_맷플롯립_KarL.pdf` | Matplotlib 수업 자료 |
| `sin-cos.pdf` | sine, cosine 그래프 저장 결과 |
| `sin-cos.png` | sine, cosine 그래프 이미지 저장 결과 |
| `README.MD` | 학습 내용 요약 |

## 기본 import

Matplotlib 그래프 작성에는 보통 아래 두 라이브러리를 함께 사용한다.

```python
import matplotlib.pyplot as plt
import numpy as np
```

`numpy`는 그래프에 사용할 배열 데이터를 만들고, `matplotlib.pyplot`은 실제 그래프를 그린다.

## 기본 선 그래프

가장 기본적인 그래프는 `plt.plot()`으로 그린다.

```python
plt.plot([1, 2, 3, 4], [1, 2, 3, 4])
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()
```

`xlabel()`, `ylabel()`은 축 이름을 설정하고, `show()`는 그래프를 화면에 표시한다.

## NumPy 배열을 이용한 그래프

`np.arange()`와 `np.square()`를 사용하면 일정한 간격의 x값과 제곱값을 쉽게 만들 수 있다.

```python
x = np.arange(-10, 11)
y = np.square(x)

plt.plot(x, y)
plt.axis([-100, 100, 0, 100])
plt.show()
```

`plt.axis([xmin, xmax, ymin, ymax])`는 그래프의 표시 범위를 정한다.

## 여러 개의 선 그래프

하나의 화면에 여러 그래프를 겹쳐 그릴 수 있다.

```python
x = np.arange(-20, 21)
y1 = x * 2
y2 = (1 / 3) * np.square(x) + 5
y3 = -(x ** 2) - 5

plt.plot(x, y1, "g--")
plt.plot(x, y2, "b-*")
plt.plot(x, y3, "rv:")
plt.axis([-30, 30, -30, 30])
plt.show()
```

선 스타일 예시는 다음과 같다.

| 표현 | 의미 |
| --- | --- |
| `g--` | 초록색 점선 |
| `b-*` | 파란색 선과 별표 마커 |
| `rv:` | 빨간색 삼각형 마커와 점선 |

## Sine, Cosine 그래프와 저장

`np.linspace()`는 지정한 구간을 일정 개수로 나눈 배열을 만든다.

```python
x = np.linspace(0, 2 * np.pi, 1000)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, "b--", label="sine wave")
plt.plot(x, y2, "r-.", label="cosine wave")
plt.legend()
plt.savefig("sin-cos.pdf")
plt.show()
```

`label`은 범례 이름이고, `plt.legend()`를 호출해야 범례가 표시된다. `plt.savefig()`는 그래프를 파일로 저장한다.

## 서브 플롯

여러 그래프를 하나의 Figure 안에 나누어 배치하려면 `plt.subplots()`를 사용한다.

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

plt.show()
```

주의할 점은 `plt.subplot()`과 `plt.subplots()`가 다르다는 것이다.

| 함수 | 용도 |
| --- | --- |
| `plt.subplot()` | 한 개의 subplot 위치를 지정 |
| `plt.subplots()` | 여러 개의 subplot과 축 배열을 한 번에 생성 |

## GridSpec 활용

`GridSpec`은 subplot을 더 자유롭게 배치할 때 사용한다.

```python
from matplotlib.gridspec import GridSpec

fig = plt.figure(figsize=(8, 5))
grid = GridSpec(2, 3, figure=fig)

X = np.random.randn(100)
Y = np.random.randn(100)
plt.subplot(grid[0, 0]).scatter(X, Y)

X = np.arange(10)
Y = np.random.uniform(1, 10, 10)
plt.subplot(grid[0, 1:]).bar(X, Y)

X = np.linspace(0, 10, 100)
Y = np.cos(X)
plt.subplot(grid[1, :2]).plot(X, Y)

Z = np.random.uniform(0, 1, (5, 5))
plt.subplot(grid[1, 2]).imshow(Z)

plt.tight_layout()
plt.show()
```

`grid[0, 1:]`, `grid[1, :2]`처럼 슬라이싱을 사용하면 여러 칸을 합친 subplot을 만들 수 있다.

## 막대그래프

막대그래프는 `plt.bar()`를 사용한다. x값과 y값의 개수는 반드시 같아야 한다.

```python
x = np.arange(3)

years = ["2010", "2011", "2012"]
domestic = [6801, 7695, 8010]
foreign = [777, 1046, 1681]

plt.bar(x, domestic, width=0.25, label="Domestic")
plt.bar(x + 0.3, foreign, width=0.25, label="Foreign")

plt.xticks(x + 0.15, years)
plt.legend()
plt.show()
```

`plt.xticks()`는 x축 눈금 위치와 표시 이름을 설정한다.

## 히스토그램

히스토그램은 데이터가 어떤 구간에 얼마나 분포하는지 보여준다.

```python
heights = np.array([
    175, 165, 164, 171, 165, 160, 164, 159,
    163, 167, 163, 172, 159, 160, 156, 162,
    166, 162, 158, 167, 160, 161, 156, 172,
    168, 165, 165, 177
])

plt.hist(heights, bins=6)
plt.xlabel("heights")
plt.ylabel("frequency")
plt.show()
```

`bins`는 데이터를 몇 개의 구간으로 나눌지 정한다.

## 누적 히스토그램

`cumulative=True`를 사용하면 누적 빈도를 그릴 수 있다.

```python
plt.hist(heights, bins=6, label="cumulative=True", cumulative=True)
plt.hist(heights, bins=6, label="cumulative=False", cumulative=False)
plt.legend(loc="upper left")
plt.show()
```

파이썬 인자 이름은 대소문자와 철자를 정확히 맞춰야 한다.

```python
cumulative=True   # 정상
Cumulative=True   # 오류
cmulative=True    # 오류
```

## 정규분포 히스토그램

`np.random.normal()`을 사용하면 평균과 표준편차를 지정한 정규분포 데이터를 만들 수 있다.

```python
f1 = np.random.normal(loc=0, scale=1, size=100000)
f2 = np.random.normal(loc=3, scale=1, size=100000)

plt.hist(f1, bins=200, color="red", alpha=0.4, label="avg = 0, std = 1")
plt.hist(f2, bins=200, color="green", alpha=0.4, label="avg = 3, std = 1")

plt.axis([-8, 8, -2, 2500])
plt.legend()
plt.show()
```

`alpha`는 투명도이며 0부터 1 사이의 값만 사용할 수 있다.

## 자주 발생한 오류와 해결

| 오류 상황 | 원인 | 해결 |
| --- | --- | --- |
| `subplot() takes 1 or 3 positional arguments but 2 were given` | `plt.subplot(2, 2)`처럼 인자 2개만 전달 | `plt.subplots(2, 2)` 사용 |
| `x and y must have same first dimension` | `plot(x, y)`의 x, y 길이가 다름 | x와 y를 같은 길이로 생성 |
| `shape mismatch` | `bar(x, y)`의 x, y 개수가 다름 | `x = np.arange(len(y))`처럼 개수 맞추기 |
| `NameError: name 'x' is not defined` | `np.arange(3)`만 쓰고 x에 저장하지 않음 | `x = np.arange(3)` 사용 |
| `np.array()` 오류 | 값을 리스트로 감싸지 않음 | `np.array([1, 2, 3])` 형태 사용 |
| `Cumulative` 또는 `cmulative` 오류 | 옵션 이름 오타 | `cumulative`로 작성 |
| `alpha` 오류 | `alpha=4`처럼 범위 초과 | `alpha=0.4`처럼 0~1 값 사용 |

## 핵심 정리

- `plt.plot()`은 선 그래프를 그린다.
- `plt.bar()`는 막대그래프를 그린다.
- `plt.hist()`는 히스토그램을 그린다.
- `plt.scatter()`는 산점도를 그린다.
- `plt.imshow()`는 2차원 배열을 이미지처럼 표시한다.
- `plt.legend()`는 범례를 표시한다.
- `plt.savefig()`는 그래프를 파일로 저장한다.
- 그래프 함수에 들어가는 x, y 데이터는 보통 길이가 같아야 한다.
- `GridSpec`을 사용하면 subplot 배치를 더 유연하게 구성할 수 있다.

---------------------------------------------------------------------------------------------------

## 2026 - 06 - 18



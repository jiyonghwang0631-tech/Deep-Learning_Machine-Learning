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

# Pandas 핵심 요약 노트

## 기본 import

```python
import pandas as pd
import numpy as np
```

## Series

- 1차원 데이터
- 리스트를 한 줄짜리 데이터로 바꿀 때 사용
- `None`은 `NaN`으로 표시됨

```python
se = pd.Series([1, 2, None, 3])
```

결측값 확인:

```python
se.isna()
```

인덱스 직접 지정:

```python
se = pd.Series([1, 2, None, 4], index=['A', 'B', 'C', 'D'])
```

값 선택:

```python
se['A']
```

## DataFrame

- 2차원 표 데이터
- 행과 열이 있음
- 엑셀 표처럼 생각하면 됨

```python
df = pd.DataFrame({
    '월': ['1월', '2월', '3월', '4월'],
    '수입': [9500, 6200, 6050, 7000],
    '지출': [5040, 2350, 2300, 4800]
})
```

열 이름 확인:

```python
df.columns
```

행 인덱스 확인:

```python
df.index
```

앞부분 확인:

```python
df.head()
```

주의:

```python
df.head
```

이렇게 쓰면 함수 실행이 아니라 함수 자체가 출력된다.

## CSV 읽기

기본 읽기:

```python
df = pd.read_csv("./vehicle_prod.csv")
```

첫 번째 열을 인덱스로 사용:

```python
df = pd.read_csv("./vehicle_prod.csv", index_col=0)
```

`vehicle_prod.csv`에서는 국가명이 인덱스가 된다.

## 열 선택

한 열 선택:

```python
df['2011']
```

여러 열 선택:

```python
df[['2007', '2008', '2009']]
```

주의:

- 한 열: 대괄호 1개
- 여러 열: 대괄호 2개

```python
df['2011']              # Series
df[['2011']]            # DataFrame
```

## loc

- 인덱스 이름으로 선택
- 열 이름으로 선택
- 문자열 날짜, 국가명 같은 이름 기반 선택

한 행 선택:

```python
df.loc['China']
```

행과 열 선택:

```python
df.loc['China', '2011']
```

여러 행 + 한 열:

```python
df.loc[['China', 'Korea'], '2011']
```

날짜 인덱스 선택:

```python
weather.loc['2012-02-11']
```

주의:

```python
weather.loc('2012-02-11')   # 틀림
weather.loc['2012-02-11']   # 맞음
```

`loc`는 함수가 아니라 선택 도구라서 `()`가 아니라 `[]`를 쓴다.

## iloc

- 위치 번호로 선택
- 0번째, 1번째처럼 숫자 위치 기준

첫 번째 행:

```python
df.iloc[0]
```

첫 번째 행, 다섯 번째 열:

```python
df.iloc[0, 4]
```

`2011` 열에서 0번째, 4번째 값:

```python
df['2011'].iloc[[0, 4]]
```

주의:

```python
new_weather_mean_windy.iloc['2012-02-11']   # 틀림
new_weather_mean_windy.loc['2012-02-11']    # 맞음
```

`iloc`는 문자열 인덱스가 아니라 숫자 위치만 사용한다.

## loc / iloc 구분

| 구분 | 기준 | 예시 |
|---|---|---|
| `loc` | 이름 | `df.loc['China']` |
| `iloc` | 위치 번호 | `df.iloc[0]` |

외우기:

- `loc`: label
- `iloc`: integer location

## 통계 함수

합계:

```python
df['수입'].sum()
```

평균:

```python
df['수입'].mean()
```

최댓값:

```python
df['수입'].max()
```

최솟값:

```python
df['수입'].min()
```

최댓값 위치:

```python
np.argmax(df['수입'])
```

## 행 방향 / 열 방향

열 기준 계산:

```python
df.sum()
```

행 기준 계산:

```python
df.sum(axis=1)
```

정리:

- `axis=0`: 세로 방향, 열별 계산
- `axis=1`: 가로 방향, 행별 계산

## 새 열 추가

연도별 값을 더해서 `total` 열 만들기:

```python
df['total'] = df.sum(axis=1)
```

연도별 평균을 `mean` 열로 만들기:

```python
df['mean'] = df[['2007', '2008', '2009', '2010', '2011']].mean(axis=1)
```

특정 열만 골라 계산해야 할 때는 열 목록을 직접 지정한다.

## 열 삭제

```python
df.drop('2007', axis=1, inplace=True)
```

뜻:

- `'2007'`: 삭제할 열 이름
- `axis=1`: 열 삭제
- `inplace=True`: 원본에 바로 반영

행 삭제는 `axis=0`.

## 새 행 추가

연도별 생산 대수 합계 행 추가:

```python
df = pd.read_csv("./vehicle_prod.csv", index_col=0)
df.loc['Total'] = df.select_dtypes(np.number).sum()
```

핵심:

- `df.loc['Total']`: `Total`이라는 새 행
- `select_dtypes(np.number)`: 숫자 열만 선택
- `sum()`: 열별 합계

결과 형태:

```text
         2007   2008   2009   2010   2011
China    ...
Korea    ...
Total   54.12  50.77  45.04  55.68  57.25
```

## 날짜 처리

날짜 문자열을 날짜 타입으로 변환:

```python
weather2['일시'] = pd.to_datetime(weather2['일시'])
```

연도 추출:

```python
weather2['year'] = pd.DatetimeIndex(weather2['일시']).year
```

월 추출:

```python
weather2['month'] = pd.DatetimeIndex(weather2['일시']).month
```

일 추출:

```python
weather2['day'] = pd.DatetimeIndex(weather2['일시']).day
```

`dt` 사용 방식:

```python
weather2['year'] = weather2['일시'].dt.year
weather2['month'] = weather2['일시'].dt.month
weather2['day'] = weather2['일시'].dt.day
```

주의:

```python
weather2['일시'] = pd.DatetimeIndex(weather2['일시']), year
```

쉼표 때문에 오른쪽이 튜플이 된다. `year`라는 변수가 없으면 오류가 난다.

올바른 방식:

```python
weather2['일시'] = pd.to_datetime(weather2['일시'])
weather2['year'] = pd.DatetimeIndex(weather2['일시']).year
```

## 자주 헷갈리는 코드

### 1. 메서드에는 괄호 붙이기

```python
df.head()       # 맞음
df.head         # 틀림
```

### 2. loc는 대괄호

```python
weather.loc['2012-02-11']      # 맞음
weather.loc('2012-02-11')      # 틀림
```

### 3. iloc는 숫자 위치

```python
df.iloc[0]      # 맞음
df.iloc['China'] # 틀림
```

### 4. 날짜에서 연도만 뽑기

```python
pd.DatetimeIndex(weather2['일시']).year
```

이 코드는 실행만 하면 연도 배열을 보여준다.

새 열로 저장하려면:

```python
weather2['year'] = pd.DatetimeIndex(weather2['일시']).year
```

### 5. 한 열과 여러 열

```python
df['2011']       # 한 열, Series
df[['2011']]     # 한 열이지만 DataFrame
```

## 시험 직전 체크

- `read_csv()`로 파일 읽기
- `index_col=0`은 첫 번째 열을 인덱스로 사용
- `head()`는 괄호 필요
- `loc`는 이름 선택
- `iloc`는 위치 번호 선택
- `axis=1`은 행 방향 계산
- 새 열 추가는 `df['열이름'] = 값`
- 새 행 추가는 `df.loc['행이름'] = 값`
- 날짜 변환은 `pd.to_datetime()`
- 연도 추출은 `.dt.year` 또는 `pd.DatetimeIndex(...).year`

---------------------------------------------------------------------------------------------------

## 2026 - 06 - 19 

# Machine Learning 실습 정리

이 폴더는 고려대학교 Machine Learning 강의자료와 Titanic 데이터셋을 활용한 Python 데이터 분석 실습 내용을 정리한 공간이다.

## 포함 파일

| 파일 | 설명 |
| --- | --- |
| `ex_01.ipynb` | Titanic 데이터셋을 이용한 데이터 로드, 결측치 처리, 시각화, 상관관계 분석 실습 노트북 |
| `titanic.csv` | Seaborn Titanic 데이터셋을 CSV로 저장한 파일 |
| `titanic_heatmap.csv` | 히트맵 분석용 전처리 결과를 저장한 파일 |
| `고려대학교_Machin_Learning_강의자료.pdf` | 머신러닝 강의자료 |

## 강의자료 기반 학습 주제

PDF 강의자료에서는 머신러닝의 기본 개념과 대표 알고리즘, 딥러닝 기초 주제가 함께 다뤄진다. 파일 내부에서 확인되는 주요 키워드는 다음과 같다.

- Machine Learning의 기본 개념과 함수 근사 관점
- 지도학습 문제에서의 분류와 예측 흐름
- KNN 알고리즘
- Kaggle Titanic 데이터셋을 활용한 생존 예측 문제
- 신경망 기반 학습으로 확장되는 CNN, Keras, AlexNet, MNIST, RNN, BPTT 관련 내용

이번 노트북 실습은 위 강의 흐름 중 **Titanic 데이터를 이용한 탐색적 데이터 분석과 머신러닝 전처리 기초**에 해당한다.

## 실습 내용 요약

### 1. 라이브러리 사용

실습에서는 다음 라이브러리를 사용했다.

```python
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

- `seaborn`: Titanic 데이터셋 로드 및 시각화
- `pandas`: 데이터프레임 처리, 결측치 확인, 컬럼 변환
- `numpy`: 수치 연산
- `matplotlib`: 그래프 출력

### 2. Titanic 데이터 로드

```python
titanic = sns.load_dataset("titanic")
```

Seaborn에서 제공하는 Titanic 데이터를 불러와 생존 여부(`survived`), 객실 등급(`pclass`), 성별(`sex`), 나이(`age`), 요금(`fare`), 동승 가족 수(`sibsp`, `parch`) 등을 분석했다.

### 3. 결측치 확인과 처리

```python
print(titanic.isnull().sum())
```

주요 결측치 처리 내용은 다음과 같다.

- `age`: 중앙값으로 결측치 대체
- `embarked`: 최빈값인 `S`로 결측치 대체
- `deck`: `C`로 결측치 대체
- `embark_town`: `Cherbourg`로 결측치 대체

예시:

```python
titanic['age'] = titanic['age'].fillna(value=titanic['age'].median())
titanic['embarked'] = titanic['embarked'].fillna(value='S')
```

결측치를 처리하는 이유는 시각화나 상관관계 분석, 이후 머신러닝 모델 학습에서 누락값으로 인한 오류를 줄이기 위해서다.

### 4. 성별에 따른 생존 분석

성별 조건 필터링을 통해 남성과 여성의 생존자 수를 비교했다.

```python
titanic[titanic['sex'] == 'male']['survived'].value_counts()
titanic[titanic['sex'] == 'female']['survived'].value_counts()
```

노트북 실행 결과:

- 남성: 사망 468명, 생존 109명
- 여성: 생존 233명, 사망 81명

이를 통해 Titanic 데이터에서는 성별이 생존 여부와 강한 관련이 있음을 확인했다.

### 5. 시각화

성별 생존 비율은 파이 차트로 비교했고, 객실 등급과 생존 여부는 countplot으로 시각화했다.

```python
sns.countplot(x='pclass', hue='survived', data=titanic)
plt.title(label='Pclass vs Survived')
```

이 시각화는 객실 등급별 생존/사망 분포를 비교하기 위한 것이다.

### 6. 상관관계 분석

`corr()`를 사용해 생존 여부와 다른 수치형 변수 간의 피어슨 상관관계를 확인했다.

```python
titanic['survived'].corr(other=titanic['adult_male'], method='pearson')
titanic['survived'].corr(other=titanic['fare'], method='pearson')
```

노트북 실행 결과:

- `survived`와 `adult_male`: 약 `-0.557`
- `survived`와 `fare`: 약 `0.257`

해석:

- `adult_male`은 생존 여부와 음의 상관관계가 크다.
- `fare`는 생존 여부와 약한 양의 상관관계가 있다.

### 7. Pairplot 분석

```python
sns.pairplot(data=titanic, hue='survived')
plt.show()
```

`pairplot`을 사용해 여러 변수 간의 관계를 한 번에 확인했다. `hue='survived'`를 지정하여 생존 여부에 따라 데이터 분포가 어떻게 달라지는지 비교했다.

### 8. 히트맵 분석용 파생 변수 생성

나이는 10년 단위 범주형 값으로 변환했다.

```python
def category_age(x):
    if x >= 70:
        return 7
    elif x >= 60:
        return 6
    elif x >= 50:
        return 5
    elif x >= 40:
        return 4
    elif x >= 30:
        return 3
    elif x >= 20:
        return 2
    elif x >= 10:
        return 1
    else:
        return 0
```

성별과 가족 수 파생 변수도 생성했다.

```python
titanic['age2'] = titanic['age'].apply(category_age)
titanic['sex'] = titanic['sex'].map({'male': 1, 'female': 0})
titanic['family'] = titanic['sibsp'] + titanic['parch'] + 1
```

- `age2`: 나이를 10년 단위 범주로 변환한 값
- `sex`: 남성 `1`, 여성 `0`으로 변환한 값
- `family`: 본인을 포함한 가족 수

### 9. 상관관계 히트맵

```python
heatmap_data = titanic[['survived', 'sex', 'age2', 'family', 'pclass', 'fare']]

sns.heatmap(
    heatmap_data.astype(float).corr(),
    linewidths=0.1,
    vmax=1.0,
    square=True,
    cmap=plt.cm.RdBu,
    linecolor='white',
    annot=True,
    annot_kws={'size': 10}
)
plt.show()
```

히트맵에서 확인한 주요 관계:

- `survived`와 `sex`는 양의 상관관계가 있다.
- `survived`와 `pclass`는 음의 상관관계가 있다.
- `survived`와 `fare`는 양의 상관관계가 있다.
- `pclass`와 `fare`는 비교적 강한 음의 상관관계가 있다.

## 실습 중 발생한 문제와 해결

### CSV 저장 권한 오류

```python
titanic.to_csv(path_or_buf='C:\\titanic_heatmap.csv', index=False)
```

`C:\` 최상위 경로는 쓰기 권한이 제한될 수 있어 `PermissionError`가 발생했다. 프로젝트 폴더 안에 저장하도록 수정한다.

```python
titanic.to_csv(path_or_buf='titanic_heatmap.csv', index=False)
```

### Pandas `map()` 경고

```python
titanic['sex'] = titanic['sex'].map(arg={'male': 1, 'female': 0})
```

`arg` 파라미터는 향후 지원이 중단될 예정이므로 다음처럼 수정한다.

```python
titanic['sex'] = titanic['sex'].map({'male': 1, 'female': 0})
```

### 히트맵에서 `sex` 값이 비어 보이는 문제

같은 셀을 반복 실행하면 이미 `1`, `0`으로 바뀐 `sex` 컬럼을 다시 `'male'`, `'female'` 기준으로 매핑하면서 전부 `NaN`이 될 수 있다.

해결 방법:

```python
titanic = sns.load_dataset('titanic')
titanic['sex'] = titanic['sex'].map({'male': 1, 'female': 0})
```

전처리 셀을 다시 실행할 때는 원본 데이터를 먼저 다시 불러오는 것이 안전하다.

## 핵심 학습 포인트

- 데이터 분석 전에는 결측치 확인과 처리가 필요하다.
- 범주형 데이터는 머신러닝과 상관관계 분석을 위해 숫자로 변환해야 한다.
- 파생 변수(`age2`, `family`)를 만들면 기존 데이터에서 더 의미 있는 분석이 가능하다.
- 시각화는 데이터의 패턴을 빠르게 이해하는 데 효과적이다.
- 상관관계는 변수 간 선형 관계를 보는 지표이며, 인과관계를 의미하지는 않는다.
- 같은 전처리 셀을 반복 실행하면 데이터 타입이나 값이 바뀌어 예상치 못한 결과가 나올 수 있다.

## 실행 순서

1. `ex_01.ipynb`를 연다.
2. 라이브러리 import 셀을 실행한다.
3. Titanic 데이터를 다시 로드한다.
4. 결측치 처리 셀을 실행한다.
5. 성별/객실등급 생존 분석 시각화를 실행한다.
6. 파생 변수 생성 후 히트맵을 실행한다.

## 정리

이번 실습은 머신러닝 모델 학습 전 단계인 데이터 이해, 전처리, 탐색적 분석의 기초를 다룬다. Titanic 생존 데이터의 성별, 나이, 가족 수, 객실 등급, 요금 정보를 활용하여 생존 여부와 관련 있는 변수를 확인하고, 이후 분류 모델 학습으로 확장할 수 있는 기반을 마련했다.

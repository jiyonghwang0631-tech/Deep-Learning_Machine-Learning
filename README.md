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

--------------------------------------------------------------------------------------------------

## 2026 - 06 - 22

## ex_02.ipynb: 선형 회귀 기초

`ex_02.ipynb`에서는 scikit-learn의 `LinearRegression`을 사용하여 가장 기본적인 선형 회귀 모델을 학습한다. 선형 회귀는 입력값 `x`와 정답값 `y` 사이의 직선 관계를 찾는 지도학습 알고리즘이다. 모델은 데이터에 가장 잘 맞는 기울기(`coef_`)와 절편(`intercept_`)을 계산하고, 이를 이용해 새로운 입력값의 결과를 예측한다.

### 1. 기본 라이브러리

```python
import matplotlib.pyplot as plt
from sklearn import linear_model
```

- `matplotlib.pyplot`: 학습 데이터와 회귀선을 시각화할 때 사용한다.
- `sklearn.linear_model`: 선형 회귀 모델을 만들 때 사용한다.

### 2. 간단한 데이터로 모델 학습

```python
reg = linear_model.LinearRegression()
x = [[0], [1], [2]]
y = [3, 4, 5]
reg.fit(x, y)
```

`LinearRegression()`으로 모델 객체를 만들고, `fit()` 메서드로 입력 데이터와 정답 데이터를 학습시킨다. scikit-learn에서 입력 데이터 `x`는 2차원 형태로 전달해야 하므로 `[[0], [1], [2]]`처럼 작성한다.

### 3. 회귀 계수와 절편 확인

```python
reg.coef_
reg.intercept_
```

- `coef_`: 회귀식의 기울기
- `intercept_`: 회귀식의 절편

선형 회귀 모델은 다음과 같은 식을 학습한다.

```text
y = coef_ * x + intercept_
```

### 4. 새로운 값 예측

```python
reg.predict([[-4]])
reg.predict([[5]])
```

`predict()`는 학습된 회귀식을 이용하여 새로운 입력값에 대한 예측 결과를 반환한다. 예측할 때도 입력값은 2차원 형태로 넣어야 한다.

### 5. 키와 몸무게 데이터 예측

```python
X = [[174], [152], [138], [128], [186]]
y = [71, 55, 46, 38, 88]

reg = linear_model.LinearRegression()
reg.fit(X, y)

prediction = reg.predict([[165]])
print(prediction)
```

이 예제에서는 키를 입력값, 몸무게를 정답값으로 사용한다. 모델을 학습한 뒤 키가 `165`인 사람의 몸무게를 예측한다.

### 6. 산점도와 회귀선 시각화

```python
plt.scatter(X, y, color='red')
plt.plot(X, reg.predict(X), color='white', linewidth=3)
plt.show()
```

- `scatter()`: 실제 데이터를 점으로 표시한다.
- `plot()`: 학습된 모델이 예측한 값을 선으로 표시한다.

산점도는 실제 데이터의 분포를 보여 주고, 회귀선은 모델이 찾은 데이터의 전체적인 경향을 보여 준다.

## ex_03.ipynb: Diabetes 데이터셋 회귀 실습

`ex_03.ipynb`에서는 scikit-learn에서 제공하는 Diabetes 데이터셋을 사용하여 회귀 모델을 학습한다. Diabetes 데이터셋은 환자의 여러 신체 지표를 입력값으로 사용하고, 1년 뒤 당뇨병 진행 정도를 예측하는 회귀 문제에 사용된다.

### 1. 라이브러리와 데이터 불러오기

```python
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import datasets

diabete = datasets.load_diabetes()
```

`sklearn.linear_model`은 모두 소문자로 작성해야 한다. `sklearn.Linear_model`처럼 대문자를 섞어 쓰면 `ModuleNotFoundError`가 발생한다.

### 2. 데이터 구조 확인

```python
x = diabete['data']
y = diabete['target']

print(x.shape)
print(y.shape)
```

Diabetes 데이터셋의 입력 데이터는 여러 개의 특성으로 구성되어 있고, 정답 데이터는 질병 진행 정도를 나타내는 수치값이다. 회귀 문제에서는 정답이 범주가 아니라 연속적인 숫자값이다.

### 3. BMI 특성만 선택

```python
bmi = x[:, 2]
x_new = x[:, np.newaxis, 2]
```

전체 특성 중 세 번째 열인 BMI 값을 선택하여 단순 선형 회귀에 사용한다. `x[:, 2]`는 1차원 배열이므로, scikit-learn 모델에 넣기 위해 `np.newaxis`를 사용해 2차원 형태로 바꾼다.

```text
x[:, 2]              -> (442,)
x[:, np.newaxis, 2]  -> (442, 1)
```

### 4. 학습 데이터와 테스트 데이터 분리

```python
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(
    x_new,
    y,
    test_size=0.1,
    random_state=0
)
```

`train_test_split()`은 데이터를 학습용과 테스트용으로 나눈다.

- `x_train`, `y_train`: 모델 학습에 사용한다.
- `x_test`, `y_test`: 모델 평가와 예측 확인에 사용한다.
- `test_size=0.1`: 전체 데이터 중 10%를 테스트 데이터로 사용한다.
- `random_state=0`: 실행할 때마다 같은 방식으로 데이터가 나뉘도록 고정한다.

### 5. 모델 생성과 학습

```python
regression = LinearRegression()
regression.fit(x_train, y_train)
```

`LinearRegression()`으로 회귀 모델을 만들고, `fit()`으로 학습 데이터를 학습시킨다.

### 6. 회귀 계수와 절편 확인

```python
regression.coef_
regression.intercept_
```

`coef_`와 `intercept_`를 확인하면 모델이 BMI와 당뇨병 진행 정도 사이의 관계를 어떤 직선으로 표현했는지 알 수 있다.

### 7. 테스트 데이터 예측

```python
y_predict = regression.predict(x_test)
print(y_predict)
print(y_test)
```

`y_predict`는 모델이 예측한 값이고, `y_test`는 실제 정답값이다. 두 값을 비교하면 모델의 예측이 실제 값과 얼마나 가까운지 확인할 수 있다.

### 8. 예측 결과 시각화

```python
plt.scatter(x_test, y_test, color='yellow', marker='.')
plt.plot(x_test, regression.predict(x_test), color='blue', linewidth=3)
plt.show()
```

테스트 데이터의 실제값을 점으로 표시하고, 학습된 회귀 모델이 예측한 값을 선으로 표시한다. 이때 `y_predict` 변수를 사용하려면 반드시 먼저 아래 코드가 실행되어 있어야 한다.

```python
y_predict = regression.predict(x_test)
```

그래프 셀만 따로 실행하면 `y_predict`가 정의되지 않아 `NameError`가 발생할 수 있다. 이런 문제를 줄이려면 그래프 셀 안에서 바로 `regression.predict(x_test)`를 호출하는 방식이 더 안전하다.

### 9. Stem 그래프

```python
plt.stem(y_test, regression.predict(x_test))
plt.show()
```

`stem()` 그래프는 실제값과 예측값의 대응 관계를 줄기 형태로 확인할 때 사용할 수 있다. 회귀 모델의 예측값이 실제값과 얼마나 차이 나는지 직관적으로 비교하는 보조 시각화로 활용할 수 있다.

## 실습 중 발생한 주요 오류와 원인

### 1. `ModuleNotFoundError: No module named 'sklearn.Linear_model'`

원인:

```python
from sklearn.Linear_model import LinearRegression
```

`Linear_model`처럼 대문자를 사용했기 때문에 발생한다. scikit-learn의 모듈 이름은 소문자다.

해결:

```python
from sklearn.linear_model import LinearRegression
```

### 2. `NameError: name 'reg' is not defined`

원인:

```python
reg.fit(X, y)
```

`reg`라는 모델 객체를 만들기 전에 `fit()`을 호출했기 때문에 발생한다.

해결:

```python
reg = linear_model.LinearRegression()
reg.fit(X, y)
```

### 3. `NameError: name 'X_test' is not defined`

원인:

```python
plt.plot(X_test, y_predict, color='blue', linewidth=3)
```

실제 노트북에서는 변수명이 `x_test`인데, 그래프 코드에서는 `X_test`처럼 대문자 `X`를 사용했기 때문에 발생한다. 파이썬은 대소문자를 구분한다.

해결:

```python
plt.plot(x_test, y_predict, color='blue', linewidth=3)
```

### 4. `NameError: name 'y_predict' is not defined`

원인:

```python
plt.plot(x_test, y_predict, color='blue', linewidth=3)
```

`y_predict`를 만들기 전에 그래프 셀을 먼저 실행했기 때문에 발생한다.

해결:

```python
y_predict = regression.predict(x_test)

plt.scatter(x_test, y_test, color='yellow', marker='.')
plt.plot(x_test, y_predict, color='blue', linewidth=3)
plt.show()
```

또는 다음처럼 예측을 그래프 코드 안에서 바로 실행한다.

```python
plt.scatter(x_test, y_test, color='yellow', marker='.')
plt.plot(x_test, regression.predict(x_test), color='blue', linewidth=3)
plt.show()
```

## 정리

`ex_02.ipynb`와 `ex_03.ipynb`는 모두 선형 회귀 모델의 기본 흐름을 연습하는 노트북이다. `ex_02.ipynb`에서는 작은 직접 입력 데이터를 이용해 회귀 모델의 생성, 학습, 예측, 시각화를 확인했고, `ex_03.ipynb`에서는 scikit-learn의 Diabetes 데이터셋을 이용해 실제 데이터셋 기반의 학습 데이터 분리, 모델 학습, 테스트 데이터 예측 과정을 실습했다.

선형 회귀 실습에서 중요한 점은 다음과 같다.

1. 입력 데이터는 scikit-learn 모델에 맞게 2차원 형태로 준비해야 한다.
2. 모델 객체를 만든 뒤 `fit()`으로 학습해야 `predict()`를 사용할 수 있다.
3. 학습 데이터와 테스트 데이터를 분리하면 모델이 보지 않은 데이터에 대해 예측을 확인할 수 있다.
4. 노트북에서는 셀 실행 순서가 중요하므로, 변수를 만드는 셀을 먼저 실행해야 한다.
5. 파이썬 변수명과 모듈명은 대소문자를 구분한다.

--------------------------------------------------------------------------------------------------

## 2026 - 06 -23

## ex_04.ipynb: Iris 데이터셋 KNN 분류

`ex_04.ipynb`에서는 Iris 데이터셋을 이용하여 KNN 분류 모델을 학습한다. 앞의 `ex_03.ipynb`가 연속적인 값을 예측하는 회귀 문제였다면, `ex_04.ipynb`는 붓꽃 품종을 맞히는 분류 문제다.

### 1. Iris 데이터셋 불러오기

```python
from sklearn import datasets

iris = datasets.load_iris()
```

Iris 데이터셋은 총 150개의 샘플과 4개의 입력 특성으로 구성된다.

```python
data = iris['data']
target = iris['target']

data.shape    # (150, 4)
target.shape  # (150,)
```

입력 특성은 꽃받침 길이, 꽃받침 너비, 꽃잎 길이, 꽃잎 너비다. 정답값은 세 가지 붓꽃 품종을 숫자로 표현한다.

```text
0: Iris-Setosa
1: Iris-Versicolour
2: Iris-Virginica
```

### 2. 학습 데이터와 테스트 데이터 분리

```python
from sklearn.model_selection import train_test_split

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=2026
)
```

전체 데이터 중 20%를 테스트 데이터로 사용한다. 실습 결과 학습 데이터는 `(120, 4)` 형태가 되었다.

### 3. KNN 모델 생성과 학습

```python
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
```

KNN은 새 데이터가 들어왔을 때 가장 가까운 이웃 데이터들의 정답을 참고하여 클래스를 결정하는 알고리즘이다. `n_neighbors=5`는 가까운 이웃 5개를 기준으로 판단한다는 의미다.

### 4. 예측과 정확도 평가

```python
y_predict = knn.predict(X_test)

from sklearn import metrics
scores = metrics.accuracy_score(y_test, y_predict)
print(scores)
```

실습 결과 정확도는 다음과 같다.

```text
0.9666666666666667
```

즉, 테스트 데이터 30개 중 대부분을 올바르게 분류했으며 약 96.7%의 정확도를 보였다.

### 5. 새로운 꽃 데이터 예측

```python
new_flower = [[3.0, 4.0, 5.0, 2.0]]
print(knn.predict(new_flower))
```

실습 결과 예측값은 `[1]`이었다. 이는 입력한 새 꽃 데이터가 `Iris-Versicolour`로 분류되었다는 뜻이다.

### 6. 혼동 행렬

```python
from sklearn.metrics import confusion_matrix

confusion = confusion_matrix(y_test, y_predict)
print(confusion)
```

실습 결과는 다음과 같다.

```text
[[11  0  0]
 [ 0 10  1]
 [ 0  0  8]]
```

혼동 행렬을 보면 Setosa와 Virginica는 모두 맞혔고, Versicolour 데이터 중 1개가 다른 클래스로 예측되었음을 알 수 있다.

## project_01.ipynb: 강아지 품종 KNN 분류 프로젝트

`project_01.ipynb`에서는 닥스훈트와 사모예드의 몸길이와 몸높이 데이터를 이용하여 품종을 분류한다. 직접 만든 작은 데이터셋으로 KNN 분류 과정을 연습하는 프로젝트다.

### 1. 데이터 준비

```python
dach_length = [77, 78, 85, 83, 73, 77, 73, 80]
dach_height = [25, 28, 29, 30, 21, 22, 17, 35]

samo_length = [75, 77, 86, 86, 79, 83, 83, 88]
samo_height = [56, 57, 50, 53, 60, 53, 49, 61]
```

닥스훈트와 사모예드 각각 8개씩, 총 16개의 데이터를 사용했다. 입력 특성은 `length`와 `height` 두 가지다.

### 2. 데이터 시각화

```python
plt.scatter(dach_length, dach_height, color='red', label='Dachshund')
plt.scatter(samo_length, samo_height, color='blue', marker='^', label='Samoyed')
plt.scatter([79], [35], color='cyan', marker='p')
plt.show()
```

빨간 점은 닥스훈트, 파란 삼각형은 사모예드, 하늘색 점은 분류하려는 알 수 없는 강아지를 의미한다.

### 3. 입력 데이터와 정답 데이터 만들기

```python
dach_data = np.column_stack((dach_length, dach_height))
samo_data = np.column_stack((samo_length, samo_height))
```

`np.column_stack()`은 길이와 높이를 한 행의 특성으로 묶어 2차원 데이터로 만든다.

```python
dach_target = [0] * 8
samo_target = [1] * 8

dogs = np.concatenate((dach_data, samo_data))
labels = np.concatenate((dach_target, samo_target))
```

닥스훈트는 `0`, 사모예드는 `1`로 라벨링했다. 최종 입력 데이터 `dogs`는 `(16, 2)` 형태이고, 정답 데이터 `labels`는 `(16,)` 형태다.

### 4. KNN 모델 학습과 예측

```python
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(3)
knn.fit(dogs, labels)

unknown_dog = [[79, 35]]
print(knn.predict(unknown_dog))
```

실습 결과 예측값은 `[0]`이었다. 따라서 길이 79, 높이 35인 알 수 없는 강아지는 닥스훈트로 분류되었다.

### 5. 평균과 가상 데이터 생성

각 품종의 길이와 높이 평균을 구한 뒤, 정규분포 난수를 이용하여 더 많은 가상 데이터를 만들었다.

```python
new_dach_length = np.random.normal(loc=78.25, scale=5.0, size=(200,))
new_dach_height = np.random.normal(loc=25.875, scale=5.0, size=(200,))

new_samo_length = np.random.normal(loc=82.125, scale=5.0, size=(200,))
new_samo_height = np.random.normal(loc=54.875, scale=5.0, size=(200,))
```

평균값은 다음과 같다.

- 닥스훈트 길이 평균: `78.25`
- 닥스훈트 높이 평균: `25.875`
- 사모예드 길이 평균: `82.125`
- 사모예드 높이 평균: `54.875`

`np.random.normal()`은 평균(`loc`)과 표준편차(`scale`)를 기준으로 정규분포 데이터를 생성한다. 여기서는 각 특성마다 200개씩 가상 데이터를 만들었다.

### 6. 가상 데이터 결합

```python
new_dach_data = np.column_stack((new_dach_length, new_dach_height))
new_samo_data = np.column_stack((new_samo_length, new_samo_height))
```

생성된 가상 데이터는 각각 `(200, 2)` 형태다. 이 데이터도 기존 데이터와 마찬가지로 KNN 모델 학습이나 시각화에 사용할 수 있다.

## KNN 분류 실습 정리

`ex_04.ipynb`와 `project_01.ipynb`는 모두 KNN 분류 알고리즘을 사용한다. `ex_04.ipynb`는 scikit-learn에서 제공하는 표준 Iris 데이터셋을 사용했고, `project_01.ipynb`는 직접 만든 강아지 길이와 높이 데이터를 사용했다.

KNN 실습에서 중요한 점은 다음과 같다.

1. KNN은 가까운 데이터의 정답을 참고하여 새 데이터를 분류한다.
2. `n_neighbors`는 참고할 이웃의 개수를 의미한다.
3. 입력 데이터 `X`는 2차원 배열, 정답 데이터 `y`는 1차원 배열로 준비한다.
4. 분류 문제에서는 `accuracy_score()`로 예측 정확도를 확인할 수 있다.
5. `confusion_matrix()`를 사용하면 어떤 클래스를 맞히고 틀렸는지 자세히 볼 수 있다.
6. 직접 만든 데이터도 `numpy`로 형태를 맞추면 scikit-learn 모델에 사용할 수 있다.

--------------------------------------------------------------------------------------------------

## 2026 - 06 - 26

# ex_05.ipynb: digits 손글씨 숫자 KNN 분류

`ex_05.ipynb`에서는 scikit-learn의 `digits` 데이터셋을 이용해 손글씨 숫자를 분류한다. `digits`는 0부터 9까지의 숫자 이미지 데이터이며, 각 이미지는 8x8 픽셀로 구성된다.

### 핵심 흐름

```python
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

digits = datasets.load_digits()

data = digits.data
target = digits.target

x_train, x_test, y_train, y_test = train_test_split(
    data,
    target,
    train_size=0.8
)

knn = KNeighborsClassifier()
knn.fit(x_train, y_train)

y_predict = knn.predict(x_test)
score = accuracy_score(y_test, y_predict)
print(score)
```

실습 결과 `data.shape`은 `(1797, 64)`, `target.shape`은 `(1797,)`였다. 8x8 이미지를 64개의 숫자 특성으로 펼쳐 KNN 모델에 넣는다.

정확도 결과:

```text
0.9861111111111112
```

`classification_report()`를 사용하면 전체 정확도뿐 아니라 숫자별 `precision`, `recall`, `f1-score`도 확인할 수 있다.

## ex_06.ipynb: 퍼셉트론과 MLP 기초

`ex_06.ipynb`에서는 퍼셉트론을 직접 구현하고, scikit-learn의 `Perceptron`과 Keras의 `Sequential` 모델을 이용해 간단한 논리 연산을 학습한다.

### 직접 구현한 퍼셉트론

```python
import numpy as np

epsilon = 0.0000001

def step_func(t):
    if t > epsilon:
        return 1
    else:
        return 0

X = np.array([
    [0, 0, 1],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
])

y = np.array([0, 0, 0, 1])
W = np.zeros(len(X[0]))
```

`X`의 마지막 값 `1`은 bias 역할을 한다. `y = [0, 0, 0, 1]`은 AND 연산의 정답이다.

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

퍼셉트론은 예측값과 정답의 차이인 `error`를 이용해 가중치 `W`를 수정한다. 실습 결과 AND 연산은 다음처럼 학습되었다.

```text
0 0 -> 0
0 1 -> 0
1 0 -> 0
1 1 -> 1
```

### scikit-learn Perceptron

```python
from sklearn.linear_model import Perceptron

X = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [0, 0, 0, 1]

clf = Perceptron(tol=1e-3, random_state=0)
clf.fit(X, y)

print(clf.predict(X))
```

직접 구현하지 않아도 `Perceptron` 클래스를 이용하면 같은 방식의 선형 분류 모델을 학습할 수 있다.

### Keras MLP 모델

```python
import tensorflow as tf
import keras

mlp = tf.keras.models.Sequential()

input_layer = keras.layers.Input(shape=(2,))
dense1 = keras.layers.Dense(32, activation='sigmoid')
dense2 = keras.layers.Dense(1, activation='sigmoid')

mlp.add(input_layer)
mlp.add(dense1)
mlp.add(dense2)

mlp.compile(loss='mse', optimizer='adam')
mlp.fit(X, y, epochs=2000)
print(mlp.predict(X))
```

Keras 모델은 `compile()`로 손실 함수와 최적화 방법을 정하고, `fit()`으로 학습한다. 은닉층을 추가한 MLP는 단층 퍼셉트론보다 복잡한 패턴을 학습할 수 있다.

## ex_07.ipynb: TensorFlow/Keras MNIST 손글씨 숫자 분류

`ex_07.ipynb`에서는 TensorFlow/Keras를 이용해 MNIST 손글씨 숫자 데이터셋을 학습한다. MNIST는 28x28 크기의 손글씨 숫자 이미지 데이터셋이다.

### 데이터와 모델

```python
import tensorflow as tf

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Input(shape=(28*28,)))
model.add(tf.keras.layers.Dense(units=512, activation='relu', name='Hidden1'))
model.add(tf.keras.layers.Dense(units=256, activation='relu', name='Hidden2'))
model.add(tf.keras.layers.Dense(units=10, activation='softmax', name='OutjuptLayer'))
```

데이터 형태는 다음과 같다.

```text
x_train: (60000, 28, 28)
y_train: (60000,)
x_test:  (10000, 28, 28)
y_test:  (10000,)
```

주의할 점은 `Input`의 위치다.

```python
tf.keras.models.Input(...)
```

위 코드는 오류가 난다. 다음처럼 사용해야 한다.

```python
tf.keras.layers.Input(shape=(28*28,))
```

또는:

```python
tf.keras.Input(shape=(28*28,))
```

### 이미지 전처리

```python
x_images = x_train.reshape((60000, 28*28))
x_images_norm = (x_images / 255).astype('float32')

x_images_test = x_test.reshape(10000, 28*28)
x_images_test_norm = (x_images_test / 255).astype('float32')
```

Dense 모델에 넣기 위해 28x28 이미지를 784개의 1차원 배열로 펼친다. 픽셀값은 0부터 255 사이이므로 255로 나누어 0부터 1 사이로 정규화한다.

### 학습, 저장, 평가

```python
model.compile(
    loss='sparse_categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

model.fit(x_images_norm, y_train, epochs=20)
model.save("MNIST_20260626_15-35.keras")
model.evaluate(x_images_test_norm, y_test)
```

실습 결과:

```text
loss: 0.1753
accuracy: 0.9802
```

테스트 데이터 기준 약 98.0% 정확도를 보였다.

### 직접 만든 이미지 예측

```python
import cv2

img = cv2.imread("digit.png.png", cv2.IMREAD_GRAYSCALE)
resize_img = cv2.resize(img, (28, 28))
resize_img = resize_img.astype('float32')

inverse_img = 255 - resize_img
inverse_img_norm = inverse_img / 255.0

result = model.predict(inverse_img_norm.reshape(1, 784))
print(result.argmax())
```

직접 만든 이미지는 MNIST와 같은 입력 형태로 맞춰야 한다. 흑백으로 읽고, 28x28로 줄이고, 색을 반전한 뒤, 0부터 1 사이로 정규화하고, `(1, 784)` 형태로 바꿔 예측한다.

실습 결과 `digit.png.png` 이미지는 숫자 `4`로 예측되었다.

## 신경망 실습 정리

1. 퍼셉트론은 입력값과 가중치의 내적 결과를 활성화 함수에 넣어 출력을 만든다.
2. 오차가 발생하면 학습률에 따라 가중치를 수정한다.
3. 단층 퍼셉트론은 선형 분리 가능한 문제에 적합하다.
4. 은닉층을 추가한 MLP는 더 복잡한 패턴을 학습할 수 있다.
5. Dense 모델에 이미지를 넣으려면 2차원 이미지를 1차원 배열로 펼친다.
6. 이미지 픽셀값은 0부터 1 사이로 정규화하면 학습이 안정적이다.
7. 다중 클래스 분류에서는 출력층에 `softmax`, 손실 함수에 `sparse_categorical_crossentropy`를 사용할 수 있다.
8. 학습한 모델은 `.keras` 파일로 저장하고 나중에 다시 불러와 예측에 사용할 수 있다.
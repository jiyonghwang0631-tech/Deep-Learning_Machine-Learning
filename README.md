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

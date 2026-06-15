# NumPy 학습 정리

> 학습일: 2026-06-15

Python의 수치 계산 라이브러리인 **NumPy**의 기본 개념과 배열 연산을
정리한 학습 기록입니다.

## 주요 학습 내용

- Python 리스트와 `ndarray`의 차이
- 배열 생성: `array()`, `zeros()`, `ones()`, `full()`, `eye()`
- 배열 정보 확인: `shape`, `ndim`, `dtype`, `size`
- 데이터 생성: `arange()`, `linspace()`, `logspace()`
- 배열 사칙연산과 브로드캐스팅

## 시작하기

```bash
pip install numpy
```

## 간단한 예시

```python
import numpy as np

# 2차원 배열 생성 및 정보 확인
data = np.array([[1, 2, 3], [4, 5, 6]])
print(data.shape)  # (2, 3)
print(data.ndim)   # 2
print(data.dtype)  # 정수 자료형

# 배열 연산과 브로드캐스팅
print(data * 2)
print(data + np.array([10, 20, 30]))

# 0부터 1까지 동일한 간격의 값 5개 생성
print(np.linspace(0, 1, 5))
```

## 학습 목표

NumPy 배열과 벡터 연산을 익혀 Pandas, OpenCV, 머신러닝 및 딥러닝에서
사용하는 데이터 처리의 기초를 다지는 것이 목표입니다.

# 포트폴리오

## 프로젝트명

KNN을 이용한 강아지 품종 분류 모델 구현

## 프로젝트 기간

2026.06

## 개발 환경 및 사용 기술

- 개발 언어: Python
- 주요 라이브러리: NumPy, Matplotlib, scikit-learn
- 개발 도구: Jupyter Notebook
- 사용 알고리즘: K-Nearest Neighbors, KNN

## 프로젝트 개요

본 프로젝트는 닥스훈트와 사모예드의 몸길이와 몸높이 데이터를 이용하여 강아지 품종을 분류하는 머신러닝 모델을 구현한 프로젝트이다.  
기본 데이터셋을 구성한 뒤, NumPy의 정규분포 난수 생성을 활용하여 추가 학습 데이터를 생성하고, KNN 분류 모델을 통해 새로운 강아지 데이터가 어느 품종에 가까운지 예측하도록 구현하였다.

## 개발 내용

먼저 닥스훈트와 사모예드의 길이, 높이 데이터를 각각 준비하였다. 각 품종의 데이터는 `np.column_stack()`을 이용하여 `[길이, 높이]` 형태의 2차원 배열로 변환하였다.

닥스훈트는 `0`, 사모예드는 `1`로 라벨링하여 지도학습이 가능하도록 구성하였다. 이후 `np.concatenate()`를 사용하여 두 품종의 데이터를 하나의 데이터셋으로 결합하였다.

초기 단계에서는 원본 데이터 16개를 이용하여 KNN 모델을 학습시키고, 길이 79, 높이 35인 강아지 데이터를 입력하여 품종 예측을 수행하였다.

추가적으로 각 품종의 길이와 높이 평균값을 기준으로 `np.random.normal()`을 사용하여 닥스훈트 200개, 사모예드 200개의 가상 데이터를 생성하였다. 생성된 총 400개의 데이터를 학습용 데이터와 테스트용 데이터로 나누고, KNN 모델의 분류 성능을 확인하였다.

## 주요 코드 흐름

```python
new_dach_data = np.column_stack((new_dach_length, new_dach_height))
new_samo_data = np.column_stack((new_samo_length, new_samo_height))

new_dach_target = np.zeros(200)
new_samo_target = np.ones(200)

all_dogs_data = np.concatenate((new_dach_data, new_samo_data))
all_dogs_target = np.concatenate((new_dach_target, new_samo_target))
```

위 코드는 새로 생성한 닥스훈트 데이터와 사모예드 데이터를 합쳐 총 400개의 데이터셋을 구성하는 부분이다. 닥스훈트 라벨은 `0`, 사모예드 라벨은 `1`로 지정하였다.

```python
all_data, new_data, all_target, new_target = train_test_split(
    all_dogs_data,
    all_dogs_target,
    test_size=0.2,
    random_state=42
)
```

전체 데이터 400개를 학습용 데이터 320개와 테스트용 데이터 80개로 분리하였다.

```python
knn_train = KNeighborsClassifier(3)
knn_train.fit(all_data, all_target)
```

KNN 모델은 가까운 이웃 3개의 데이터를 기준으로 품종을 분류하도록 설정하였다.

## 구현 결과

총 400개의 데이터를 기준으로 학습 데이터와 테스트 데이터를 분리한 결과는 다음과 같다.

```text
all_dogs_data.shape   -> (400, 2)
all_dogs_target.shape -> (400,)
all_data.shape        -> (320, 2)
new_data.shape        -> (80, 2)
```

모델 학습 후 테스트 데이터에 대한 예측을 수행하였고, `accuracy_score()`를 이용하여 정확도를 확인하였다.

```text
테스트 데이터 정확도: 0.9875
학습 데이터 score: 실행 시 생성되는 난수 데이터에 따라 변동
테스트 데이터 score: 실행 시 생성되는 난수 데이터에 따라 변동
```

그래프에서는 학습용 데이터와 테스트용 데이터를 품종별로 구분하여 시각화하였다.

```python
plt.scatter(all_data[all_target == 0, 0], all_data[all_target == 0, 1], label='All Dachshund')
plt.scatter(all_data[all_target == 1, 0], all_data[all_target == 1, 1], label='All Samoyed')

plt.scatter(new_data[new_target == 0, 0], new_data[new_target == 0, 1], label='New Dachshund')
plt.scatter(new_data[new_target == 1, 0], new_data[new_target == 1, 1], label='New Samoyed')
```

이를 통해 닥스훈트와 사모예드의 데이터 분포가 길이와 높이를 기준으로 구분되는 것을 확인할 수 있었다.

## 결과 및 느낀 점

이번 프로젝트를 통해 머신러닝 분류 문제에서 입력 데이터와 정답 라벨을 구성하는 방법을 학습하였다. 또한 `train_test_split()`을 활용하여 학습 데이터와 테스트 데이터를 분리하고, 모델이 학습하지 않은 데이터에 대해 어느 정도 정확하게 예측하는지 확인할 수 있었다.

KNN 알고리즘은 복잡한 수식 없이 가까운 데이터의 분포를 기준으로 분류를 수행하기 때문에, 머신러닝의 기본적인 분류 흐름을 이해하는 데 적합하였다. 특히 데이터의 형태가 `(샘플 수, 특성 수)` 구조로 맞춰져야 한다는 점과, 입력 데이터와 라벨의 개수가 반드시 일치해야 한다는 점을 실습을 통해 확인하였다.

## 활용 방안 및 추후 개발 방향

현재 프로젝트는 길이와 높이 두 가지 특성만을 사용하여 품종을 분류하지만, 추후에는 몸무게, 귀 길이, 다리 길이 등 더 다양한 특성을 추가하여 분류 성능을 높일 수 있다.

또한 실제 이미지 데이터를 활용하여 CNN 기반의 강아지 품종 분류 모델로 확장할 수 있으며, 웹 또는 GUI 프로그램과 연동하여 사용자가 입력한 강아지 정보를 바탕으로 품종을 예측하는 응용 프로그램으로 발전시킬 수 있다.

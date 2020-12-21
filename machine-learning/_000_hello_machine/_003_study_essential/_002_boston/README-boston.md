# Predict price of boston housing

    2020-12-28


## 과제 내용 

### 1. 데이터 이해

```python
from tensorflow.keras.datasets import boston_housing

(x_train, y_train), (x_test, y_test) = boston_housing.load_data()

# 컬럼 의미 파악하기
# ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']


# x와 y의 관계 생각하기
```

### 2. description model build

```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models

# 1. models
# 2. layers
# 3. compile **args

```

### 3. train model description

```python
# model.fit

```

## 학습 목록

- 반복 학습으로 머신러닝을 구현
- 손실함수인 mse 활용
- Sequential model
- multi layer perceptron
- sns library
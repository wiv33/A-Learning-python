# Predict price of boston housing

    2020-12-28

## Reference

    모두의 딥러닝

## initialize code

```python
import tensorflow as tf
from tensorflow.keras import models, layers, losses
from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/wiv33/A-Learning-python/master/machine-learning/_000_hello_machine/_003_study_essential/_003_wine/data/wine.csv")

x_train, x_test, y_train, y_test = train_test_split(df.iloc[:, :-1], df.iloc[:, -1])

# ... 딥러닝 구현 
# layers
# models

# build model

# train model
```

## 학습 목록

- layers 추가
    - BatchNormalization()
        * 미니 배치마다 normalize 한다는 것의 의미

    - Dropout(rate=)
        * node(units)의 연산을 막는

- compile args 확인하기
    * loss function
        1. losses.mean_squared_error
        2. losses.categorical_crossentropy
        3. losses.binary_crossentropy

- layer 여러 층으로 생성하여 accuracy 성능을 확인하기
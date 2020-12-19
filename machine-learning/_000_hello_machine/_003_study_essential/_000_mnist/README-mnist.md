# MNIST 손글씨 데이터

    2020-12-21


## 과제 내용 - 데이터 이해해오기

```python
from tensorflow.keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
```

## 학습 목록

- 고수준 API keras 활용
- dataset shape 접하기
- accuracy 검증 시각화
- 단층 / 다층 layer 구현
- Pycharm 활용 맛보기
- numpy 기초 다루기
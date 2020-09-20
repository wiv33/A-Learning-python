import numpy as np
from keras.datasets import mnist

# 예시
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
train_images = train_images.reshape((60000, 28 * 28))

"""
reshape
"""
# implement
x = np.array([[0., 1.],
              [2., 3.],
              [4., 5.]])

print(x.shape)

assert 6 % x.shape[0] == 0
x = x.reshape((6, 1))
print(x)

assert x.shape[0] == 2 * 3
x = x.reshape((2, 3))
print(x)

"""
크기 변환은 전치(transposition)라고 한다.
행렬의 전치는
행과 열을 바꾸는 것
x.transpose(x)
x[i, :] => x[:, i]
"""

x = np.zeros((300, 20))
x = np.transpose(x)
print(x.shape)

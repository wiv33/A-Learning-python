""" 경사하강법
임의의 선을 긋고 오차를 줄여나간다.
미분과 편미분
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = [[2, 81], [4, 93], [6, 91], [8, 97]]

x = [i[0] for i in data]
y = [i[1] for i in data]

# 그래프
plt.figure(figsize=(8, 5))
plt.scatter(x, y)
plt.show()

# 리스트로 되어 있는 x와 y 값을 numpy 배열로 바꾸기
x_data = np.array(x)
y_data = np.array(y)

# 기울기 a와 절편 b의 초기화
a, b = 0, 0

# learning rate
lr = 0.05

epochs = 2001

for i in range(epochs):
    y_pred = a * x_data + b  # ax + b
    error = y_data - y_pred  # 오차 구하기

    # 오차 함수를 a로 미분한 값
    a_diff = -(1 / len(x_data)) * sum(x_data * error)

    # 오차 함수를 b로 미분한 값
    b_diff = -(1 / len(x_data)) * sum(y_data - y_pred)

    # 학습률을 곱하여 해당 값 업데이트
    a = a - lr * a_diff
    b = b - lr * b_diff

    if i % 10 == 0:
        print('epoch = %.f, 기울기 = %.04f, 절편 = %.04f' % (i, a, b))


# 앞서 구한 기울기와 절편을 이용해 그래프를 다시 그리기

y_pred = a * x_data + b
plt.scatter(x, y)
plt.plot([min(x_data), max(x_data)], [min(y_pred), max(y_pred)])
plt.show()


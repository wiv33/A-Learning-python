import numpy as np
import matplotlib.pyplot as plt

"""이번 코드로 가로축 수치가 작아진다.
"""


# 학습 데이터 읽기
train = np.loadtxt('./data/click.csv', delimiter=",", skiprows=1)

train_x = train[:,0]
train_y = train[:,1]

theta0 = np.random.rand()
theta1 = np.random.rand()

# 예측함수
def f(x):
    return theta0 + theta1 * x

# 목적함수
def E(x, y):
    return 0.5 * np.sum((y - f(x))**2)

# 표준화
mu = train_x.mean() # 평균
sigma = train_x.std()


def standardize(x):
    return (x - mu) / sigma

train_z = standardize(train_x)

# 점 그래프를 그린다
plt.plot(train_z, train_y, 'o')
plt.show()
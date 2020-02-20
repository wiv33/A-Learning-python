import numpy as np
import matplotlib.pyplot as plt

train = np.loadtxt('./data/click.csv', delimiter=",", skiprows=1)

train_x = train[:,0]
train_y = train[:,1]

# 목적함수
def E(x, y):
    return 0.5 * np.sum((y - f(x))**2)

# 표준화
mu = train_x.mean() # 평균
sigma = train_x.std()

def standardize(x):
    return (x - mu) / sigma

train_z = standardize(train_x)

# 매개변수 초기화
theta = np.random.rand(3)

# 학습 데이터를 행렬의 형태로 만든다
def to_matrix(x):
    return np.vstack([np.ones(x.shape[0]), x, x**2]).T

X = to_matrix(train_z)

# 예측함수
def f(x):
    return np.dot(x, theta)

# 학습률
ETA = 1e-3 # 10^-3

#오차의 차분
diff = 1

# 학습을 반복한다.
error = E(X, train_x)

while diff > 1e-2:
    # 매개변수를 갱신한다.
    theta = theta - ETA * np.dot(f(X) - train_y, X)
    # 이전의 오차와의 차분을 계산
    current_error = E(X, train_y)
    diff = error - current_error
    error = current_error

x = np.linspace(-3, 3, 100)

plt.plot(train_z, train_y, 'o')
plt.plot(x, f(to_matrix(x)))
plt.show()
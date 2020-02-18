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


# 학습률
ETA = 1e-3 # 10^-3

# 오차의 차분
diff = 1

# 갱신 횟수
count = 0

# 학습을 반복
error = E(train_z, train_y)

while diff > 1e-3:
    # 갱신 결과를 저장
    tmp0 = theta0 - ETA * np.sum((f(train_z) - train_y))
    tmp1 = theta1 - ETA * np.sum((f(train_z) - train_y) * train_z)

    # 매개변수 저장
    theta0 = tmp0
    theta1 = tmp1

    #이전 loop 오차와의 차분을 계산한다
    current_error = E(train_z, train_y)
    diff = error - current_error
    error = current_error

    # 로그를 출력
    count += 1
    log = '{}회째: theta0 = {:.3f}, theta1 = {:.3f}, 차분={:.4f}'
    print(log.format(count, theta0, theta1, diff))




# 그래프를 그린다

x = np.linspace(-3, 3, 100) # line
plt.plot(train_z, train_y, 'o')
plt.plot(x, f(x))
plt.show()
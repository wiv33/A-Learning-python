import matplotlib.pylab as plt
import numpy as np


def step_function(x):
    return np.array(x > 0, dtype=np.int)


# -5부터 4.9까지 0.1 간격으로 배열을 생성한다.
x = np.arange(-5.0, 5.0, .1)
y = step_function(x)

plt.plot(x, y)
plt.ylim(-.1, 1.1)  # y 범위 지정
plt.show()

# 0이 초과되는 시점부터 1을 반환하여 출력이 '계단처럼' 생겨서 `계단함수`이다.

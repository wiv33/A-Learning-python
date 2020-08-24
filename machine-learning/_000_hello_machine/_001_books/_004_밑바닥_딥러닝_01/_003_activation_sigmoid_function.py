import matplotlib.pylab as plt
import numpy as np


def sigmoid(x):
    exp = np.exp(-x)
    print("exp = {0}\n\t= {0} + 1 \n\t= {1}".format(exp, (1 + exp)))
    return 1 / (1 + exp)


x = np.array([-1., 1., 2.])
print(sigmoid(x))

x = np.arange(-5., 5., 0.1)
y = sigmoid(x)

plt.plot(x, y)
plt.ylim(-.1, 1.1)  # Y축 지정
plt.show()

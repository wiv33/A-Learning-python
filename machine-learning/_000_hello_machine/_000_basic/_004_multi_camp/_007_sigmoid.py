import numpy as np

import matplotlib.pyplot as plt


def sigmoid(input):
    return 1.0 / (1 + np.exp(-input))


z = np.linspace(-8, 8, 1000)

y = sigmoid(z)

plt.plot(z, y)
plt.axhline(y=0, ls='dotted', color='k')
plt.axhline(y=0.5, ls='dotted', color='k')
plt.axhline(y=1, ls='dotted', color='k')
plt.yticks(np.arange(0, 1, step=0.25))
plt.xlabel('z')
plt.ylabel("y(z)")
plt.show()


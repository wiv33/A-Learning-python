"""
미분
"""
import matplotlib.pylab as plt
import numpy as np


def numerical_diff(f, x):
    h = 10e-10
    return (f(x + h) - f(x)) / h


def numerical_diff_2(f, x):
    h = 10e-4
    return (f(x + h) - f(x - h)) / (2 * h)


def function_1(x):
    """수치 미분의 예"""
    return .01 * x ** 2 + .1 * x


x = np.arange(.0, 20.0, .01)
y = function_1(x)

plt.xlabel('x')
plt.ylabel("f(x)")
plt.plot(x, y)
plt.show()

# numerical_diff(function_1, 5)
# 0.20001000000013924
# numerical_diff(function_1, 10)
# 0.30001000000012823


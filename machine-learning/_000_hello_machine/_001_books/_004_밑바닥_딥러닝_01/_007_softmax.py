import numpy as np


def softmax(a):
    exp_a = np.exp(a)
    print("1", exp_a)
    sum_exp_a = np.sum(exp_a)
    print("2", sum_exp_a)
    y = exp_a / sum_exp_a
    print("3", y)
    return y


a = np.array([.3, 2.9, 4.])
res = softmax(a)
assert sum(res) == 1.0

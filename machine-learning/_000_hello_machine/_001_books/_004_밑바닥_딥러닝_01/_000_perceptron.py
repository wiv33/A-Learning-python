import numpy as np


def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7

    tmp = x1 * w1 + x2 * w2
    print("tmp = {}, theta = {}".format(tmp, theta))

    if tmp <= theta:
        return 0
    else:
        return 1


print(AND(1, 1))
print(AND(0, 1))
print("=================+")


def AND2(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


print(AND2(0, 1))
print(AND2(1, 1))
print("==================================================")


def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7

    tmp = np.sum(x * w) + b

    if tmp <= 0:
        return 0
    else:
        return 1


print(NAND(1, 1))  # 0
print(NAND(0, 1))  # 1

print("=-================")


def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2

    temp = np.sum(x * w) + b

    if temp <= 0:
        return 0
    else:
        return 1


print(OR(0, 1))  # 1 : temp = 0.3
print(OR(1, 1))  # 1 : temp = 0.8
print(OR(0, 0))  # 0 : temp = -0.2

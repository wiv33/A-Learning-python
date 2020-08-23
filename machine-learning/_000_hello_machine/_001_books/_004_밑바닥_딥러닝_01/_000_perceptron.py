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

print("======================")


def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y


print(XOR(0, 0))  # 0
print(XOR(1, 0))  # 1
print(XOR(1, 1))  # 0


# 퍼셉트론은 입출력을 갖춘 알고리즘이다. 입력을 주면 정해진 규칙 에따른 값을 출력한다.
# 퍼셉트론에서는 '가중치'와 '편향'을 매개변수로 설정한다.
# 퍼셉트론으로 AND, OR 게이트 등의 논리 회로를 표현할 수 있다.
# XOR 게이트는 단충 퍼셉트론으로는 표현할 수 없다.
# 2층 퍼셉트론을 이용하면 XOR 게이트를 표현할 수 있다.
# 단층 퍼셉트론은 직선형 영역만 표현할 수 있고, 다층 퍼셉트론은 비선형 영역도 표현할 수 있다.
# 다층 퍼셉트론은 (이론상) 컴퓨터를 표현할 수 있다.

"""
Rectified Linear Unit
    0을 넘으면 그 입력을 그대로 출력하고,
    0이하면 0을 출력한다.
"""
import numpy as np


def relu(x):
    return np.maximum(0, x)


print(relu(2))  # 2
print(relu(-1))  # 0

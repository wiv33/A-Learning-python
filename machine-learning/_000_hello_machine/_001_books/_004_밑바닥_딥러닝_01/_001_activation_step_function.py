# def step_function(x):
#     return 1 if x > 0 else 0
#
import numpy as np


def step_function(x):
    y = x > 0
    return y.astype(np.int)


# print(step_function(np.array([0, 1])))


# exam
x = np.array([-1.0, 1.0, 2.0])
print(x)
#  1. [-1.  1.  2.]

y = x > 0
print(y)
#  2. [False  True  True]

result = y.astype(np.int)
print(result)
#  3. [0 1 1]

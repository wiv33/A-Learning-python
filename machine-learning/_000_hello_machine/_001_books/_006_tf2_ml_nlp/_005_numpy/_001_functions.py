import numpy as np

a = np.zeros((2, 3))
print(a)
# [[0. 0. 0.]
#  [0. 0. 0.]]

ones = np.ones((2, 1))
print(ones)
# [[1.]
#  [1.]]

c = np.empty((2, 2))
print(c)
# [[2.39345636e-316 0.00000000e+000]
#  [0.00000000e+000 0.00000000e+000]]

d = np.arange(10, 30, 5)
print(d)
# [10 15 20 25]

e = np.full((2, 2), 4.)
print(e)
# [[4. 4.]
#  [4. 4.]]

f = np.eye(3)
print(f)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

g = np.random.random((2, 2))
print(g)
# [[0.25704602 0.9994835 ]
#  [0.41104405 0.32230873]]

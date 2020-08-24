import numpy as np

X = np.array([1, 2])
assert X.shape == (2,)

W = np.array([[1, 3, 5], [2, 4, 6]])
assert W.shape == (2, 3)

Y = np.dot(X, W)
assert Y.shape == (3,)

# ====================================================

X = np.array([1.0, .5])
W1 = np.array([[.1, .3, .5], [.2, .4, .6]])
B1 = np.array([.1, .2, .3])

assert X.shape == (2,)
assert W1.shape == (2, 3)
assert B1.shape == (3,)

dot = np.dot(X, W1)
assert np.array_equal(dot, [.2, .5, .8])

A1 = dot + B1
assert np.array_equal(A1, [.30000000000000004, .7, 1.1])

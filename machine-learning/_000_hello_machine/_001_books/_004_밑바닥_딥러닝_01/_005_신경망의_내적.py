import numpy as np

X = np.array([1, 2])
assert X.shape == (2,)

W = np.array([[1, 3, 5], [2, 4, 6]])
assert W.shape == (2, 3)

Y = np.dot(X, W)
assert Y.shape == (3,)

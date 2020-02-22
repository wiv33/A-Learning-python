import numpy as np

v = np.array([1, 2, 3])  # v의 shape는 (3,)
w = np.array([4, 5])  # x의 shape (2,)
x = np.array([[1, 2, 3], [4, 5, 6]])

x + v
# result
# array([[2, 4, 6],
#        [5, 7, 9]])

x + w
# result: error

x.T + w
# result
# array([[ 5,  9],
#        [ 6, 10],
#        [ 7, 11]])

(x.T + w).T
# result
# array([[ 5,  6,  7],
#        [ 9, 10, 11]])

####
x + np.reshape(w, (2, 1))
# result
# array([[ 5,  6,  7],
#        [ 9, 10, 11]])
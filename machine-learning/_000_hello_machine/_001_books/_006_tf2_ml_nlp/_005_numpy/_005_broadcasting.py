import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([1, 0, 1])
y = np.empty_like(a)

for i in range(3):
    y[i, :] = a[i, :] + b

# print(y)
# [[ 2  2  4]
#  [ 5  5  7]
#  [ 8  8 10]]

c = a + b
print(c)
# [[ 2  2  4]
#  [ 5  5  7]
#  [ 8  8 10]]
import numpy as np


def clear():
    print('\n' * 100)


a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print(a + b)
print(np.add(a, b))
# [11 22 33]


print(b - a)
print(np.subtract(b, a))
# [ 9 18 27]


print(a ** 2)
# [1 4 9]

print(b < 15)
# [ True False False]

print(b[b < 15])
# [10]

clear()

C = np.array([[1, 2], [3, 4]])
D = np.array([[10, 20], [30, 40]])

print(C * D)
# [[ 10  40]
#  [ 90 160]]

print(np.dot(C, D))  # 내적 (dot product) 계산
print(C.dot(D))
# [[ 70 100]
#  [150 220]]

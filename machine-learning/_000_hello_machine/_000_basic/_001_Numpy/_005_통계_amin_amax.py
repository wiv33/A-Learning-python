import numpy as np

# 배열의 미니멈 값을 축을 따라 반환
A = np.array([[1,2,3], [6,5,4], [7,9,8]])

amin = np.amin(A, axis=0)
# print(amin)
# [1 2 3]

amin = np.amin(A, axis=1)
# print(amin)
# [1 4 7]


print(np.amax(A, axis=0))
# [7 9 8]

print(np.amax(A, axis=1))
# [3 6 9]
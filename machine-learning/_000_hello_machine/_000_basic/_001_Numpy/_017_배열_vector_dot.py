import numpy as np

"""dot의 경우
앞 배열과 뒤 배열의 행의 크기가 일치해야 한다.
벡터 간 크기가 일치

"""
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])

v = np.array([9, 10])
w = np.array([11, 12])

# 벡터의 내적:
# 둘 다 벡터가 들어오면 내적
v.dot(w)
np.dot(v, w)

# 행렬과 벡터의 곱
# dimension 1인 배열 [29 67]
x.dot(v)
np.dot(x, v)

# 행렬 곱
# dimension 2인 배열
x.dot(y)
np.dot(x, y)

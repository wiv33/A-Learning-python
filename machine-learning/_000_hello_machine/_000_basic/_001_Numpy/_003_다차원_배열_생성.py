import numpy as np

# 우와..
# 초기화가 안된 배열
# 행이 2개, 열이 3개
empty = np.empty((2, 3))
# print(empty)

# 형태를 그대로 가져온다.
like = np.empty_like(empty)
# print(like)
# [[2.12199579e-314 0.00000000e+000 0.00000000e+000]
#  [0.00000000e+000 0.00000000e+000 0.00000000e+000]]

# 초기화 한다.
zeros = np.zeros((3, 3))
# print(zeros)
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]

zeros_int = np.zeros((2, 3), dtype=int)
# print(zeros_int)
# [[0 0 0]
#  [0 0 0]]

# 구조 그대로, 0 초기화
zeros_like = np.zeros_like(zeros_int)
# print(zeros_like)
# [[0 0 0]
#  [0 0 0]]

# 1로 초기화
ones = np.ones((3, 3))
# print(ones)
# [[1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]]



# 다차원 안에 이차원 집합
# identity
identity = np.identity(2)
# print(identity)
# [[1. 0.]
#  [0. 1.]]


np_identity = np.identity(3, dtype=int)
# print(np_identity)
# [[1 0 0]
#  [0 1 0]
#  [0 0 1]]


# eye는 identity에 파라미터 몇 개 주지 않으면 ...
np.eye(3)

np.eye(3,4)

np.eye(3, 4, 1)


# 초기화를 10으로 10 * np.ones(2,3)과 동일
np.full((2,3), 10)

arange = np.arange(start=1.0, stop=5, step=1)
# print(arange)
# [1. 2. 3. 4.]

# linear space
# 가운데에 몇개 들어갈 것인지 정해주는 것
linspace = np.linspace(2.0, 3.0, num=10)
print(linspace)
# [2.         2.11111111 2.22222222 2.33333333 2.44444444 2.55555556
#  2.66666667 2.77777778 2.88888889 3.        ]

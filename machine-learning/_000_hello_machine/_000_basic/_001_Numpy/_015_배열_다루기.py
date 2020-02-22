import numpy as np

## x가 10*10*3의 다차원 배열일 때, x의 두 번째 차원이 150인 2차원 배열이 되도록 reshape 하세요.
x = np.ones([10, 10, 3])

np.reshape(x, [2, 150])
np.reshape(x, [2, 150]).shape
# result
# (2, 150)


## x가 [[1,2,3],[4,5,6]]일 때, [1 4 2 5 3 6]으로 변환하세요.
x = np.array([[1, 2, 3], [4, 5, 6]])
np.ravel(x.T)
x.T.flatten()
# result
# array([1, 4, 2, 5, 3, 6])


## x가 [[1,2,3],[4,5,6]]일 때, flatten한 후 다섯 번째 원소를 가져오세요.
x = np.array([[1, 2, 3], [4, 5, 6]])
out = x.flatten()[4]
out
# result
# 5


## x와 y를 연결하여 아래의 배열을 생성
# [[1,2,3,7,8,9],[4,5,6,10,11,12]]
x = np.array([[1,2,3],[4,5,6]])
y = np.array([[7,8,9],[10,11,12]])

np.concatenate((x,y))

## x와 y를 연결해서 아래의 배열을 생성
# [[1,2,3],
# [4,5,6],
# [7,8,9],
# [10,11,12]]

np.concatenate((x,y), axis=0)

# result
# array([[ 1,  2,  3],
#        [ 4,  5,  6],
#        [ 7,  8,  9],
#        [10, 11, 12]])


## x가 [0,1,2]일 때, [0,0,1,1,2,2]를 생성

x = np.array([0,1,2])

"""오답 목록"""
np.concatenate((x,x))
# result: array([0, 1, 2, 0, 1, 2])

np.add(x, x)
# result: array([0, 2, 4])

np.append(x, x)
# result: array([0, 1, 2, 0, 1, 2])
"""오답 목록 끝"""

# 배열의 몇 번을 반복할 것인지
np.repeat(x, 2)

np.array([x[0],x[0],x[1],x[1],x[2],x[2]])

## x가 [0,0,0,1,2,3,0,2,1,0]일 때 앞 뒤의 0을 제거
x = np.array([0,0,0,1,2,3,0,2,1,0])

x[3:9]
# result: array([1, 2, 3, 0, 2, 1])

np.trim_zeros(x)
# result: array([1, 2, 3, 0, 2, 1])
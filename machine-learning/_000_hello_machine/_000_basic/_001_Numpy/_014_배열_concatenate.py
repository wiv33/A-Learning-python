import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
b = np.array([[9, 10, 11, 12]])

""" 자주하는 실수 **
기존 배열의 인덱싱 후 
transpose 하려면 1차원이라 되지 않는다.
"""

# 배열의 형태가 같아야 한다.
# transpose 후 연결할 수 있다.
np.concatenate((a,b), axis=0)
# result :
# all the input array dimensions for the concatenation axis must match exactly,
# but along dimension 1, the array at index 0 has size 2 and the array at index 1 has size 4

np.concatenate((a.T, b), axis=0)
# array([[ 1,  3,  5,  7],
#        [ 2,  4,  6,  8],
#        [ 9, 10, 11, 12]])

np.concatenate((a, b.T), axis=1)
# result
# array([[ 1,  2,  9],
#        [ 3,  4, 10],
#        [ 5,  6, 11],
#        [ 7,  8, 12]])

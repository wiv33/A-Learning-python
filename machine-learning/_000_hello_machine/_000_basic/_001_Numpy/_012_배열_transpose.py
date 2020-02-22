import numpy as np
""" transpose
배열.T 입력하면 된다.
ex) a.T

    *데이터는 그대로며
    _001_에서 stride의 이동의 기준 변경(이동할 byte 크기의 변경)으로
    transpose 한다.
"""
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

a.T
# result
# array([[ 1,  5,  9],
#        [ 2,  6, 10],
#        [ 3,  7, 11],
#        [ 4,  8, 12]])


import numpy as np

a = np.array([[1, 2, 3, 4, ], [5, 6, 7, 8], [9, 10, 11, 12]])

"""다차원 배열 슬라이싱

a[ : , : ]
슬라이싱의
a[행 시작:행 끝, 열 시작: 열 끝]

시작 값은 포함, 끝 값은 미포함

shape
"""

# 행 전체,
# 열 끝은
# 슬라이싱 하지 않는 코드
a_ = a[:, 1:4]
print(a_)

# 위 코드와 같음.
# 생략하면 기본 값으로 열의 끝이다.
ab = a[:,1]
print(ab)

ac = a[:2]

# indexing
a[0, 0]

# 연속되지 않은 행을 가져오는 방법
# 배열을 넣는다.
a[[0,2],0:4]
# result
# array([[ 1,  2,  3,  4],
#        [ 9, 10, 11, 12]])

a[:,[1,3]]
# result
# array([[ 2,  4],
#        [ 6,  8],
#        [10, 12]])

a[:,[0,1,3]]
# result
# array([[ 1,  2,  4],
#        [ 5,  6,  8],
#        [ 9, 10, 12]])

print(a, a.shape, a.ndim)
# result
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]] (3, 4) 2


# =======================================================
#                   행
# =======================================================

# 슬라이싱만 사용할 땐
# ::차원이 유지된다.

a_slicing = a[:1,]
print(a_slicing, a_slicing.shape, a_slicing.ndim)
# result
# [[1 2 3 4]] (1, 4) 2

# 인덱싱&슬라이싱 혼합사용 시
# ::차원이 유지되지 않는다.(1차원으로 됨)

a_indexed_slice = a[0, :]
print(a_indexed_slice, a_indexed_slice.shape, a_indexed_slice.ndim)
# result
# [1 2 3 4] (4,) 1

# =======================================================
#                   열
# =======================================================

slicedCol = a[:, 0:1]
print(slicedCol, slicedCol.shape, slicedCol.ndim)
# result
# [[1]
#  [5]
#  [9]] (3, 1) 2

# 혼합
indexed_col = a[:, 0]
print(indexed_col, indexed_col.shape, indexed_col.ndim)
# result
# [1 5 9] (3,) 1
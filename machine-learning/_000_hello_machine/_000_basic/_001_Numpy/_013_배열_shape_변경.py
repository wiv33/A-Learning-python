import numpy as np

"""차원의 변경
np.arange(6)
# result
[0,1,2,3,4,5]

.reshape((3,2))
# result
array([[0, 1],
       [2, 3],
       [4, 5]])
"""
a = np.arange(6).reshape((3, 2))

np.reshape(a, (2, 3))
# result
# array([[0, 1, 2],
#        [3, 4, 5]])

np.reshape(a, (6, 1))
# result
# array([[0],
#        [1],
#        [2],
#        [3],
#        [4],
#        [5]])

np.reshape(a, (1, 6))
# result
# array([[0, 1, 2, 3, 4, 5]])

np.reshape(a, 6)
# result : 차원이 낮아진다.
# array([0, 1, 2, 3, 4, 5])


# ============================================ ravel ==========================================

np.ravel(a)
# result
# array([0, 1, 2, 3, 4, 5])

a.ravel()
# result
# array([0, 1, 2, 3, 4, 5])


# ===== flatten
# deep copy
np.ndarray.flatten(a)
# result
# array([0, 1, 2, 3, 4, 5])

# 위와 같음
a.flatten()
# a.flatten()
# result
# array([1, 2, 3, 4, 5, 6, 7, 8])



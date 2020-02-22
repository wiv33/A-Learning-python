import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])

bool_a = a > 2
# result
# >>> bool_a
# array([[False, False],
#        [ True,  True],
#        [ True,  True],
#        [ True,  True]])

a[bool_a]
# result
# >>> a[bool_a]
# array([3, 4, 5, 6, 7, 8])

# ===================================================

print(a[a>3], a[a>3].shape, a[a>3].ndim)
# result
# [4 5 6 7 8] (5,) 1


import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6]])

# result :a
# array([[1, 2],
#        [3, 4],
#        [5, 6]])

a[[0,1,2], [0,1,0]]
# result
# array([1, 4, 5])

# 설명: 앞 뒤에 각 좌표 배열을 모아놓은 것.
# a[[x좌표],[y좌표]]

a[[0,1,1],[0,1,1]]
# result
# array([1, 4, 4])
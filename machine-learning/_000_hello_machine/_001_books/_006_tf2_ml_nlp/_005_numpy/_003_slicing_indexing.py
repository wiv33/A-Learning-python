import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7])

# 마지막 원소
print(a[-1])

# 인덱스 2부터 5전까지
print(a[2:5])

print('\n' * 77)

metric = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
# (1, 2) >>> 6
print(metric[1, 2])

# 1열의 모든 원소
print(metric[:, 1])
# [2 5 8]


# 마지막 행
print(metric[-1])
# [7 8 9]



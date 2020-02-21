import numpy as np

A = np.array([[5, 2, 6], [1, 4, 9], [3, 7, 8]])


# 분산
# variance
print(np.var(A, 0))
np.var(A, 1)
# array([ 2.88888889, 10.88888889,  4.66666667])
np.var(A)
# 6.666666666666667

# 표준 편차
# standard deviation

np.std(A, 0) # array([1.63299316, 2.05480467, 1.24721913])
np.std(A, 1) # array([1.69967317, 3.29983165, 2.1602469 ])
np.std(A) #2.581988897471611
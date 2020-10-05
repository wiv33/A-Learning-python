import numpy as np
import pandas as pd

a = pd.Series([1, 2, 3, 4, 5, 6, 13])
print(a)
# 0     1
# 1     2
# 2     3
# 3     4
# 4     5
# 5     6
# 6    13
# dtype: int64

data = np.array(['a', 'b', 'c', 'd', 'f'])
b = pd.Series(data)
print(b)
# 0    a
# 1    b
# 2    c
# 3    d
# 4    f
# dtype: object

c = pd.Series(np.arange(10, 30, 5))
print(c)
# 0    10
# 1    15
# 2    20
# 3    25

"""
인덱스 설정과
딕셔너리를 통한 시리즈 생성
"""

a = pd.Series(['a', 'b', 'c'], index=[10, 20, 30])
print(a)
# 10    a
# 20    b
# 30    c
# dtype: object

my_dict = {'a': 10, 'b': 20, 'c': 30}
b = pd.Series(my_dict)
print(b)
# a    10
# b    20
# c    30
# dtype: int64

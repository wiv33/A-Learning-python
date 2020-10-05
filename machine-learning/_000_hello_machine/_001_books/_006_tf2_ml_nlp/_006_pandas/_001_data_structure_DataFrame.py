import pandas as pd

"""
pd.DataFrame(data, index, columns, dtype, copy)
"""

l = pd.DataFrame([1, 3, 5, 7, 10])
print(l)
#     0
# 0   1
# 1   3
# 2   5
# 3   7
# 4  10

d = {'Name': ['cho', 'kim', 'lee'], 'Age': [28, 31, 38]}
b = pd.DataFrame(d)
print(b)
#   Name  Age
# 0  cho   28
# 1  kim   31
# 2  lee   38


a = pd.DataFrame(data=[['apple', 7000], ['banana', 6000], ['kiwi', 13000]],
                 columns=['name', 'price'])
print(a)
#      name  price
# 0   apple   7000
# 1  banana   6000
# 2    kiwi  13000

print(a.describe())
#               price
# count      3.000000
# mean    8666.666667
# std     3785.938897
# min     6000.000000
# 25%     6500.000000
# 50%     7000.000000
# 75%    10000.000000
# max    13000.000000

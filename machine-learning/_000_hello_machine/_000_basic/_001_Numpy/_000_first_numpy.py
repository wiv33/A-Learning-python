import numpy as np

# Array
mathScoreNDarray = np.array([[11, 12, 13], [21,22,23], [31,32,33]])
# print(mathScoreNDarray)

print(mathScoreNDarray + 1)

sum = np.sum(mathScoreNDarray)
print(sum)

average = np.average(mathScoreNDarray)
print(average)

mean = np.mean(mathScoreNDarray, axis=1)
print(mean)


# mean과 average의 차이
"""산술 평균인 mean
    가중 평균 average
"""

np.mean(range(1, 11))

np.average(range(1,11))

# 가중평균
np_average = np.average(range(1, 11), weights=range(10, 0, -1))
print(np_average)
# 4.0
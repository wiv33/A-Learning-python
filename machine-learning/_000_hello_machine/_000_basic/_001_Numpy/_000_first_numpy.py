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


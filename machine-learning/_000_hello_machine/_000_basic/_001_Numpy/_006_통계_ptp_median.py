import numpy as np

A = np.array([[5, 2, 6], [1, 4, 9], [3, 7, 8]])

# ptp 배열의 최대와 최소 값의 차분
# print(np.ptp(A))  #  위 배열의 최대와 최소의 차이는 7

# print(np.median(A))  # A의 중간 값
# print(np.median(A, axis=0))  # axis=0 중간 값 [3. 4. 8.]

print(np.median(A, axis=1))  # axis=1 중간 값 [5. 4. 7.]

# arithmetic mean
print(np.mean(A, 0))
print(np.mean(A, 1))
print(np.mean(A))

# 가중 평균을 사용하려면 average를 사용해야 한다.

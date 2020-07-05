import numpy as np

x = np.array([2, 4, 6, 8])
y = np.array([81, 93, 91, 97])

x_mean = np.mean(x)
y_mean = np.mean(y)

# 기울기 공식의 분모
divisor = sum([(i - x_mean) ** 2 for i in x])


# 기울기 공식의 분자
# 최소 제곱법
def top(x, mean_x, y, y_mean):
    d = 0
    for i in range(len(x)):
        d += (x[i] - mean_x) * (y[i] - y_mean)
    return d


dividend = top(x, x_mean, y, y_mean)

# 분모 나누기 분자
a = dividend / divisor

#
b = y_mean - (x_mean * a)

print("기울기 a = {}, y 절편 b = {} ".format(a, b))

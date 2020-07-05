import numpy as np

fake_a_b = [3, 76]

data = [[2, 81], [4, 93], [6, 91], [8, 97]]

x = [i[0] for i in data]
y = [i[1] for i in data]


def predict(num):
    """y = ax + b """
    return fake_a_b[0] * num + fake_a_b[1]


def mse(y_hat, param_y):
    return ((y_hat - param_y) ** 2).mean()


def mse_val(predict_result, y):
    return mse(np.array(predict_result), np.array(y))


predict_result = []

# 모든 x 값을 한 번씩 대입
for i in range(len(x)):
    # 그 결과에 해당하는 predict_result
    predict_result.append(predict(x[i]))
    print('공부시간={}, 실제 점수={}, 예측 점수 ={}'.format(x[i], y[i], predict(x[i])))

print("mse 최종 값 : {}".format(mse_val(predict_result, y)))

# result
#
# 공부시간=2, 실제 점수=81, 예측 점수 =82
# 공부시간=4, 실제 점수=93, 예측 점수 =88
# 공부시간=6, 실제 점수=91, 예측 점수 =94
# 공부시간=8, 실제 점수=97, 예측 점수 =100
# mse 최종 값 : 11.0

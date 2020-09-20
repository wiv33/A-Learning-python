"""
output = relu(dot(w * input) + b)
:W
- 가중치 또는 훈련되는 파라미터

1. 초기엔 랜덤 값으로 시작하여 의미없는 수치 생성
2. 이후 피드백 신호에 기초하여 가중치가 점진적으로 조정될 것
    (training loop)

f(x) = y
epsilon_x만큼 증가시켰을 때
y가 epsilon_y만큼 바뀐다.

f(x + epsilon_x) = y + epsilon_y
기울기의 방향과 기울기 값을 알아보는 계산 엑셀 주소 (코딩 야학)
https://docs.google.com/spreadsheets/d/1XfE4HvjhqxU335DuW5-vHdX6ssVMfiaBCb1p9jN-U6Y/edit#gid=0


#
텐서 연산의 번화율 - gradient
# W를 input x에 행렬곱 했을 때 예측값 y의 영향도
y_pred = dot(W, x)

# y 예측과 y의 차이가 오류값이 된다.
loss_value = loss(y_pred, y)

"""

# nesterov momentum
"""

past_velocity = 0.
momentum = 0.1
while loss > 0.01:
    w, loss, gradient = get_current_parameters()
    velocity = momentum * past_velocity - learning_date * gradient
    w = w + momentum * velocity - learning_rate * gradient
    past_velocity = velocity
    update_parameter(w)
"""

from keras import optimizers
# 일반적으로 모멘텀은 0.9를 많이 사용한다.
sgd = optimizers.SGD(lr=0.01, momentum=0.9, nesterov=True)
network.compile(optimizers=sgd)

"""
변화율 연결: 역전파 알고리즘
backpropagation
"""

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

"""
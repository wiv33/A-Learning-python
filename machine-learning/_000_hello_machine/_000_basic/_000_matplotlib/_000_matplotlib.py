import numpy as np
import matplotlib.pyplot as plt

# 학습 데이터 읽기
train = np.loadtxt('./data/click.csv', delimiter=",", skiprows=1)

## 배열의 슬라이싱 -> [시작:끝]
## :,1 => 배열 1번 인덱스의 y값을 가져옴.
train_x = train[:,0]
train_y = train[:,1]

print(train_y, end=" 끝")

# 점 그래프를 그린다
plt.plot(train_x, train_y, 'o')
plt.show()
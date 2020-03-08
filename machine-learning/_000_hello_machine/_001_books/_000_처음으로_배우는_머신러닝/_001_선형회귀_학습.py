from sklearn import datasets
from sklearn.linear_model import LinearRegression
import numpy as np

boston = datasets.load_boston()

lr = LinearRegression()
print("==================================================")
print(boston.data, end=" ::X\n")
print("==================================================\n")
print(boston.target, end= "::y\n")
fit = lr.fit(boston.data, boston.target)
print("fit start ::: ==============\n")
print(fit)
# 학습 끝

print(boston.data[2])
print(boston.data[2].reshape(1, -1))
lr.predict(boston.data[2].reshape(1, -1))

print([x for x in zip(boston.feature_names, lr.coef_)])

# 사이킷런에서의 학습과 예측은
#   모델 객체 생성 -> fit 함수 -> predict 함수 순서로 이루어진다.


from sklearn import datasets
from sklearn import ensemble
import matplotlib.pyplot as plt

diabetes = datasets.load_diabetes()

# 독립변수와 반응변수로 구분한다.
diabetes_X = diabetes.data
diabetes_Y = diabetes.target
diabetes_feature = diabetes.feature_names

# 당뇨병 환자 예측
print(diabetes_X, diabetes_X.shape, diabetes_feature)

# 연속 값 예측, 회귀분석
print("=====================================")
print(diabetes_Y, diabetes_Y.shape)

model = ensemble.RandomForestRegressor()
model.fit(diabetes_X, diabetes_Y)

# 결정계수 표시
r2 = model.score(diabetes_X, diabetes_Y)
print('결정계수 ', r2)

model.predict(diabetes_X)

# age
plt.scatter(diabetes_X[:, 0], diabetes_Y, marker='+', c='blue')
plt.scatter(diabetes_X[:, 0], model.predict(diabetes_X), marker='o', c='red')
plt.show()

# 그래프 표시 - sex
plt.scatter(diabetes_X[:, 1], diabetes_Y, marker='+', c='blue')
plt.scatter(diabetes_X[:, 1], model.predict(diabetes_X), marker='o', c='red')
plt.show()


# 그래프 표시 - bmi
plt.scatter(diabetes_X[:, 2], diabetes_Y, marker='+', c='blue')
plt.scatter(diabetes_X[:, 2], model.predict(diabetes_X), marker='o', c='red')
plt.show()


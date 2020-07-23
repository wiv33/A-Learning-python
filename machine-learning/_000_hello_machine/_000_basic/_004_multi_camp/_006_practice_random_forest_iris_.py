from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)

# print(df)

# print(iris.target, iris.target_names)

df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# print(df.head())

print(sum(np.random.uniform(0, 1, len(df)) < 0.75))

df['is_train'] = np.random.uniform(0, 1, len(df)) < .75

# print(df.head())


train, test = df[df['is_train'] == True], df[df['is_train'] == False]

train.head()

print('train len : {}'.format(len(train)))
print('test len : {}'.format(len(test)))

features = df.columns[:4]
print(features)

y = pd.factorize(train['species'])[0]
print(y)

#  tree  개수
clf = RandomForestClassifier(n_estimators=10)

clf.fit(train[features], y)
clf.predict(test[features])

clf.predict_proba(test[features])

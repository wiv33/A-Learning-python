import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

sns.set(style='darkgrid')

iris = load_iris()
iris_data = iris.data
print(iris_data[:5])
iris_labels = iris.target

iris_df = pd.DataFrame(data=iris_data, columns=iris.feature_names)
iris_df['label'] = iris_labels
print(iris_df.head())

sns.pairplot(data=iris_df,
             y_vars=iris_df.columns,
             hue='label',
             height=5)

plt.show()

X_train, X_test, y_train, y_test = train_test_split(iris_data, iris_labels, test_size=.2)

dt_clf = DecisionTreeClassifier()
knn_clf = KNeighborsClassifier()

dt_clf.fit(X_train, y_train)
knn_clf.fit(X_train, y_train)

y1_pred = dt_clf.predict(X_test)
y2_pred = knn_clf.predict(X_test)

print('DecisionTree Accuracy: {:.4f}'.format(accuracy_score(y_test, y1_pred)))

print("K-NN Accuracy: {:.4f}".format(accuracy_score(y_test, y2_pred)))


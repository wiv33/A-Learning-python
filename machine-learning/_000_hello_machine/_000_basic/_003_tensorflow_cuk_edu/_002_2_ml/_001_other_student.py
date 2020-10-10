import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset("iris")
sns.distplot(iris["sepal_width"],
             hist=True,
             kde=True,
             rug=True)
plt.show()
import pandas as pd

data_frame = pd.read_csv('./data/train.csv')

data_frame.plot()
data_sum = data_frame.cumsum()
data_sum.plot()

import pandas as pd

data_frame = pd.read_csv('./data/train.csv')

print(data_frame['userID'])
# 0       fe292163d06253b716e9a0099b42031d
# 1       6377fa90618fae77571e8dc90d98d409
# 2       8ec0888a5b04139be0dfe942c7eb4199
# 3       f862b39f767d3a1991bdeb2ea1401c9c
# 4       cac14930c65d72c16efac2c51a6b7f71
#                       ...
# 5995    68cb94b97d00979f4e8127915885b641
# 5996    c0b199d73bdf390c2f4c3150b6ee1574
# 5997    3ab88dd28f749fe4ec90c0b6f9896eb5
# 5998    75b4af0dacbc119eadf4eeb096738405
# 5999    67adefb430df142b099bed89bd491524
# Name: userID, Length: 6000, dtype: object

print(data_frame['jobID'][:3])  # jobID 앞에서부터 3개만 또는 인덱스 3 전까지
# 0    15de21c670ae7c3f6f3f1f37029303c9
# 1    55b37c5c270e5d84c793e486d798c01d
# 2    0fcbc61acd0479dc77e3cccc0f5ffca7
# Name: jobID, dtype: object


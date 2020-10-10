import pandas as pd

DATA_IN_PATH = './data_in/refine/'
TRAIN_CLEAN_DATA = 'train_clean.csv'

def rf(path):
    return "{}{}".format(DATA_IN_PATH, path)

train_data = pd.read_csv(rf(TRAIN_CLEAN_DATA))

reviews = list(train_data['review'])
sentiments = list(train_data['sentiment'])

sentences =  []

for rev in reviews:
    sentiments.append(rev.split())



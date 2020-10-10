import pandas as pd

DATA_IN_PATH = './data_in/refine/'
TRAIN_CLEAN_DATA = 'train_clean.csv'


def rp(s):
    return "{}{}".format(DATA_IN_PATH, s)


train_data = pd.read_csv(rp(TRAIN_CLEAN_DATA),
                         header=0,
                         delimiter=',',
                         quoting=3)

reviews = list(train_data['review'])
sentiments = list(train_data['sentiment'])

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(min_df=.0,
                             analyzer='char',
                             sublinear_tf=True,
                             ngram_range=(1, 3),
                             max_features=5000)

# reviews: [sentence, sentence, sentence]
X = vectorizer.fit_transform(reviews)


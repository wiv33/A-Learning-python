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
"""
min_df: 
    설정한 값보다 특정 토큰의 df 값이 더 적게 나오면 벡터화 과정에서 제거
    
analyzer: 
    분석하기 위한 기준 단위
        word - 단어
        char - 하나의 문자
        
sublinear_tf:
     문서의 빈도 수에 대한 스무딩 여부 결정
     smoothing
     
ngram_range:
    빈도의 기본 단위 범위
    
max_features:
    각 벡터의 최대 길이
    특징의 길이를 설정
    
"""
# reviews: [sentence, sentence, sentence]
X = vectorizer.fit_transform(reviews)

from sklearn.model_selection import train_test_split
import numpy as np

RANDOM_SEED = 33
TEST_SPLIT = .2

y = np.array(sentiments)

X_train, X_eval, y_train, y_eval = train_test_split(X, y, test_size=TEST_SPLIT,
                                                    random_state=RANDOM_SEED)

from sklearn.linear_model import LogisticRegression

lgs = LogisticRegression(class_weight='balanced')
"""
class_weight:
    balanced:
        각 레벨에 대해 평균 있게 학습
"""
lgs.fit(X_train, y_train)
print('Accuracy: {:f}'.format(lgs.score(X_eval, y_eval)))
# Accuracy: 0.862600

# submit

TEST_CLEAN_DATA = 'test_clean.csv'

test_data = pd.read_csv(rp(TEST_CLEAN_DATA), header=0, delimiter=',', quoting=3)
print(test_data.head())

# 벡터화할 때 평가 데이터에 대해서는 fit을 호출하지 않고 transform만 호출한다.

test_data_vecs = vectorizer.transform(test_data['review'])

test_predicted = lgs.predict(test_data_vecs)
print(test_predicted)

DATA_OUT_PATH = '../data_out/'

import os

if not os.path.exists(DATA_OUT_PATH):
    os.makedirs(DATA_OUT_PATH)

ids = list(test_data['id'])
answer_dataset = pd.DataFrame({'id': ids, 'sentiment': test_predicted})
answer_dataset['id'] = answer_dataset['id'].apply(lambda x: x.replace("\"", ''))
answer_dataset.to_csv(DATA_OUT_PATH + 'lgs_tfidf_answer.csv', index=False)

print(answer_dataset.info())

# kaggle competitions submit -c word2vec-nlp-tutorial -f submission.csv -m "Message"

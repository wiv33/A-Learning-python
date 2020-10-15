import pandas as pd

DATA_IN_PATH = '../data_in/refine/'
TRAIN_CLEAN_DATA = 'train_clean.csv'


def rf(path):
    return "{}{}".format(DATA_IN_PATH, path)


train_data = pd.read_csv(rf(TRAIN_CLEAN_DATA))

""" word2vecㅇ의 경우 단어로 표현된 리스트를 입력값으로 넣어야 한다. """
reviews = list(train_data['review'])
sentiments = list(train_data['sentiment'])

sentences = []

# 각 리뷰 == 하나의 문자열
# 문자열 => split
for rev in reviews:
    sentiments.append(rev.split())

# 학습 시 필요한 하이퍼파라미터
"""
num_features
    각 단어에 대해 임베딩된 벡터의 차원을 정한다.

min_word_count
    모델에 의미 잇는 단어를 가지고 학습하기 위해 적은 빈도 수의 단어들은 학습하지 않는다.

num_workers
    모델 학습 시 학습을 위한 프로세스 개수를 지정한다.
    
context
    word2vec을 수행하기 위한 컨텍스트 윈도 크기를 지정한다.

down_sampling
    word2vec 학습을 수행할 때 빠른 학습을 위해 정답 단어 라벨에 대한 다운샘플링 비율을 지정한다.
    0.001
    
"""
num_features = 300
min_word_count = 40
num_workers = 4
context = 10
downsampling = 1e-3

# pip install gensim

import logging
from gensim.models import word2vec

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',
                    level=logging.INFO)

print('Training model...')

model = word2vec.Word2Vec(sentences=sentences,
                          workers=num_workers,
                          size=num_features,
                          min_count=min_word_count,
                          window=context,
                          sample=downsampling)

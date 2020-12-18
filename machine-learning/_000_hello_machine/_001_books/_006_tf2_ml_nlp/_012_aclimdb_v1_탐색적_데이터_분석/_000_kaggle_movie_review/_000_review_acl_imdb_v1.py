import os

import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras import utils

data_set = tf.keras.utils.get_file(
    fname='imdb.tar.gz',
    origin='http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz',
    extract=True
)


# /home/ps/.keras/datasets/imdb.tar.gz

def directory_data(directory):
    data = {}
    data['review'] = []
    for file_path in os.listdir(directory):
        with open(os.path.join(directory, file_path), 'r') as file:
            data['review'].append(file.read())

    return pd.DataFrame.from_dict(data)


def data(directory):
    pos_df = directory_data(os.path.join(directory, 'pos'))
    neg_df = directory_data(os.path.join(directory, 'neg'))
    pos_df['sentiment'] = 1
    neg_df['sentiment'] = 0

    print(pos_df.head(), end='\n==\n')
    print(neg_df.head(), end='\n==\n')

    return pd.concat([pos_df, neg_df])


train_df = data(os.path.join(os.path.dirname(data_set), 'aclImdb', 'train'))
test_df = data(os.path.join(os.path.dirname(data_set), 'aclImdb', 'test'))

print(train_df.head())

reviews = list(train_df['review'])

print(reviews[0:2])

"""
아래 작업은 문장에 포함된 단어와 알파벳의 개수에 대한 
데이터 분석을 수월하게 만들기 위함
"""

# 문자열 문장 리스트를 토크나이징
tokenized_reviews = [r.split() for r in reviews]

# 토크나이징된 리스트에 대한 각 길이를 저장 (단어 개수)
review_len_by_token = [len(t) for t in tokenized_reviews]
print(review_len_by_token[0: 3])

# 토크나이징된 것을 붙여서 음절의 길이를 저장 (알파벳 총 길이)
review_len_by_eumjeol = [len(s.replace(" ", '')) for s in reviews]
print(review_len_by_eumjeol[0: 3])

#


import matplotlib.pylab as plt

# 그래프 이미지 크기 설정
# figsize: (가로, 세로) 튜플
plt.figure(figsize=(12, 5))

# 히스토그램 선언
"""
bins: 히스토그램 값에 대한 버킷 범위
alpha: 그래프 색상 투명도
color: 그래프 색상
label: 그래프에 대한 라벨
"""
plt.hist(review_len_by_token, bins=50, alpha=.5, color='r', label='word')
plt.hist(review_len_by_eumjeol, bins=50, alpha=.5, color='b', label='alphabet')
plt.yscale('log', nonposy='clip')

# 그래프 제목
plt.title('Review Length histogram')

# x label
plt.xlabel('Review length')
plt.ylabel('Number of Reviews')
plt.show()

print('문장 최대 길이: {}'.format(np.max(review_len_by_token)))
print('문장 최소 길이: {}'.format(np.min(review_len_by_token)))
print('문장 평균 길이: {:.2f}'.format(np.mean(review_len_by_token)))
print('문장 길이 표준편차: {:.2f}'.format(np.std(review_len_by_token)))
print('문장 중간 길이: {}'.format(np.median(review_len_by_token)))

# 사분위의 대한 경우는 0~100 스케일로 돼 있음
"""
전체 뎅터에서 1/4, 3/4 지점을 의미
"""
print("제1사분위 길이: {}".format(np.percentile(review_len_by_token, 25)))
print("제3사분위 길이: {}".format(np.percentile(review_len_by_token, 75)))

# Box plt
# 문장 내 단어 수에 대한 히스토그램
plt.figure(figsize=(12, 5))
# 박스 플롯 생성
# 첫 번째 인자: 여러 분포에 대한 데이터 리스트를 입력
# labels: 입력한 데이터에 대한 라벨
# showmeans: 평균값을 마크함
plt.boxplot([review_len_by_token],
            labels=['token'],
            showmeans=True)
plt.show()

# 문장 내 알파벳 개수 히스토그램
plt.figure(figsize=(12, 5))
plt.boxplot([review_len_by_eumjeol],
            labels=['Eumjeol'],
            showmeans=True)
plt.show()

from wordcloud import WordCloud, STOPWORDS

wordcloud = WordCloud(stopwords=STOPWORDS,
                      background_color='black',
                      width=800,
                      height=800).generate(''.join(train_df['review']))

plt.figure(figsize=(15, 10))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()

import seaborn as sns

sentiment = train_df['sentiment'].value_counts()
fig, axe = plt.subplots(ncols=1)
fig.set_size_inches(6, 3)
sns.countplot(train_df['sentiment'])

fig.show()
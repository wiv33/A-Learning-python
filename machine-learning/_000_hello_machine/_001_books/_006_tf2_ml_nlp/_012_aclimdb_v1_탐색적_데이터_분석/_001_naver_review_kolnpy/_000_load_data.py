import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import os
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS

DATA_IN_PATH = './data_in/'


def visit_file_size():
    print("파일 크기: ")

    for file in os.listdir(DATA_IN_PATH):
        if 'txt' in file:
            print(file.ljust(30) + str(round(os.path.getsize(DATA_IN_PATH + file) / 1000000, 2)) + 'MB')


visit_file_size()

train_data = pd.read_csv(DATA_IN_PATH + 'ratings_train.txt', header=0, delimiter='\t', quoting=3)

print(train_data.head(1))

print(f'전체 학습 데이터의 개수: {len(train_data)}')

train_length = train_data['document'].astype(str).apply(len)
print(train_length.head())

# 그래프에 대한 이미지 크기 선언
# figsize: (가로, 세로)

plt.figure(figsize=(12, 7))
# 히스토그램 선언
# bins: 히스토그램 값에 대한 버킷 범위
# range: x축 값의 범위
# alpha: 그래프 색상 투명도
# color: 그래프 색상
# label: 그래프에 대한 라벨
plt.hist(train_length,
         bins=200,
         alpha=.5,
         color='r',
         label='word',
         edgecolor='black')
plt.yscale('log', nonposy='clip')

# 그래프 제목
plt.title('Log-Histogram of length of review')
# 그래프 x축 라벨
plt.xlabel('Length of review')
# 그래프 y축 라벨
plt.ylabel('Number of review')
plt.show()

print(f'리뷰 길이 최댓값: {np.max(train_length)}')
print(f'리뷰 길이 최솟값: {np.min(train_length)}')
print(f'리뷰 길이 평균값: {np.mean(train_length)}')
print(f'리뷰 길이 표준편차: {np.std(train_length)}')
print(f'리뷰 길이 중간값: {np.median(train_length)}')
print(f'리뷰 길이 제1사분위: {np.percentile(train_length, 25)}')
print(f'리뷰 길이 제3사분위: {np.percentile(train_length, 75)}')

plt.figure(figsize=(12, 7))
# 박스 플롯 생성
# 첫 번재 파라미터: 여러 분포에 대한 데이터 리스트를 입력
# labels: 입력한 데이터에 대한 라벨
# showmeans: 평균값을 마크

plt.boxplot(train_length,
            labels=['counts'],
            showmeans=True)

plt.show()

train_review = [review for review in train_data['document'] if type(review) is str]

word_cloud = WordCloud(stopwords=STOPWORDS,
                       background_color='black',
                       width=800,
                       height=800) \
    .generate(' '.join(train_review))

plt.imshow(word_cloud, interpolation='bilinear')
plt.axis('off')
plt.show()

fig, ax = plt.subplots(ncols=1)
fig.set_size_inches(6, 3)
sns.countplot(train_data['label'])
plt.show()

print(f'긍정 리뷰 개수: {train_data["label"].value_counts()[1]}')
print(f'부정 리뷰 개수: {train_data["label"].value_counts()[0]}')

train_word_counts = train_data['document'].astype(str).apply(lambda x: len(x.split(' ')))

plt.figure(figsize=(15, 10))
plt.hist(train_word_counts, bins=50,
         facecolor='r',
         label='train',
         edgecolor='black')
plt.title('Log-Histogram of word count in review', fontsize=15)
plt.yscale('log', nonposy='clip')
plt.legend()
plt.xlabel('Number of word', fontsize=15)
plt.ylabel('Number of reviews', fontsize=15)
plt.show()

print(f'리뷰 단어 개수 최댓값: {np.max(train_word_counts)}')
print(f'리뷰 단어 개수 최솟값: {np.min(train_word_counts)}')
print(f'리뷰 단어 개수 평균값: {np.mean(train_word_counts)}')
print(f'리뷰 단어 개수 표준편차: {np.std(train_word_counts)}')
print(f'리뷰 단어 개수 중간값: {np.median(train_word_counts)}')
print(f'리뷰 단어 개수 제1사분위: {np.percentile(train_word_counts, 25)}')
print(f'리뷰 단어 개수 제3사분위: {np.percentile(train_word_counts, 75)}')

qmarks = np.mean(train_data['document'].astype(str).apply(lambda x: '?' in x))
fullstop = np.mean(train_data['document'].astype(str).apply(lambda x: '.' in x))

print(f'물음표가 있는 질문: {qmarks * 100}%')
print(f'마침표가 있는 질문: {fullstop * 100}%')
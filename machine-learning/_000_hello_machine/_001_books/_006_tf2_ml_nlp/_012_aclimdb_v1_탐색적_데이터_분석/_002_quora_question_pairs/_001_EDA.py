import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import os
import seaborn as sns
from pathlib import Path
from wordcloud import WordCloud

getcwd = os.getcwd()
print(getcwd)

DATA_IN_PATH = './data_in/'
train_data = pd.read_csv(DATA_IN_PATH + "train.csv")
print(train_data.head(1))

print('파일크기: ')
for file in os.listdir(DATA_IN_PATH):
    if 'csv' in file and 'zip' not in file:
        print(file.ljust(30) + str(round(os.path.getsize(DATA_IN_PATH + file) / 1000000, 2)) + 'MB')

print(f'전체 학습 데이터의 개수: {len(train_data)}')

train_set = pd.Series(train_data.iloc[:, 3].tolist() + train_data.iloc[:, 4].tolist()).astype(str)

# 질문 중복 여부 확인
print(f'교육 데이터의 총 질문 수: {len(np.unique(train_set))}')

print(f'반복해서 나타는 질문 수: {np.sum(train_set.value_counts() > 1)}')


# result: train_set.value_counts()
# What are the best ways to lose weight? 161
# How can you look at someone's private Instagram account without following them? 120

# result: np.sum(train_set.value_counts() > 1)
# 111873


# 히스토그램
def show_hist(bins, v_range, alpha, color, edge_color, label, **kwargs):
    """
    :param bins: 히스토그램 값 버킷 범위
    :param v_range: x축 값의 범위
    :param alpha: 그래프 색상 투명도
    :param color: 색상
    :param label: 그래프 라벨
    :param edge_color: 그래프 선
    :return:
    """
    plt.figure(figsize=(12, 7))
    plt.hist(kwargs['data'],
             bins=bins,
             alpha=alpha,
             color=color,
             range=v_range,
             edgecolor=edge_color,
             label=label,
             rwidth=.7)

    if kwargs['log']:
        plt.yscale('log', nonposy='clip')

    plt.title(kwargs['title'], fontsize=kwargs['fontsize'])
    plt.xlabel(kwargs['xlabel'], fontsize=kwargs['fontsize'])
    plt.ylabel(kwargs['ylabel'], fontsize=kwargs['fontsize'])
    plt.legend()
    plt.show()


kwargs = {
    'data': train_set.value_counts(),
    'title': 'Log-Histogram of occurrences of question',
    'log': True,
    'fontsize': 15,
    'xlabel': 'Number of occurrences of question',
    'ylabel': 'Number of questions'
}
show_hist(50, [0, 170], .5, 'r', 'black', 'word', **kwargs)

print(f'중복 최대 개수: {np.max(train_set.value_counts())}')
print(f'중복 최소 개수: {np.min(train_set.value_counts())}')
print("중복 평균 개수: {:.2f}".format(np.mean(train_set.value_counts())))
print("중복 표준편차: {:.2f}".format(np.std(train_set.value_counts())))
print(f'중복 중간길이 개수: {np.median(train_set.value_counts())}')
print(f'중복 제1사분위: {np.percentile(train_set.value_counts(), 25)}')
print(f'중복 제3사분위: {np.percentile(train_set.value_counts(), 75)}')

plt.figure(figsize=(12, 7))
# 박스 플롯
plt.boxplot([train_set.value_counts()],
            labels=['counts'],
            showmeans=True)
plt.show()

cloud = WordCloud(width=800, height=700) \
    .generate(" ".join(train_set.astype(str)))

plt.figure(figsize=(15, 10))
plt.imshow(cloud)
plt.axis('off')
plt.show()

# 0, 1 시각화
fig, axe = plt.subplots(ncols=1)
fig.set_size_inches(6, 3)
sns.countplot(train_data['is_duplicate'])
plt.show()

# 전체 길이 분석
train_length = train_set.apply(len)

kwargs = {
    'data': train_length,
    'title': 'Normalised histogram of character count in questions',
    'fontsize': 15,
    'log': False,
    'xlabel': 'Number of characters',
    'ylabel': 'Probability',
    'facecolor': 'r'
}

show_hist(bins=200, v_range=[0, 200], alpha=.7, color='r', edge_color='black', label='train', **kwargs)

print(f'질문 길이 최댓값: {np.max(train_length)}')
print('질문 길이 평균값: {:2f}'.format(np.mean(train_length)))
print('질문 길이 표준편차: {:2f}'.format(np.std(train_length)))
print(f'질문 길이 중간값: {np.median(train_length)}')
print(f'질문 길이 제1사분위: {np.percentile(train_length, 25)}')
print(f'질문 길이 제3사분위: {np.percentile(train_length, 75)}')

# boxplot
plt.figure(figsize=(12, 7))
plt.boxplot(train_length,
            labels=['char counts'],
            showmeans=True)
plt.show()

train_word_counts = train_set.apply(lambda x: len(x.split(" ")))

kwargs = {
    'data': train_word_counts,
    'title': 'Normalised histogram of word count in questions',
    'fontsize': 15,
    'log': False,
    'xlabel': 'Number of words',
    'ylabel': 'Probability',
    'facecolor': 'r'
}
show_hist(50, [0, 50], .7, 'r', 'black', 'train', **kwargs)

print(f'질문 단어 개수 최댓값: {np.max(train_word_counts)}')
print('질문 단어 개수 평균값: {:2f}'.format(np.mean(train_word_counts)))
print('질문 단어 개수 표준편차: {:2f}'.format(np.std(train_word_counts)))
print(f'질문 단어 개수 중간값: {np.median(train_word_counts)}')
print(f'질문 단어 개수 제1사분위: {np.percentile(train_word_counts, 25)}')
print(f'질문 단어 개수 제3사분위: {np.percentile(train_word_counts, 75)}')
print(f'질문 단어 개수 99퍼센트: {np.percentile(train_word_counts, 99)}')

plt.figure(figsize=(12, 7))
plt.boxplot(train_word_counts,
            labels=['word counts'],
            showmeans=True)
plt.show()


def contains_char(x, item):
    return item in x


# 물음표
qmarks = np.mean(train_set.apply(contains_char, item='?'))
# [] 수식
math = np.mean(train_set.apply(contains_char, item='[math]'))
# 마침표
fullstop = np.mean(train_set.apply(contains_char, item='.'))

# 첫 글자가 대문자
capital_first = np.mean(train_set.apply(lambda x: x[0].isupper()))
# 대문자가 몇 개
capitals = np.mean(train_set.apply(lambda x: max([y.isupper() for y in x])))
# 숫자가 몇 개
numbers = np.mean(train_set.apply(lambda x: max([y.isdigit() for y in x])))

print('물음표가 있는 질문: {:.2f}%'.format(qmarks * 100))
print('수식이 있는 질문: {:.2f}%'.format(math * 100))
print('질문이 가득 찼을 때: {:.2f}%'.format(fullstop * 100))
print('첫 글자가 대문자인 질문: {:.2f}%'.format(capital_first * 100))
print('대문자가 있는 질문: {:.2f}%'.format(capitals * 100))
print('숫자가 있는 질문: {:.2f}%'.format(numbers * 100))

# 물음표가 있는 질문: 99.87%
# 수식이 있는 질문: 0.12%
# 질문이 가득 찼을 때: 6.31%
# 첫 글자가 대문자인 질문: 99.81%
# 대문자가 있는 질문: 99.95%
# 숫자가 있는 질문: 11.83%
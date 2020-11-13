import zipfile

DATA_IN_PATH = './data_in/'

file_list = ['labeledTrainData.tsv.zip', 'unlabeledTrainData.tsv.zip', 'testData.tsv.zip']

for f in file_list:
    zipRef = zipfile.ZipFile(DATA_IN_PATH + f, 'r')
    zipRef.extractall(DATA_IN_PATH)
    zipRef.close()

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

# %matplotlib inline  # 그래프 바로 그리기

"""# 데이터 프레임으로 만들기"""

train_data = pd.read_csv("{}labeledTrainData.tsv".format(DATA_IN_PATH),
                         header=0,
                         delimiter='\t',
                         quoting=3)

train_data.head()

"""# 데이터 분석 순서

1. 데이터 크기
2. 데이터의 개수
3. 각 리뷰의 문자 길이 분포
4. 많이 사용된 단어
5. 긍정, 부정 데이터의 분포
6. 각 리뷰의 단어 개수 분포
7. 특수문자 및 대문자, 소문자 비율

## 1. 데이터(파일)의 크기
"""

print("파일 크기 : ")
for f in os.listdir(DATA_IN_PATH):
    if 'tsv' in f and 'zip' not in f:
        # print(f.ljust(30))
        print(f.ljust(30) + str(round(os.path.getsize(DATA_IN_PATH + f) / 1000000, 2)) + "MB")

"전체 학습 데이터 개수: {}".format(len(train_data))

train_length = train_data['review'].apply(len)
train_length.head()

"""## 주요 설정

### 그래프 이미지 크기 설정

* figsize: (가로, 세로) tuple
"""

plt.figure(figsize=(12, 5))

"""### 히스토그램

* bins: 히스토그램 값 버킷 범위
* range: x축 값의 범위
* alpha: 그래프 색상 투명도
* color: 그래프 색상
* label: 그래프 라벨


    ValueError: 'square' is not a valid value for scale; supported values are 'linear', 'log', 'symlog', 'logit', 'function', 'functionlog'


* yscale 첫 번째 인자의 유효 값
  - 'linear' 
  - 'log'
  - 'symlog'
  - 'logit'
  - 'function'
  - 'functionlog'
    
```python
plt.yscale()
```

### 결과 내용

    0 ~ 6000: 대부분의 데이터가 밀집한 상태
    10000 이상: 이상치로 간주
"""

plt.hist(train_length,
         bins=200,
         alpha=.5,
         color='r',
         label='word')

# 로그의 크기를 가지도록 설정
plt.yscale('log', nonposy='clip')

plt.title('Log-Histogram of length of review')
plt.xlabel('Length of review')
plt.ylabel('Number of review')

"""## 통곗값 확인

- 리뷰 길이 최댓값
"""

print('리뷰 길이 최댓값: {}'.format(np.max(train_length)))

print('리뷰 길이 최솟값: {}'.format(np.min(train_length)))

print('리뷰 길이 평균값: {:.2f}'.format(np.mean(train_length)))

print('리뷰 길이 표준편차: {:.2f}'.format(np.std(train_length)))

print('리뷰 길이 중간값: {}'.format(np.max(train_length)))

"""백분위 표시
    -> 특정집단의 점수분포상에서 한 개인의 상대적 위치를 알수있는 유도점수
    25는 25% 위치에 해당한 값
    75는 75% 위치의 값
    100% 값은 리뷰 길이 최댓값과 동일한 값

- 사분위에 대한 경우는 0 ~ 100 스케일로 돼 있음
"""

print('리뷰 길이 제1사분위: {}'.format(np.percentile(train_length, 25)))
print('리뷰 길이 제3사분위: {}'.format(np.percentile(train_length, 75)))
print('리뷰 길이 제4사분위: {}'.format(np.percentile(train_length, 100)))

"""## 박스 plot

* 첫 번째 인자: 여러 분포에 대한 데이터 리스트 입력
* labels: 입력한 데이터 라벨
* showmeans: 평균값을 `마크`
"""

plt.boxplot(train_length,
            labels=['counts'],
            showmeans=True)

"""## 리뷰에서 많이 사용된 단어 확인

### Word Cloud
"""

# !pip install wordcloud

from wordcloud import WordCloud

cloud = WordCloud(width=800,
                  height=600).generate(" ".join(train_data['review']))
plt.figure(figsize=(20, 15))
plt.imshow(cloud)
plt.axis('off')

"""## 긍정, 부정 데이터 분포 확인

### 씨본 (`seaborn`)
"""

fig, axe = plt.subplots(ncols=1)
fig.set_size_inches(7, 4)
sns.countplot(train_data['sentiment'])

"""- sns.countplot()의 `argument` 확인하기
  * 0과 1
  * 각 숫자의 개수를 출력
"""

train_data['sentiment'].head()

"""- 각 라벨의 값 출력"""

print("긍정 리뷰 개수: {}".format(train_data['sentiment'].value_counts()[1]))
print("부정 리뷰 개수: {}".format(train_data['sentiment'].value_counts()[0]))

"""## 단어 추출 - WordCloud

- 띄어쓰기 기준으로 하나의 단어라고 가정
"""

train_word_counts = train_data['review'].apply(lambda x: len(x.split(' ')))

train_word_counts.head()

plt.figure(figsize=(15, 10))
plt.hist(train_word_counts,
         bins=50,
         facecolor='r',
         label='train')
plt.title("Log-Histogram of word count in review",
          fontsize=15)
plt.yscale('log',
           nonposy='clip'
           )
plt.legend()
plt.xlabel('Number of words', fontsize=15)
plt.ylabel('Number of reviews', fontsize=15)

"""## 통곗값 출력"""

print("리뷰 단어 개수 최댓값: {}".format(np.max(train_word_counts)))
print("리뷰 단어 개수 최솟값: {}".format(np.min(train_word_counts)))
print("리뷰 단어 개수 평균값: {:.2f}".format(np.mean(train_word_counts)))
print("리뷰 단어 개수 표준편차: {:.2f}".format(np.std(train_word_counts)))
print("리뷰 단어 개수 중간값: {}".format(np.median(train_word_counts)))

"""- 사분위 (백분위)"""

print('리뷰 단어 개수 제1사분위 : {}'.format(np.percentile(train_word_counts, 25)))
print('리뷰 단어 개수 제3사분위 : {}'.format(np.percentile(train_word_counts, 75)))

"""# 각 리뷰의 구두점, 대소문자 비율"""


def extract_by_func(func):
    return train_data['review'].apply(func)


def mt(x):
    return x * 100


qmarks = np.mean(extract_by_func(lambda x: '?' in x))  # 물음표가 구두점으로 쓰임
fullstop = np.mean(extract_by_func(lambda x: '.' in x))  # 마침표
capital_first = np.mean(extract_by_func(lambda x: x[0].isupper()))  # 첫 번째 대문자
capitals = np.mean(extract_by_func(lambda x: max([y.isupper() for y in x])))  # 대문자 개수
numbers = np.mean(extract_by_func(lambda x: max([y.isdigit() for y in x])))  # 숫자 개수

print('물음표가 있는 질문: {:.2f}'.format(mt(qmarks)))
print('마침표가 있는 질문: {:.2f}'.format(mt(fullstop)))
print('첫 글자가 대문자인 질문: {:.2f}'.format(mt(capital_first)))
print('대문자가 있는 질문: {:.2f}'.format(mt(capitals)))
print('숫자가 있는 질문: {:.2f}'.format(mt(numbers)))

"""# 위 분석을 바탕으로 `전처리 시작`

## 주요 패키지

- ## json
  
- ## bs4.BeautifulSoup
- ## nltk.corpus.stopwords
- ## tensorflow.python.keras.preprocessing.sequence.pad_sequences
- ## tensorflow.python.keras.preprocessing.txt.Tokenizer
"""

# !pip install nltk

import re
import json
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from tensorflow.python.keras.preprocessing.sequence import pad_sequences
from tensorflow.python.keras.preprocessing.text import Tokenizer

"""## 데이터 하나를 자세히 보기

    전처리 방향성을 결정하기 위함
"""

DATA_IN_PATH
df_train_data = pd.read_csv("{}labeledTrainData.tsv".format(DATA_IN_PATH),
                            header=0,
                            delimiter='\t')
df_train_data.iloc[0, 2]

"""## [전처리] HTML 태그, 특수문자 제거"""

review = df_train_data.iloc[0, 2]
review_text = BeautifulSoup(review, 'lxml').get_text()
review_text = re.sub('[^a-zA-Z]', ' ', review_text)  # 영문자 제외, 모두 공백으로 변환

review_text

"""## [전처리] 불용어 제거

    조사, 관사와 같은 어휘는
    감정 분석에 영향을 미치지 않다고 판단하여
    불용어에 포함시켰다.

- ### 제거 방법
  #### - 불용어로 정의한 사전을 이용
  #### - (현재 기준)nltk 사전을 활용
  #### - 모든 단어 소문자로 변경

영어 불용어 set 만들기
"""

# nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
len(stop_words)

"""## - [전처리] 소문자로 변경 후 불용어를 제거"""

review_text = review_text.lower()
words = review_text.split()
words = [w for w in words if not w in stop_words]

len(words)

"""## - [전처리] 다시 하나의 글로 합친다."""

clean_review = ' '.join(words)
clean_review

"""# 한 사이클의 전처리 과정을 모든 데이터에 반영할 함수 정의"""


def ps_preprocessing(arg_review, remove_stopwords=False):
    # 1. HTML 태그 제거
    local_review_text = BeautifulSoup(arg_review, 'lxml').get_text()

    # 2. 영어가 아닌 특수문자를 공백으로 치환
    local_review_text = re.sub('[^a-zA-Z]', ' ', local_review_text)

    # 3. 대문자를 소문자로 바꾸고 공백 단위로 텍스트를 나누어 리스트로 만듦
    local_words = local_review_text.lower().split()

    # 3-1 불용어 제거하지 않을 경우 바로 반환
    if not remove_stopwords:
        return ' '.join(local_words)

    # 4. 불용어 제거

    # 영어 불용어 불러오기
    stops = set(stopwords.words('english'))
    # 불용어가 아닌 단어로 이뤄진 새로운 리스트 생성
    local_words = [w for w in local_words if not w in stops]

    # 5. 단어 리스트를 공백을 넣어서 하나의 글로 합친다.
    return ' '.join(local_words)


clean_train_reviews = []
for review in df_train_data['review']:
    clean_train_reviews.append(ps_preprocessing(review, remove_stopwords=True))

clean_train_reviews[0]

"""### * 전처리한 텍스트와 긍정 부정 값 매핑"""

clean_train_df = pd.DataFrame(
    {'review': clean_train_reviews,
     'sentiment': df_train_data['sentiment']})

clean_train_df.head()

"""## - [전처리] 전처리한 데이터에서 각 단어를 `인덱스로 벡터화`

    각 리뷰가 텍스트가 아닌 인덱스의 벡터로 구성될 것
    각 인덱스가 어떤 단어를 의미하는지 확인할 수 있어야 한다.
"""

tokenizer = Tokenizer()
tokenizer.fit_on_texts(clean_train_reviews)
text_sequences = tokenizer.texts_to_sequences(clean_train_reviews)
text_sequences[0]

"""### 단어 사전 확인하기

    변환된 인덱스는 단어 사전을 통해 의미 확인
    <PAD>는 padding을 의미
"""

word_vocab = tokenizer.word_index
word_vocab['<PAD>'] = 0
print(word_vocab)

print("전체 단어 개수: %d" % len(word_vocab))

"""### 단어 사전과 전체 단어 개수는 이후 모델에서 사용되기 때문에 저장한다."""

data_configs = {}
data_configs['vocab'] = word_vocab
data_configs['vocab_size'] = len(word_vocab)

"""## - [전처리] 입력값의 길이를 동일하게 하는 `패딩`

    1. 특정 길이를 최대 길이로 정하고
    2. 초과하는 데이터의 뒷부분을 제거
    3. 모자란 데이터의 경우 0을 ~~앞에서~~ **뒤에서** 채운다
"""

MAX_SEQUENCE_LENGTH = 174  # 문장 최대 길이
train_inputs = pad_sequences(text_sequences, maxlen=MAX_SEQUENCE_LENGTH,
                             #  padding='pre'
                             padding='post'
                             )
print('Shape of train data : ', train_inputs.shape)

"""## [전처리] 정답을 넘파이로 변환

    이후 전처리한 데이터를 저장할 때 넘파이 형태로 저장
"""

train_labels = np.array(train_data['sentiment'])
print('Shape of label tensor: ', train_labels.shape)

"""# 데이터 전처리 흐름

1. 원본 텍스트
2. 인덱스 변환
3. 사이즈 패딩
4. 벡터화

# 전처리 데이터 저장

- 정제된 텍스트 데이터: **CSV**
- 벡터화한 데이터: **ndarray**
- 정답 라벨: **ndarray**
- 데이터 정보(단어 사전, 전체 단어 개수): **json**
"""

REFINE = DATA_IN_PATH + "refine/"
TRAIN_INPUT_DATA = 'train_input.npy'
TRAIN_LABEL_DATA = 'train_label.npy'
TRAIN_CLEAN_DATA = 'train_clean.csv'
DATA_CONFIGS = 'data_configs.npy'

if not os.path.exists(REFINE):
    os.makedirs(REFINE)

# 전처리된 데이터를 넘파이 형태로 저장
np.save(open(REFINE + TRAIN_INPUT_DATA, 'wb'), train_inputs)
np.save(open(REFINE + TRAIN_LABEL_DATA, 'wb'), train_labels)

# 정제된 텍스트를 CSV 형태로 저장
clean_train_df.to_csv(REFINE + TRAIN_CLEAN_DATA, index=False)

# 데이터 사전을 JSON 형태로 저장
json.dump(data_configs, open(REFINE + DATA_CONFIGS, 'w'), ensure_ascii=False)

"""# 평가(test)데이터 전처리

## 주의사항

  학습 데이터 전처리 후 __평가 데이터 전처리 시__
  학습 데이터에 적용한 토크나이저 객체를 계속 사용해야 인덱스가 같다.

---
"""

test_data = pd.read_csv(DATA_IN_PATH + "testData.tsv",
                        header=0,
                        delimiter='\t',
                        quoting=3)
clean_test_reviews = []
for review in test_data['review']:
    clean_test_reviews.append(ps_preprocessing(review, remove_stopwords=True))

clean_test_df = pd.DataFrame(
    {'review': clean_test_reviews,
     'id': test_data['id']}
)
test_id = np.array(test_data['id'])

tokenizer.fit_on_texts(clean_test_reviews)
test_sequences = tokenizer.texts_to_sequences(clean_test_reviews)
test_inputs = pad_sequences(test_sequences,
                            maxlen=MAX_SEQUENCE_LENGTH,
                            padding='post')


def refine(s) -> str:
    return "{}{}".format(REFINE, s)


TEST_INPUT_DATA = 'test_input.npy'
TEST_CLEAN_DATA = 'test_clean.csv'
TEST_ID_DATA = 'test_id.npy'

np.save(open(refine(TEST_INPUT_DATA), 'wb'), test_inputs)
np.save(open(refine(TEST_ID_DATA), 'wb'), test_id)
clean_test_df.to_csv(refine(TEST_CLEAN_DATA), index=False)

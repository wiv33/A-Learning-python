from typing import Set

import pandas as pd
import numpy as np
import os
import re
import json
import konlpy
from konlpy.tag import Okt
from tensorflow.python.keras.preprocessing.sequence import pad_sequences
from tensorflow.python.keras.preprocessing.text import Tokenizer

DATA_IN_PATH = './data_in/'
train_data = pd.read_csv(DATA_IN_PATH + 'ratings_train.txt',
                         header=0,
                         quoting=3,
                         delimiter='\t')

print(train_data['document'][:5])

# tag::하나의 문장을 기준으로 데이터 정제 확인[]

# 특수문자 제거
# TODO submit 218p train['document'] => train_data['document]
review_txt = re.sub('[^가-힣ㄱ-ㅎㅏ-ㅣ\\s]', '', train_data['document'][0])

okt = Okt()
# 어간 추출
# stemming = True
review_txt = okt.morphs(review_txt, stem=True)

print(review_txt)

# stopwords 추가하기
stop_words: Set[str] = set('은 는 이 가 하 아 것 들 의 있 되 수 보 주 등 한'.split())

clean_review = [token for token in review_txt if not token in stop_words]

# input : 아 더빙.. 진짜 짜증나네요 목소리
# output : ['더빙', '진짜', '짜증나다', '목소리']
# end::하나의 문장을 기준으로 데이터 정제 확인[]


# 재사용하기 쉽게 전처리 과정을 하나의 함수로 만듦
from multiprocessing import Pool


def ps_preprocessing(review, param_okt: konlpy.tag.Okt,
                     remove_stopwords=False,
                     stop_words=[]):
    """

   :param review: 전처리할 텍스트
   :param param_okt: okt 객체를 반복적으로 생성하지 않고 재사용
   :param remove_stopwords: 불용어 제거 여부
   :param stop_words: 불용어 사전은 사용자가 직접 입력하도록 설정
   :return: 정제된(불용어 제거 + 어간 추출) 텍스트
   """

    review_text = re.sub('[^가-힣ㄱ-ㅎ-ㅏ-ㅣ\\s]', '', review)

    word_review = param_okt.morphs(review_text, stem=True)
    if remove_stopwords:
        word_review = [token for token in word_review if not token in stop_words]

    return word_review


clean_train_review = []

for review in train_data['document']:
    # 비어있는 데이터에서 멈추지 않도록 `문자열인 경우 진행`
    if type(review) == str:
        clean_train_review.append(ps_preprocessing(review,
                                                   okt,
                                                   remove_stopwords=True,
                                                   stop_words=stop_words
                                                   ))
    else:
        clean_train_review.append([])

#
# def multiprocessing(reviews, **kwargs):
#     workers = kwargs.pop('workers')
#     pool = Pool(processes=workers)
#     result = pool.map(ps_preprocessing, [rev for rev in np.array_split(reviews, workers)])
#     pool.close()
#     print(result)
#     return [[].extend(res) for res in result]
#

print(clean_train_review[:5])

# multi_result = multiprocessing(train_data['document'], workers=4)

# tag::preprocessing test data[]
test_data = pd.read_csv(DATA_IN_PATH + 'ratings_test.txt',
                        header=0,
                        quoting=3,
                        delimiter='\t')

clean_test_review = []

for review in test_data['document']:
    if type(review) == str:
        clean_test_review.append(ps_preprocessing(review,
                                                  okt,
                                                  remove_stopwords=True,
                                                  stop_words=stop_words))
    else:
        clean_test_review.append([])
# end::preprocessing test data[]

# tag::학습/평가 데이터 => 인덱스 벡터 -> 패딩[]
tokenizer = Tokenizer()
tokenizer.fit_on_texts(clean_test_review)
train_sequences = tokenizer.texts_to_sequences(clean_train_review)
test_sequences = tokenizer.texts_to_sequences(clean_test_review)

word_vocab = tokenizer.word_index  # 단어 사전 형태

# review `평균 문장 길이가 8`
MAX_SEQUENCE_LENGTH = 8  # 문장 최대 길이

# 학습 데이터 벡터화
train_inputs = pad_sequences(train_sequences,
                             maxlen=MAX_SEQUENCE_LENGTH,
                             padding='post')
train_labels = np.array(train_data['label'])

# 평가 데이터 벡터화
test_inputs = pad_sequences(test_sequences,
                            maxlen=MAX_SEQUENCE_LENGTH,
                            padding='post')
test_labels = np.array(test_data['label'])
# end::학습/평가 데이터 => 인덱스 벡터 -> 패딩[]

# tag::전처리 텍스트/라벨 저장[]

TRAIN_INPUT_DATA = 'nsmc_train_input.npy'
TRAIN_LABEL_DATA = 'nsmc_train_label.npy'
TEST_INPUT_DATA = 'nsmc_test_input.npy'
TEST_LABEL_DATA = 'nsmc_test_label.npy'
DATA_CONFIGS = 'data_configs.json'

data_configs = {
    'vocab': word_vocab,
    'vocab_size': len(word_vocab) + 1  # size 1 추가
}

# if not os.path.exists(DATA_IN_PATH):
#     os.makedirs(DATA_IN_PATH)

# 전처리 학습 데이터 np로 저장
np.save(open(DATA_IN_PATH + TRAIN_INPUT_DATA, 'wb'), train_inputs)
np.save(open(DATA_IN_PATH + TRAIN_LABEL_DATA, 'wb'), train_labels)

# 전처리 평가 데이터 np로 저장
np.save(open(DATA_IN_PATH + TEST_INPUT_DATA, 'wb'), test_inputs)
np.save(open(DATA_IN_PATH + TEST_LABEL_DATA, 'wb'), test_labels)
# end::전처리 텍스트/라벨 저장[]

json.dump(data_configs, open(DATA_IN_PATH + DATA_CONFIGS, 'w'),
          ensure_ascii=False)

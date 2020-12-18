import json
import re

import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

# tag::read file[]
DATA_IN_PATH = './data_in/'
# ['id', 'qid1', 'qid2', 'question1', 'question2', 'is_duplicate']
train_data = pd.read_csv(DATA_IN_PATH + "train.csv", encoding='UTF-8')
# end::read file[]

# tag::라벨 개수의 평균을 맞추는 작업[]
train_pos_data = train_data.loc[train_data['is_duplicate'] == 1]
train_neg_data = train_data.loc[train_data['is_duplicate'] == 0]

print(train_neg_data.info())
print(train_pos_data.info())
class_difference = len(train_neg_data) - len(train_pos_data)
sample_frac = 1 - (class_difference / (len(train_neg_data)))
# negative 안에서 sample_frac 만큼 다시 추출해서 대입
# sample_frac == 0.5852831268846044
train_neg_data = train_neg_data.sample(frac=sample_frac)

print(f'중복 질문 개수: {len(train_pos_data)}')
print(f'중복이 아닌 질문 개수: {len(train_neg_data)}')

# 다시 합치기
train_data = pd.concat([train_neg_data, train_pos_data])
# end::라벨 개수의 평균을 맞추는 작업[]


# tag::1. 문자열에 대한 전처리[]
FILTERS = "([~.,!?\"':;)(])"
change_filter = re.compile(FILTERS)

# questions1 = [str(s) for s in train_data['question1']]
# questions2 = [str(s) for s in train_data['question2']]

questions1 = train_data.iloc[:, 3].astype(str).tolist()
questions2 = train_data.iloc[:, 4].astype(str).tolist()

filtered_questions1 = [re.sub(change_filter, "", q).lower() for q in questions1]
filtered_questions2 = [re.sub(change_filter, "", q).lower() for q in questions2]
# end::1. 문자열에 대한 전처리[]

# tag::tokenizer[]
# 두 **문장**을 합쳐 단어사전 생성
tokenizer = Tokenizer()
tokenizer.fit_on_texts(filtered_questions1 + filtered_questions2)
# end::tokenizer[]

# tag::**문장 안에** 있는 각 **단어**들을 인덱스로 변환[]
# [2, 21, 8569, 251, 46, 3017], [9, 15, 309, 43, 3, 56, 65, 515]
questions1_sequence = tokenizer.texts_to_sequences(filtered_questions1)
questions2_sequence = tokenizer.texts_to_sequences(filtered_questions2)
# end::**문장 안에** 있는 각 **단어**들을 인덱스로 변환[]


# tag::texts sequence padding[]
# 최대 길이는 질문의 평균 단어가 31개이기 때문이다.
# 저자 - **다양한 값으로 실험했을 때** 최고의 값
MAX_SEQUENCE_LENGTH = 31

q1_data = pad_sequences(questions1_sequence, maxlen=MAX_SEQUENCE_LENGTH, padding='post')
q2_data = pad_sequences(questions2_sequence, maxlen=MAX_SEQUENCE_LENGTH, padding='post')
# end::texts sequence padding[]


# type(tokenizer.word_index) == dict
assert type(tokenizer.word_index) == dict
word_vocab = tokenizer.word_index
# word_vocab["<PAD>"] = 0

labels = np.array(train_data['is_duplicate'], dtype=int)
print(f'Shape of question1 data: {q1_data.shape}')
print(f'Shape of question2 data: {q2_data.shape}')
print(f'Shape of label: {labels.shape}')
print(f'Words in index: {len(word_vocab)}')

# tag::단어 사전과 전체 단어 수 저장[]
data_configs = {
    'vocab': word_vocab,
    'vocab_size': len(word_vocab)
}

# TODO submit 251p: q1_train.npy => train_q1.npy, q2_train.npy => train_a2.npy
TRAIN_Q1_DATA = 'train_q1.npy'
TRAIN_Q2_DATA = 'train_q2.npy'

# TODO submit 251p: label_train.npy => train_label.npy
TRAIN_LABEL_DATA = 'train_label.npy'
DATA_CONFIGS = 'data_configs.json'

np.save(open(DATA_IN_PATH + TRAIN_Q1_DATA, 'wb'), q1_data)
np.save(open(DATA_IN_PATH + TRAIN_Q2_DATA, 'wb'), q2_data)
np.save(open(DATA_IN_PATH + TRAIN_LABEL_DATA, 'wb'), labels)

json.dump(data_configs, open(DATA_IN_PATH + DATA_CONFIGS, 'w'))
# end::단어 사전과 전체 단어 수 저장[]


# test_data 전처리 시작
# tag::test_data preprocessing[]
test_data = pd.read_csv(DATA_IN_PATH + 'test.csv', encoding='utf-8')

print(test_data.info())
valid_ids = [type(x) == int for x in test_data.test_id]
test_data = test_data[valid_ids].drop_duplicates()
print("-" * 30)
print(test_data.info())

test_questions1 = [str(s) for s in test_data['question1']]
test_questions2 = [str(s) for s in test_data['question2']]

filtered_test_questions1 = [re.sub(change_filter, "", q).lower() for q in test_questions1]
filtered_test_questions2 = [re.sub(change_filter, "", q).lower() for q in test_questions2]

test_questions1_sequence = tokenizer.texts_to_sequences(filtered_test_questions1)
test_questions2_sequence = tokenizer.texts_to_sequences(filtered_test_questions2)

test_q1_data = pad_sequences(test_questions1_sequence, maxlen=MAX_SEQUENCE_LENGTH, padding='post')
test_q2_data = pad_sequences(test_questions2_sequence, maxlen=MAX_SEQUENCE_LENGTH, padding='post')

# TODO submit 253p: (3563475, 11) => 31, [전체 문장 길이를 11로] => [전체 문장 길이를 31로]
print(f'Shape of question1 data: {test_q1_data.shape}')
print(f'Shape of question2 data: {test_q2_data.shape}')
# end::test_data preprocessing[]

test_id = np.array(test_data['test_id'])
TEST_Q1_DATA = 'test_q1.npy'
TEST_Q2_DATA = 'test_q2.npy'
TEST_ID_DATA = 'test_id.npy'

np.save(open(DATA_IN_PATH + TEST_Q1_DATA, 'wb'), test_q1_data)
np.save(open(DATA_IN_PATH + TEST_Q2_DATA, 'wb'), test_q2_data)
np.save(open(DATA_IN_PATH + TEST_ID_DATA, 'wb'), test_id)

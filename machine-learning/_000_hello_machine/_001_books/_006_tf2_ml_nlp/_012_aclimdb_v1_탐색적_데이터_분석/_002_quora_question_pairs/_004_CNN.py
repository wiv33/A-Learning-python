from abc import ABC

import numpy as np
import pandas as pd
import json
from tensorflow.keras import layers
import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import os
import matplotlib.pyplot as plt

SEED_NUM = 1234
tf.random.set_seed(SEED_NUM)

DATA_IN_PATH = './data_in/'
DATA_OUT_PATH = '/data_out/'

TRAIN_Q1_DATA_FILE = 'train_q1.npy'
TRAIN_Q2_DATA_FILE = 'train_q2.npy'
TRAIN_LABEL_DATA_FILE = 'train_label.npy'
DATA_CONFIGS = 'data_configs.json'

# tag::load data[]
q1_data = np.load(open(DATA_IN_PATH + TRAIN_Q1_DATA_FILE, 'rb'))
q2_data = np.load(open(DATA_IN_PATH + TRAIN_Q2_DATA_FILE, 'rb'))
labels = np.load(open(DATA_IN_PATH + TRAIN_LABEL_DATA_FILE, 'rb'))
prepro_configs = json.load(open(DATA_IN_PATH + DATA_CONFIGS, 'r'))


# end::load data[]

# tag::Embedding[]
class SentenceEmbedding(layers.Layer):
    def __init__(self, **kwargs):
        super(SentenceEmbedding, self).__init__()

        self.conv = layers.Conv1D(kwargs['conv_num_filters'],
                                  kwargs['conv_window_size'],
                                  activation=tf.keras.activations.relu,
                                  padding='same')
        self.max_pool = layers.MaxPool1D(kwargs['max_pool_seq_len'], 1)
        self.dense = layers.Dense(kwargs['sent_embedding_dimension'],
                                  activation=tf.keras.activations.relu)

    def call(self, x):
        x = self.conv(x)
        x = self.max_pool(x)
        x = self.dense(x)
        return tf.squeeze(x, 1)


# end::Embedding[]


# tag::model[]
class SentenceSimilarityModel(tf.keras.Model, ABC):
    def __init__(self, **kwargs):
        super(SentenceSimilarityModel, self).__init__(name=kwargs['model_name'])

        self.word_embedding = layers.Embedding(kwargs['vocab_size'], kwargs['word_embedding_dimension'])
        self.base_encoder = SentenceEmbedding(**kwargs)
        self.hypo_encoder = SentenceEmbedding(**kwargs)  # hypothesis - [ㅎㅏㅣ]이퍼[ㄸㅅㅔ]시스
        self.dense = layers.Dense(kwargs['hidden_dimension'],
                                  activation=tf.keras.activations.relu)
        self.logit = layers.Dense(1, activation=tf.keras.activations.sigmoid)
        self.dropout = layers.Dropout(kwargs['dropout_rate'])

    def call(self, x):
        x1, x2 = x
        b_x = self.word_embedding(x1)
        h_x = self.word_embedding(x2)
        b_x = self.dropout(b_x)
        h_x = self.dropout(h_x)

        b_x = self.base_encoder(b_x)
        h_x = self.hypo_encoder(h_x)

        e_x = tf.concat([b_x, h_x], -1)
        e_x = self.dense(e_x)
        e_x = self.dropout(e_x)
        return self.logit(e_x)


# end::model[]


model_name = 'cnn_similarity'
BATCH_SIZE = 1024
NUM_EPOCHS = 100
VALID_SPLIT = .1
MAX_LEN = 31

kwargs = {
    'model_name': model_name,
    # tag::단어 임베딩에 사용[]
    # TODO submit 265p: prepro_configs['vocab_size'] => vocab_size + 1 ?
    'vocab_size': prepro_configs['vocab_size'] + 1,
    'word_embedding_dimension': 100,
    # end::단어 임베딩에 사용[]
    # tag::합성곱에 사용[]
    'conv_num_filters': 300,
    'conv_window_size': 3,
    'max_pool_seq_len': MAX_LEN,
    # end::합성곱에 사용[]
    # tag::문장 임베딩 차원 값[]
    'sent_embedding_dimension': 128,
    # end::문장 임베딩 차원 값[]
    'dropout_rate': .2,
    # tag::마지막 Dense layer 차원 값[]
    'hidden_dimension': 200,
    # end::마지막 Dense layer 차원 값[]
    'output_dimension': 1
}

# tag::모델 생성[]
model = SentenceSimilarityModel(**kwargs)

model.compile(optimizer=tf.keras.optimizers.Adam(1e-3),
              loss=tf.keras.losses.BinaryCrossentropy(),
              metrics=[tf.keras.metrics.BinaryAccuracy(name='accuracy')])
# end::모델 생성[]

# tag::모델 학습 저장[]
earlystop_callback = EarlyStopping(monitor='val_accuracy', min_delta=.0001, patience=1)

checkpoint_path = DATA_OUT_PATH + model_name + '/weights.h5'
checkpoint_dir = os.path.dirname(checkpoint_path)

if os.path.exists(checkpoint_dir):
    print(f'{checkpoint_dir} - folder already exists\n')
else:
    os.makedirs(checkpoint_dir, exist_ok=True)
    print(f'{checkpoint_dir} - folder create complete\n')

cp_callback = ModelCheckpoint(checkpoint_path, monitor='val_accuracy',
                              verbose=1,
                              save_best_only=True,
                              save_weights_only=True)
# end::모델 학습 저장[]

# tag::fit[]
history = model.fit((q1_data, q2_data), labels, batch_size=BATCH_SIZE,
                    epochs=NUM_EPOCHS,
                    validation_split=VALID_SPLIT,
                    callbacks=[earlystop_callback, cp_callback])
# end::fit[]


# tag::visualizer[]
def plot_graphs(history, string):
    plt.plot(history.history[string])
    plt.plot(history.history['val_' + string], '')
    plt.xlabel("Epochs")
    plt.ylabel(string)
    plt.legend([string, 'val_' + string])
    plt.show()


plot_graphs(history, 'loss')
plot_graphs(history, 'accuracy')
# end::visualizer[]


DATA_IN_PATH = './data_in/'
# tag::submit[]
TEST_Q1_DATA_FILE = 'test_q1.npy'
TEST_Q2_DATA_FILE = 'test_q2.npy'
TEST_ID_DATA_FILE = 'test_id.npy'

test_q1_data = np.load(open(DATA_IN_PATH + TEST_Q1_DATA_FILE, 'rb'))
test_q2_data = np.load(open(DATA_IN_PATH + TEST_Q2_DATA_FILE, 'rb'))
test_id_data = np.load(open(DATA_IN_PATH + TEST_ID_DATA_FILE, 'rb'), allow_pickle=True)

SAVE_FILE_NM = 'weights.h5'
model.load_weights(os.path.join(DATA_OUT_PATH, model_name, SAVE_FILE_NM))

predictions = model.predict((test_q1_data, test_q2_data), batch_size=BATCH_SIZE)
predictions = predictions.squeeze(-1)

output = pd.DataFrame(data={'test_id': test_id_data, 'is_duplicate': list(predictions)})

output.to_csv(DATA_OUT_PATH + 'cnn_predict.csv', index=False, quoting=3)
# end::submit[]

# kaggle competitions submit -c quora-question-pairs -f cnn_predict.csv -m "submit predict by CNN"
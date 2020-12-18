import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import os
import json

from tqdm import tqdm

DATA_IN_PATH = './data_in/'
DATA_OUT_PATH = './data_out/'

INPUT_TRAIN_DATA = 'nsmc_train_input.npy'
LABEL_TRAIN_DATA = 'nsmc_train_label.npy'
DATA_CONFIGS = 'data_configs.json'

train_input = np.load(open(DATA_IN_PATH + INPUT_TRAIN_DATA, 'rb'))
train_input = pad_sequences(train_input, maxlen=train_input.shape[1])

train_label = np.load(open(DATA_IN_PATH + LABEL_TRAIN_DATA, 'rb'))
prepro_configs = json.load(open(DATA_IN_PATH + DATA_CONFIGS, 'r'))

# tag::파라미터 정의[]

model_name = 'cnn_classifier_kr'
BATCH_SIZE = 512
NUM_EPOCHS = 2
VALID_SPLIT = .1
MAX_LEN = train_input.shape[1]

kwargs = {'model_name': model_name,
          'vocab_size': prepro_configs['vocab_size'],
          'embedding_size': 128,
          'num_filters': 100,
          'dropout_rate': .5,
          'hidden_dimension': 250,
          'output_dimension': 1}


# end::파라미터 정의[]

# tag::모델함수[]

class CNNClassifier(tf.keras.Model):
    def __init__(self, **kwargs):
        super(CNNClassifier, self).__init__(name=kwargs['model_name'])
        self.embedding = layers.Embedding(input_dim=kwargs['vocab_size'],
                                          output_dim=kwargs['embedding_size'])
        self.conv_list = [layers.Conv1D(filters=kwargs['num_filters'],
                                        kernel_size=kernel_size,
                                        padding='valid',
                                        activation=tf.keras.activations.relu,
                                        kernel_constraint=tf.keras.constraints.MaxNorm(max_value=3.))
                          for kernel_size in [3, 4, 5]]
        self.pooling = layers.GlobalMaxPool1D()
        self.dropout = layers.Dropout(kwargs['dropout_rate'])
        self.fc1 = layers.Dense(units=kwargs['hidden_dimension'],
                                activation=tf.keras.activations.relu,
                                kernel_constraint=tf.keras.constraints.MaxNorm(max_value=3.))
        self.fc2 = layers.Dense(units=kwargs['output_dimension'],
                                activation=tf.keras.activations.sigmoid,
                                kernel_constraint=tf.keras.constraints.MaxNorm(max_value=3.))

    def call(self, x):
        x = self.embedding(x)
        x = self.dropout(x)
        x = tf.concat([self.pooling(conv(x)) for conv in self.conv_list], axis=1)
        x = self.fc1(x)
        x = self.fc2(x)
        return x


# end::모델함수[]


# tag::모델 학습[]
model = CNNClassifier(**kwargs)

model.compile(optimizer=tf.keras.optimizers.Adam(),
              loss=tf.keras.losses.BinaryCrossentropy(),
              metrics=[tf.keras.metrics.BinaryAccuracy(name='accuracy')])
# end::모델 학습[]


# tag::early callback[]
earlystop_callback = EarlyStopping(monitor='val_accruacy', min_delta=0.0001, patience=2)

checkpoint_path = DATA_OUT_PATH + model_name + '/weights.h5'
checkpoint_dir = os.path.dirname(checkpoint_path)

if os.path.exists(checkpoint_dir):
    print(f'{checkpoint_dir} - Folder already exists\n')
else:
    os.makedirs(checkpoint_dir, exist_ok=True)
    print(f'{checkpoint_dir} - Folder create complete \n')

cp_callback = ModelCheckpoint(checkpoint_path, monitor='val_accuracy',
                              verbose=1,
                              save_best_only=True,
                              save_weights_only=True)
# end::early callback[]

# tag::fit[]
history = model.fit(train_input, train_label, batch_size=BATCH_SIZE, epochs=NUM_EPOCHS,
                    validation_split=VALID_SPLIT, callbacks=[earlystop_callback, cp_callback])


def plot_graphs(history, string):
    plt.plot(history.history[string])
    plt.plot(history.history['val_' + string], '')
    plt.xlabel("Epochs")
    plt.ylabel(string)
    plt.legend([string, 'val_' + string])
    plt.show()


plot_graphs(history, 'loss')
plot_graphs(history, 'accuracy')
# end::fit[]


# tag::TEST[]
INPUT_TEST_DATA = 'nsmc_test_input.npy'
LABEL_TEST_DATA = 'nsmc_test_label.npy'
SAVE_FILE_NM = 'weights.h5'

test_input = np.load(open(DATA_IN_PATH + INPUT_TEST_DATA, 'rb'))
print(test_input)
print(test_input.shape[1])
test_input = pad_sequences(test_input, maxlen=test_input.shape[1])
test_label_data = np.load(open(DATA_IN_PATH + LABEL_TEST_DATA, 'rb'))
# end::TEST[]

model.load_weights(os.path.join(DATA_OUT_PATH, model_name, SAVE_FILE_NM))
model.evaluate(test_input, test_label_data)

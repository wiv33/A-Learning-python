import tensorflow as tf
from tensorflow import keras

print(tf.__version__)

# 신경망과 훈련 매개변수
EPOCHS = 200
BATCH_SIZE = 128
VERBEOSE = 1
NB_CLASSES = 10  # output의 demension
N_HIDDEN = 128
VALIDATION_SPLIT = 0.2  # 검증

# MNIST 데이터셋 로드
# 검증

mnist = keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
RESHAPED = 784

x_train = x_train.reshape(60000, RESHAPED)
x_test = x_test.reshape(10000, RESHAPED)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

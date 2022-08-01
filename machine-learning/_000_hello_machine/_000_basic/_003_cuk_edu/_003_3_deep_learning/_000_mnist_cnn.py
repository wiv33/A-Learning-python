
import numpy as np
from keras.datasets import mnist
from keras import layers, models, utils, callbacks
# LOAD LIBRARIES
from sklearn.model_selection import train_test_split
from keras.utils.np_utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D, AvgPool2D, BatchNormalization, Activation
import matplotlib.pyplot as plt
import tensorflow as tf
# tag::load data[]
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# end::load data[]

# tag::one hot encoding[]
num_classes = len(np.unique(y_test))

y_train = utils.to_categorical(y_train, num_classes)
y_test = utils.to_categorical(y_test, num_classes)
# end::one hot encoding[]


# tag::scale x 0 or 1[]
# 0-255 -> 0.0 - 1.0
x_train, x_test = x_train / 255., x_test / 255.
# end::scale x 0 or 1[]

# tag::expand dimension[]
# 맨 마지막에 차원을 확장(추가)한다.
x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)

# data shape
data_shape = x_train.shape[1:]
# end::expand dimension[]

# tag::divide train data and eval data[]
# 검증 시 기계가 한 번도 보지 못한 데이터로 하기 위함
x_train, x_eval = x_train[:50000], x_train[50000:]
y_train, y_eval = y_train[:50000], y_train[50000:]
# end::divide train data and eval data[]


tf.debugging.set_log_device_placement(True)
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:  # gpu가 있다면, 용량 한도를 5GB로 설정
  tf.config.experimental.set_virtual_device_configuration(gpus[0],
        [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=4*1024)])


# tag::build model[]
model = models.Sequential()

model.add(Conv2D(5,kernel_size=3,input_shape=(28,28,1)))
model.add(BatchNormalization())
model.add(Activation('relu'))

model.add(Flatten())
model.add(Dense(10, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics='accuracy')
# end::build model[]
print(model.summary())

# tag::train model[]
# 학습 시작
history = model.fit(x_train, y_train,
                    epochs=20,
                    batch_size=1,
                    verbose=True,
                    validation_data=(x_test, y_test))


def visit_score(name, sc):
    print('{}: {:.4f}'.format(name, sc))


sc_loss, sc_accuracy = model.evaluate(x_eval, y_eval)
visit_score('loss', sc_loss)
visit_score('accuracy', sc_accuracy)
# end::train model[]

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.show()

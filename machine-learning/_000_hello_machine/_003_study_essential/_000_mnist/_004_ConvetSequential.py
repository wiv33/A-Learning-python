import numpy as np
from keras.datasets import mnist
from tensorflow.keras import layers, models, utils

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


# tag::build model[]
model = models.Sequential([
    layers.Input(shape=data_shape),
    layers.Conv2D(filters=32, kernel_size=(3, 3)),
    layers.Activation(activation='relu'),
    layers.MaxPooling2D(pool_size=(2, 2)),

    layers.Conv2D(64, kernel_size=(3, 3)),
    layers.Activation('relu'),
    layers.MaxPooling2D(pool_size=(2, 2)),

    # flatten
    layers.Flatten(),
    layers.Dropout(.3),

    # output
    layers.Dense(units=10),
    layers.Activation('softmax'),
])

print(model.summary())

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics='accuracy')
# end::build model[]


# tag::train model[]
# 학습 시작
model.fit(x_train, y_train,
          epochs=5,
          batch_size=128,
          verbose=False,
          validation_data=(x_test, y_test),
          validation_split=.1, )


def visit_score(name, sc):
    print('{}: {:.4f}'.format(name, sc))


sc_loss, sc_accuracy = model.evaluate(x_eval, y_eval)
visit_score('loss', sc_loss)
visit_score('accuracy', sc_accuracy)
# end::train model[]

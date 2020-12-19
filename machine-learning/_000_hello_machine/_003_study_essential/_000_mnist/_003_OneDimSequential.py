from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# tag::load data[]
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# end::load data[]

# tag::label one hot encoding[]
num_classes = 10

y_train = to_categorical(y_train, num_classes)
y_test = to_categorical(y_test, num_classes)
# end::label one hot encoding[]

# tag::scale x[]
# scale 0 or 1
x_train = x_train / 255.
x_test = x_test / 255.
# 255 = 1, 0 = 0.
# end::scale x[]

# tag::divide train data and eval data[]
x_train, x_eval = x_train[:50000, ], x_train[50000:, ]
y_train, y_eval = y_train[:50000, ], y_train[50000:, ]
# end::divide train data and eval data[]
data_shape = x_train.shape[1:]
print(x_train.shape)

# tag::build model[]
model = models.Sequential([
    layers.Input(shape=data_shape),
    layers.Flatten(),  # 784
    layers.Dense(units=256),
    layers.Activation('relu'),
    layers.Dense(units=32),
    layers.Activation('relu'),

    # output
    layers.Dense(num_classes, activation='softmax'),
])
print(model.summary())

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics='accuracy')
# end::build model[]


# tag::train model[]
model.fit(x_train, y_train,
          epochs=5,
          batch_size=128,
          validation_data=(x_test, y_test),
          verbose=False,
          validation_split=.1)


# end::train model[]

def visit_score(name, sc):
    print('{}: {:.4f}'.format(name, sc))


score = model.evaluate(x_eval, y_eval)
visit_score('loss', score[0])
visit_score('accuracy', score[1])

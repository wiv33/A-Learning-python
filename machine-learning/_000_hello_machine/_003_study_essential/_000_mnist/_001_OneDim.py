import numpy as np
from tensorflow.keras import layers, models, activations, optimizers, losses
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# data load
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# one hot encoder
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# scale 0 or 1
x_train = x_train.astype(np.float32) / 255
x_test = x_test.astype(np.float32) / 255

# divide `train data` and `eval data`
x_train, x_eval = x_train[:50000, ], x_train[50000:, ]
y_train, y_eval = y_train[:50000, ], y_train[50000:, ]

# build model
X = layers.Input(shape=(28, 28))
H = layers.Flatten()(X)

H = layers.Dense(units=128)(H)
H = layers.Activation(activation='relu')(H)

H = layers.Dropout(rate=0.3)(H)
H = layers.Dense(units=10)(H)
Y = layers.Activation(activation=activations.softmax)(H)

model = models.Model(X, Y)

# train model
model.compile(loss=losses.categorical_crossentropy,
              optimizer=optimizers.Adam(learning_rate=0.001),
              metrics=['accuracy'])

print(model.summary())

history = model.fit(x_train, y_train,
                    epochs=5,
                    batch_size=33,
                    verbose=True,
                    validation_data=(x_test, y_test),
                    validation_split=0.1)

score = model.evaluate(x_eval, y_eval, verbose=False)
print('loss: {:.4f}'.format(score[0]))
print('accuracy: {:.4f}'.format(score[1]))

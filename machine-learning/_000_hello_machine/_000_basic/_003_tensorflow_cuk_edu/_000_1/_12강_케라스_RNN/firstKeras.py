# download
# https://github.com/keras-team/keras/tree/master/examples

from keras.preprocessing import sequence
from keras.datasets import imdb
from keras import layers, models


# 전처리
class Data:
    def __init__(self, max_features=20000, max_len=80):
        (x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)
        x_train = sequence.pad_sequences(x_train, maxlen=max_len)
        y_train = sequence.pad_sequences(y_train, max_len)

        self.x_train, self.y_train = x_train, y_train
        self.x_test, self.y_test = x_test, y_test


class RNN_LSTM(models.Model):
    def __init__(self, max_features, max_len):
        x = layers.Input((max_len,))
        h = layers.Embedding(max_features, 128)(x)
        h = layers.LSTM(128, dropout=0.2, recurrent_dropout=0.2)(h)
        y = layers.Dense(1, activation='sigmoid')(h)
        super().__init__(x, y)

        self.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


class Machine(object):
    def __init__(self, max_features=20000, max_len=80):
        self.data = Data(max_features, max_len)
        self.model = RNN_LSTM(max_features, max_len)

    def run(self, epoch=3, batch_size=32):
        data = self.data
        model = self.model
        model.fit(data.x_train, data.y_train, batch_size=batch_size, epoch=epoch,
                  validation_data=(data.x_test, data.y_test))
        score, acc = model.evaluate(data.x_test, data.y_test, batch_size=batch_size)

        print('Test performance : accuracy = {}, loss = {}'.format(acc, score))


def main():
    m = Machine()
    m.run()


if __name__ == '__main__':
    Data()

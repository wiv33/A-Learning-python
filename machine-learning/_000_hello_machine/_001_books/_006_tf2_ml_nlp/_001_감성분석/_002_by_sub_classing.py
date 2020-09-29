import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, preprocessing


class CustomModel(tf.keras.Model):
    def __init__(self, vocab_size, embed_dimension, hidden_dimension, output_dimension):
        super(CustomModel, self).__init__(name='custom_model')
        self.embedding = layers.Embedding(vocab_size, embed_dimension)
        self.dense_layer = layers.Dense(hidden_dimension, activation='swish')
        self.output_layer = layers.Dense(output_dimension, activation='sigmoid')

    def call(self, inputs):
        x = self.embedding(inputs)
        x = tf.reduce_mean(x, axis=1)
        x = self.dense_layer(x)
        return self.output_layer(x)


samples = [
    '너 오늘 예뻐 보인다.',
    '나는 오늘 기분이 더러워',
    '끝내주는데, 좋은 일이 있나봐',
    '나 좋은 일이 생겼어',
    '아 오늘 진짜 짜증나',
    '환상적인데, 정말 좋은거 같아',
]
labels = [[1], [0], [1], [1], [0], [1]]

tokenizer = preprocessing.text.Tokenizer()

tokenizer.fit_on_texts(samples)
input_sequences = tokenizer.texts_to_sequences(samples)
print(input_sequences)
word_index = tokenizer.word_index
# print(word_index)

batch_size = 2
num_epochs = 100
vocab_size = len(word_index) + 1
emb_size = 128
hidden_dimension = 256
output_dimension = 1

model = CustomModel(vocab_size=vocab_size,
                    embed_dimension=emb_size,
                    hidden_dimension=hidden_dimension,
                    output_dimension=output_dimension)

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.fit(input_sequences, labels, epochs=num_epochs, batch_size=batch_size)

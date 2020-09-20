import keras
from keras import models, layers

(train_images, train_labels), (test_images, test_labels) = keras.datasets.mnist.load_data()

# 훈련 데이터
train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255

# 테스트 데이터
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
network.add(layers.Dense(10, activation='softmax'))

network.compile(optimizer='rmsprop',
                # ValueError: Shapes (None, 1) and (None, 10) are incompatible
                # loss='categorical_crossentropy',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

network.summary()

"""
88p
네트워크 128개 샘플씩 미니 배치로 훈련 데이터를 다섯 번 반복한다.
(전체 훈련 데이터에 수행되는 각 반복을 에포크라 한다)
각 반복마다 네트워크가 배치에서 손실에 대한 가중치의 그래디언트를 계산하고,
가중치를 업데이트 한다.
다섯 번의 에포크 동안 네트워크는 2,345번의 그래디언트 업데이트를 수행할 것.
(에포크마다 496번, 마지막 샘플의 개수는 96개 {60000/128})
"""
network.fit(train_images, train_labels, epochs=5, batch_size=128)

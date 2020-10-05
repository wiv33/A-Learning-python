import matplotlib.pylab as plt
import tensorflow as tf
from tensorflow import keras

cifar10 = keras.datasets.cifar10

(train_data, train_labels), (test_data, test_labels) = cifar10.load_data()

train_dataset = tf.data.Dataset.from_tensor_slices((train_data, train_labels))
test_dataset = tf.data.Dataset.from_tensor_slices((test_data, test_labels))

for image, label in train_dataset.take(2):
    plt.figure()
    plt.imshow(image)


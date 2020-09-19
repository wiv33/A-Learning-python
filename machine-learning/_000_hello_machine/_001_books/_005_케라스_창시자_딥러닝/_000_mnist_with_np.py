import matplotlib.pylab as plt
from keras.datasets import mnist

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print("{}\n{}\n{}".format(train_images.shape, train_images.ndim, train_images.dtype))

plt.imshow(train_images[4], cmap=plt.cm.binary)
plt.show()

print(train_images[10:100].shape)
print(train_images[10:100, :, :].shape)
print(train_images[10:100, :28, :28].shape)

print(train_images[:, :14, :14].shape)
print(train_images[:, 7:-7, 7:-7].shape)



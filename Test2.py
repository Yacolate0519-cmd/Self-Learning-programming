import matplotlib.pyplot as plt
import tensorflow as tf

tf.config.list_physical_devices('GPU')
data_idx = 42

fashion_mnist = tf.keras.datasets.fashion_mnist(train_images, train_labels)
(valid_images, valid_labels) = fashion_mnist.load_data()

plt.show()
plt.imshow(train_images[data_idx], cmap = 'gray')
plt.colorbar()
plt.grid(False)
plt.show()

import os

from numpy import genfromtxt
from PIL import Image
import numpy as np

my_data = genfromtxt('sign_mnist_train.csv', delimiter=',')[1:]
my_data2 = genfromtxt('sign_mnist_test.csv', delimiter=',')[1:]
my_data = np.concatenate((my_data, my_data2), axis=0)

image_names = my_data[:, 0]
image_pixels = my_data[:, 1:]

image_size = int(np.sqrt(image_pixels.shape[1]))

iter = 0
labels = "ABCDEFGHIGKLMNOPQRSTUVWXYZ"

for i in range(len(image_names)):
    image_data = image_pixels[i, :].reshape((image_size, image_size)).astype(np.uint8)

    image = Image.fromarray(image_data)

    image_name = str(int(image_names[i]))
    image_name_iter = str(int(image_names[i]))+str(iter) + '_mnist.jpg'
    if not os.path.exists(f'sign_language_dataset/{labels[int(image_name)]}'):
        os.makedirs(f'sign_language_dataset/{labels[int(image_name)]}')
    image.save(f'sign_language_dataset/{labels[int(image_name)]}/{labels[int(image_name)]}{image_name_iter}')
    iter += 1

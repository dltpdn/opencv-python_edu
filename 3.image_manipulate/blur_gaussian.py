import cv2
import numpy as np
import matplotlib.pyplot as plt

file_name = '../img/gaussian_noise.jpg'

img = cv2.imread(file_name)
blur = cv2.GaussianBlur(img, (5, 5), 0)

gaussk = cv2.getGaussianKernel(5, 0)
blur2 = cv2.filter2D(img, -1, gaussk*gaussk.T)
print(gaussk)
print(blur2)

plt.subplot(131)
plt.imshow(img)
plt.title('origin')

plt.subplot(132)
plt.imshow(blur)
plt.title('GaussianBlur')

plt.subplot(133)
plt.imshow(blur2)
plt.title('getGaussian')

plt.show()

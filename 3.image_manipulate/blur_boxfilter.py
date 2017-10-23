import cv2
import numpy as np
import matplotlib.pyplot as plt

file_name = '../img/opencv_logo.png'

img = cv2.imread(file_name)
blur1 = cv2.boxFilter(img, -1, (5,5))
blur2 = cv2.boxFilter(img, -1, (5,5), normalize=False)


plt.subplot(131)
plt.imshow(img)
plt.title('origin')

plt.subplot(132)
plt.imshow(blur1)
plt.title('boxFilter')

plt.subplot(133)
plt.imshow(blur2)
plt.title('normalize-False')

plt.show()

import cv2
import numpy as py
import matplotlib.pyplot as plt

file_name = "../img/salt_pepper_noise.jpg"

img = cv2.imread(file_name)
blur = cv2.medianBlur(img, 7)

plt.subplot(121)
plt.imshow(img)
plt.title('original')

plt.subplot(122)
plt.imshow(blur)
plt.title('mediaBlur')

plt.show()

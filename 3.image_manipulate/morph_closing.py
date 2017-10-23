import cv2
import numpy as np
import matplotlib.pyplot as plt

file_name = '../img/morph_hole.png'
img = cv2.imread(file_name)

k = np.ones( (5,5), np.uint8)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, k)

plt.subplot(121)
plt.imshow(img)
plt.title('Original')

plt.subplot(122)
plt.imshow(closing)
plt.title('Opening')

plt.show()
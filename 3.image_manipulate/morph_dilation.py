import cv2
import numpy as np
import matplotlib.pyplot as plt

file_name = '../img/morphological.png'
img = cv2.imread(file_name)

k = np.ones( (5,5), np.uint8)
dst = cv2.dilate(img, k)

plt.subplot(121)
plt.imshow(img)
plt.title('Original')

plt.subplot(122)
plt.imshow(dst)
plt.title('Dilation')

plt.show()
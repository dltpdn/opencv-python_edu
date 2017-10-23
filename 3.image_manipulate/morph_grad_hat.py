import cv2
import numpy as np
import matplotlib.pyplot as plt

file_name = '../img/moon_gray.jpg'
img = cv2.imread(file_name)

k5 = np.ones( (5,5), np.uint8)
k9 = cv2.getStructuringElement(cv2.MORPH_RECT, (9,9))

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, k9)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, k9)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, k9)

imgs = [img, gradient, tophat, blackhat]
tits = ['Original', 'Gradient', 'Top Hat', 'Black Hat']

for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(imgs[i])
    plt.title(tits[i])
    plt.xticks([]), plt.yticks([])

plt.show()
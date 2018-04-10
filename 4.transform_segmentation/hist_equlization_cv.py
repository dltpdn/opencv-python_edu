import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread('../img/yate.jpg', cv2.IMREAD_GRAYSCALE)

img2 = cv2.equalizeHist(img)
merged = np.hstack((img, img2))
cv2.imshow('result', merged)
hist = cv2.calcHist([img], [0], None, [256], [0, 255])
hist2 = cv2.calcHist([img2], [0], None, [256], [0,255])

plt.subplot(121)
plt.plot(hist)
plt.subplot(122)
plt.plot(hist2)
plt.show()
import numpy as np
import cv2
import matplotlib.pylab as plt

filename = '../img/model3.jpg'
img1 = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)




plt.subplot(131)
hist1 = cv2.calcHist([img1], [0], None, [256], [0,256])
plt.plot(hist1)
plt.title('cv2.calcHist')

plt.subplot(132)
hist2, bins = np.histogram(img1.ravel(), 256, [0, 256])
plt.plot(hist2)
plt.title('np.histogram')

plt.subplot(133)
plt.hist(img1.ravel(), 256, [0,256])
plt.title('plt.hist')

plt.show()

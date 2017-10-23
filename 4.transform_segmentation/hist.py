import numpy as np
import cv2
import matplotlib.pylab as plt

filename = '../img/model3.jpg'
#filename = '../img/rgb.jpg'
img1 = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(filename)




plt.subplot(141)
hist1 = cv2.calcHist([img1], [0], None, [256], [0,256])
print(hist1.shape)
print(hist1)
plt.plot(hist1)
plt.title('cv2.calcHist')

plt.subplot(142)
hist2, bins = np.histogram(img1.ravel(), 256, [0, 256])
plt.plot(hist2)
plt.title('np.histogram')

plt.subplot(143)
plt.hist(img1.ravel(), 256, [0,256])
plt.title('plt.hist')

plt.subplot(144)
plt.title('color hist')
color=('b', 'g', 'r')
for i, clr in enumerate(color):
    hist = cv2.calcHist([img2], [i], None, [256], [0, 256])
    plt.plot(hist, color=clr)
    
plt.show()

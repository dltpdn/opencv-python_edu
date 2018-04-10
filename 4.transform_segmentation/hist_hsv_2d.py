import cv2
import matplotlib.pylab as plt

img = cv2.imread('../img/chroma_key.jpg')
cv2.imshow('chromakey', img)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

hist0 = cv2.calcHist([hsv], [0], None, [180], [0, 180])
hist1 = cv2.calcHist([hsv], [1], None, [256], [0, 256])
plt.subplot(131)
plt.plot(hist0)
plt.plot(hist1)

hist2d = cv2.calcHist([hsv], [0,1], None, [180, 256], [0, 180, 0,256])
cv2.imshow('hist2d', hist2d)
plt.subplot(132)
plt.plot(hist2d)

hist2d_ = cv2.calcHist([hsv], [0,1], None, [60, 64], [0, 180, 0,256])
plt.subplot(133)
p= plt.imshow(hist2d_)
plt.colorbar(p)
plt.show()


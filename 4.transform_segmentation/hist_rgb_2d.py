import numpy as np
import cv2
import matplotlib.pylab as plt


filename = '../img/wingwall.jpg'
img = cv2.imread(filename)

chans = cv2.split(img)
plt.subplot(131)
#p = plt.imshow(cv2.calcHist([img], [0,1], None, [32, 32], [0,256, 0,256]))
p = plt.imshow(cv2.calcHist([img], [0,1], None, [32, 32], [0,256, 0,256]))
plt.colorbar(p)
plt.title('2D Histo for B and R')


plt.subplot(132)
p = plt.imshow(cv2.calcHist([img], [1,2], None, [32, 32], [0,256, 0,256]))
plt.colorbar(p)
plt.title('2D Histo for G and R')

plt.subplot(133)
p = plt.imshow(cv2.calcHist([img], [0,2], None, [32, 32], [0,256, 0,256]))
plt.colorbar(p)
plt.title('2D Histo for B and R')

plt.show()

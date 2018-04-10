import numpy as np
import cv2
import matplotlib.pylab as plt


filename = '../img/wingwall.jpg'
img = cv2.imread(filename)


plt.subplot(121)
plt.imshow(img[:,:,::-1])

plt.subplot(122)
plt.title('color hist')
color=('b', 'g', 'r')
for i, clr in enumerate(color):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=clr)
    
plt.show()

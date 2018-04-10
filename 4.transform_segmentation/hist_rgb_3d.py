import numpy as np
import cv2
import matplotlib.pylab as plt

# Not woking source code. 

filename = '../img/wingwall.jpg'
img = cv2.imread(filename)
hist = cv2.calcHist([img], [0,1,2], None, [8,8,8], [0,256, 0,256, 0,256])
print(hist)
p = plt.imshow(hist)
plt.colorbar(p)
plt.title('3D Histo for B and R')

plt.show()

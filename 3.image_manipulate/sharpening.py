import cv2
import numpy as np
import matplotlib.pylab as plt

file_name="../img/moon_gray.jpg"

img = cv2.imread(file_name)
kernel1 = np.array([[-1, -1, -1],
                    [-1, 9, -1],
                     [-1, -1, -1]]) 
dst1 = cv2.filter2D(img, -1, kernel1) 
kernel2 = np.array([[0, -1, 0],
                    [-1, 5, -1],
                     [0, -1, 0]]) 
dst2 = cv2.filter2D(img, -1, kernel2) 

plt.subplot(1,3,1)
plt.imshow( img)
plt.title('origin')

plt.subplot(1,3,2)
plt.imshow( dst1)
plt.title('sharpening')

plt.subplot(1,3,3)
plt.imshow( dst2)
plt.title('Laflacian')
plt.show()

import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread('../img/yate.jpg')
img2 = img.copy()

for c in range(0, 2):
   img2[:,:,c] = cv2.equalizeHist(img[:,:,c])

merged = np.hstack((img, img2))
cv2.imshow('result', merged)
cv2.waitKey()
cv2.destroyAllWindows()
import cv2
import numpy as np
import matplotlib.pylab as plt

#HSV equalizeHist() is not effective
img = cv2.imread('../img/yate.jpg')
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

img_hsv[:,:,2] = cv2.equalizeHist(img_hsv[:,:,2])

img2 = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

merged = np.hstack((img, img2))
cv2.imshow('result', merged)
cv2.waitKey()
cv2.destroyAllWindows()
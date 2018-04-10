import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread('../img/yate.jpg')
img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
img2 = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

merged = np.hstack((img, img2))
cv2.imshow('result', merged)
cv2.waitKey()
cv2.destroyAllWindows()
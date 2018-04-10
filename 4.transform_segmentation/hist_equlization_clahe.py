import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread('../img/yate.jpg', cv2.IMREAD_GRAYSCALE)
clahe = cv2.createCLAHE(clipLimit=2,  tileGridSize=(8,8))
img2 = clahe.apply(img)

merged = np.hstack((img, img2))
cv2.imshow('result', merged)
cv2.waitKey()
cv2.destroyAllWindows()
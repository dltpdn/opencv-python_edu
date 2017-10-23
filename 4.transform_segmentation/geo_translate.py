import cv2
import numpy as np
img = cv2.imread('../img/fish.jpg')
rows,cols = img.shape[0:2]

M = np.float32([[1,0,100],
                [0,1,50]])  # matrix
dst = cv2.warpAffine(img,M,(cols+100,rows+50))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
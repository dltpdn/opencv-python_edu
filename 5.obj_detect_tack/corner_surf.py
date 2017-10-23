import cv2
import numpy as np

img = cv2.imread('../img/model.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

surf = cv2.xfeatures2d.SURF_create()
surf.setHessianThreshold(10000)

#surf.setUpright(True)
keypoints, desc = surf.detectAndCompute(gray, None)
#img = cv2.drawKeypoints(img, keypoints, img)
img = cv2.drawKeypoints(img, keypoints, img, (255,0,0),4)

cv2.imshow('SURF', img)
cv2.waitKey()
cv2.destroyAllWindows()
import cv2
import numpy as np

img = cv2.imread('../img/model.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#sift = cv2.SIFT() #for v 2.4
sift = cv2.xfeatures2d.SIFT_create() # for v3.2+
keypoints = sift.detect(gray, None)
img = cv2.drawKeypoints(img, keypoints, img)
cv2.imshow('SIFT', img)
img = cv2.drawKeypoints(img, keypoints, img, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('SIFT DRAW', img)
cv2.waitKey()
cv2.destroyAllWindows()
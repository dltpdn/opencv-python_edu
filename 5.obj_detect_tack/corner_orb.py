import cv2
import numpy as np

img = cv2.imread('../img/model.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

orb = cv2.ORB_create()
kp, desc = orb.detectAndCompute(img, None)

img = cv2.drawKeypoints(img, kp, img,  flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('ORB', img)

cv2.waitKey()
cv2.destroyAllWindows()
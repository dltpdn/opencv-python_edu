import cv2
import numpy as np

img = cv2.imread('../img/rpi_box.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('../img/box_on_desk.jpg', cv2.IMREAD_GRAYSCALE)
res = None

orb = cv2.ORB_create()
kp1, desc1 = orb.detectAndCompute(img, None)
kp2, desc2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(desc1, desc2)

matches = sorted(matches, key=lambda x:x.distance)
res = cv2.drawMatches(img, kp1, img2, kp2, matches[:30], res, flags=0)

cv2.imshow('Feature Matching', res)

cv2.waitKey()
cv2.destroyAllWindows()

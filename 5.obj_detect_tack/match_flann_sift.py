import cv2, numpy as np
from nbformat.sign import algorithms

img1 = cv2.imread('../img/rpi_box.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('../img/box_on_desk.jpg', cv2.IMREAD_GRAYSCALE)
res = None

sift = cv2.xfeatures2d.SIFT_create()
kp1, desc1 = sift.detectAndCompute(img1, None)
kp2, desc2 = sift.detectAndCompute(img2, None)

FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)

flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(desc1, desc2, k=2)

factor=0.7
good = []
for m,n in matches:
    if m.distance < factor*n.distance:
        good.append(m)
res = cv2.drawMatches(img1, kp1, img2, kp2, good, res)
cv2.imshow('Matching', res)
cv2.waitKey()
cv2.destroyAllWindows()
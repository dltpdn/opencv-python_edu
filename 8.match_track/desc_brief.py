import cv2
import numpy as np

img = cv2.imread('../img/house.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#star = cv2.xfeatures2d.StarDetector_create()
fast = cv2.FastFeatureDetector_create(50)
brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()

kp1 = fast.detect(img, None)
kp2, desc = brief.compute(img, kp1)

print(desc.shape)
print(desc)
img1 = cv2.drawKeypoints(img, kp1, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
img2 = cv2.drawKeypoints(img, kp2, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('BRIEF', img1)
cv2.imshow('BRIEF2', img2)

cv2.waitKey()
cv2.destroyAllWindows()
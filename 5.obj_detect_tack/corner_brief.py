import cv2
import numpy as np

img = cv2.imread('../img/model.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

star = cv2.xfeatures2d.StarDetector_create()
brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()

kp1 = star.detect(img, None)
kp2, desc = brief.compute(img, kp1)

print(desc.shape)
print(desc)
img = cv2.drawKeypoints(img, kp1, img)
img = cv2.drawKeypoints(img, kp2, img)

cv2.imshow('BRIEF', img)

cv2.waitKey()
cv2.destroyAllWindows()
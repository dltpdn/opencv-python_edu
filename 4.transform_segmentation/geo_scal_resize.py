import cv2
import numpy as np

img = cv2.imread('../img/fish.jpg')
height, width = img.shape[:2]
shrink = cv2.resize(img,None,fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)
zoom = cv2.resize(img,(int(1.5*width), int(1.5*height)), interpolation = cv2.INTER_CUBIC)

cv2.imshow("original", img)
cv2.imshow("shirink", shrink)
cv2.imshow("zoom", zoom)
cv2.waitKey(0)
cv2.destroyAllWindows()
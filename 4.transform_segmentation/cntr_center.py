import cv2
import numpy as np

file_name = "../img/shapes.png"
img = cv2.imread(file_name)
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, th = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY_INV)

img2, contours, hierachy = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    mmt = cv2.moments(c)
    cx = int(mmt['m10']/mmt['m00'])
    cy = int(mmt['m01']/mmt['m00'])
    print("cent:",cx, cy)
    print("area:", mmt['m00'], cv2.contourArea(c))
    print("perimeter:", cv2.arcLength(c, True))
    cv2.circle(img, (cx, cy), 5, (0, 0, 255), -1)

for key, value in mmt.items():
    print("%s:%f" % (key,value) )
    

cv2.imshow('center', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


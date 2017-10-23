import cv2
import numpy as np

def getCentroid(contour):
    mmt = cv2.moments(contour)
    cx = int(mmt['m10']/ mmt['m00'])
    cy = int(mmt['m01']/ mmt['m00'])
    return (cx, cy)


file_name = '../img/shapes.png'
img = cv2.imread(file_name)
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, th = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY_INV)
_,contours, _ = cv2.findContours(th, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE )

print('Number of contours:', len(contours))

contours.sort(key=getCentroid)
for i, contour in enumerate(contours,1):
    cx,cy = getCentroid(contour)
    cv2.drawContours(img, [contour], -1, (0,255,0), -1)
    cv2.putText(img, '%d'%i, (cx,cy), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,255), 2)
    cv2.imshow('count shapes', img)
    cv2.waitKey(0)

cv2.destroyAllWindows()
import cv2
import numpy as py

file_name = '../img/4star.jpg'
img = cv2.imread(file_name)
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, th = cv2.threshold(imgray, 127,255, cv2.THRESH_BINARY_INV)
_, contours, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

contour = contours[0]
hull = cv2.convexHull(contour)
cv2.drawContours(img, [hull], 0, (0,0,255),2)
hull = cv2.convexHull(contour, returnPoints=False)

defects = cv2.convexityDefects(contour, hull)
print(defects, defects.shape)

for i in range(defects.shape[0]):
    startP, endP, farthestP, distance = defects[i, 0]
    start = tuple(contour[startP][0])
    end = tuple(contour[endP][0])
    farthest = tuple(contour[farthestP][0])
    
    cv2.circle(img, farthest, 3, (0,255,0), -1)
cv2.imshow('Convex defects', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
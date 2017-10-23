import cv2
import numpy as py

file_name = '../img/4star.jpg'
img = cv2.imread(file_name)
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, th = cv2.threshold(imgray, 127,255, cv2.THRESH_BINARY_INV)
_, contours, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

contour = contours[0]
cv2.drawContours(img, [contour], 0, (0,255,0),2)

p1 = (100,100)
p2 = (200,200)
cv2.circle(img, p1, 3, (255,0,0), -1)
cv2.circle(img, p2, 3, (255,0,255), -1)

dist1 = cv2.pointPolygonTest(contour, p1, True)
dist2 = cv2.pointPolygonTest(contour, p2, True)
print(dist1, dist2)
cv2.putText(img, '%f'%dist1, p1, cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
cv2.putText(img, '%f'%dist2, p2, cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)

cv2.imshow('Convex defects', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
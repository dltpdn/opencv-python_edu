import cv2
import numpy as np

file_name = '../img/hand_drawn.jpg'
img = cv2.imread(file_name)
img2 = img.copy()
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, th = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY_INV)
temp, contours, heiarchy = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
cv2.drawContours(img, [cnt], -1, (0, 255,0), 3)

print(cv2.isContourConvex(cnt))
hull = cv2.convexHull(cnt)
cv2.drawContours(img2, [hull], -1, (0,255,0), 3)

cv2.imshow('contour', img)
cv2.imshow('convex hull', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np

file_name = "../img/lightning.png"
img = cv2.imread(file_name)
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, th = cv2.threshold(imgray, 127,255,cv2.THRESH_BINARY_INV)

im, contours, hr = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contr = contours[0]

rows,cols = img.shape[:2]
[vx,vy,x,y] = cv2.fitLine(contr, cv2.DIST_L2,0,0.01,0.01)
print(vx,vy,x,y)
cv2.line(img,(0,-x*(vy/vx) + y), (cols-1, (cols-x)*(vy/vx) + y),(0,255,0),2)
cv2.circle(img, (x, y), 3, (0,0,255), -1)

cv2.imshow('Enclosing Circle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
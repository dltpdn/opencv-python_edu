import cv2
import numpy as np

img = cv2.imread('../img/sudoku.jpg')
c,w,h = img.shape[::-1]
print(w, h)
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(imgray, 100, 200 )
lines = cv2.HoughLines(edges, 1, np.pi/180, 130)
print(len(lines))
for line in lines:
    r,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    print(r, (a, b))
    x0 = a*r
    y0 = b*r
    cv2.circle(img, (abs(x0), abs(y0)), 3, (0,0,255), -1)
   
    x1 = int(x0 + w*(-b))
    y1 = int(y0 + h * a)
    x2 = int(x0 - w*(-b))
    y2 = int(y0 - h*a)
    cv2.line(img, (x1, y1), (x2, y2), (0,255,0), 1)
    print(x0, y0, x1, y1, x2, y2)
cv2.imshow('hough line', img)
cv2.waitKey()
cv2.destroyAllWindows()
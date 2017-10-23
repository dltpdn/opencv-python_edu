import cv2
import numpy as np

img = cv2.imread('../img/sudoku.jpg')
c,w,h = img.shape[::-1]
print(w, h)
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(imgray, 100, 200 )
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, 5, 10)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1,y1), (x2, y2), (0,255,0), 1)


cv2.imshow('Probability hough line', img)
cv2.waitKey()
cv2.destroyAllWindows()
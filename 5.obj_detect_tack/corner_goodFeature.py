import cv2
import numpy as np

img = cv2.imread('../img/chess_board.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 81, 0.01, 10)
corners = np.int0(corners)

for corner in corners:
    x, y = corner[0]
    cv2.rectangle(img, (x-10, y-10), (x+10, y+10), (0,255,0), 2)

cv2.imshow('Corners', img)
cv2.waitKey()
cv2.destroyAllWindows()
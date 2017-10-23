import cv2
import numpy as np

img = cv2.imread('../img/chess_board.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corner = cv2.cornerHarris(gray, 2,3,0.05)
corner = cv2.dilate(corner, None)
print(corner.min(), corner.max())
print(img.shape, corner.shape)
img[ corner >0.1*  corner.max() ] = [0,0,255]
cv2.imshow('Harris Corner', img)
cv2.waitKey()
cv2.destroyAllWindows()
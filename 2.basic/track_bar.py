import cv2
import numpy as np

def callback(x):
    print(x)
    r = cv2.getTrackbarPos('R','track-bar')
    g = cv2.getTrackbarPos('G','track-bar')
    b = cv2.getTrackbarPos('B','track-bar')
    img[:] = [b,g,r]

img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('track-bar')
cv2.createTrackbar('R','track-bar',0,255, callback)
cv2.createTrackbar('G','track-bar',0,255, callback )
cv2.createTrackbar('B','track-bar',0,255, callback)

while(1):
    cv2.imshow('track-bar',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
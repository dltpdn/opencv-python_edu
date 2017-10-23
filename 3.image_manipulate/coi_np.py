import cv2, time
import numpy as np

img = cv2.imread('../img/wingwall.jpg')
h, w = img.shape[:2]

b,g,r = img[:,:,0], img[:,:,1], img[:,:,2] 

blue = np.zeros( (h, w, 3), dtype=np.uint8)
blue[:,:,0] = b
green = np.zeros( (h, w, 3), dtype=np.uint8)
green[:,:,1] = g
red = np.zeros((h, w, 3), dtype=np.uint8)
red[:,:,2] = r

cv2.imshow('oring', img)
cv2.imshow('blue', blue)
cv2.imshow('green', green)
cv2.imshow('red', red)

cv2.waitKey(0)
cv2.destroyAllWindows()
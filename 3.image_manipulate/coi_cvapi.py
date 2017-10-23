import cv2, time
import numpy as np

img = cv2.imread('../img/wingwall.jpg')
h, w = img.shape[:2]

b,g,r = cv2.split(img)  

z = np.zeros( (h, w) , dtype=np.uint8)
blue = cv2.merge( (b, z, z))
green = cv2.merge((z, g, z))
red = cv2.merge((z, z, r))

cv2.imshow('blue', blue)
cv2.imshow('green', green)
cv2.imshow('red', red)

cv2.waitKey(0)
cv2.destroyAllWindows()
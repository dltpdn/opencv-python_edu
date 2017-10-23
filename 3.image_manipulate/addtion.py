import cv2
import numpy as np

a = np.array([250], dtype=np.uint8)
b = np.array([10], dtype=np.uint8)
c = a + b
print(a, b)
print( a+b )  # 250 + 10 = 260, 260 - 256 = 4
print( cv2.add(a, b)) #over 255

img1 = cv2.imread('../img/wingwall.jpg')
img2 = cv2.imread('../img/yate.jpg')

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img1+img2', img1+img2)
cv2.imshow('cv2.add(img1,img2)', cv2.add(img1,img2))

cv2.waitKey(0)
cv2.destroyAllWindows()
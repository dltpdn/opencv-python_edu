import numpy as np, cv2

img1 = np.zeros( ( 200,400), dtype=np.uint8)
img2 = np.zeros( ( 200,400), dtype=np.uint8)

img1[:, :200] = 255
img2[100:150, 150:350] = 255

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)

cv2.imshow('bitwise_and', cv2.bitwise_and(img1, img2))
cv2.imshow('bitwise_or', cv2.bitwise_or(img1, img2))
cv2.imshow('bitwise_xor', cv2.bitwise_xor(img1, img2))
cv2.imshow('bitwise_not(img1)', cv2.bitwise_not(img1))
cv2.waitKey()
cv2.destroyAllWindows()


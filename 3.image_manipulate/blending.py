import cv2
import numpy as np

alpha = 0.5

a = np.array([250], dtype=np.uint8)
b = np.array([10], dtype=np.uint8)
c = (1- alpha) * a  + alpha * b
c = c.astype(np.uint8)
print( a, b, c )

img1 = cv2.imread('../img/wingwall.jpg')
img2 = cv2.imread('../img/yate.jpg')

blended = img1 *alpha + img2 * (1-alpha)
blended = blended.astype(np.uint8)
cv2.imshow('img1 * 0.3 + img2 * 0.7', blended)

dst = cv2.addWeighted(img1, alpha, img2, (1-alpha), 0) #src1, alpha, src2, beta(1-alpha), gamma ==> src*alpha + src2*beta +gamma
cv2.imshow('cv2.addWeighted', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
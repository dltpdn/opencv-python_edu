import cv2
import numpy as np

img = cv2.imread('../img/water_coins.jpg')
cv2.imshow('original', img)
cv2.waitKey()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('gray', gray)
#cv2.waitKey()
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
#cv2.imshow('thresh', thresh)
#cv2.waitKey()

kernel = np.ones((3,3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
#cv2.imshow('opening', opening)
#cv2.waitKey()

sure_bg = cv2.dilate(opening, kernel, iterations=3)
#cv2.imshow('sure_bg', sure_bg)
#cv2.waitKey()

dst = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
print(dst.min(),dst.max())
dst = ( (dst / (dst.max() - dst.min())) * 255 ).astype(np.uint8)
cv2.imshow('dist_transform', dst)
cv2.waitKey()

ret, sure_fg = cv2.threshold(dst, 0.7*dst.max(), 255,0)
cv2.imshow('sure_fg', sure_fg)
cv2.waitKey()

unkown = cv2.subtract(sure_bg, sure_fg)
cv2.imshow('unkown', unkown)
cv2.waitKey()
ret, markers = cv2.connectedComponents(sure_fg)
markers = markers+1
markers[unkown ==255] = 0
cv2.imshow('marker', markers.astype(np.uint8))
cv2.waitKey()

markers = cv2.watershed(img, markers)
img[markers == -1] = [0,0,255]
cv2.imshow('watershed', img)
cv2.waitKey()


cv2.destroyAllWindows()
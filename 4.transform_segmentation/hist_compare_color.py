import cv2

img1 = cv2.imread('../img/observatory1.jpg')
img2 = cv2.imread('../img/observatory2.jpg')
img3 = cv2.imread('../img/observatory3.jpg')
img4 = cv2.imread('../img/danjong.jpg')

hsv1 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
hsv2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
hsv3 = cv2.cvtColor(img3, cv2.COLOR_BGR2HSV)
hsv4 = cv2.cvtColor(img4, cv2.COLOR_BGR2HSV)

hist1 = cv2.calcHist([hsv1], [0,1], None, [180,256], [0,180,0, 256])
hist2 = cv2.calcHist([hsv2], [0,1], None, [180,256], [0,180,0, 256])
hist3 = cv2.calcHist([hsv3], [0,1], None, [180,256], [0,180,0, 256])
hist4 = cv2.calcHist([hsv4], [0,1], None, [180,256], [0,180,0, 256])

cv2.normalize(hist1, hist1, 0, 1, cv2.NORM_MINMAX)
cv2.normalize(hist2, hist2, 0, 1, cv2.NORM_MINMAX)
cv2.normalize(hist3, hist3, 0, 1, cv2.NORM_MINMAX)
cv2.normalize(hist4, hist4, 0, 1, cv2.NORM_MINMAX)

ret1 = cv2.compareHist(hist1, hist1, cv2.HISTCMP_CORREL)
ret2 = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
ret3 = cv2.compareHist(hist1, hist3, cv2.HISTCMP_CORREL)
ret4 = cv2.compareHist(hist1, hist4, cv2.HISTCMP_CORREL)
print(ret1, ret2, ret3, ret4)
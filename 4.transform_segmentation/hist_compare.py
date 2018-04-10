import cv2

img1 = cv2.imread('../img/observatory1.jpg')
img2 = cv2.imread('../img/observatory2.jpg')
img3 = cv2.imread('../img/observatory3.jpg')
img4 = cv2.imread('../img/danjong.jpg')

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
gray3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
gray4 = cv2.cvtColor(img4, cv2.COLOR_BGR2GRAY)

hist1 = cv2.calcHist([gray1], [0], None, [256], [0, 256])
hist2 = cv2.calcHist([gray2], [0], None, [256], [0, 256])
hist3 = cv2.calcHist([gray3], [0], None, [256], [0, 256])
hist4 = cv2.calcHist([gray4], [0], None, [256], [0, 256])

cv2.normalize(hist1, hist1, 0, 1, cv2.NORM_MINMAX)
cv2.normalize(hist2, hist2, 0, 1, cv2.NORM_MINMAX)
cv2.normalize(hist3, hist3, 0, 1, cv2.NORM_MINMAX)
cv2.normalize(hist4, hist4, 0, 1, cv2.NORM_MINMAX)

ret1 = cv2.compareHist(hist1, hist1, cv2.HISTCMP_CORREL)
ret2 = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
ret3 = cv2.compareHist(hist1, hist4, cv2.HISTCMP_CORREL)
print(ret1, ret2, ret3)
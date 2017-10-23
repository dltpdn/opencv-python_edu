import cv2
import matplotlib.pylab as plt

img = cv2.imread('../img/model3.jpg')
#img = cv2.imread('../img/rgb.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

hist0 = cv2.calcHist([hsv], [0], None, [180], [0, 180])
hist1 = cv2.calcHist([hsv], [1], None, [256], [0, 256])

plt.subplot(121)
plt.plot(hist0)
plt.plot(hist1)

hist2d = cv2.calcHist([hsv], [0,1], None, [180, 256], [0, 180, 0,256])

plt.subplot(122)
plt.plot(hist2d)

#print( (hist0.dot(hist1) ==hist2d))
plt.show()

cv2.imshow('hist2d', hist2d)
cv2.waitKey()
cv2.destroyAllWindows()
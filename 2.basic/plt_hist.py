import matplotlib.pylab as plt
import cv2

img = cv2.imread('../img/model2.jpg', cv2.IMREAD_GRAYSCALE)
d1 = img.ravel()

plt.subplot(1,2,1)
plt.title('img')
plt.imshow(img, cmap='gray')
plt.subplot(122)
plt.title('hist')
plt.hist(d1, 255)
plt.show()


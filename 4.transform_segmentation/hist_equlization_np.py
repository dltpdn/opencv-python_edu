import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread('../img/yate.jpg', cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape[:2]
hist = cv2.calcHist([img], [0], None, [256], [0, 255])
#hist, bins = np.histogram(img.ravel(), 256, [0, 255])
cdf = hist.cumsum()

cdf_m = np.ma.masked_equal(cdf, 0)
print(cdf_m[0])
cdf_m = (cdf_m - cdf_m.min()) /(cdf_m.max()-cdf_m.min()) *255

cdf = np.ma.filled(cdf_m,0).astype('uint8')

img2 = cdf[img]
merged = np.hstack((img, img2))
cv2.imshow('result', merged)
hist2 = cv2.calcHist([img2], [0], None, [255], [0,255])

plt.subplot(121)
plt.plot(hist)
plt.subplot(122)
plt.plot(hist2)
plt.show()
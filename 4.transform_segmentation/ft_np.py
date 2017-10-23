import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('../img/model.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

f = np.fft.fft2(img) # apply Fourier Transform to img
fshift = np.fft.fftshift(f) # center 0
magnitude_spectrum = 20*np.log(np.abs(fshift)) #spectrum

rows, cols = img.shape
crow, ccol = rows//2, cols//2 #center 

d = 10
fshift[crow-d:crow+d, ccol-d:ccol+d] = 0

# inverse from frequency to image
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

img_new = np.uint8(img_back);
ret, thresh = cv2.threshold(img_new,30,255,cv2.THRESH_BINARY_INV)

plt.subplot(221),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])

plt.subplot(222),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Spectrum'), plt.xticks([]), plt.yticks([])

plt.subplot(223),plt.imshow(img_back, cmap = 'gray')
plt.title('FT'), plt.xticks([]), plt.yticks([])

plt.subplot(224),plt.imshow(thresh, cmap = 'gray')
plt.title('Threshold With FT'), plt.xticks([]), plt.yticks([])
plt.show()

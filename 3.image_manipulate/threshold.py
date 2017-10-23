import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread('../img/gray-gradient.jpg', cv2.IMREAD_GRAYSCALE)

t_np = np.zeros_like(img)
t_np[ img > 127] = 255 

ret, t_bin = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, t_bininv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, t_truc = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, t_2zr = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, t_2zrinv = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['origin','Numpy', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
imgs = [img, t_np, t_bin, t_bininv, t_truc, t_2zr, t_2zrinv]

for i in range(len(imgs)):
    plt.subplot(2,4, i+1)
    plt.imshow(imgs[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
    
plt.show()

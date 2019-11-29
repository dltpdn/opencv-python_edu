import cv2
import numpy as np
import matplotlib.pyplot as plt

img = np.arange(9, dtype=np.uint8).reshape(3,3)
print("input\n", img)

k = np.zeros((3,3), np.float32)
k[0,0] = 1
#k[2,2] = 1
print("kernel\n", k)

#filtered = cv2.filter2D(img, -1, k, anchor=(1,1), borderType=cv2.BORDER_CONSTANT)
filtered = cv2.filter2D(img, -1, k, borderType=cv2.BORDER_CONSTANT)
print("output\n",filtered)

plt.subplot(1,2,1)
plt.imshow(img, cmap='gray')
plt.subplot(1,2,2)
plt.imshow(filtered, cmap='gray')
plt.show()
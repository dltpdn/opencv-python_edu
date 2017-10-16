import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('../img/model.jpg')
img2 = cv2.imread('../img/model2.jpg')
img3 = cv2.imread('../img/model3.jpg')

img1_rgb = np.zeros(img1.shape, dtype=np.uint8)
img1_rgb[:,:,2],img1_rgb[:,:,1], img1_rgb[:,:,0] = img1[:,:,0], img1[:,:,1], img1[:,:,2]

b,g,r = cv2.split(img2)
img2_rgb = cv2.merge([r,g,b])

img3_rgb = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)

plt.subplot(1,3,1).axis('off')
plt.imshow(img1_rgb)
plt.subplot(1,3,2).axis('off')
plt.imshow(img2_rgb)
plt.subplot(1,3,3).axis('off')
plt.imshow(img3_rgb)
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
plt.show()
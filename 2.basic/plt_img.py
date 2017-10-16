import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../img/model.jpg')
plt.imshow(img)
#plt.xticks([])
#plt.yticks([])
plt.show()
import cv2
import numpy as np
from matplotlib import pyplot as plt

file_name = '../img/fish.jpg'
img = cv2.imread(file_name)
rows, cols = img.shape[:2]

pts1 = np.float32([[50,50], [200,50], [50,200]])
pts2 = np.float32([[40,80], [200,50], [100,150]])

cv2.circle(img, (50,50), 5, (2550,0), -1)
cv2.circle(img, (200,50), 5, (0,255,0), -1)
cv2.circle(img, (50,200), 5, (0,0,255), -1)

m = cv2.getAffineTransform(pts1, pts2)
print(m)
result = cv2.warpAffine(img, m, (cols, rows))

# cv2.imshow('origin',img)
# cv2.imshow('affin', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
plt.subplot(121);plt.imshow(img);plt.title('origin')
plt.subplot(122);plt.imshow(result);plt.title('affine')
plt.show()
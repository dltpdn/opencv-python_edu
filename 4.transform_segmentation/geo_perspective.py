import cv2
import numpy as np
import matplotlib.pyplot as plt

file_name = "../img/wingwall.jpg"
img = cv2.imread(file_name)
cols, rows = img.shape[:2]

pts1 = np.float32([[30,10], [30,517], [670, 100], [670,313]])

pts2 = np.float32([[30,10], [30,517], [670, 30], [670,517]])

cv2.circle(img, (30,10), 10, (255,0,0), -1)
cv2.circle(img, (30,517), 10, (0,255,0), -1)
cv2.circle(img, (670,100), 10, (0,0,255), -1)
cv2.circle(img, (670,313), 10, (0,255,255), -1)

mtrx = cv2.getPerspectiveTransform(pts1, pts2)
result = cv2.warpPerspective(img, mtrx, (rows, cols))

# plt.subplot(121)
# plt.imshow(img)
# plt.title('origin')
# 
# plt.subplot(122)
# plt.imshow(result)
# plt.title('perspective')
# plt.show()

cv2.imshow("origin", img)
cv2.imshow('perspective', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
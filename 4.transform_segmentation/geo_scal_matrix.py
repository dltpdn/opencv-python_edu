import cv2
import numpy as np

img = cv2.imread('../img/fish.jpg')

height, width = img.shape[:2]

m_shrink = np.float32([[0.5, 0, 0],
                            [0, 0.5, 0]])  # matrix
m_zoom = np.float32([[1.5, 0, 0],
                          [0, 1.5, 0]])  # matrix

shrink = cv2.warpAffine(img, m_shrink, (int(width*0.5), int(height*0.5)) )
zoom = cv2.warpAffine(img, m_zoom, (int(width*1.5), int(height*1.5)) )

cv2.imshow("original", img)
cv2.imshow("shrink", shrink)
cv2.imshow("zoom", zoom)
cv2.waitKey(0)
cv2.destroyAllWindows()
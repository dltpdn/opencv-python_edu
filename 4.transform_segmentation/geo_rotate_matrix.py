import cv2
import numpy as np


img = cv2.imread('../img/fish.jpg')
rows,cols = img.shape[0:2]
print(rows, cols)
d45 = 45.0 * np.pi / 180
d90 = 90.0 * np.pi / 180
m45 = np.float32( [[ np.cos(d45), -1* np.sin(d45), 0],
                    [np.sin(d45), np.cos(d45), 0]])
m90 = np.float32( [[ np.cos(d90), -1* np.sin(d90), rows],
                    [np.sin(d90), np.cos(d90), 0]])

r45 = cv2.warpAffine(img,m45,(cols,rows))
r90 = cv2.warpAffine(img,m90,(rows,cols))

cv2.imshow("origin", img)
cv2.imshow("45", r45)
cv2.imshow("90", r90)

cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np


img = cv2.imread('../img/fish.jpg')
rows,cols = img.shape[0:2]

matrix_45 = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
matrix_90 = cv2.getRotationMatrix2D((cols/2,rows/2),90,0.5)

print(matrix_45)
r45 = cv2.warpAffine(img, matrix_45,(cols,rows))
r90 = cv2.warpAffine(img, matrix_90,(cols,rows))

cv2.imshow('origin',img)
cv2.imshow("45", r45)
cv2.imshow("90", r90)

cv2.waitKey(0)
cv2.destroyAllWindows()
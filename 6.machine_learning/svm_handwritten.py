import cv2
import numpy as np

digit_img = cv2.imread('../img/digits.png')
small = cv2.pyrDown(digit_img)
cv2.imshow('digits', small)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray = cv2.cvtColor(digit_img, cv2.COLOR_BGR2GRAY)
print(gray.shape)
cells = [np.hsplit(row, 100) for row in np.vsplit(gray, 50)]
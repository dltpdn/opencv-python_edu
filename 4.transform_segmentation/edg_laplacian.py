import cv2
import numpy as np
import matplotlib.pyplot as plt

file_name = "../img/sudoku.jpg"

img = cv2.imread(file_name)

laplacian = cv2.Laplacian(img, -1)


cv2.imshow('origin',img)
cv2.imshow('Laplacian', laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()
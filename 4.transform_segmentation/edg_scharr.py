import cv2
import numpy as np
import matplotlib.pyplot as plt

file_name = "../img/sudoku.jpg"

img = cv2.imread(file_name)

sobelx = cv2.Sobel(img, -1, 1, 0, -1)
sobely = cv2.Sobel(img, -1, 0, 1, -1) 

scharrx = cv2.Scharr(img, -1, 1, 0)
scharry = cv2.Scharr(img, -1, 0, 1)

cv2.imshow('origin',img)
cv2.imshow('Sobelx', sobelx)
cv2.imshow('Sobely', sobely)
cv2.imshow('Scharr_x', scharrx)
cv2.imshow('Scharr_y', scharry)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''
imgs = [('Origin', img), ('Gx', edge_gx), ('Gy', edge_gy), ('Gx+Gy', edge_gx + edge_gy)]

for i in range(4):
    plt.subplot(2,2,i+1)
    plt.title(imgs[i][0])
    plt.imshow(imgs[i][1])
    plt.xticks([]), plt.yticks([])
plt.show()
'''
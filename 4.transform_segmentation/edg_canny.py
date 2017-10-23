import cv2
import numpy as np
import matplotlib.pyplot as plt

file_name = "../img/sudoku.jpg"

img = cv2.imread(file_name)

edges = cv2.Canny(img,100,200)


cv2.imshow('origin',img)
cv2.imshow('Canny', edges)

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
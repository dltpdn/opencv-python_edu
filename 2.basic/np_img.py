import cv2
import numpy as np


img = np.zeros( (120,120), dtype=np.uint8)
img[25:35, :] = 45
img[55:65, :] = 115
img[85:95, :] = 160
img[:, 35:45] = 205
img[:, 75:85] = 255

cv2.imshow('Gray', img)


img2 = np.zeros( (120,120,3), dtype=np.uint8) #all black screen
img2[25:35, : ] = [255,0,0]  #horizontal red line
img2[55:65, : ] = [0,255,0]  #horizontal red line
img2[85:95, : ] = [0,0,255]  #horizontal red line
img2[ : , 35:45] = [255,255,0] #vertical red line
img2[ : , 75:85] = [255,0,255] #vertical red line
cv2.imshow('Color', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np

winSize = (20,20)
blockSize = (10,10)#blockSize = (8,8)
blockStride = (5,5)#blockStride = (4,4)#half of blocSize
cellSize = (10,10)#cellSize = (8,8)
nbins = 9

hogDesc = cv2.HOGDescriptor(winSize,blockSize,blockStride,cellSize,nbins)

img = cv2.imread('../img/pistol.jpg')
cv2.imshow('img',img)
hog = hogDesc.compute(img)
print(hog)
#cv2.imshow('hog', hog)
cv2.waitKey()
cv2.destroyAllWindows()
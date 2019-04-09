import cv2
import numpy as np
import math
import matplotlib.pylab as plt

win_name = "img"

def distort(img, k):
    rows, cols = img.shape[:2]
    mapy, mapx = np.indices((rows, cols),dtype=np.float32)

    mapx = (2*mapx - cols)/cols
    mapy = (2*mapy - rows)/rows

    r = np.sqrt(mapx**2 + mapy**2)
    ru = r/(1-k*r**2)

    theta = np.arctan2(mapx, mapy)

    mapx =  np.sin(theta)* ru 
    mapy =  np.cos(theta)* ru

    mapx = ((mapx + 1)*cols)/2
    mapy = ((mapy + 1)*rows)/2

    distored = cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)
    return distored

def onChange(x):                                        
    k = cv2.getTrackbarPos('k',win_name)
    k = (k-5) /10
    print(k)
    distored = distort(img.copy(), k)
    cv2.imshow(win_name, distored)


#img = cv2.imread('../img/girl.jpg')
img = np.full((500,500,3), 255, np.uint8)
img[::10, :, :] = 0
img[:, ::10, :] = 0
cv2.imshow(win_name, img)
cv2.createTrackbar('k', win_name, -10, 10, onChange)  


cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
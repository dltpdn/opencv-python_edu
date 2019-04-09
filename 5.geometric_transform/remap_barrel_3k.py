import cv2
import numpy as np

win_name = 'img'

def distort(img, k1, k2, k3):
    rows, cols = img.shape[:2]
    mapy, mapx = np.indices((rows, cols),dtype=np.float32)

    mapx = (2*mapx - cols)/cols
    mapy = (2*mapy - rows)/rows

    r = np.sqrt(mapx**2 + mapy**2)
    ru = r*(1+k1*(r**2) + k2*(r**4) + k3*(r**6)) 
    theta = np.arctan2(mapx, mapy)

    mapx =  np.sin(theta)* ru 
    mapy =  np.cos(theta)* ru

    mapx = ((mapx + 1)*cols)/2
    mapy = ((mapy + 1)*rows)/2

    distored = cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)
    return distored

def onChange(x):                                        
    k1 = cv2.getTrackbarPos('k1',win_name)
    k2 = cv2.getTrackbarPos('k2',win_name)    
    k3 = cv2.getTrackbarPos('k3',win_name)    
    k1 = (k1-5) /10
    k2 = (k2-5) /10
    k3 = (k3-5) /10
    distored = distort(img.copy(), k1, k2, k3)
    cv2.imshow(win_name, distored)


img = cv2.imread('../img/girl.jpg')

cv2.imshow(win_name, img)
cv2.createTrackbar('k1', win_name, -10, 10, onChange)  
cv2.createTrackbar('k2', win_name, -10, 10, onChange)
cv2.createTrackbar('k3', win_name, -10, 10, onChange)

cv2.waitKey()
cv2.destroyAllWindows()
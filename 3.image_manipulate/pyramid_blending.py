import cv2
import numpy as np,sys

apple = cv2.imread('../img/apple.png')
orange = cv2.imread('../img/orange.png')


rows, cols = apple.shape[:2]
print(apple.shape, orange.shape)

# generate Gaussian pyramid for A
gaussian = apple.copy()
gpApple = [gaussian]
for i in range(6):
    gaussian = cv2.pyrDown(gaussian) #bigiest -> smallest
    gpApple.append(gaussian)

# generate Gaussian pyramid for B
gaussian = orange.copy()
gpOrange = [gaussian]
for i in range(6):
    gaussian = cv2.pyrDown(gaussian)  #biggiest -> smallest
    gpOrange.append(gaussian)

# generate Laplacian Pyramid for A
lpApple = [gpApple[5]]#smallest gaussian apple
for i in range(5,0,-1):
    GE = cv2.pyrUp(gpApple[i])
    GE = cv2.resize(GE, (gpApple[i-1].shape[1], gpApple[i-1].shape[0]))
    L = cv2.subtract(gpApple[i-1],GE)
    lpApple.append(L)  # smallest --> biggest
    
# generate Laplacian Pyramid for B
lpOrange = [gpOrange[5]]#smallest gaussian orange
for i in range(5,0,-1):
    GE = cv2.pyrUp(gpOrange[i])
    GE = cv2.resize(GE, (gpOrange[i-1].shape[1], gpOrange[i-1].shape[0]))
    L = cv2.subtract(gpOrange[i-1],GE)
    lpOrange.append(L) #smallest -> biggest
    
# Now add left and right halves of images in each level
LS = []
idx = 0
for la,lb in zip(lpApple,lpOrange):
    rows, cols = la.shape[:2]
    ls = np.hstack((la[:, :cols//2], lb[:,cols//2:]))
    LS.append(ls)  #smallest -> biggest
    cv2.imshow('lp%d'%idx, ls)
    idx+=1
   
# now reconstruct
ls_ = LS[0]
idx=0
for i in range(1,6):
    ls_ = cv2.pyrUp(ls_)
    print(ls_.shape, LS[i].shape)
 #   ls_ = cv2.resize(ls_, (LS[i].shape[1], LS[i].shape[0]))
    ls_ = cv2.add(ls_, LS[i])  #
    idx+=1
# image with direct connecting each half

real = np.hstack((apple[:, :cols//2],orange[:, cols//2:]))
cv2.imshow('Pyramid_blending2.jpg',ls_)
cv2.imshow('Direct_blending.jpg',real)
cv2.waitKey(0)
cv2.destroyAllWindows()

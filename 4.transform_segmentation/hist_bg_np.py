import cv2
import numpy as np
from matplotlib import pyplot as plt


target = np.zeros((90,90,3), dtype=np.uint8)
target[:, :30, 0 ] = 255
target[:, 30:60, 1] = 255
target[:, 60:90, 2] = 255
target = cv2.imread('../img/chroma_key.jpg')
hsvt = cv2.cvtColor(target,cv2.COLOR_BGR2HSV)

cv2.imshow('rgb', target)
#roi is the object or region of object we need to find

roi = np.zeros((90,10, 3), dtype=np.uint8)
roi[:, :, 1] =255
#roi = cv2.imread('../img/chrome_key_green2.jpg')
roi = target[:200, 200:, :]
hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

cv2.imshow('green screen', roi)
#target is the image we search in


# Find the histograms. I used calcHist. It can be done with np.histogram2d also
M = cv2.calcHist([hsv],[0, 1], None, [180, 256], [0, 180, 0, 256] )
I = cv2.calcHist([hsvt],[0, 1], None, [180, 256], [0, 180, 0, 256] )
print("M",M.dtype, np.where(M!=0), M[M!=0])
print("I", I.dtype, np.where(I!=0), I[I!=0])

R = M/(I+1)

h,s,v = cv2.split(hsvt)
B = R[h.ravel(),s.ravel()]

B = np.minimum(B,1) #it means the numbers in array are rate, so can't let it over 1 
B = B.reshape(hsvt.shape[:2]) # B is the array that is returned from cv2.calcBackProject()
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
print(B)
cv2.filter2D(B,-1,disc,B)
print(B)
B = np.uint8(B)
print(B)
cv2.normalize(B,B,0,255,cv2.NORM_MINMAX)  # make rate to 0~255, actually it makes grayscale singlechannel
print(B)

ret,thresh = cv2.threshold(B,50,255, cv2.THRESH_BINARY_INV)
cv2.imshow('re', thresh)

#thr = cv2.merge((thresh, thresh, thresh))
thr = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)
res2 = cv2.bitwise_and(target, thr)
cv2.imshow('res', res2)
cv2.waitKey()
cv2.destroyAllWindows()
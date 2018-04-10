import cv2
import numpy as np
import matplotlib.pyplot as plt

drag = False
x0,y0 = -1,-1

def onMouse(event, x, y, flag, param):
    global drag, x0, y0, img
    if event == cv2.EVENT_LBUTTONDOWN:
        drag = True
        x0, y0 = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drag:
            draw = img.copy()
            cv2.rectangle(draw, (x0,y0), (x, y), (0,0,255), 2)
            cv2.imshow('original', draw)
    elif event == cv2.EVENT_LBUTTONUP:
        drag = False
        w = abs(x - x0)
        h = abs(y - y0)
        if w > 0 and h > 0:
            draw = img.copy()
            roi = draw[y0:y0+h, x0:x0+w]
            
            cv2.rectangle(draw, (x0, y0), (x, y), (0,0,255), 2)
            cv2.imshow('original', draw)
            backProjection(img, roi)

def backProjection(img, roi):
    hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    
    M = cv2.calcHist([hsv_roi],[0, 1], None, [180, 256], [0, 180, 0, 256] )
    I = cv2.calcHist([hsv_img],[0, 1], None, [180, 256], [0, 180, 0, 256] )
    R = M/(I+1)

#     plt.subplot(131)
#     plt.title('M-roi')
#     plt.plot(M)
#     plt.subplot(132)
#     plt.title('I-img')
#     plt.plot(I)
#     plt.subplot(133)
#     plt.title('R-ratio')
#     plt.plot(R)
#     plt.show()
    
    
    h,s,v = cv2.split(hsv_img)
    B = R[h.ravel(),s.ravel()]
    B = np.minimum(B,1) #it means the numbers in array are rate, so can't let it over 1 
    B = B.reshape(hsv_img.shape[:2]) # B is the array that is returned from cv2.calcBackProject()
    cv2.imshow('B', B)

    disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    cv2.filter2D(B,-1,disc,B)
    cv2.normalize(B,B,0,255,cv2.NORM_MINMAX)  # make rate to 0~255, actually it makes grayscale singlechannel
    B = np.uint8(B)
    ret,thresh = cv2.threshold(B, 10, 255, cv2.THRESH_BINARY)
    cv2.imshow('re', thresh)
    
    thr = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)
    res2 = cv2.bitwise_and(img, thr)
    cv2.imshow('res', res2)
    cv2.waitKey()
    cv2.destroyAllWindows()



img = cv2.imread('../img/roses.jpg')
cv2.imshow('original', img)
cv2.setMouseCallback('original', onMouse, param=None)
cv2.waitKey()
cv2.destroyAllWindows()

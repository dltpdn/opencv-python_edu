import numpy as np
import cv2
import matplotlib.pylab as plt

ix, iy = -1, -1
mode =False
img1, img2 = None, None

def onMouse(event, x, y, flag, param):
    global ix, iy, mode, img1, img2
    if event == cv2.EVENT_LBUTTONDOWN:
        mode = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if mode:
            img1 = img2.copy()
            cv2.rectangle(img1, (ix,iy), (x, y), (0,0,255), 2)
            cv2.imshow('original', img1)
    elif event == cv2.EVENT_LBUTTONUP:
        mode = False
        if ix >= x or iy >=y:
            return
        cv2.rectangle(img1, (ix, iy), (x,y), (0,0,255), 2)
        roi=img1[iy:y, ix:x]
        backProjection(img2, roi)
    return

def backProjection(img, roi):
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    hsvt = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    roihist = cv2.calcHist([hsv], [0,1], None, [180, 256], [0,180, 0, 256])    
    dst = cv2.calcBackProject([hsvt], [0,1], roihist, [0,180, 0,256], 1)
    cv2.normalize(roihist, roihist, 0,255, cv2.NORM_MINMAX)
    disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
    cv2.filter2D(dst, -1, disc, dst)

    #ret, thr = cv2.threshold(dst, 50, 255, cv2.THRESH_BINARY)
    ret, thr = cv2.threshold(dst, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    k = np.ones( (5,5), np.uint8)
    thr = cv2.morphologyEx(thr, cv2.MORPH_CLOSE, k)
    cv2.imshow('thr', thr)
    thr_not = cv2.bitwise_not(thr)
    #thr_clr = cv2.merge((thr_not, thr, thr))
    thr_clr = cv2.cvtColor(thr_not, cv2.COLOR_GRAY2BGR)
    res = cv2.bitwise_and(img, thr_clr)
    cv2.imshow('backproj', res)
    bg = cv2.imread('../img/park.jpg')
    bg2 = cv2.bitwise_and(bg, bg, mask=thr)
    result = cv2.add(bg2, res)
    cv2.imshow('result', result)
    
img1 = cv2.imread('../img/chroma_key.jpg')
print(img1.shape)
img2 = img1.copy()
cv2.namedWindow('original')
cv2.namedWindow('backproj')
cv2.setMouseCallback('original', onMouse, param=None)
cv2.imshow('backproj', img2)
while True:
    cv2.imshow('original', img1)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
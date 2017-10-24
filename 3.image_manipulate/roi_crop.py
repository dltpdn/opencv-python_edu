import cv2
import numpy as np

drag = False
x0,y0 = -1,-1

def onMouse(event,x,y,flags,param):
    global drag, x0, y0, img
    if event == cv2.EVENT_LBUTTONDOWN:
        drag = True
        x0 = x
        y0 = y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drag:
            draw = img.copy()
            cv2.rectangle(draw, (x0, y0), (x, y), (255,0,0), 2)
            cv2.imshow('img', draw)
    elif event == cv2.EVENT_LBUTTONUP:
        if drag:
            drag = False
            w = abs(x - x0)
            h = abs(y - y0)
            if w >0 and h >0:
                draw = img.copy()
                crop = draw[y0:y0+h, x0:x0+w]
                cv2.imshow('crop', crop)
                cv2.moveWindow('crop', width, 0)
                
                cv2.rectangle(draw, (x0, y0), (x, y), (0,0,255), 2)
                cv2.line(crop, (0, 0), (w,h), (0,255,0), 1)
                print(crop.base)
                cv2.imshow('img', draw)

img = cv2.imread('../img/yate.jpg')
height,width = img.shape[:2]

cv2.namedWindow('img')
cv2.moveWindow('img', 0,0)
cv2.setMouseCallback('img', onMouse)
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()

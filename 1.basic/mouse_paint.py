import cv2
import numpy as np

drawing = False # true if mouse is pressed
mode = True
color = (0,0,255)
ix,iy = -1,-1

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode

    if event == cv2.EVENT_LBUTTONDOWN :
        drawing = True
        ix,iy = x,y
        if event == cv2.EVENT_LBUTTONDOWN:
            mode = True
        else:
            mode = False

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            print(flags, param)
            if mode:
                cv2.circle(img,(x,y),5,color,-1)
            else:
                cv2.circle(img, (x,y), 5, (0,0,0), -1)
                print(mode)

    elif event == cv2.EVENT_LBUTTONUP or event == cv2.EVENT_RBUTTONUP:
        drawing = False
            
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('r'):
        color = (0,0,255)
    elif k == ord('g'):
        color = (0,255,0)
    elif k == ord('b'):
        color = (255,0,0)
    elif k == 27:
        break

cv2.destroyAllWindows()            
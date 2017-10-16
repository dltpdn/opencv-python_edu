import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)

# mouse callback function
def draw_circle(event,x,y,flags,param):
    print("event: %d, x : %d, y:%d" % (event, x, y))
    if event == cv2.EVENT_LBUTTONDOWN: 
        cv2.circle(img,(x,y),30,(255,0,0),-1)


cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
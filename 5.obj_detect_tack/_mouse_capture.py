import numpy as np, cv2


filename = '../img/highway.mp4'

isInit = True
drag = False
mode_pause = False 

roi_x, roi_y, roi_h, roi_w = -1,-1, -1, -1
target = None
img, frame = None, None
width, height = -1, -1

def onMouse(event, x, y, flags, param):
    global drag, target,frame,img, roi_x, roi_y,roi_w, roi_h, width, height
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drag = True
        roi_x, roi_y = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drag:
            img = frame.copy()
            roi_h,roi_w = abs(roi_y - y), abs(roi_x - x)
            cv2.rectangle(img, (roi_x,roi_y), (roi_x+roi_w, roi_y+roi_h), (255,0,0), 2)
            cv2.imshow(filename, img)  
        
    elif event == cv2.EVENT_LBUTTONUP:
        drag = False
        img= frame.copy()
        roi_h,roi_w = abs(roi_y - y), abs(roi_x - x)
        cv2.rectangle(img, (roi_x,roi_y), (roi_x+roi_w, roi_y+roi_h), (0,255,0), 2)
        cv2.imshow(filename, img)  
        cv2.imshow('target', frame[roi_y:roi_y+roi_h, roi_x:roi_x+roi_w])
        cv2.moveWindow('target', w,0)
        target = (roi_x, roi_y, roi_w, roi_h)

def pause():
    global mode_pause
    mode_pause = not mode_pause
    while mode_pause :
        key = cv2.waitKey(1)
        if key == ord(' '):
            mode_pause = not mode_pause
            break
        elif key == 27:
            return True

cap = cv2.VideoCapture(filename)
cv2.namedWindow(filename)
cv2.moveWindow(filename, 0,0)
cv2.setMouseCallback(filename, onMouse)

ret, frame = cap.read()   
h, w = frame.shape[:2]
cv2.imshow(filename, frame)

while True:
    ret, frame = cap.read()   
    if not ret:
        print("no frame")
        break

    if isInit:
        if pause():
            break
        isInit = False
    img = frame.copy()     
    if target is not None:
        if drag:
            color = (255,0,0)
        else:
            color = (0,255,0)
        x,y,w,h = target
        cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
    cv2.imshow(filename, img)   
    if isInit:
        h, w = frame.shape[:2]
        if pause():
            break
        isInit = False 

    key = cv2.waitKey(1) & 0xff
    if key == 27: #esc
        break
    elif key == ord(' '):
       if pause():
           break
        
        
cap.release()
cv2.destroyAllWindows()
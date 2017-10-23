import numpy as np
import cv2

filename = '../img/slow_traffic.mp4'

drag = False
isInit = True
mode_pause = False 

roi_x, roi_y, roi_h, roi_w = -1,-1, -1, -1
img, frame = None, None
width, height = -1, -1
roi_hist =None
track_window = None

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


def onMouse(event, x, y, flags, param):
    global drag, track_window,frame,img, roi_x, roi_y,roi_w, roi_h, width, height
    
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
        cv2.rectangle(img, (roi_x,roi_y), (roi_x+roi_w, roi_y+roi_h), (0,255,0), 2)
        cv2.imshow(filename, img)  
        cv2.imshow('target', frame[roi_y:roi_y+roi_h, roi_x:roi_x+roi_w])
        cv2.moveWindow('target', width,0)
        track_window = (roi_x, roi_y, roi_w, roi_h)
        setTarget()

def setTarget():
    global track_window, roi_hist
    c,r,w,h = track_window
    # set up the dROI for tracking
    roi = frame[r:r+h, c:c+w]
    hsv_roi =  cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
    roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
    #roi_hist = cv2.calcHist([hsv_roi],[0],None,[180],[0,180])
    cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
    # Setup the termination criteria, either 10 iteration or move by atleast 1 pt

cap = cv2.VideoCapture(filename)
cv2.namedWindow(filename)
cv2.moveWindow(filename, 0,0)
cv2.setMouseCallback(filename, onMouse)
fps = cap.get(cv2.CAP_PROP_FPS) #3.x
#fps = cap.get(cv2.cv.CAP_PROP_FPS) #2.x
print("fps:", fps)

term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )
ret, frame = cap.read()   
height, width = frame.shape[:2]
cv2.imshow(filename, frame)


while True:
    ret ,frame = cap.read()
    if not ret:
        print("no frame")
        break
    
    if isInit:
        if pause():
            break
        isInit = False
    img = frame.copy() 

    if roi_hist is not None:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
        # apply meanshift to get the new location
        ret, track_window = cv2.CamShift(dst, track_window, term_crit)
        # Draw it on image
        pts = cv2.boxPoints(ret)
        pts = np.int0(pts)
        cv2.polylines(img,[pts],True, 255,2)
    cv2.imshow(filename,img)
    key = cv2.waitKey(60) & 0xff
    if key == 27:
        break
    elif key == ord(' '):
       if pause():
           break
        
   
cv2.destroyAllWindows()
cap.release()
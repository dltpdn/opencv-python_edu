import numpy as np, cv2

drag = False

x1, y1, height,width = -1,-1, -1, -1
roi_hist, target = None, None
img, frame = None, None
roi = None


def onMouse(event, x, y, flags, param):
    global drag, target,roi_hist, frame,img, x1, y1, roi, width, height
    if event == cv2.EVENT_LBUTTONDOWN:
        drag = True
        x1, y1 = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drag:
            height,width = abs(y1 - y), abs(x1 - x)
            target = (x1, y1, width, height)
    elif event == cv2.EVENT_LBUTTONUP:
        drag = False
        cv2.imshow('target', frame[y1:y1+height, x1:x1+width])
        roi = frame[y1:y1+height, x1:x1+width]
        roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        roi_hist = cv2.calcHist([roi], [0], None, [180], [0,180])
        cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
        

cap = cv2.VideoCapture(0)
cv2.namedWindow('frame')
cv2.moveWindow('frame', 0,0)
cv2.setMouseCallback('frame', onMouse)

termination =  (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
while True:
    ret, frame = cap.read()    
    if not ret:
        continue
    img = frame.copy()
    if target is not None:
        if drag:
            color = (255,0,0)
        else:
            color = (0,255,0)
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            dst = cv2.calcBackProject([hsv], [0], roi_hist, [0,180], 1)
            ret, target = cv2.meanShift(dst, target, termination)

        x,y,w,h = target
        cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
    cv2.imshow('frame', img)
    
    if cv2.waitKey(1) & 0xff == 27:
        break
cap.release()
cv2.destroyAllWindows()
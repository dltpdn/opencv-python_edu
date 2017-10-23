import numpy as np
import cv2
cap = cv2.VideoCapture('../img/walking.avi')
#cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()
#fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
retry = 0
while(1):
    ret, frame = cap.read()
    if not ret:
        print("no frame")
        break
    fgmask = fgbg.apply(frame)
    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
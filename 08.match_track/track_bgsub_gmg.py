import numpy as np
import cv2
cap = cv2.VideoCapture('../img/walking.avi')

#fgbg = cv2.createBackgroundSubtractorGMG() # create object
fgbg = cv2.bgsegm.createBackgroundSubtractorGMG() # create object
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3)) #kernel for morphology

while(1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel) # filtering for reduce noise
    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
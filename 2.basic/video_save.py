import numpy as np
import cv2

fps = 20.0 #frame per sec
cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'MJPG')#MJPG for Mac, DIVX for Windows
#fourcc = cv2.VideoWriter_fourcc(*'DIVX')#MJPG for Mac, DIVX for Windows
#fourcc = cv2.VideoWriter_fourcc('D','I','V','X')
#fourcc = ord('D') + (ord('I') <<8) + (ord('V') << 16) + (ord('X') <<24)   #1482049860

out = cv2.VideoWriter('./mycam.avi',fourcc, fps, (int(cap.get(3)),int(cap.get(4))))

while True:
    ret, frame = cap.read()
    if ret==True:
        cv2.imshow('frame',frame)
        out.write(frame)
        if cv2.waitKey(1) & 0xFF == 27: #esc
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
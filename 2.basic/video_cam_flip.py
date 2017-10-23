import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,1) #0, 1, -1
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == 27: #esc
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
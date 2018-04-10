import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

while True:
    ret, frame = cap.read()
    if ret==True:
        cv2.imshow('frame',frame)
        key = cv2.waitKey(1) & 0xFF
        if key == 27: #esc
            break
        elif key == ord(' '):
            cv2.imwrite('capture.jpg', frame)
    else:
        break

cap.release()
cv2.destroyAllWindows()
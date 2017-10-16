import cv2

cap = cv2.VideoCapture(0) #0 or -1

print("width: %d, height:%d" % (cap.get(3), cap.get(4)) )
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
print("resized width: %d, height:%d" % (cap.get(3), cap.get(4)) )

while cap.isOpened():
    ret, img = cap.read()
    if ret:
        cv2.imshow('camera-0', img)
        if cv2.waitKey(1) & 0xFF == 27: #esc
            break
    else:
        print('no camera!')
        break
cap.release()
cv2.destroyAllWindows()
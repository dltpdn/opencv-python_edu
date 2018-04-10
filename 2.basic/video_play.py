import cv2

video_file = "../img/Megamind.avi"

cap = cv2.VideoCapture(video_file) #0 or -1
if cap.isOpened():
    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow(video_file, img)
        else:
            print('no more frame.')
            break
else:
    print("can't open video.")
cap.release()
cv2.destroyAllWindows()
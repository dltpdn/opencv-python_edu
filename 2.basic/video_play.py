import cv2

video_file = "../img/Megamind.avi"

cap = cv2.VideoCapture(video_file) #0 or -1
while cap.isOpened():
    ret, img = cap.read()
    if ret:
        cv2.imshow(video_file, img)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    else:
        print('no video file!', video_file)
        break
cap.release()
cv2.destroyAllWindows()
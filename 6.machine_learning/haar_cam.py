import cv2

cascade_xml = '../data/haarcascade_frontalface_default.xml'
eye_xml = '../data/haarcascade_eye.xml'

cascade = cv2.CascadeClassifier(cascade_xml)
eye_cascade = cv2.CascadeClassifier(eye_xml)

cam = cv2.VideoCapture(0)
#cam.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
#cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
while True:    
    ret, img = cam.read()
    if not ret:
        print('no frame')
        break
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    
#    faces = cascade.detectMultiScale(gray, 1.3, 5) #, scaleFactor=1.1, minNeighbors=3, minSize=(80,80), flags=cv2.HAAR_SCALE_IMAGE)
#    faces = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(80,80), flags=cv2.HARR_SCALE_IMAGE) #v2.x
    faces = cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(80,80)) #v3.x
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255,0),2)
        roi = gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi)
        for i, (ex, ey, ew, eh) in enumerate(eyes):
            if i >= 2:
                break
            cv2.rectangle(img[y:y+h, x:x+w], (ex,ey), (ex+ew, ey+eh), (255,0,0),2  )
    cv2.imshow('facedetect', img)
    if 0xFF & cv2.waitKey(5) == 27:
        break
cv2.destroyAllWindows()

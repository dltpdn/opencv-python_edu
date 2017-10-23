import cv2
import numpy as np
import os
import os.path

# Get the training data we previously made
data_path = './faces/all_face.xml'
photo_dir = './faces'

accuracy = 90
users = dict([])

dirs = [d for d in os.listdir(photo_dir) if os.path.isdir(os.path.join(photo_dir, d))]
for dir in dirs:
    name = dir.split('_')[0]
    id = dir.split('_')[1]
    users[id] = name

# Initialize facial recognizer
#model = cv2.createLBPHFaceRecognizer()
#model = cv2.face.createLBPHFaceRecognizer()  #cv 3.2.0
model = cv2.face.LBPHFaceRecognizer_create()  #cv2 3.3.0
# NOTE: For OpenCV 3.0 use cv2.face.createLBPHFaceRecognizer()

# load trained data from xml to model 
model.read(data_path)
print("trained model loaded sucessefully")
#model.write('face.xml')

face_classifier = cv2.CascadeClassifier('../data/haarcascade_frontalface_default.xml')




# Open Webcam
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        print("no frame")
        break
    
        # Convert image to grayscale
    image = frame.copy()
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if faces is ():
        cv2.putText(image, "No Face Found", (220, 120) , cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
        cv2.putText(image, "Locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
    else:
        for (x,y,w,h) in faces:
            cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,255),2)
            face = image[y:y+h, x:x+w]
            face = cv2.resize(face, (200, 200))
        
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            # Pass face to prediction model
            # "results" comprises of a tuple containing the label and the confidence value
            results = model.predict(face)
            print(results)
            uid = int(results[0]/10000)
            print(uid)
            if results[1] < 500:
                confidence = int( 100 * (1 - (results[1])/500) )
                uname = users[str(uid)]
            if confidence > accuracy:
                cv2.putText(image, "Match", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            else:
                cv2.putText(image, "Not Match", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
            display_string =  '{}({}%)'.format(uname, confidence)
            print(display_string)
            cv2.putText(image, display_string, (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (255,120,150), 2)
    cv2.imshow('Face Recognition', image )
        
    if cv2.waitKey(1) == 27: #esc Key
        break
        
cap.release()
cv2.destroyAllWindows()     
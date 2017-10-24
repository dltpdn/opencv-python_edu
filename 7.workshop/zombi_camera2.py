import numpy as np
import cv2
import math

face_cascade = cv2.CascadeClassifier('../data/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('../data/haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

windowClose = np.ones((2,2),np.uint8)
windowOpen = np.ones((2,2),np.uint8)
windowErode = np.ones((2,2),np.uint8)

while True:
    ret, img = cap.read()
    if img is not None:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        faces = face_cascade.detectMultiScale(gray)
        for (x,y,w,h) in faces:
            #cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for i, (ex,ey,ew,eh) in enumerate(eyes):
                if i >= 2 :
                    break
                #cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                roi_eye = roi_gray[ey:ey+eh, ex:ex+ew]
                eye = roi_color[ey:ey+eh, ex:ex+ew]
                roi_eye = cv2.GaussianBlur(roi_eye, (5, 5), 0)
                
                ret, roi_eye = cv2.threshold(roi_eye, 40, 255, cv2.THRESH_BINARY_INV)
                
                #roi_eye = cv2.morphologyEx(roi_eye, cv2.MORPH_ERODE, windowErode)
                #roi_eye = cv2.morphologyEx(roi_eye, cv2.MORPH_OPEN, windowOpen)
                #roi_eye = cv2.morphologyEx(roi_eye, cv2.MORPH_CLOSE, windowClose)
                _, contours, hierarchy = cv2.findContours(roi_eye, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
                #cv2.drawContours(eye, contours, -1, (0,0,255), 1)
                #cv2.imshow('eye'+str(i), roi_eye)
                #cv2.moveWindow('eye'+str(i), img.shape[1], i*eh+(i*30))
                
                for contour in contours:
                    area = cv2.contourArea(contour)
                    rect = cv2.boundingRect(contour)
                    x, y, width, height = rect
                    radius = 0.25 * (width + height)
                    
                    area_condition = (100 <= area <= 200)
                    symmetry_condition = (abs(1 - float(width)/float(height)) <= 0.2)
                    fill_condition = (abs(1 - (area / (math.pi * math.pow(radius, 2.0)))) <= 0.3)
                
                    if area_condition and symmetry_condition and fill_condition:
                        cv2.circle(eye, (int(x + radius), int(y + radius)), int(1.3*radius), (0,0,255), -1)            
            
        cv2.imshow('img',img)
        key = cv2.waitKey(10) & 0xFF
        if key == 27:
            break
cv2.destroyAllWindows()
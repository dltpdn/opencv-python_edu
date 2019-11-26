import cv2
import numpy as np


def distort(roi):
        h, w = roi.shape[:2]
        # 렌즈 효과
        ## 렌즈 효과, 중심점 이동
        map_y, map_x = np.indices((h, w), dtype=np.float32)
        map_lenz_x = (2*map_x - w)/w
        map_lenz_y = (2*map_y - h)/h
        ## 렌즈 효과, 극좌표 변환
        r, theta = cv2.cartToPolar(map_lenz_x, map_lenz_y)
        ## 볼록 렌즈 효과 매핑 좌표 연산
        r[r< 1] = r[r<1] **2  
        ## 렌즈 효과, 직교 좌표 복원
        map_convex_x, map_convex_y = cv2.polarToCart(r, theta)
        map_convex_x = ((map_convex_x + 1)*w)/2
        map_convex_y = ((map_convex_y + 1)*h)/2

        #roi2 = img2[y:y+h, x:x+w]
        convex = cv2.remap(roi,map_convex_x,map_convex_y,cv2.INTER_LINEAR)      
        return convex


cascade_xml = '../data/haarcascade_frontalface_default.xml'
eye_xml = '../data/haarcascade_eye.xml'

cascade = cv2.CascadeClassifier(cascade_xml)
eye_cascade = cv2.CascadeClassifier(eye_xml)
cam = cv2.VideoCapture(0)
rows, cols =  cam.get(cv2.CAP_PROP_FRAME_WIDTH)//2, cam.get(cv2.CAP_PROP_FRAME_HEIGHT)//2
cam.set(cv2.CAP_PROP_FRAME_WIDTH, cols)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, rows)

while True:    
    ret, img = cam.read()
    if not ret:
        print('no frame')
        break
    img2 = img.copy()
    img_draw = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    
#    faces = cascade.detectMultiScale(gray, 1.3, 5) #, scaleFactor=1.1, minNeighbors=3, minSize=(80,80), flags=cv2.HAAR_SCALE_IMAGE)
#    faces = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(80,80), flags=cv2.HARR_SCALE_IMAGE) #v2.x
    faces = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(80,80)) #v3.x
    for(x,y,w,h) in faces:
        #cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255,0),2)
        roi = gray[y:y+h, x:x+w]
        # distort face
        convex = distort(img.copy()[y:y+h, x:x+w])
        img2[y:y+h, x:x+w] = convex
        
        eyes = eye_cascade.detectMultiScale(roi, scaleFactor=1.2)
        for i, (ex, ey, ew, eh) in enumerate(eyes):
            # distort face
            #convex = distort(img.copy()[y+ey:y+ey+eh, x+ex:x+ex+ew])
            #img2[y+ey:y+ey+eh, x+ex:x+ex+ew] = convex

            if i >= 2:
                break
            cv2.rectangle(img_draw[y:y+h, x:x+w], (ex,ey), (ex+ew, ey+eh), (255,0,0),2  )
            
    merged = np.hstack((img_draw, img2))
    cv2.imshow('facedetect', merged)
    if 0xFF & cv2.waitKey(5) == 27:
        break
cv2.destroyAllWindows()

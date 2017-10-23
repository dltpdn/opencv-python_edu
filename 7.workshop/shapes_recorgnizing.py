import cv2
import numpy as np

file_name = "../img/someshapes.jpg"

img = cv2.imread(file_name)
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, th = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY_INV)
_, contours, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    angle_points = len(approx)
    print("angle points", angle_points)
    
    mmt = cv2.moments(contour)
    cx = int(mmt['m10']/mmt['m00'])
    cy = int(mmt['m01']/mmt['m00'])
    
    shape = "Unkown"
    bgcolor = (0,0,0) 
    if angle_points == 3:
        shape = "Triangle"
        bgcolor = (0,255,0)
    elif angle_points == 4:
        x,y,w,h = cv2.boundingRect(contour)
        if abs(w-h) <= 3:
            shape = 'Square'
            bgcolor = (0,125,255)
        else:
            shape = 'Rectangle'
            bgcolor = (0,0,255)
    elif angle_points == 10:
        shape = 'Star'
        bgcolor = (255,255,0)
    elif angle_points >= 15:
        shape = 'Circle'
        bgcolor = (0,255,255)
    
    cv2.drawContours(img, [contour], -1, bgcolor, -1)
    cv2.putText(img, shape, (cx-50, cy), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,0), 1)
    cv2.imshow('Identifying Shapes', img)
    cv2.waitKey(0)
cv2.destroyAllWindows()
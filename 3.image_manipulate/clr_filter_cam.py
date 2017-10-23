import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3,480)
cap.set(4,320 )
while True:
    ret, frame = cap.read()
    if not ret:
        print('no frame')
        break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    blue1 = np.array([90, 50, 50])
    blue2 = np.array([120, 255,255])
    green1 = np.array([45, 50,50])
    green2 = np.array([75, 255,255]);
    red1 = np.array([0, 50,50])
    red2 = np.array([15, 255,255]);
    yellow1 = np.array([20, 50,50])
    yellow2 = np.array([35, 255,255]);
    
    mask_blue = cv2.inRange(hsv, blue1, blue2)
    mask_green = cv2.inRange(hsv, green1, green2)
    mask_red = cv2.inRange(hsv, red1, red2)
    mask_yellow = cv2.inRange(hsv, yellow1, yellow2)
    res_blue = cv2.bitwise_and(frame, frame, mask=mask_blue)
    res_green = cv2.bitwise_and(frame, frame, mask=mask_green)
    res_red = cv2.bitwise_and(frame, frame, mask=mask_red)
    res_yellow = cv2.bitwise_and(frame, frame, mask=mask_yellow)
    
    cv2.imshow('original', frame)
    cv2.imshow('blue', res_blue)
    cv2.imshow('green', res_green)
    cv2.imshow('red', res_red)
    cv2.imshow('yellow', res_yellow)
    if (cv2.waitKey(1) & 0xFF) == 27:
        break
    
cv2.destroyAllWindows()
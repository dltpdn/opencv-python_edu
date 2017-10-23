import cv2
import numpy as np
import matplotlib.pylab as plt

#image = cv2.imread('../img/bicycle.jpg')
image = cv2.imread('../img/bottlecaps.jpg')
blur = cv2.GaussianBlur(image, (3,3), 0)
gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

#circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 60, param2=60)#for bycycle
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 2.5, 60, param2=100, minRadius=40, maxRadius=60)#for bottlecaps

if circles is not None:
    print('found circle :', circles.shape[1])
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv2.circle(image,(i[0], i[1]), i[2], (255, 0, 0), 2)
        cv2.circle(image, (i[0], i[1]), 2, (0,255,0), 5)
    cv2.imshow('detected circles', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("there is no circle.")
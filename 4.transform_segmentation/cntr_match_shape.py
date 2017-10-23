import cv2
import numpy as np

file_name1 = '../img/4star.jpg'
file_name2 = '../img/shapestomatch.jpg'
target = cv2.imread(file_name1)
shapes = cv2.imread(file_name2)
cv2.imshow('target', target)
#cv2.waitKey()

targetGray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
shapesGray = cv2.cvtColor(shapes, cv2.COLOR_BGR2GRAY)

ret, targetTh = cv2.threshold(targetGray, 127, 255, cv2.THRESH_BINARY_INV)
ret, shapesTh = cv2.threshold(shapesGray, 127, 255, cv2.THRESH_BINARY_INV)

_, contours, _ = cv2.findContours(targetTh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
targetCntr = contours[0]

_, contours, _ = cv2.findContours(shapesTh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

matchs = []
for contr in contours:
    match = cv2.matchShapes(targetCntr, contr, cv2.CONTOURS_MATCH_I3, 0.0)
    print(match)
    matchs.append( (match, contr) )
    cv2.putText(shapes, '%f'%match, tuple(contr[0][0]), cv2.FONT_HERSHEY_PLAIN, 1,(0,0,255),1 )
    
matchs.sort(key=lambda x : x[0])

cv2.drawContours(shapes, [matchs[0][1]], -1, (0,255,0), 3)
cv2.imshow('Match Shape', shapes)
cv2.waitKey()
cv2.destroyAllWindows()

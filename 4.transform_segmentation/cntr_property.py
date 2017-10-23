import cv2
import numpy as np

img = cv2.imread('../img/korea.jpg')
cv2.imshow('origin', img)
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, th = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY_INV)
im, contours, hr = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

contours.sort(key=cv2.contourArea, reverse=True)
k_peninsula = contours[0]
cv2.drawContours(img, [k_peninsula], -1, (0,0,0), 2)

mmt = cv2.moments(k_peninsula)
cx = int(mmt['m10']/mmt['m00'])
cy = int(mmt['m01']/mmt['m00'])

x,y,w,h = cv2.boundingRect(k_peninsula)
korea_rect_area = w*h
korea_area = cv2.contourArea(k_peninsula)
hull = cv2.convexHull(k_peninsula)
hull_area = cv2.contourArea(hull)
ellipse = cv2.fitEllipse(k_peninsula)

aspect_ratio = w/h
extent = korea_area/korea_rect_area
solidity = korea_area / hull_area

print("Korea aspect ratio : %f" % aspect_ratio)
print("Korea extent : %f" % extent)
print("Korea Solidity: %f" % solidity)
print("Korea Orientation: %f" % ellipse[2])

equavalent_diameter = np.sqrt(4*korea_area/np.pi)
korea_radius = int(equavalent_diameter/2)

cv2.circle(img, (cx, cy), 3, (0,0,255), -1)
cv2.circle(img, (cx, cy), korea_radius, (0,0,255), 2)
cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 2)
cv2.ellipse(img, ellipse, (255,0,0), 2)

leftmost = tuple(k_peninsula[k_peninsula[:, :, 0].argmin()][0])
rightmost = tuple(k_peninsula[k_peninsula[:, :, 0].argmax()][0])
topmost = tuple(k_peninsula[k_peninsula[:, :, 1].argmin()][0])
bottommost = tuple(k_peninsula[k_peninsula[:, :, 1].argmax()][0])

cv2.circle(img, leftmost, 3, (0,0,255), -1)
cv2.circle(img, rightmost, 3, (0,0,255), -1)
cv2.circle(img, topmost, 3, (0,0,255), -1)
cv2.circle(img, bottommost, 3, (0,0,255), -1)
cv2.imshow('Korea Peninsula', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('korea', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
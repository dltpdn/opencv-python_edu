#-*-coding:utf-8 -*-
import cv2

img = cv2.imread('../img/model.jpg')

lower_reso = cv2.pyrDown(img) # img x 1/4
higher_reso = cv2.pyrUp(img) # img x 4

cv2.imshow('img', img)
cv2.imshow('lower', lower_reso)
cv2.imshow('higher', higher_reso)

cv2.waitKey(0)

cv2.destroyAllWindows()

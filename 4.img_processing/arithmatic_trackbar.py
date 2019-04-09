import cv2
import numpy as np

win_name = "Arithmatic"
trackbar_name = "Brightness"
def onChange(x):
    img2 = cv2.add(img, x)
    cv2.imshow(win_name, img2)

img = cv2.imread('../img/girl.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow(win_name, img)
cv2.createTrackbar(trackbar_name, win_name, 0, 255, onChange)
cv2.setTrackbarMax(trackbar_name, win_name, 255)
cv2.setTrackbarMin(trackbar_name, win_name, -255)
cv2.setTrackbarPos(trackbar_name, win_name, 0)

cv2.waitKey()
cv2.destroyAllWindows()


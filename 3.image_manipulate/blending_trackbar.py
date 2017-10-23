import cv2
import numpy as np

img1 = cv2.imread('../img/wingwall.jpg')
img2 = cv2.imread('../img/yate.jpg')


def onMouse(x):
    pass

cv2.namedWindow("ImageMixing")
cv2.createTrackbar('Fade','ImageMixing', 0, 100, lambda x : None)


while True:
    alpha = cv2.getTrackbarPos('Fade', 'ImageMixing')
    alpha = alpha/100.0
    dst = cv2.addWeighted(img1, 1-alpha, img2, alpha, 0) 
    cv2.imshow('ImageMixing', dst)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
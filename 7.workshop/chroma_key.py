import cv2
import numpy as np

img = cv2.imread('../img/chroma_key.jpg')
img_park = cv2.imread('../img/park.jpg')
h, w = img_park.shape[:2]
img = cv2.resize(img, (w,h), interpolation = cv2.INTER_CUBIC)
chroma = img[:10, :10, :]

hsv_chroma = cv2.cvtColor(chroma, cv2.COLOR_BGR2HSV)
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
chroma_h, chroma_s, chroma_v = cv2.split(hsv_chroma)

lower = np.array([chroma_h.min()-5, 0, 0])
upper = np.array([chroma_h.max()+5, 255,255])
mask = cv2.inRange(hsv_img, lower, upper)
mask_inv = cv2.bitwise_not(mask)
fg = cv2.bitwise_and(img, img, mask=mask_inv)
bg = cv2.bitwise_and(img_park, img_park, mask=mask)
added = fg + bg
cv2.imshow('origin', img)
cv2.imshow('fg', fg)
cv2.imshow('bg', bg)
cv2.imshow('added', added)
cv2.waitKey()
cv2.destroyAllWindows()
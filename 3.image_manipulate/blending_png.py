import cv2
import numpy as np

img_cat = cv2.imread('../img/cat.png', cv2.IMREAD_UNCHANGED)
#img_cat = cv2.imread('../img/cat.png')
print(img_cat.shape)
img_cat = cv2.resize(img_cat, None, fx=0.3, fy=0.3)
cv2.imshow('cat', img_cat)

img_park = cv2.imread('../img/park.jpg')
cv2.imshow('park', img_park)
cv2.waitKey()
ret, mask = cv2.threshold(img_cat[:,:,3], 1, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
cat_h, cat_w = img_cat.shape[:2]
park_h, park_w = img_park.shape[:2]
img = cv2.cvtColor(img_cat, cv2.COLOR_BGRA2BGR)
(roi_y, roi_x) = park_h//2-cat_h//2, park_w//2-cat_w//2
park_roi = img_park[roi_y:roi_y+cat_h, roi_x:roi_x+cat_w ]


masked_cat = cv2.bitwise_and(img, img, mask=mask)
masked_park = cv2.bitwise_and(park_roi, park_roi, mask=mask_inv)
added = masked_cat + masked_park
img_park[roi_y:roi_y+cat_h, roi_x:roi_x+cat_w] = added
cv2.imshow('mask', mask)
cv2.imshow('mask_inv', mask_inv)
cv2.imshow('cat', img)
cv2.imshow('park', img_park)
cv2.imshow('park_roi', park_roi)
cv2.imshow('masked_cat', masked_cat)
cv2.imshow('masked_park', masked_park)
cv2.waitKey()
cv2.destroyAllWindows() 
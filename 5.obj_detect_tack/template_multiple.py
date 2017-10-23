import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../img/mario.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("mario", img)

template = cv2.imread('../img/mario_template.png',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(imgray,template,cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
threshold = max_val * (1-0.01)
print("max:%f, threshold : %f" %(max_val, threshold))

loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

cv2.imshow('Question Box',img)
cv2.waitKey()
cv2.destroyAllWindows()
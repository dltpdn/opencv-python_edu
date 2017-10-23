import cv2
import numpy as np
import random
from matplotlib import pyplot as plt

img = cv2.imread('../img/contour_hierarchy.jpg')

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray,125,255,0)

image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(hierarchy)
for i in range(len(contours)):
    b = random.randrange(1,255)
    g = random.randrange(1,255)
    r = random.randrange(1,255)

    cnt = contours[i]
    img = cv2.drawContours(img, [cnt], -1,(b,g,r), 2)
    cv2.putText(img, '%d'%i, tuple(cnt[0,0]), cv2.FONT_HERSHEY_PLAIN, 2, (b,g,r), 2)
cv2.imshow('Hierarchy', img)
cv2.waitKey()
cv2.destroyAllWindows()
plt.show()

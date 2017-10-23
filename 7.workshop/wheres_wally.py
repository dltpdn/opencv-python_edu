import cv2
import numpy as np
import matplotlib.pyplot as plt

target = cv2.imread('../img/wally_beach.jpg')
cv2.imshow('Where is Wally?', target)
cv2.waitKey()


gray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)

template = cv2.imread('../img/wally.jpg', cv2.IMREAD_GRAYSCALE)
w, h = template.shape[:: -1]

res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
cv2.rectangle(target, top_left, bottom_right, (0,0,255), 3)    
    
cv2.imshow('Found Wally!', target)
cv2.waitKey()
cv2.destroyAllWindows()    
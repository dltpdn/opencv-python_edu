import cv2
import numpy as np

img = cv2.imread('../img/yate.jpg')

#364X320, 13x27
lighthouse = img[320:320+27, 364:364+13]

cv2.rectangle(img, (364,320), (364+13,320+27), (0,255,0))
cv2.imshow("habor", img)

cv2.imshow("light house",lighthouse)

cv2.waitKey(0)
cv2.destroyAllWindows()
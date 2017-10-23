import cv2
import numpy as np

file_name="../img/model.jpg"
win_name = 'filter2D'

img = cv2.imread(file_name)
cv2.namedWindow(win_name)
cv2.createTrackbar('kernel', win_name, 1, 100, lambda x : None)
while(True):
    if cv2.waitKey(1) & 0xFF == 27:
        break
    k = cv2.getTrackbarPos('kernel', win_name)
    if k == 0:
        k=1
    kernel = np.ones( (k, k), np.float32) / (k**2)
    dst = cv2.filter2D(img, -1, kernel) #-1 : cv2.CV_8U
    cv2.imshow(win_name, dst)
        
cv2.destroyAllWindows()
        

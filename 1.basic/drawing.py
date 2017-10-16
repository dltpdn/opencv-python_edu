import cv2
import numpy as np

img = np.zeros( (512,512, 3), dtype=np.uint8)

cv2.line(img, (0,0), (511, 511), (255, 0,0) , 5) #arr, start, end, color(BGR), thickness
cv2.rectangle(img, (384,0), (509,128), (0,255,0), 3) #arr, (left-top),(right-bottom),color(GBR), thickness 
cv2.circle(img, (447,63), 63, (0,0,255), -1), #arr, center(x,y), radius, color, thickness(-1:fill)
cv2.ellipse(img, (256,256), (50,100), 45, 180, 360, (255,255,0), -1) #array, center(x,y), axes_len(first,second),angle, startAngle,endAnalge, color, thickness, lineType, shift
cv2.ellipse(img,(256,256),(200,100),0,45,225,(0,0,255),4)
pts = np.array( [[100,100], [150,150], [125,200],[75,200], [50,150]], dtype=np.int32)
pts.reshape( (-1,1,2))
cv2.polylines(img, [pts], True, (0,255,255), 5)

cv2.putText(img, 'OpenCV Test', (10, 500), cv2.FONT_HERSHEY_SIMPLEX, 4, (255,255,255), 2, cv2.LINE_AA)#:16

cv2.imshow('drwaing', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
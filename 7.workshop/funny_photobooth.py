import cv2
import numpy as np
import math

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
rows, cols = 240, 320
map_y, map_x = np.indices((rows, cols), dtype=np.float32)

map_mirror_x = map_x.copy()
map_mirror_y = map_y.copy()    
for r in range(rows):
    for c in range(cols):
        if c >= cols/2:
            map_mirror_x.itemset((r,c), cols-c-1)
    
map_wave_x = map_x + 15*np.sin(map_y/20)
map_wave_y = map_y + 15*np.sin(map_x/20)    
    
while True:
    ret, frame = cap.read()
    mirror=cv2.remap(frame,map_mirror_x,map_mirror_y,cv2.INTER_LINEAR)
    wave = cv2.remap(frame,map_wave_x,map_wave_y,cv2.INTER_LINEAR)
    merged = np.hstack((mirror, frame, wave))
    cv2.imshow('merged',merged)
    if cv2.waitKey(1) & 0xFF== 27:
        break
cap.release
cv2.destroyAllWindows()


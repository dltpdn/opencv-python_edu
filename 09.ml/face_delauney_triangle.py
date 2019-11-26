import cv2
import numpy as np
import time

import face_landmark as fmark
 
def draw_delaunay(img, subdiv ) :
    triangleList = subdiv.getTriangleList()
    h, w = img.shape[:2]
    for t in triangleList :
        pts = t.reshape(-1,2).astype(np.int32)
        # 좌표 중에 이미지 영역을 벗어나는 것을 제외(음수 등)
        if (pts < 0).sum() or (pts[:, 0] > w).sum() or (pts[:, 1] > h).sum(): 
            continue
        cv2.polylines(img, [pts], True, (255, 255,255), 1, cv2.LINE_AA)
        
if __name__ == '__main__':
    img = cv2.imread("../img/man_face.jpg")
    img_orig = img.copy()
    h, w = img.shape[:2]

    points = fmark.getPoints(img)
    subdiv = cv2.Subdiv2D((0,0,w,h))
    for p in points :
        subdiv.insert(p)
        if True: #animation
            img_draw = img.copy()
            draw_delaunay( img_draw, subdiv)        
            cv2.imshow("Delaunay", img_draw)
            cv2.waitKey(100)
    draw_delaunay( img, subdiv)
    
    for p in points :
        cv2.circle( img, p, 2, (0,0,255), 1, cv2.LINE_AA)
 
    cv2.imshow("Delaunay",img)
    cv2.waitKey(0)
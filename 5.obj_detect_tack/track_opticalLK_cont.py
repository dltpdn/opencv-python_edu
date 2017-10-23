import numpy as np, cv2

feature_params = dict(maxCorners=200,
                      qualityLevel=0.01,
                      minDistance=7,
                      blockSize=7)
lk_params = dict(winSize=(15,15), 
                 maxLevel=2, 
                 criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

track_len = 10
detect_interval = 5
tracks=[]
blackscreen = False

cap = cv2.VideoCapture('../img/slow_traffic.mp4')
frame_idx = 0
blackscreen = False
width = int(cap.get(3))
height = int(cap.get(4))
prevImg = None
currImg = None
    
while True:
    ret, frame = cap.read()
    if not ret:
        break
    currImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    if blackscreen:
        frame = np.zeros((height, width, 3), np.uint8)
    if len(tracks) > 0:
        p0 = np.float32([tr[-1] for tr in tracks]).reshape(-1,1,2)
        
        p1, st, err = cv2.calcOpticalFlowPyrLK(prevImg, currImg, p0, None, **lk_params)
        p0r, st, err = cv2.calcOpticalFlowPyrLK(currImg, prevImg, p1, None, **lk_params)
        d = abs(p0-p0r).reshape(-1,2).max(-1)
        good = d < 1
        new_tracks =[]
        for tr, (x,y), good_flag in zip(tracks, p1.reshape(-1,2), good):
            if not good_flag:
                continue
            tr.append((x,y))
            if len(tr) > track_len:
                del tr[0]
                
            new_tracks.append(tr)
            cv2.circle(frame, (x,y), 2, (0,255,0), -1)
        tracks = new_tracks
        cv2.polylines(frame, [np.int32(tr) for tr in tracks], False, (0,255,0))
        
    if frame_idx % detect_interval == 0:
        mask = np.zeros_like(currImg)
        mask[:] = 255
        for x,y in [np.int32(tr[-1]) for tr in tracks]:
            cv2.circle(mask, (x,y), 5, 0, -1)
        p = cv2.goodFeaturesToTrack(currImg, mask=mask, **feature_params)
        if p is not None:
            for x, y in np.float32(p).reshape(-1, 2):
                tracks.append([(x,y)])
                
    frame_idx += 1
    prevImg = currImg
    
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xff == 27:
        break
    
cap.release()
cv2.destroyAllWindows()
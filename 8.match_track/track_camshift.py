import numpy as np
import cv2

filename = '../img/slow_traffic.mp4'
#filename = '../img/slow.flv'
roi_hist = None     # 추적 객체 히스토그램 저장 변수
win_name = 'MeanShift Tracking'
termination =  (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

cap = cv2.VideoCapture(filename)
fps = cap.get(cv2.CAP_PROP_FPS) # 프레임 수 구하기
delay = int(1000/fps)
print(delay)
isInit = True
while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break    
    img_draw = frame.copy()
    
    if roi_hist is not None:  # 추적 대상 객체 히스토그램 등록 됨
        # 전체 영상 hsv 컬로 변환 ---
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # 전체 영상 히스토그램과 roi 히스트그램 역투영 ---
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0,180], 1)
        # 역 투영 결과와 초기 추적 위치로 평균 이동 추적 ---
        ret, (x,y,w,h) = cv2.CamShift(dst, (x,y,w,h), termination)
        # 새로운 위치에 사각형 표시 ---
        #(x,y,w,h) = window
        cv2.rectangle(img_draw, (x,y), (x+w, y+h), (0,255,0), 2)
        # 컬러 영상과 역투영 영상을 통합해서 출력
        result = np.hstack((img_draw, cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)))
    else:  # 추적 대상 객체 히스토그램 등록 안됨
        cv2.putText(img_draw, "Hit the Space to set target to track", (10,30),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 1, cv2.LINE_AA)
        result = img_draw

    cv2.imshow(win_name, result)
    key = cv2.waitKey(delay) & 0xff
    if  key == 27: # Esc
        break
    if key == ord(' ') or isInit: # 스페이스-바, ROI 설정
        x,y,w,h = cv2.selectROI(win_name, frame, False)
        if w and h :    # ROI가 제대로 설정됨
            # 초기 추적 대상 위치로 roi 설정
            roi = frame[y:y+h, x:x+w]
            # roi를 HSV 컬러로 변경
            roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
            # 너무 어두운 영역 제외 시키기 위한 마스크(
            mask = cv2.inRange(roi, np.array((0., 60.,30.)), np.array((180.,255.,255.)))
            mask = None
            # roi에 대한 히스토그램 계산
            roi_hist = cv2.calcHist([roi], [0], mask, [180], [0,180])
            cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
            isInit = False
        else:                       # ROI 설정 안됨
            roi_hist = None
else:
    print('no camera!')
cap.release()
cv2.destroyAllWindows()
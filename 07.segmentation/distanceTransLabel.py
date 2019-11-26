import cv2
import numpy as np

# 이미지를 읽어서 바이너리 스케일로 변환
img = cv2.imread('../img/2full_body.jpg')
imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, biimg = cv2.threshold(imggray, 127, 255, cv2.THRESH_BINARY_INV)

# 거리 변환 ---①
dst, labels = cv2.distanceTransformWithLabels(biimg, cv2.DIST_L2, 5)
print( np.unique(labels))
# 거리 값을 0 ~ 255 범위로 정규화 ---②
dst = (dst/(dst.max()-dst.min()) * 255).astype(np.uint8)
# 거리 값에 쓰레시홀드로 완전한 뼈대 찾기 ---③
skeleton = cv2.adaptiveThreshold(dst, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 7, -3)
# 결과 출력
skeleton = cv2.cvtColor(skeleton, cv2.COLOR_GRAY2BGR)
for i in np.unique(labels):
    skeleton[labels==i ] =  [int(j) for j in np.random.randint(0,255, 3)]

cv2.imshow('origin', img)
cv2.imshow('dist', dst)
cv2.imshow('skel', skeleton)
cv2.waitKey(0)
cv2.destroyAllWindows()

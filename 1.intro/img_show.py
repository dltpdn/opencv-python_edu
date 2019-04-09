import cv2

img_file = "../img/girl.jpg" # 실행 후 표시할 이미지 경로 --------①
img = cv2.imread(img_file) 

if not img is None:
    cv2.imshow('IMG', img)
    while True:
        key = cv2.waitKey(0) #& 0xFF
        if key  == 27:
            cv2.destroyAllWindows()
            break
else:
    print('No image file.')
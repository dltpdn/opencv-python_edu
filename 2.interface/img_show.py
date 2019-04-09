import cv2

img_file = "./img/girl.jpg" # 실행 후 표시할 이미지 경로 --------①
img = cv2.imread(img_file) 

if img is not None:
    cv2.imshow('IMG', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print('No image file.')
    
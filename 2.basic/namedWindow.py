import cv2

img_file = "../img/model.jpg"

#img = cv2.imread(img_file)
#img = cv2.imread(img_file, cv2.IMREAD_COLOR) #default
#img = cv2.imread(img_file, cv2.IMREAD_UNCHANGED)
img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)

cv2.namedWindow(img_file, cv2.WINDOW_AUTOSIZE)
#cv2.namedWindow(img_file, cv2.WINDOW_NORMAL)

if not img is None:
    cv2.imshow(img_file, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("no file:", img_file)
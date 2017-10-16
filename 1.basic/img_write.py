import cv2

img_file = "../img/model.jpg"

img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
cv2.imshow(img_file, img)
key = cv2.waitKey(0) & 0xFF

if key == 27: #esc
    cv2.destroyAllWindows()
elif key == ord('s'):
    print('saving file.');
    cv2.imwrite("./gray.jpg", img) #file format depends on file extension
    cv2.destroyAllWindows()

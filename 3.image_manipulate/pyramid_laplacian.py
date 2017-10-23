import cv2

img = cv2.imread('../img/model.jpg')
cols, rows = img.shape[:2]
print('origin', rows, cols)
lower = cv2.pyrDown(img)
print('lower', lower.shape[1], lower.shape[0])
higher = cv2.pyrUp(lower)
print('higher', higher.shape[1], higher.shape[0])

higher = cv2.resize(higher, (rows, cols))
laplacian = cv2.subtract(img, higher)


cv2.imshow('laplacian', laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()

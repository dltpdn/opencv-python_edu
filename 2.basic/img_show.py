import cv2

img_file = "../img/model.jpg"
img = cv2.imread(img_file)

if not img is None:
    print(type(img))
    while True:
        cv2.imshow('model', img)
        if cv2.waitKey(0) & 0xFF == 27:
            break
    cv2.destroyAllWindows()
else:
    print("no file:" , img_file)
import cv2
import numpy as np

names = ['airplanes', 'Faces', 'Leopards','Motorbikes' ]
imgs = ['../img/aircraft.jpg','../img/leopard.jpg', '../img/man_face.jpg', '../img/motorbike.jpg']

detector = cv2.xfeatures2d.SIFT_create()
bowextractor = cv2.BOWImgDescriptorExtractor(detector, cv2.BFMatcher(cv2.NORM_L2))
dictionary = np.load('./101dict.npy')
bowextractor.setVocabulary(dictionary)
svm  = cv2.ml.SVM_load('./svm_bow.xml')

for i, path in enumerate(imgs):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hist = bowextractor.compute(gray, detector.detect(gray))
    ret, result = svm.predict(hist)

    name = names[int(result[0][0])]
    txt, base = cv2.getTextSize(name, cv2.FONT_HERSHEY_PLAIN, 2, 3)
    x,y = 10, 50
    cv2.rectangle(img, (x,y-base-txt[1]), (x+txt[0], y+txt[1]), (30,30,30), -1)
    cv2.putText(img, name, (x,y), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0), 2, cv2.LINE_AA)
    cv2.imshow(path, img)
cv2.waitKey(0)
cv2.destroyAllWindows()
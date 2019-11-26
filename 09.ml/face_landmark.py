# ref(Example code) : http://dlib.net/face_landmark_detection.py.html
# ref2(annotation map to 68) :https://ibug.doc.ic.ac.uk/resources/facial-point-annotations/
import cv2
import numpy as np
import dlib

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

def getFaceRects(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rects = detector(gray)
    return rects

def getShape(img, rect):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return predictor(gray, rect)

def rect2coords(rect):
	x = rect.left()
	y = rect.top()
	w = rect.right() - x
	h = rect.bottom() - y
	return (x, y, w, h)

def getPoints(img):
	points = []
	rects = getFaceRects(img)
	for rect in rects:
		shape = getShape(img, rect)
		for i in range(68):
			part = shape.part(i)
			points.append((part.x, part.y))
	return points


if __name__ == '__main__':
    img = cv2.imread("../img/man_face.jpg")

    faces = getFaceRects(img)
    for f_rect in faces:
        (x,y,w,h) = rect2coords(f_rect)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)

        shape = getShape(img, f_rect)
        for i in range(68):
            part = shape.part(i)
            cv2.circle(img, (part.x, part.y), 2, (0, 0, 255), 1)
            cv2.putText(img, str(i), (part.x, part.y), cv2.FONT_HERSHEY_PLAIN, 1,(255,255,255))

    cv2.imshow("face landmark", img)
    cv2.waitKey(0)
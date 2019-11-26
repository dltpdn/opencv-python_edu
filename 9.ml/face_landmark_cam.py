# ref(Example code) : http://dlib.net/face_landmark_detection.py.html
# ref2(annotation map to 68) :https://ibug.doc.ic.ac.uk/resources/facial-point-annotations/

# Instruction to run
# 1. Install CMake (http://cmake.org/download)
# 2. Install dlib (pip install dlib)
# 3. Download shape_predictor_68_face_landmarks.dat file (http://dlib.net/files/)
import cv2
import dlib
import numpy as np

import face_landmark as fmark


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    cap.set(cv2.cv2.CAP_PROP_FRAME_WIDTH, 320)
    cap.set(cv2.cv2.CAP_PROP_FRAME_HEIGHT, 240)
    cv2.namedWindow('face land mark', cv2.WINDOW_NORMAL | 16)

    while cap.isOpened():
        _, img = cap.read()
        faces = fmark.getFaceRects(img)

        for face in faces:
            shape = fmark.getShape(img, face)
            for i in range(68):
                part = shape.part(i)
                cv2.circle(img, (part.x, part.y), 1, (0, 0, 255), -1)
                #cv2.putText(img, str(i), (x,y), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255))
        cv2.imshow("face land mark", img)
        key = cv2.waitKey(1) 
        if key == 27:
            break
    cap.release()




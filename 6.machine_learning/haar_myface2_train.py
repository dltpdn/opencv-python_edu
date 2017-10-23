import cv2
import numpy as np
import os 
import os.path 

photo_dir = './faces'

# Get the training data we previously made
accuracy = 85

datas = dict([])
# Create arrays for training data and labels
Training_Data, Labels = [], []

try:
    dirs = [d for d in os.listdir(photo_dir) if os.path.isdir(os.path.join(photo_dir, d))]
    for dir in dirs:
        u_label = dir.split('_')[1]
        path = os.path.join(photo_dir, dir)
        onlyfiles = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        # Open training images in our datapath
        # Create a numpy array for training data
        for files in onlyfiles:
            
            label = os.path.splitext(files)[0]
            image_path = os.path.join(path, files)
            print(image_path)
            images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            Training_Data.append(np.asarray(images, dtype=np.uint8))
            Labels.append( (int(u_label)) * 10000 + int(label))
except Exception as e:
    print(e)

# Create a numpy array for both training data and labels
Labels = np.asarray(Labels, dtype=np.int32)

# Initialize facial recognizer
#model = cv2.createLBPHFaceRecognizer()
#model = cv2.face.createLBPHFaceRecognizer()  #cv 3.2.0
model = cv2.face.LBPHFaceRecognizer_create()  #cv2 3.3.0
# NOTE: For OpenCV 3.0 use cv2.face.createLBPHFaceRecognizer()

# Let's train our model 
model.train(np.asarray(Training_Data), np.asarray(Labels))
print("Model trained sucessefully")
model.write('./faces/all_face.xml')
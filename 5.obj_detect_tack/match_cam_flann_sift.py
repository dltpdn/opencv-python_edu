import cv2
import numpy as np


def sift_detector(new_image, image_template):
    # Function that compares input image to template
    # It then returns the number of SIFT matches between them
    
    image1 = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)
    image2 = image_template
    
    # Create SIFT detector object
    sift = cv2.xfeatures2d.SIFT_create()

    # Obtain the keypoints and descriptors using SIFT
    keypoints_1, descriptors_1 = sift.detectAndCompute(image1, None)
    keypoints_2, descriptors_2 = sift.detectAndCompute(image2, None)

    # Define parameters for our Flann Matcher
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 3)
    search_params = dict(checks = 100)

    # Create the Flann Matcher object
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    # Obtain matches using K-Nearest Neighbor Method
    # the result 'matchs' is the number of similar matches found in both images
    matches = flann.knnMatch(descriptors_1, descriptors_2, k=2)

    # Store good matches using Lowe's ratio test
    good_matches = []
    for m,n in matches:
        if m.distance < 0.7 * n.distance:
            good_matches.append(m) 

    return len(good_matches)


cap = cv2.VideoCapture(0)
w = 640; h=480
cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)

print(cap.get(cv2.CAP_PROP_FPS))
cap.set(cv2.CAP_PROP_FPS, 5)
print(cap.get(cv2.CAP_PROP_FPS))
# Load our image template, this is our reference image
image_template = cv2.imread('../img/rpi_box.jpg', 0) 

while True:

    # Get webcam images
    ret, frame = cap.read()
    # Get height and width of webcam frame
    height, width = frame.shape[:2]

    # Define ROI Box Dimensions
    left = width // 3
    right = (width // 3) * 2
    top = (height // 2) - (height // 4)
    bottom = (height // 2) + (height // 4)

    
    # Draw rectangular window for our region of interest   
    cv2.rectangle(frame, (left,top), (right,bottom), (255,255,255), 3)
    
    # Crop window of observation we defined above
    cropped = frame[top:bottom , left:right]
    
    # Flip frame orientation horizontally
    frame = cv2.flip(frame,1)
    
    # Get number of SIFT matches
    matches = sift_detector(cropped, image_template)

    # Display status string showing the current no. of matches 
    cv2.putText(frame,str(matches),(left,bottom+10), cv2.FONT_HERSHEY_COMPLEX, 0.5,(0,255,0),1)
    
    # Our threshold to indicate object deteciton
    # We use 10 since the SIFT detector returns little false positves
    threshold = 10
    
    # If matches exceed our threshold then object has been detected
    if matches > threshold:
        cv2.rectangle(frame, (left,top), (right,bottom), (0,255,0), 3)
        cv2.putText(frame,'Object Found',(left,top-10), cv2.FONT_HERSHEY_COMPLEX, 1 ,(0,255,0), 1)
    
    cv2.imshow('win', frame)
    cv2.moveWindow('win', 0, 0)
    if cv2.waitKey(1) & 0xFF == 27: #ESC Key
        break

cap.release()
cv2.destroyAllWindows()   
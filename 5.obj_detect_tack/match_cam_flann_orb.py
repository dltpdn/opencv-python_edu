import cv2, time
import numpy as np


def ORB_detector(new_image, image_template):
    # Function that compares input image to template
    # It then returns the number of ORB matches between them
    
    image1 = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)

    # Create ORB detector with 1000 keypoints with a scaling pyramid factor of 1.2
    #orb = cv2.ORB(1000, 1.2)
    orb = cv2.ORB_create(1000, 1.2)

    # Detect keypoints of original image
    (kp1, des1) = orb.detectAndCompute(image1, None)

    # Detect keypoints of rotated image
    (kp2, des2) = orb.detectAndCompute(image_template, None)

    # Create matcher 
    # Note we're no longer using Flannbased matching
   # Define parameters for our Flann Matcher
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 3)
    #search_params = dict(checks = 100)
    FLANN_INDEX_LSH = 6
    #index_params = dict(algorithm = 255, table_number=6, key_size=12, multi_probe_level=1)
    #index_params = dict(algorithm = FLANN_INDEX_LSH, table_number=12, key_size=20, multi_probe_level=2)
    search_params = dict(checks = 100)
    # Create the Flann Matcher object
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    # Obtain matches using K-Nearest Neighbor Method
    # the result 'matchs' is the number of similar matches found in both images
    #matches = flann.knnMatch(np.float32(des1), np.float32(des2), 2)
    if  not des1.size or not des2.size:
        print('empty')
        return 0
    #matches = flann.knnMatch(des1, des2, k=2)
    matches = flann.knnMatch(np.asarray(des1, np.float32), np.asarray(des2, np.float32), k=2)
    good_matches = []
    for m,n in matches:
        if m.distance < 0.7 * n.distance:
            good_matches.append(m) 

    return len(good_matches)


cap = cv2.VideoCapture(0) #1280,720
w = 640;h=480
cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FPS))
cap.set(cv2.CAP_PROP_FPS, 10)
print(cap.get(cv2.CAP_PROP_FPS))
# Load our image template, this is our reference image
image_template = cv2.imread('../img/rpi_box.jpg', 0) 
# image_template = cv2.imread('images/kitkat.jpg', 0) 
while True:
    # Get webcam images
    ret, frame = cap.read()
    if not ret:
        continue
    # Get height and width of webcam frame
    height, width = frame.shape[:2]

    # Define ROI Box Dimensions (Note some of these things should be outside the loop)
    left = width // 3
    bottom = (height // 2) + (height // 4)
    right = (width // 3) * 2
    top = (height // 2) - (height // 4)
    
    # Draw rectangular window for our region of interest
    cv2.rectangle(frame, (left,top), (right,bottom), (255,255,255), 3)
    
    # Crop window of observation we defined above
    cropped = frame[top:bottom , left:right]

    # Flip frame orientation horizontally
    frame = cv2.flip(frame,1)
    
    # Get number of ORB matches 
    matches = ORB_detector(cropped, image_template)
    
    # Display status string showing the current no. of matches 
    output_string = str(matches)
    cv2.putText(frame, output_string, (left,bottom+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
    
    # Our threshold to indicate object deteciton
    # For new images or lightening conditions you may need to experiment a bit 
    # Note: The ORB detector to get the top 1000 matches, 300 is essentially a min 30% match
    threshold = 5
    
    # If matches exceed our threshold then object has been detected
    if matches > threshold:
        cv2.rectangle(frame, (left,top), (right,bottom), (0,255,0), 3)
        cv2.putText(frame,'Object Found',(left,top-10), cv2.FONT_HERSHEY_COMPLEX, 1 ,(0,255,0), 1)
    
    cv2.imshow('Object Detector using ORB', frame)
    cv2.moveWindow('Object Detector using ORB', 0,0)
    if cv2.waitKey(1) == 27: #ESC Key
        break

cap.release()
cv2.destroyAllWindows()   
import numpy as np
import cv2

# Let's take a look at our digits dataset
image = cv2.imread('../img/digits.png')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
small = cv2.pyrDown(image)
cv2.imshow('Digits Image', small)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Split the image to 5000 cells, each 20x20 size
# This gives us a 4-dim array: 50 x 100 x 20 x 20
cells = [np.hsplit(row,100) for row in np.vsplit(gray,50)]

# Convert the List data type to Numpy Array of shape (50,100,20,20)
x = np.array(cells)
print ("The shape of our cells array: " + str(x.shape))

# Split the full data set into two segments
# One will be used fro Training the model, the other as a test data set
train = x[:,:90].reshape(-1,400).astype(np.float32) # Size = (3500,400)
test = x[:,90:100].reshape(-1,400).astype(np.float32) # Size = (1500,400)

# Create labels for train and test data
k = [0,1,2,3,4,5,6,7,8,9]
train_labels = np.repeat(k,450)[:,np.newaxis]
test_labels = np.repeat(k,50)[:,np.newaxis]

# Initiate kNN, train the data, then test it with test data for k=3
#knn = cv2.KNearest()
knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)

ret, result, neighbors, distance = knn.findNearest(test, k=3)

# Now we check the accuracy of classification
# For that, compare the result with test_labels and check which are wrong
matches = result == test_labels
correct = np.count_nonzero(matches)
accuracy = correct * (100.0 / result.size)
print("correct : %d , result.size : %d, Accuracy is = %.2f" % (correct, result.size, accuracy, ) + "%")

knn.save('digits.yaml') # but knn.load(..) is not implemented

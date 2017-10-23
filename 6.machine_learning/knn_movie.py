import cv2
import numpy as np
import matplotlib.pyplot as plt

trainData = np.random.randint(0,100,(25,2)).astype(np.float32)
responses = (trainData[:, 0] >trainData[:,1]).astype(np.float32)

romantic = trainData[responses==1]
action = trainData[responses==0]

plt.scatter(action[:,0],action[:,1],s=80,marker='^', c="blue", label='action')
plt.scatter(romantic[:,0],romantic[:,1], s=80, c='m', marker='o', label="romantic")

newcomer = np.random.randint(0,100,(1,2)).astype(np.float32)
plt.scatter(newcomer[:,0],newcomer[:,1],200,'r','*', label="new")
knn = cv2.ml.KNearest_create()
knn.train(trainData, cv2.ml.ROW_SAMPLE, responses)
ret, results, neighbours ,dist = knn.findNearest(newcomer, 3)#K=3

print( "result(0=action, 1:romantic):  {}\n".format(results) )
print( "neighbours:  {}\n".format(neighbours) )
print( "distance:  {}\n".format(dist) )
label = results == 1 and "romantic" or "action" 

anno_x, anno_y = newcomer.ravel()
plt.annotate(label, xy=(anno_x + 1, anno_y+1), xytext=(anno_x+5, anno_y+10), arrowprops={'color':'green'})
plt.xlabel('kiss count')
plt.ylabel('hit count')
plt.legend(loc="upper right")
plt.show()
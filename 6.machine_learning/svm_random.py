import cv2
import numpy as np
import matplotlib.pylab as plt
 
trainData = np.random.randint(0,100,(25,2)).astype(np.float32)
responses = np.random.randint(0,2,(25,1))

print(trainData.shape, responses.shape)

red = trainData[responses.ravel()==0]
plt.scatter(red[:,0],red[:,1],80,'r','^')
blue = trainData[responses.ravel()==1]
plt.scatter(blue[:,0],blue[:,1],80,'b','s')

newcomer = np.random.randint(0,100,(1,2)).astype(np.float32)
#newcomer = np.array([(50,50)]).astype(np.float32)
#newcomer = np.array([(400,400)]).astype(np.float32)
plt.scatter(newcomer[:,0],newcomer[:,1],80,'g','o')

C=1
model = cv2.ml.SVM_create()
#model.setGamma(gamma)
#model.setC(C)
model.setKernel(cv2.ml.SVM_RBF)
#model.setKernel(cv2.ml.SVM_LINEAR)
model.setType(cv2.ml.SVM_C_SVC)
model.train(trainData, cv2.ml.ROW_SAMPLE, responses)
model.save('./svmtrain.xml')


#model  = cv2.ml.SVM_create()
#model2.read('./svmtrain.xml')
ret, results = model.predict(newcomer)
print('ret', ret)
print("result, 0=red, 1=blue:  {}\n".format(results))

plt.show()
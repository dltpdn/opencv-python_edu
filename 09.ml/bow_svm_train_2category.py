import cv2
import numpy as np
import os, glob, time

startT = time.time()
dictionary_size = 50
categories =  ['airplanes', 'Motorbikes' ]
base_path = "../img/101_ObjectCategories/"

detector = cv2.xfeatures2d.SIFT_create()
matcher = cv2.BFMatcher(cv2.NORM_L2)
bowTrainer = cv2.BOWKMeansTrainer(dictionary_size)

train_paths = []
train_labels = []
print('Adding descriptor to BOWTrainer...')
for idx, category in enumerate(categories):
    dir_path = base_path + category
    img_paths = glob.glob(dir_path +'/*.jpg')
    img_len = len(img_paths)
    for i, img_path in enumerate(img_paths):
        train_paths.append(img_path)
        train_labels.append(idx)
        img = cv2.imread(img_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        kpt, desc= detector.detectAndCompute(gray, None)
        bowTrainer.add(desc)
        print('\t%s %d/%d(%.2f%%)'%(category,i+1, img_len, (i+1)/img_len*100), end='\r')
    print()
print('\nAdding descriptor completed...')
print('Starting Dictionary clustering(%d)...It will take several time...'%dictionary_size)

dictionary = bowTrainer.cluster()
np.save('./airplanes_dict.npy', dictionary)    # .npy extension is added if not given
#dictionary = np.load('./101dict.npy')
print('Dictionary Clustering completed...dictionary shape:',dictionary.shape)
bowExtractor = cv2.BOWImgDescriptorExtractor(detector, matcher)
bowExtractor.setVocabulary(dictionary)

train_desc = []
for i, path in enumerate(train_paths):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hist = bowExtractor.compute(gray, detector.detect(gray))
    train_desc.extend(hist)
    print('Compute histogram training set...(%.2f%%)'%((i+1)/len(train_paths)*100),end='\r')
print("\nsvm items", len(train_desc), len(train_desc[0]))
svm = cv2.ml.SVM_create()
print('svm training...')
svm.trainAuto(np.array(train_desc), cv2.ml.ROW_SAMPLE, np.array(train_labels))
svm.save('./svm_bow_airplanes.xml')
#svm  = cv2.ml.SVM_load('./svm_bow.xml')
print('svm training completed.')

########## evaluation ##############

print("Accuracy:")
for label, dir_name in enumerate(categories):
    labels = []
    results = []
    img_paths = glob.glob(base_path + '/'+dir_name +'/*.*')
    for img_path in img_paths:
        labels.append(label)
        img = cv2.imread(img_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        feature = bowExtractor.compute(gray, detector.detect(gray))
        ret, result = svm.predict(feature)
        resp = result[0][0]
        results.append(resp)

    labels = np.array(labels)
    results = np.array(results)
    err = (labels != results)
    err_mean = err.mean()
    print('\t%s: %.2f %%' % (dir_name, (1 - err_mean)*100))
print('Elapsed: %s'%time.strftime('%H:%M:%S', time.gmtime(time.time()-startT)))
import cv2
import numpy as np, matplotlib.pyplot as plt
import glob, math

names = ['10a', '10b', '50a', '50b', '100a', '100b', '500a', '500b']

def preprocess(img, limit=4.5 ):
    h, w = img.shape[:2]
    mask = np.zeros_like(img)
    center = (w//2, h//2)
    r = h if h<w else w
    radius = r//2
    cv2.circle(mask, center, radius-5, (255,255,255), -1, cv2.LINE_AA)
    masked = cv2.bitwise_and(img, mask)
    gray = cv2.cvtColor(masked, cv2.COLOR_BGR2GRAY)

    clahe = cv2.createCLAHE(limit)
    gray = clahe.apply(gray)
    return gray

sift = cv2.xfeatures2d.SIFT_create()
bowDiction = cv2.BOWImgDescriptorExtractor(sift, cv2.BFMatcher(cv2.NORM_L2))
dictionary = np.load('./dict_coin25000.npy')
bowDiction.setVocabulary(dictionary)

svm  = cv2.ml.SVM_load('./svm_bow_coin25000.xml')
coin_paths = glob.glob('../img/coins/*.*')
for i, coin_path in enumerate(coin_paths):
    img = cv2.imread(coin_path)
    gray = preprocess(img)
    feature = bowDiction.compute(gray, sift.detect(gray))
    ret, result = svm.predict(feature)

    name = names[int(result[0][0])]
    print(ret, result, name)
    plt.subplot(math.ceil(len(coin_paths)/5), 5, i+1)
    plt.imshow(img[:,:,::-1])
    plt.title(name)
    plt.xticks([]);plt.yticks([])
plt.show()
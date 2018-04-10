import cv2
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

def otsu_intraclass(img):
    hist = cv2.calcHist([img],[0],None,[256],[0,256])
    hist_norm = hist.ravel()/hist.max()
    Q = hist_norm.cumsum()

    bins = np.arange(256)

    fn_min = np.inf
    thresh = -1

    for i in range(1,256):
        p1,p2 = np.hsplit(hist_norm,[i]) # probabilities
        q1,q2 = Q[i],Q[255]-Q[i] # cum sum of classes
        b1,b2 = np.hsplit(bins,[i]) # weights
    
        # finding means and variances
        m1,m2 = np.sum(p1*b1)/q1, np.sum(p2*b2)/q2
        v1,v2 = np.sum(((b1-m1)**2)*p1)/q1,np.sum(((b2-m2)**2)*p2)/q2
    
        # calculates the minimization function
        fn = v1*q1 + v2*q2
        if fn < fn_min:
            fn_min = fn
            thresh = i
    return thresh
    
def otsu_interclass(img):

    nbins = 256#np.max(img)-np.min(img) #256 # or np.max(img)-np.min(img) for images with non-regular pixel values
    print(nbins)
    pixel_counts  = Counter(img.ravel())
    counts = np.array([0 for x in range(nbins)])
    for c in sorted(pixel_counts):
        counts[c] = pixel_counts[c]
    p = counts/sum(counts)
    sigma_b = np.zeros((nbins, 1))

    for t in range(nbins):
        q_L = sum(p[:t]) 
        q_H = sum(p[t:]) 
        if q_L ==0 or q_H == 0:
            continue
        miu_L = sum(np.dot(p[:t], np.transpose(np.matrix([i for i in range(t)]) )))/q_L
        miu_H = sum(np.dot(p[t:], np.transpose(np.matrix([i for i in range(t, nbins)]))))/q_H
        sigma_b[t] = q_L*q_H*(miu_L-miu_H)**2

    return np.argmax(sigma_b)

file_name = "../img/noise.jpg"
#file_name = "../img/lena_noise.jpg"
#file_name = "../img/face_noise.jpg"

origin = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)
blur = cv2.GaussianBlur(origin, (5,5), 0)

inter_th = otsu_interclass(blur)
intra_th = otsu_intraclass(blur)

ret1, th1 = cv2.threshold(blur, inter_th, 255, cv2.THRESH_BINARY)
ret2, th2 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print("inter_th: %d, intra_th: %d, THRESH_OTSU th : %d " % (inter_th, intra_th, ret2))

imgs = [origin, th1, th2]
titles = ['Origin', inter_th, "THRESH_OTSU"]

for i in range(3):
    plt.subplot(1,3,i+1)
    plt.imshow(imgs[i], 'gray')
    plt.title(titles[i]),
    plt.xticks([]), plt.yticks([])
    
plt.show()

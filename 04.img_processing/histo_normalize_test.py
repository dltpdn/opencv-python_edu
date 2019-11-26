import cv2
import numpy as np

a = np.array([70,96,98,98,100], dtype=np.uint8)

b = np.zeros_like(a)
c = cv2.normalize(a, None, 0, 100, cv2.NORM_MINMAX)
b = (a - a.min()) * (100-70) / (a.max() - a.min()) + 70

#print(a, b, c)

eh = cv2.calcHist([a], [0], None, [101], [0, 101])
cdf = eh.cumsum()
cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m - cdf_m.min()) / 4 * 100
cdf = np.ma.filled(cdf_m, 0).astype(np.uint8)
em = cdf[a]
print(em)
print("#"*80)


e = cv2.equalizeHist(a)
e2 = cv2.normalize(e, None, 0, 100, cv2.NORM_MINMAX)
print(e2)

print("#"*80)
############################ 히스토그램 정규화를 통화 이퀄라이즈 ########
hist = cv2.calcHist([a], [0], None, [101], [0, 101])
nhist = cv2.normalize(hist, None, 1,0, cv2.NORM_L1)
cnhist = nhist.cumsum()
eq = cnhist * 100
eqed = eq[a]
print(eqed)#hist, nhist, cnhist, eq, eqed)

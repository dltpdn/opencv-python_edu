import cv2
import numpy as np
import matplotlib.pyplot as plt

img = np.array([[0,0,1,4,4,5],
                [0,1,3,4,3,4],
                [1,3,4,2,1,3],
                [4,4,3,1,0,0],
                [5,4,2,1,0,0],
                [5,5,4,3,1,0]], dtype=np.uint8)

hist = cv2.calcHist([img], [0], None, [6], [0,6]).reshape(-1)
print(hist)

min_class_v = None
threshold= 0
for t in range(6):
    w1 = hist[:t].sum() / hist.sum()
    w2 = hist[t:].sum() / hist.sum()
    m1 = np.nan_to_num(img[img<t].mean())
    m2 = np.nan_to_num(img[img>=t].mean())
    v1 = np.nan_to_num(img[img<t].var())
    v2 = np.nan_to_num(img[img>=t].var())
    #v1 = np.nan_to_num(((m1 - img[img<t]) **2).mean())
    #v2 = np.nan_to_num(((m2 - img[img>=t]) **2).mean())

    in_class_v = w1* v1 + w2* v2
    print(f"t:{t}, w1:{w1:.2f}, w2:{w2:.2f}, m1:{m1:.2f}, m2:{m2:.2f}, v1:{v1:.2f}, v2:{v2:.2f}, inter class v:{in_class_v:.2f}")
    if min_class_v is None or min_class_v > in_class_v :
        min_class_v = in_class_v
        threshold = t
print(f"threshold : {threshold}, min inter class variance:{min_class_v:.2f}")

plt.subplot(1,2,1)
plt.bar(range(6),hist)
plt.subplot(1,2,2)
plt.imshow(img, cmap='gray')
plt.show()

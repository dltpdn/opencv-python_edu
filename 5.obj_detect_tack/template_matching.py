import cv2
import numpy as np
import matplotlib.pyplot as plt

model = cv2.imread('../img/model.jpg')
template = cv2.imread('../img/model_template.jpg')

c, w, h = template.shape[:: -1]

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for method_name in methods:
    img = model.copy()
    print(method_name)
    method = eval(method_name)
    try:
        res = cv2.matchTemplate(img, template, method)
        print(res.shape, res)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    except :
        print('Error', method_name)
        continue
    
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(img, top_left, bottom_right, (0,0,255),2)    
    
    plt.subplot(121)
    plt.imshow(res, cmap='gray')
    plt.title('Matching Result')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122)
    rgb=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)    
    plt.imshow(rgb)
    plt.title('Detected Point')
    plt.xticks([]), plt.yticks([])
    plt.suptitle(method_name)
    plt.show()
    
import cv2
import numpy as np
import matplotlib.pyplot as plt

file_name = "../img/noise.jpg"

img = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)
print(img.shape)

ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
blur = cv2.GaussianBlur(img, (5,5), 0)
ret, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
 
imgs = [img, 0, th1, img, 0, th2, blur, 0, th3]
titles = ['Original', 'Histogram', 'Global', 'Original', 'Histogram', 'Otsu', 'Original', 'Histogram', 'Outs after blur'] 
for i in range(3):
    plt.subplot(3,3,i*3+1)
    plt.imshow(imgs[i*3], 'gray')
    plt.title(titles[i*3]),
    plt.xticks([]), plt.yticks([])
    
    plt.subplot(3,3,i*3+2)
    plt.hist(imgs[i*3].ravel(),256)  #ravel: make 1-D array
    plt.title(titles[i*3+1]),
    plt.xticks([]), plt.yticks([])

    plt.subplot(3,3,i*3+3)
    plt.imshow(imgs[i*3+2], 'gray')
    plt.title(titles[i*3+2]),
    plt.xticks([]), plt.yticks([])

plt.show()
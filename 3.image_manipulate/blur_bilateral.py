import cv2
import matplotlib.pyplot as plt

file_name = "../img/gaussian_noise.jpg"
img = cv2.imread(file_name)

blur1 = cv2.GaussianBlur(img, (5,5), 0)
blur2 = cv2.bilateralFilter(img, 25, 75, 75)

plt.subplot(131)
plt.imshow(img)
plt.title('original')

plt.subplot(132)
plt.imshow(blur1)
plt.title('gaussian')

plt.subplot(133)
plt.imshow(blur2)
plt.title('bilateral')

plt.show()


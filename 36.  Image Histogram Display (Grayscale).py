import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Exp 1.png', 0)
plt.hist(img.ravel(), 256, [0, 256])
plt.title('Grayscale Histogram')
plt.show()

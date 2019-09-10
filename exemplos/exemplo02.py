from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

img = cv2.imread('lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(img)
plt.title('lena')
plt.show()
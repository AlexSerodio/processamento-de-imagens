# %matplotlib inline
from matplotlib import pyplot as plt 
import cv2

img = plt.imread('Cenario.jpg')
(thresh, blackAndWhiteImage) = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
 
cv2.imshow('Black white image', blackAndWhiteImage)
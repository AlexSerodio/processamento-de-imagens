import cv2
import numpy as np

img = cv2.imread('lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
(T, bin) = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
kernel = np.ones((5,5), np.uint8)
img_erosion = cv2.erode(bin, kernel, iterations=1)
img_dilation = cv2.dilate(bin, kernel, iterations=1)
cv2.imshow('original', img)
cv2.imshow('Erosao', img_erosion)
cv2.imshow('Dilatacao', img_dilation)
cv2.waitKey(0)
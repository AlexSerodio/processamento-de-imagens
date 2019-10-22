# Author: Alex Seródio Gonçalves

import cv2
import numpy as np

kernel = np.ones((3, 3))

original_image = cv2.imread('mama6.jpg')
original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

# erode = cv2.erode(original_image, kernel, iterations = 1)
# opening = cv2.dilate(erode, kernel, iterations = 1)
# tophat = cv2.subtract(original_image, opening)
tophat = cv2.morphologyEx(original_image, cv2.MORPH_TOPHAT, kernel)


# dilate = cv2.dilate(original_image, kernel, iterations = 1)
# closing = cv2.erode(dilate, kernel, iterations = 1)
# blackhat = cv2.subtract(closing, original_image)
blackhat = cv2.morphologyEx(original_image, cv2.MORPH_BLACKHAT, kernel)

k1 = cv2.add(original_image, tophat)
k = cv2.subtract(k1, blackhat)

no_background = cv2.subtract(k, original_image)
(thresh, binarizada) = cv2.threshold(no_background, 25, 255, cv2.THRESH_BINARY)

cv2.imshow("Imagem original", original_image)
cv2.imshow("Resultado", binarizada)
cv2.waitKey(0)
import numpy as np
import cv2

img = cv2.imread('olho.jpg', 0)
img = cv2.medianBlur(img, 5)

circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 400,
                    param1=20, param2=20, minRadius=0, maxRadius=50)

circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    cv2.circle(img, (i[0], i[1]), i[2], (0,255,0), thickness=2)

cv2.imshow('gray_img', img)
cv2.waitKey(0)
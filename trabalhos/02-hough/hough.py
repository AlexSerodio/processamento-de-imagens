import numpy as np
import cv2

img1 = cv2.imread('olho.jpg')
img = cv2.imread('olho.jpg', 0)
img = cv2.medianBlur(img, 5)
gray_img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray_img, 100, 255, cv2.THRESH_BINARY)

# Create mask
height, width = img.shape
mask = np.zeros((height, width), np.uint8)

edges = cv2.Canny(thresh, 100, 200)

cv2.imshow('gray_img', edges)

# circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 300,
#                     param1=30, param2=50, minRadius=0, maxRadius=250)

# circles = np.uint16(np.around(circles))

# for i in circles[0,:]:
#     cv2.circle(img, (i[0], i[1]), i[2], (0,255,0), thickness=2)
#     cv2.circle(mask, (i[0], i[1]), i[2], (0,255,0), thickness=-1)

# # Copy that image using that mask
# masked_data = cv2.bitwise_and(img1, img1, mask=mask)

# # Apply Threshold
# _, thresh = cv2.threshold(mask, 1, 255, cv2.THRESH_BINARY)

# # Find Contour
# contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# x, y, w, h = cv2.boundingRect(contours[0])

# print(contours)
# print(x, y, w, h)

# # Crop masked_data
# crop = masked_data[y:y+h, x:x+w]

# cv2.imshow('gray_img', img)
# cv2.imshow('Cropped Eye', crop)
cv2.waitKey(0)
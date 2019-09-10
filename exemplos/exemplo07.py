import cv2

img = cv2.imread('lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
median = cv2.medianBlur(img,7)
cv2.imshow("lena", median)
cv2.waitKey(0)
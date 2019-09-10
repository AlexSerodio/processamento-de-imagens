import cv2

img = cv2.imread('lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
(T, bin) = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
cv2.imshow("lena", bin)
cv2.waitKey(0)
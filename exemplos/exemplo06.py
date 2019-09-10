import cv2

img = cv2.imread('lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.blur(img,(5,5))
cv2.imshow("lena", blur)
cv2.waitKey(0)
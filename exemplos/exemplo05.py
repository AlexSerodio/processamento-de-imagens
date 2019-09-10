import cv2

img = cv2.imread('lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
suave = cv2.GaussianBlur(img, (7, 7), 0)
cv2.imshow("normal", img)
cv2.imshow("blur", suave)
cv2.waitKey(0)
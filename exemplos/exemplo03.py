import cv2

img = cv2.imread('lena.jpg')
(canalAzul, canalVerde, canalVermelho) = cv2.split(img)
cv2.imshow("Vermelho", canalVermelho)
cv2.imshow("Verde", canalVerde)
cv2.imshow("Azul", canalAzul)
cv2.waitKey(0)
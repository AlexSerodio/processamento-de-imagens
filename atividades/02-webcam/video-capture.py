import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    (b, g, r) = cv2.split(frame)
    (thresh, threshold) = cv2.threshold(b, 35, 255, cv2.THRESH_BINARY)

    # Display the resulting frame
    cv2.imshow('frame', threshold)
    key = cv2.waitKey(30) & 0xFF
    if key == 27:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
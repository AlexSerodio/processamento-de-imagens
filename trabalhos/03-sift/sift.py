import numpy as np
import cv2
from matplotlib import pyplot as plt

# Initiate SIFT detector
orb = cv2.ORB_create() 

def match(name_img_base, name_img):
    img1 = cv2.imread(name_img_base, 0)                        # queryImage
    img2 = cv2.imread(name_img, 0)     # trainImage
    
    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    return cv2.drawMatches(img1, kp1, img2, kp2, matches[:30], None, flags=2)

for i in range(1, 12):    
    result = match('entrada/50km.jpg', 'dataset/imagem50km_{:02d}.jpg'.format(i))
    
    print('dataset/imagem50km_{:02d}.jpg'.format(i))
    cv2.imshow('match', result)
    cv2.waitKey(0)

for i in range(1, 12):    
    result = match('entrada/lombada.jpg', 'dataset/imagemLombada_{:02d}.jpg'.format(i))
    
    print('dataset/imagemLombada_{:02d}.jpg'.format(i))
    cv2.imshow('match', result)
    cv2.waitKey(0)

for i in range(1, 12):    
    result = match('entrada/pare.jpg', 'dataset/imagemPare_{:02d}.jpg'.format(i))
    
    print('dataset/imagemPare_{:02d}.jpg'.format(i))
    cv2.imshow('match', result)
    cv2.waitKey(0)
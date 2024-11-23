import cv2
import numpy as np

img = cv2.imread("./test_img.png")

(height, width, channle) = img.shape

for i in range(height):
    for j in range(width):
        G = np.abs(img[i][j] - [218, 56, 50])
        B = np.abs(img[i][j] - [111, 245, 115])
        R = np.abs(img[i][j] - [65, 72, 196])
        if np.sum(R) < 100:
            img[i][j] = [255, 0, 255]
        elif np.sum(G) < 100:
            img[i][j] = [0, 255, 255]
        elif np.sum(B) < 100:
            img[i][j] = [255, 255, 0]
        
cv2.imshow('img', img)
cv2.waitKey()
            

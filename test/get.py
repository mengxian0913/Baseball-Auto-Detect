import cv2
import numpy as np

global img

def onMouse(event, x, y, flag, param):
    x,y = y, x
    if img.ndim != 3:
        print("(x, y) = %d, %d" %(x, y), end=" ")
    else:
        print("(x, y) = %d %d" %(x, y), end=" ")
        print("R, G, B = (%3d, %3d, %3d)" %(img[x, y, 2], img[x, y, 1], img[x, y, 0]))

img = cv2.imread("./test_img.png", -1)
cv2.namedWindow("onMouse")
cv2.setMouseCallback("onMouse", onMouse)
cv2.imshow("img", img)
cv2.waitKey()


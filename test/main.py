import cv2
import numpy as np

target = [226, 159, 72]

def reset(img):
    (height, width, channel) = img.shape
    for i in range(height):
        for j in range(width):
            B = np.abs(img[i][j] - target)
            if np.sum(B) < 350:
                img[i][j] = [255, 255, 255]
    return img

def getROI(img):
    start_x = start_y = end_x = end_y = 0
    (height, width, channel) = img.shape
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            W = np.abs(img[i][j] - [255, 255, 255])
            if np.array_equal(img[i-1][j], img[i][j - 1]) and not np.array_equal(img[i - 1][j], img[i][j]) :
                print(img[i][j])
                print(np.sum(W))
                start_x, start_y = j, i
                print("JEIOF")
            if np.array_equal(img[i + 1][j], img[i][j + 1]) and not np.array_equal(img[i + 1][j], img[i][j]):
                if start_x == 0 and start_y == 0:
                    continue

                end_x, end_y = j, i
                break

    return start_x, start_y, end_x, end_y

def main():
    img = cv2.imread("./test_img2.png")
    img = reset(img)
    start_x, start_y, end_x, end_y = getROI(img)
    print(start_x, start_y, end_x, end_y)
    for i in range(start_y, end_y):
        for j in range(start_x, end_x):
            img[i][j] = target

    cv2.imshow('img', img)
    cv2.waitKey()


if __name__ == "__main__":
    main()

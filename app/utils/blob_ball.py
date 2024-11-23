import cv2
import numpy as np


def blob_3b(frame, mog, roi, filters):
    start_x, start_y, end_x, end_y = roi
    roi_frame = frame[start_y:end_y, start_x:end_x]
    roi_frame = cv2.GaussianBlur(roi_frame, (19, 19), 15)
    minarea, maxarea = filters

    fg_mask = mog.apply(roi_frame) # 區分前景背景
    _, th = cv2.threshold(fg_mask, 200, 255, cv2.THRESH_BINARY) # 移除灰色等，將圖片二值化

    close_es = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    open_es = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

    closing = cv2.morphologyEx(th, cv2.MORPH_CLOSE, close_es, iterations=1)
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, open_es, iterations=1)

    # opening = cv2.medianBlur(opening, 5)  # 可以對圖像進行模糊處理以減少噪音
    cv2.imshow('opening', opening)
    # cv2.imwrite('opening.png', opening)

    # 找到圖像中的輪廓
    contours, _ = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    ball_x = -1
    ball_y = -1
    radius = -1

    # 遍歷輪廓來找到可能的球
    for contour in contours:
        # 獲取輪廓的邊界框和半徑
        (x, y), radius = cv2.minEnclosingCircle(contour)
        
        # 根據半徑篩選出球（可以根據實際情況調整半徑大小）
        if minarea < radius < maxarea:  # 假設球的半徑範圍
            # 畫出圓圈
            center = (int(x), int(y))
            ball_x = start_x + x
            ball_y = start_y + y
            radius = int(radius)
            break

    return int(ball_x), int(ball_y), radius
import cv2
from config import window_width, window_height, window_x, window_y, cap, start_x, start_y, end_x, end_y, pre_x
from utils.parameters import BlobParameters1b as Params1b
from utils.blob_ball import blob_3b
from utils.writeCSV import writeCSV

mog = cv2.createBackgroundSubtractorMOG2()
fps = cap.get(cv2.CAP_PROP_FPS) # get video FPS
frame_number = 0
roi = (start_x, start_y, end_x, end_y)
filters = (5, 1000)
position_list = []

cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Video', window_width, window_height)
# cv2.moveWindow('Video', window_x, window_y)

mouse_x, mouse_y = -1, -1

def mouse_callback(event, x, y, flags, param):
    global mouse_x, mouse_y
    if event == cv2.EVENT_MOUSEMOVE:
        mouse_x, mouse_y = x, y

cv2.setMouseCallback('Video', mouse_callback)

if not cap.isOpened():
    print("無法打開影片")
    exit()

while True:
    ret, frame = cap.read()
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print('width: ', width)
    print('height: ', height)
    break
    
    if not ret:
        print("影片结束")
        break
    

    ball_x, ball_y, radius = blob_3b(frame, mog, roi, filters)

    if ball_x != -1 and ball_y != -1:
        print('ball_x: ', ball_x, '\tball_y: ', ball_y, '\tball_radius: ', radius)


    if ball_x != -1 and ball_y != -1 and ball_x < end_x and 0 < pre_x - ball_x < 350:
        # print('ball_x: ', ball_x, '\tball_y: ', ball_y, '\tball_radius: ', radius)
        cv2.circle(frame, (ball_x, ball_y), 10, (0, 0, 255), -1)
        pre_x = ball_x
        position_list.append({
            'time': round(frame_number / fps, 2), 
            'x': ball_x,
            'y': ball_y
        })
    start_x, start_y, end_x, end_y = roi
    cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), (0, 0, 255), 2)
    cv2.imshow('Video', frame)
    frame_number += 1
    
    if cv2.waitKey(25) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

writeCSV(position_list) # write the data in the csv file

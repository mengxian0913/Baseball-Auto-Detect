import cv2, os
from dotenv import load_dotenv
import tkinter as tk
load_dotenv()

camera = 5
video = 31

start_x = 300
start_y = 650
end_x = 1900
end_y = 1100
pre_x = end_x

if camera == 6:
  start_x = 500
  start_y = 600
  end_x = 2050
  end_y = 1100
  pre_x = start_x


window_width = int(os.getenv('WINDOW_WIDTH', 640))
window_height = int(os.getenv('WINDOW_HEIGHT', 480))

path = f"../../movement2/Cam_{camera}/cam_{camera}_{video}.mp4"
cap = cv2.VideoCapture(path)

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.withdraw() # 隱藏視窗

window_x = (screen_width - window_width) // 2
window_y = (screen_height - window_height) // 2

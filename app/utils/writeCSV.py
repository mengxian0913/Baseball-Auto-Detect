import csv
from config import camera, video

file_name = f'cam_{camera}_{video}'

def writeCSV(position_list):
  # 打開一個新的 CSV 檔案進行寫入
  with open(f'../ballCSV{camera}/{file_name}.csv', mode='w', newline='') as file:
      writer = csv.writer(file)
      
      # 寫入 CSV 檔的標題
      writer.writerow(['time(s)', 'x', 'y'])
      
      # 寫入每一行的數據
      for i in position_list:
          writer.writerow([i['time'], i['x'], i['y']])

  print("CSV 檔案已成功寫入 positions.csv")
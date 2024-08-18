

import cv2
import os

def save_video_frames(folder_path):
    for file in os.listdir(folder_path):
        if file.endswith(".mp4"):
            video_path = os.path.join(folder_path, file)
            cap = cv2.VideoCapture(video_path)
            frame_count = 0
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                image_file_name = f"{file.strip('.mp4')}_{frame_count}.jpg"
                image_path = os.path.join(folder_path, image_file_name)
                cv2.imwrite(image_path, frame)
                frame_count += 1
            cap.release()

folder_path = "C:\\Users\\97409\\Desktop\\MP4"  # 替换为实际的文件夹路径
save_video_frames(folder_path)
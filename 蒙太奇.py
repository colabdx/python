import cv2
import numpy as np

# 视频文件路径列表
video_paths = [
    'video1.mp4',  # 第一个视频文件路径
    'video2.mp4',  # 第二个视频文件路径
    'video3.mp4'   # 第三个视频文件路径
]

# 获取视频的基本参数
frame_width = 640
frame_height = 480
fps = 24

# 创建视频写入对象
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_video = cv2.VideoWriter('montage.mp4', fourcc, fps, (frame_width, frame_height))

# 读取视频并创建蒙太奇效果
for video_path in video_paths:
    cap = cv2.VideoCapture(video_path)
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # 调整视频大小以适应蒙太奇布局
        frame = cv2.resize(frame, (frame_width // 3, frame_height // 3))
        
        # 创建一个空白画布
        canvas = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)
        
        # 将视频片段放置到画布的相应位置
        x = (video_paths.index(video_path) % 3) * (frame_width // 3)
        y = (video_paths.index(video_path) // 3) * (frame_height // 3)
        canvas[y:y+frame_height//3, x:x+frame_width//3] = frame
        
        # 写入蒙太奇视频
        output_video.write(canvas)
    
    cap.release()

# 释放资源
output_video.release()

print("蒙太奇视频制作完成，文件名为 'montage.mp4'")

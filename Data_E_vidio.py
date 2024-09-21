import cv2
def get_video_info(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("无法打开视频文件")
        return
    # 获取视频总帧数
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    # 获取视频帧率
    fps = cap.get(cv2.CAP_PROP_FPS)
    # 获取视频时长（秒）
    duration = total_frames / fps
    print(f"视频总帧数: {total_frames}")
    print(f"视频帧率: {fps}")
    print(f"视频时长（秒）: {duration}")
    cap.release()
video_path=(r'C:\\Users\\YSY15\\Desktop\\vedio_data\\32.31.250.103\\20240501_20240501125647_20240501140806_125649.mp4') 
get_video_info(video_path) 


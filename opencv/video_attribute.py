import cv2

vp = '/home/vs/Videos/test_video/漏气识别_OriVideo_正常-轻微_苏州辰宏布业_5564119301988_00_01_20220217_134500.avi'
vp2 = '/home/vs/Videos/test_video_output/漏气识别_OriVideo_正常-轻微_苏州辰宏布业_5564119301988_00_01_20220217_134500_output.avi'
video = cv2.VideoCapture(vp2)

fps = video.get(cv2.CAP_PROP_FPS)
frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f"帧率：{fps}\n帧数：{frame_count}\n每一帧的宽度：{frame_width}\n每一帧的高度{frame_height}\n")




# 帧率：19.0
# 帧数：17056.0
# 每一帧的宽度：1280
# 每一帧的高度960

# 帧率：19.0
# 帧数：0.0
# 每一帧的宽度：1280
# 每一帧的高度960
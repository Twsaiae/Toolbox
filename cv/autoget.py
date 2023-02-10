import os
import random
import numpy as np

for root, dirs, files in os.walk(r"/home/vs/data_new/CLT/20220305_英通/20220305_英通车冲数据"):  # 这里就填文件夹目录就可以了
    for file in files:
        # 获取文件路径
        if '.mp4' in file:
            src1 = os.path.join(root, file)
            cap = cv2.VideoCapture(src1)
            dst = os.path.join(root, file[:-4])
            os.makedirs(dst, exist_ok=True)
            # d = '吴中区住建局_2015G14一期_出入口枪机_20201204173200-20201204173500_1'
            # cap = cv2.VideoCapture('/data/AI_car_needtohandle/AI视频源数据资料/1.环境视频数据/1.2 密闭运输/2020-12-07/吴中区住建局_2015G14一期/%s.mp4' % d)
            # os.makedirs('/data/AI_car_needtohandle_out/AI视频源数据资料/1.环境视频数据/1.2 密闭运输/2020-12-07/吴中区住建局_2015G14一期/%s' % d)

            frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
            n_frame = int(frames)
            print('总帧数：', frames, n_frame)  # 整个视频的总帧数
            # fps = cap.get(cv2.CAP_PROP_FPS)  # 帧率 每秒展示多少张图片
            i = 1
            frameRate = 50  # 帧数截取间隔（每隔100帧截取一帧）
            while True:
                r, f = cap.read()
                if r:
                    # x, y = f.shape[0:2]
                    # f1 = cv2.resize(f, (int(2*y / 3), int(2*x / 3)))
                    # k = random.randint(0, 28)
                    # ymin = 40 - k
                    # ymax = 600 + k
                    # xmin = 40 - k
                    # xmax = 600 + k
                    # f3 = f1[40:600, 40:600, :]  # 第一次是 560*560    110 810  200 900
                    # f = f1[ymin:ymax, xmin:xmax, :]  # 第一次是 560*560
                    if i % frameRate == 0:
                        print("开始截取视频第：" + str(i) + " 帧")
                        save_path = os.path.join(dst, str(i) + '.jpg')
                        # 这里就可以做一些操作了：显示截取的帧图片、保存截取帧到本地
                        cv2.imwrite(save_path, f)  # 这里是将截取的图像保存在本地
                    i = i + 1
                    cv2.waitKey(0)
                else:
                    print("所有帧都已经保存完成")
                    break
            cap.release()

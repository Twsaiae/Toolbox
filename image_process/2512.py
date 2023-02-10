"""
超分时候将原图变成512*512的多个小图
"""
import os.path
from pathlib import Path
from tqdm import tqdm
import math
import sys
import cv2
import numpy as np

src = Path('C:/Users/Administrator/Desktop/TEST_OUTPUT/src')
src = Path('E:/pycharmproject/MDexiNed/data1')
dst = Path('E:/pycharmproject/MDexiNed/data')
dst.mkdir(parents=True, exist_ok=True)
image_list = tqdm(src.iterdir())
for image_path in image_list:
    name = image_path.stem
    print(name, image_path)
    src_img = cv2.imread(str(image_path))
    h, w, c = src_img.shape

    blank = np.zeros((h + 512, w + 512, 3), np.uint8)
    blank[0:h, 0:w] = src_img

    up_left_x = 0
    up_left_y = 0
    i = 0
    x_num = math.ceil(w / 512)
    y_num = math.ceil(h / 512)
    x_end = 0
    y_end = 1
    while True:
        i += 1
        x_end += 1
        # 开始截图，然后保存
        img = blank[up_left_y:up_left_y + 512, up_left_x:up_left_x + 512]

        cv2.imwrite(f'{dst}/{name}_{i}.png', img)
        # 初始点往右走512
        up_left_x += 512
        # # 判断是否可以再走下一步，如果超出就x归零，y+512
        # if up_left_x + 512 > w:
        #     up_left_x = 0
        #     up_left_y += 512
        #     # 走到最后边后还需要判断是否走到了最下面，如果y+512大于h，那我们就退出
        #     if up_left_y + 512 > h:
        #         break

        if x_end == x_num:
            x_end = 0
            y_end += 1
            up_left_x = 0
            up_left_y += 512
            if y_end > y_num:
                break
# print(math.ceil(512/512))

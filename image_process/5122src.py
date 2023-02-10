"""
超分时候将多个小图拼接回原图大小
"""
# from pathlib import Path
import os
import numpy as np
import cv2
from tqdm import tqdm
import sys
import math

src = 'E:/pycharmproject/MDexiNed/data1'
src2 = 'E:/pycharmproject/MDexiNed/result/BIPED2CLASSIC/fused'
dst = 'E:/pycharmproject/MDexiNed/dst'
os.makedirs(dst, exist_ok=True)

image_list = tqdm(os.listdir(src))
s_image_list = os.listdir(src2)

for image in image_list:
    name = os.path.splitext(image)[0] + '_'
    image_path = os.path.join(src, image)

    src_img = cv2.imread(image_path)

    # blank = np.zeros_like(src_img, dtype=np.uint8)
    h, w, c = src_img.shape
    blank = np.zeros((h + 512, w + 512, 3), np.uint8)

    # 这张图片x轴放多少张图片
    x_num = math.ceil(w / 512)

    mo = []
    # 算出有多少个图片
    for one in s_image_list:
        if name in str(one):
            mo.append(one)
    num = len(mo)

    # 读取多有这些图片开始往里面放,起始点0,0
    x = 0
    y = 0
    x_end = 0
    for i in range(num):
        x_end += 1
        i += 1
        img_path = os.path.join(src2, f"{name}{i}.png")
        img = cv2.imread(img_path)
        # print(i, blank.shape)
        if img is None:
            print('Error: Could not load image')
            sys.exit()
        # print(y, x, blank[y:y + 512, x:x + 512].shape, img.shape)
        blank[y:y + 512, x:x + 512] = img
        x += 512
        if x_end == x_num:
            x_end = 0
            x = 0
            y += 512

    save_path = os.path.join(dst, name + 'fused_output.png')
    cv2.imwrite(save_path, blank)

"""
M、 N分别为图像的宽和高，以像素为单位。在 a - b色度平面上,等效圆的中心坐标为 ( da , db ) ,半径为 M 。等效圆的中心到 a - b色度平面中性轴原点为 ( a = 0, b = 0)的距离 D 。
由等效圆在 a - b色度平面上的具体位置,来判断图像整体的偏色。da > 0,偏红,否则偏绿。db > 0,偏黄,否则偏蓝。引入偏色因子 K, K值越大 ,偏色越严重。
"""
import os
import cv2
import numpy as np
import math


def color_deviation(image_path):
    image = cv2.imread(image_path)
    img_lab = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
    l, a, b = cv2.split(img_lab)
    h, w, _ = image.shape
    # print(a.shape)
    # print(h, w)
    sum_a = np.sum(a)
    sum_b = np.sum(b)
    # print(sum_a,sum_b)
    mn = w * h
    # print(mn)
    da = sum_a / mn - 128
    db = sum_b / mn - 128
    # print(da, db)
    # 求平均色度
    D = math.sqrt(da * da + db * db)
    # print(D)
    # 求色度中心距
    a = a.astype(np.int16)
    a2 = a - 128 - da
    a3 = np.maximum(a2, -a2)
    # a3 = a2**2
    b = b.astype(np.int16)
    b2 = b - 128 - db
    b3 = np.maximum(b2, -b2)
    # b3 = b2**2
    # print(a2,a3,b2,b3)
    ma = np.sum(a3)
    mb = np.sum(b3)
    # print(ma,mb)
    ma = ma / mn
    mb = mb / mn
    M = math.sqrt(ma * ma + mb * mb)
    # 阈值设置为1就行
    K = D / M

    return K


# k = color_deviation('/home/vs/Pictures/10.jpg')
# print(k)

src = '/home/vs/Pictures/所有场景'
for item in os.listdir(src):
    if item[-4:] == '.jpg':
        path = os.path.join(src, item)
        k = color_deviation(path)
        print(f'{item}的色差值为{k}')

# src = '/home/vs/Pictures/图片偏红光'
# i = 1
# for item in os.listdir(src):
#     path = os.path.join(src, item)
#     path2 = os.path.join(src, f'{i}.jpg')
#     os.rename(path, path2)
#     i = i+1

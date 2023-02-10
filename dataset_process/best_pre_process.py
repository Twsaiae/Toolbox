"""
能够将原图增强
"""
import os

import cv2
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm


def custom_blur_demo(image):
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)  # 锐化
    dst = cv2.filter2D(image, -1, kernel=kernel)
    cv2.imshow("custom_blur_demo", dst)


def gama_transfer(img, power1):
    # if len(img.shape) == 3:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = 255 * np.power(img / 255, power1)
    img = np.around(img)
    img[img > 255] = 255
    out_img = img.astype(np.uint8)
    return out_img


if __name__ == '__main__':
    # src = 'E:/tendency_project_data/heizi/1'
    src = r'C:\Users\Thor\Desktop\test'
    # src = 'E:/tendency_project_data/heizi/Test/1/NG'
    # dst = 'E:/tendency_project_data/heizi/Test/1/NG_Enhanced'
    # dst = 'E:/tendency_project_data/heizi/2'
    dst = r'C:\Users\Thor\Desktop\test_output'
    os.makedirs(dst, exist_ok=True)
    img_list = tqdm(os.listdir(src))
    for i in img_list:
        path = os.path.join(src, i)
        dst_path = os.path.join(dst, i)
        image = cv2.imread(path, 0)
        gam = gama_transfer(image, 1.5)
        gam = cv2.cvtColor(gam, cv2.COLOR_RGB2GRAY)
        equ = cv2.equalizeHist(gam)
        # equ = cv2.equalizeHist(image)
        # cv2.imshow('1',gam)
        # cv2.waitKey(0)
        cv2.imwrite(dst_path, gam)


















    # path_1 = 'E:/tendency_project_data/heizi/2/python.bmp'
    # path_2 = 'E:/tendency_project_data/heizi/2/c++.bmp'
    # img_1 = cv2.imread(path_1)
    # img_2 = cv2.imread(path_2)
    # print(img_1,img_2)
    # a = [1,4]
    # b = [2,4]
    # a = np.array(a)
    # b = np.array(b)


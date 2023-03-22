'''
    这是图片数据增强的代码，可以对图片实现：
    1. 尺寸随机缩放
    2. 旋转（任意角度，如45°，90°，180°，270°）
    3. 翻转（水平翻转，垂直翻转）
    4. 明亮度改变（变亮，变暗）
    5. 像素平移（往一个方向平移像素，空出部分自动填补黑色）
    6. 添加噪声（椒盐噪声，高斯噪声）

'''
import os
import time

import cv2
import numpy as np
import random
import re
from tqdm import tqdm

'''
缩放
'''


# 放大缩小
def Scale(image, scale1, scale2):
    return cv2.resize(image, None, fx=scale1, fy=scale2, interpolation=cv2.INTER_LINEAR)


'''
翻转
'''


# 水平翻转
def Horizontal(image):
    return cv2.flip(image, 1, dst=None)  # 水平镜像


# 垂直翻转
def Vertical(image):
    return cv2.flip(image, 0, dst=None)  # 垂直镜像


# 旋转，R可控制图片放大缩小
def Rotate(image, angle=15, scale=0.9):
    w = image.shape[1]
    h = image.shape[0]
    # rotate matrix
    M = cv2.getRotationMatrix2D((w / 2, h / 2), angle, scale)
    # rotate
    image = cv2.warpAffine(image, M, (w, h))
    return image


'''  
明亮度 
'''


# 变暗
def Darker(image, percetage=0.7):
    image_copy = image.copy()
    w = image.shape[1]
    h = image.shape[0]
    # get darker
    for xi in range(0, w):
        for xj in range(0, h):
            image_copy[xj, xi, 0] = int(image[xj, xi, 0] * percetage)
            image_copy[xj, xi, 1] = int(image[xj, xi, 1] * percetage)
            image_copy[xj, xi, 2] = int(image[xj, xi, 2] * percetage)
    return image_copy


# 明亮
def Brighter(image, percetage=1.3):
    image_copy = image.copy()
    w = image.shape[1]
    h = image.shape[0]
    # get brighter
    for xi in range(0, w):
        for xj in range(0, h):
            image_copy[xj, xi, 0] = np.clip(int(image[xj, xi, 0] * percetage), a_max=255, a_min=0)
            image_copy[xj, xi, 1] = np.clip(int(image[xj, xi, 1] * percetage), a_max=255, a_min=0)
            image_copy[xj, xi, 2] = np.clip(int(image[xj, xi, 2] * percetage), a_max=255, a_min=0)
    return image_copy


def adjust_brightness(image, value=50):
    """
    调整图像的明亮度
    :param image: 图像
    :param value: 明亮度增加的值，可以为正数或负数
    :return: 调整后的图像
    """
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = np.where((255 - v) < value, 255, v + value)
    v = np.where(v < 0, 0, v)
    v = v.astype(dtype='uint8')
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img


def adjust_darkness(image, value=-30):
    """
    调整图像的明亮度
    :param image: 图像
    :param value: 明亮度增加的值，可以为正数或负数
    :return: 调整后的图像
    """
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = np.where((255 - v) < value, 255, v + value)
    v = np.where(v < 0, 0, v)
    v = v.astype(dtype='uint8')
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img


# 平移
def Move(img, x, y):
    img_info = img.shape
    height = img_info[0]
    width = img_info[1]

    mat_translation = np.float32([[1, 0, x], [0, 1, y]])  # 变换矩阵：设置平移变换所需的计算矩阵：2行3列
    # [[1,0,20],[0,1,50]]   表示平移变换：其中x表示水平方向上的平移距离，y表示竖直方向上的平移距离。
    dst = cv2.warpAffine(img, mat_translation, (width, height))  # 变换函数
    return dst


'''
增加噪声
'''


# 椒盐噪声
def SaltAndPepper(src, percetage=0.05):
    SP_NoiseImg = src.copy()
    SP_NoiseNum = int(percetage * src.shape[0] * src.shape[1])
    for i in range(SP_NoiseNum):
        randR = np.random.randint(0, src.shape[0] - 1)
        randG = np.random.randint(0, src.shape[1] - 1)
        randB = np.random.randint(0, 3)
        if np.random.randint(0, 1) == 0:
            SP_NoiseImg[randR, randG, randB] = 0
        else:
            SP_NoiseImg[randR, randG, randB] = 255
    return SP_NoiseImg


# # 高斯噪声
# def GaussianNoise(image,percetage=0.05):
#     G_Noiseimg = image.copy()
#     w = image.shape[1]
#     h = image.shape[0]
#     G_NoiseNum=int(percetage*image.shape[0]*image.shape[1])
#     for i in range(G_NoiseNum):
#         temp_x = np.random.randint(0,h)
#         temp_y = np.random.randint(0,w)
#         G_Noiseimg[temp_x][temp_y][np.random.randint(3)] = np.random.randn(1)[0]
#     return G_Noiseimg

def Blur(img):
    blur = cv2.GaussianBlur(img, (7, 7), 1.5)
    # #      cv2.GaussianBlur(图像，卷积核，标准差）
    return blur


def TestOnePic():
    test_jpg_loc = r"data/rose/3.jpg"
    test_jpg = cv2.imread(test_jpg_loc)
    cv2.imshow("Show Img", test_jpg)
    # img1 = Blur(test_jpg)
    # cv2.imshow("Img 1", img1)

    # a = random.uniform(0.5, 1.5)
    # b = random.uniform(0.5, 1.5)
    img_scale = Scale(test_jpg, 1.5, 1.5)
    # cv2.imwrite(os.path.join(a, "scaledl" + file_i), img_scale)
    # cv2.imwrite('try.jpg', img1)
    # cv2.waitKey(0)
    # img2 = GaussianNoise(test_jpg,0.01)
    cv2.imshow("Img 2", img_scale)
    cv2.waitKey(0)


def random_resize(root_path, imagefile_name):
    # resize to 0.5-1.5 times
    src = os.path.join(root_path, imagefile_name)
    src2 = os.path.join(root_path, 'annotations')

    for item in tqdm(os.listdir(src)):
        if '.png' not in item and '.jpg' not in item:
            continue
        path_1 = os.path.join(src, item)

        img_1 = cv2.imread(path_1)

        d = random.uniform(0.5, 1.5)
        e = random.uniform(0.5, 1.5)
        img_scale_1 = Scale(img_1, d, e)

        cv2.imwrite(os.path.join(src, "scaled" + item), img_scale_1)

        for item2 in os.listdir(src2):
            match = re.match(item.split('.')[0], item2)
            if match:
                path_2 = os.path.join(src2, item2)
                img_2 = cv2.imread(path_2)
                img_scale_2 = Scale(img_2, d, e)
                cv2.imwrite(os.path.join(src2, "scaled" + item2), img_scale_2)
    print('random resize done')


def makedirs(path):
    if not os.path.exists(path):
        os.makedirs(path)


def random_move(root_path, imagefile_name):
    # resize to 0.5-1.5 times
    src = os.path.join(root_path, imagefile_name)
    src2 = os.path.join(root_path, 'annotations')
    # src3 = os.path.join(root_path, 'random_move')
    # makedirs(src3)
    # src4 = os.path.join(root_path, 'random_move_annotations')
    # makedirs(src4)

    for item in tqdm(os.listdir(src)):
        if '.png' not in item and '.jpg' not in item:
            continue
        path_1 = os.path.join(src, item)

        img_1 = cv2.imread(path_1)

        d = random.randint(30, 300)
        e = random.randint(30, 300)
        # img_scale_1 = Scale(img_1, d, e)
        img_move_1 = Move(img_1, d, e)

        cv2.imwrite(os.path.join(src, "move" + item), img_move_1)

        for item2 in os.listdir(src2):
            match = re.match(item.split('.')[0], item2)
            if match:
                path_2 = os.path.join(src2, item2)
                img_2 = cv2.imread(path_2)
                # img_scale_2 = Scale(img_2, d, e)
                # cv2.imwrite(os.path.join(src2, "scl" + item2), img_scale_2)
                img_move_2 = Move(img_2, d, e)

                cv2.imwrite(os.path.join(src2, "move" + item2), img_move_2)
    print('random move done')

    # # move
    # img_move = Move(img_i,15,15)
    # cv2.imwrite(os.path.join(a, "move" + file_i), img_move)

    # # resize to 1.5 times
    # img_scale = Scale(img_i, 1.5)
    # cv2.imwrite(os.path.join(a, "scaledb" + file_i), img_scale)

    # # horizontal
    # img_horizontal = Horizontal(img_i)
    # cv2.imwrite(os.path.join(a, "horizontal" + file_i), img_horizontal)

    # # vertical
    # img_vertical = Vertical(img_i)
    # cv2.imwrite(os.path.join(a, "vertical" + file_i), img_vertical)

    # # rotate90
    # img_rotate = Rotate(img_i,90)
    # cv2.imwrite(os.path.join(a, "rotate90" + file_i), img_rotate)

    # rotate180
    # img_rotate = Rotate(img_i, 180)
    # cv2.imwrite(os.path.join(a, "rotate180" + file_i), img_rotate)

    # # darker 像素级别，比较耗时，首先进行
    # img_darker = Darker(img_i)
    # cv2.imwrite(os.path.join(a, "darker" + file_i), img_darker)

    # # brighter 最慢的大兄弟，没有之一，就离谱
    # img_brighter = Brighter(img_i)
    # cv2.imwrite(os.path.join(a, "brighter" + file_i), img_brighter)

    # # salt 椒盐模糊
    # img_salt = SaltAndPepper(img_i, 0.05)
    # cv2.imwrite(os.path.join(a, "salt" + file_i), img_salt)

    # # blur 速度还好
    # img_blur = Blur(img_i)
    # cv2.imwrite(os.path.join(a, "blur" + file_i), img_blur)


if __name__ == "__main__":

    # src = r'C:\Users\Thor\Desktop\noone\image1\all_image'
    # aug_name_list = ["horizontal", "vertical", "blur", "brighter", "darker"]
    # aug_list = [Horizontal, Vertical, Blur, Brighter, Darker]
    #
    # for idx, aug_name in enumerate(aug_list):
    #     print(f"{aug_name_list[idx]}开始进行...")
    #     dst = src + f"_{aug_name_list[idx]}"
    #     os.makedirs(dst, exist_ok=True)
    #     for img_name in tqdm(os.listdir(src)):
    #         img_path = os.path.join(src, img_name)
    #         dst_path = f"{dst}/{os.path.splitext(img_name)[0]}_{aug_name_list[idx]}{os.path.splitext(img_name)[-1]}"
    #
    #         src_image = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), 1)
    #         dst_image = aug_name(src_image)
    #         cv2.imencode(os.path.splitext(img_name)[-1], dst_image)[1].tofile(dst_path)
    #     print(f"{aug_name_list[idx]}已结束")
    #     time.sleep(3)
    img = cv2.imdecode(np.fromfile(r'C:\Users\Thor\Downloads\大面\四合一\中气泡\0.492772_TB_0IQCB17940000HCAK9003508_2022_1.bmp', dtype=np.uint8), 1)
    img2 = adjust_brightness(img)
    cv2.imshow('img', img)
    cv2.imshow('img2', img2)
    cv2.waitKey(0)

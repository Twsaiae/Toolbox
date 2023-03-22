"""
将分类数据集中的数据自动数据增强到每个类别数据均衡
输入：数据集的地址+想采用的数据增强手段
输出：随机增强后的均衡数据集
"""
import os
import shutil
import time

import numpy as np
import cv2
from random import choice
from tqdm import tqdm
from data_aug import Horizontal, Vertical


def h_v(img):
    output = Horizontal(img)
    output = Vertical(output)
    return output


def one_dataset_balanced(data_path, method_list):
    dst_path = f"{data_path}_output"
    data_volume_list = []
    for img_list_name in os.listdir(data_path):
        img_list_path = os.path.join(data_path, img_list_name)
        # data_volume_list[img_list_name] = len(os.listdir(img_list_path))
        data_volume_list.append(len(os.listdir(img_list_path)))
    max_num = max(data_volume_list)
    method_num = len(method_list)
    # can_more = pow(2, method_num)
    # 一次性进几个
    can_more = method_num + 1  ###########################################################################################

    # # 计算完数据量和可以用的数据增强后，首先判断这件事能不能做，不能做就报错
    # for i in data_volume_list:
    #     assert i * can_more >= max_num
    # 具体怎么做呢？要看情况
    for idx, img_list_name in enumerate(os.listdir(data_path)):
        img_list_path = os.path.join(data_path, img_list_name)
        dst_img_list_path = os.path.join(dst_path, img_list_name)
        os.makedirs(dst_img_list_path, exist_ok=True)
        # print(idx, img_list_name, data_volume_list[idx])
        if data_volume_list[idx] * 2 >= max_num:
            # 随机选择，增强到相同个数即可
            count = 0
            copy_num = max_num - data_volume_list[idx]
            for img_name in tqdm(os.listdir(img_list_path)):
                count += 1
                img_path = os.path.join(img_list_path, img_name)
                dst_img_path = os.path.join(dst_img_list_path, img_name)
                shutil.copy(img_path, dst_img_path)
                if count <= copy_num:
                    dst_generating_img_path = f"{dst_img_list_path}/{os.path.splitext(img_name)[0]}_generating{os.path.splitext(img_name)[-1]}"
                    # src_image = cv2.imread(img_path)
                    src_image = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), 1)
                    dst_image = choice(method_list)(src_image)
                    # cv2.imwrite(dst_generating_img_path, dst_image)
                    cv2.imencode(os.path.splitext(img_name)[-1], dst_image)[1].tofile(dst_generating_img_path)

        else:
            # 遍历着，一次添加can_more张图片进去，直到个数大于等于max_num
            count = 0
            copy_num = max_num - data_volume_list[idx]
            for img_name in tqdm(os.listdir(img_list_path)):
                count += method_num
                img_path = os.path.join(img_list_path, img_name)
                dst_img_path = os.path.join(dst_img_list_path, img_name)
                shutil.copy(img_path, dst_img_path)
                if count <= copy_num:
                    # src_image = cv2.imread(img_path)
                    src_image = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), 1)

                    for index, method in enumerate(method_list):
                        dst_generating_img_path = f"{dst_img_list_path}/{os.path.splitext(img_name)[0]}_generating_{index}{os.path.splitext(img_name)[-1]}"
                        dst_image = method(src_image)
                        # cv2.imwrite(dst_generating_img_path, dst_image)
                        cv2.imencode(os.path.splitext(img_name)[-1], dst_image)[1].tofile(dst_generating_img_path)
    print(
        f"{data_path}数据集结束##########################################################################################")
    time.sleep(3)


if __name__ == '__main__':
    # path = r'E:\项目整理\0_2023_213\class图片\大面_4\0_cando'
    # for i in os.listdir(path):
    #     i_path = os.path.join(path, i)
    #     for j in os.listdir(i_path):
    #         data_path = os.path.join(i_path, j)
    #         # print(j_path)
    #         # data_path = r'E:\项目整理\0_2023_213\class图片\大面_4\0_cando\try\train'
    #         more_way = [Horizontal, Vertical, h_v]
    #         one_dataset_balanced(data_path, more_way)



    data_path = r'C:\Users\Thor\Desktop\test'
    more_way = [Horizontal, Vertical, h_v]
    one_dataset_balanced(data_path, more_way)
"""
input 单个类图片  扩充比例  扩充方式
"""
import os
from random import choice
import math
import cv2
import numpy as np

from dataset_process.data_aug import Horizontal, Vertical, Blur


def one_cls_aug(image_list, aug_ratio, aug_method_list):
    """
    Args:
        image_list:存放所有读入的图片
        aug_ratio: 这些图片需要增加的比例，需要大于等于1
        aug_method_list: 存放所有可以用的数据增强方法
    Returns:
    """
    # 用来存放最终增加后的图片
    after_aug_image_list = []
    src_image_num = len(image_list)
    aug_image_num = math.ceil(aug_ratio * src_image_num)
    need_aug_image_num = aug_image_num - src_image_num
    method_num = len(aug_method_list)

    # 增加的比例小于1就报错,大于可以增加的极限比例就报错
    # assert 1 <= aug_ratio <= pow(2,
    #                              method_num), f"您输入的增强比例不满足要求，比例需在1-{pow(2, method_num)}之间，您还可以通过添加增强方法来提高比例上限"
    assert 1 <= aug_ratio

    # 1、要求数据需要增加的比例<=2(原图数量*2>=需要达到的数据量)      遍历原图采取随机方法增强，直到达到目标数量
    if aug_ratio <= 2:

        count = 0
        for one_image in image_list:
            count += 1
            if count > need_aug_image_num:
                break
            after_aug_image_list.append(choice(aug_method_list)(one_image))


    # 2、要求数据增加的比例<=数据增加的可用方法+1(原图数量*增强方法的数量>=需要达到的数据量)     int(aug_ratio)+1次遍历原图，遍历使用增强方法增强数据，直到达到目标数量
    elif aug_ratio <= method_num + 1:
        count = 0
        for i in range(math.ceil(aug_ratio) - 1):
            for one_image in image_list:
                count += 1
                if count > need_aug_image_num:
                    break
                after_aug_image_list.append(aug_method_list[i](one_image))

    # 3、要求数据增加的比例<=数据增加可用方法的组合极限（原图数量*（2的n次方，n为增强方法的数量）） 采用自己做这件事的思路来循环，增强后放回，在对放回后的完整数据增强，然后再放回
    # elif aug_ratio <= pow(2, method_num):
    else:
        count = 0
        for i in range(math.ceil(math.log(aug_ratio, 2))):
            one_aug_image_list = []
            for one_image in image_list:
                count += 1
                if count > need_aug_image_num:
                    break
                one_aug_image_list.append(aug_method_list[i](one_image))
            image_list.extend(one_aug_image_list)

    after_aug_image_list.extend(image_list)
    return after_aug_image_list


if __name__ == '__main__':
    _image_list = []
    src = r'C:\Users\Thor\Desktop\3'
    for img in os.listdir(src):
        img_path = os.path.join(src, img)
        src_image = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), 1)
        _image_list.append(src_image)
    _aug_ratio = 2
    _aug_method_list = [Horizontal, Vertical, Blur]

    output = one_cls_aug(_image_list, _aug_ratio, _aug_method_list)

    print(len(_image_list), len(output))

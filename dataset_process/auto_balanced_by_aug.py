"""
我要做一件事，就是把一个分类数据集的数据变得平衡一些，通过数据增强的方法，而可用的数据增强我会放到一个list中，然后如果它的数量比较多，就不用数据增强，或者少用，如果数据比较少，那么就尽可能的通过数据增强变得平衡一些
"""
import os
from data_aug import adjust_darkness, adjust_brightness, Horizontal, Vertical
from one_class_augmentation import one_cls_aug
import cv2
import numpy as np

if __name__ == '__main__':

    # 1. 首先要知道每个类别的数量，要知道最大的类别的数量，最小的类别的数量
    src = r'C:\Users\Thor\Downloads\大面\四合一'
    dst = r'C:\Users\Thor\Downloads\大面\四合一_增强'
    class_path_list = []
    class_name_list = []
    class_num_list = []
    for i in os.listdir(src):
        i_path = os.path.join(src, i)
        class_name_list.append(i)
        class_path_list.append(i_path)
        class_num_list.append(len(os.listdir(i_path)))

    max_num = max(class_num_list)
    min_num = min(class_num_list)

    # 2. 然后要知道每个类别的数据增强的方法
    aug_list = [Horizontal, Vertical, adjust_brightness, adjust_darkness]
    set_max_num = min_num * 2 ** len(aug_list)
    print('最大的类别的数量：', max_num, '最小的类别的数量：', min_num, '采用的数据增强的方法种数：', len(aug_list),
          '设置的最大的数量：', set_max_num)

    # 3. 确定每个类别的增强比例，放到一个list中
    aug_ratio_list = [set_max_num / i for i in class_num_list]
    print('每个类别的增强比例：', aug_ratio_list)

    # 4. 开始增强
    for i in range(len(class_path_list)):
        print('正在增强类别：', class_name_list[i], '增强比例：', aug_ratio_list[i],
              '增强前的数量：', class_num_list[i], '增强后的数量：', set_max_num)
        os.makedirs(os.path.join(dst, class_name_list[i]), exist_ok=True)
        image_list = []
        for img in os.listdir(class_path_list[i]):
            img_path = os.path.join(class_path_list[i], img)
            src_image = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), 1)
            image_list.append(src_image)
        aug_method_list = aug_list
        aug_ratio = aug_ratio_list[i]
        output = one_cls_aug(image_list, aug_ratio, aug_method_list)
        for j in range(len(output)):
            cv2.imencode('.bmp', output[j])[1].tofile(
                os.path.join(dst, class_name_list[i], class_name_list[i] + '_' + str(j) + '.bmp'))

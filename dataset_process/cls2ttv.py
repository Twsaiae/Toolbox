"""
输入数据集地址，然后划分成相同比例/最大相同数量的数据集   ttv:train test val
"""
import os
import json
import shutil
from tqdm import tqdm

mode = 0
data_path = r'E:\分类数据集\number_cam\data2\data2'
dst_path = r'E:\分类数据集\number_cam\data2_for_train'

# cla_dict = dict((val, key) for key, val in enumerate(os.listdir(data_path)))
# print(cla_dict)
# json_str = json.dumps(cla_dict, indent=4, ensure_ascii=False)
# with open('class_indices.json', 'w') as json_file:
#     json_file.write(json_str)

if mode == 0:
    for class_name in os.listdir(data_path):

        class_name_path = os.path.join(data_path, class_name)
        train_class_name_dst_path = f"{dst_path}/train/{class_name}"
        test_class_name_dst_path = f"{dst_path}/test/{class_name}"
        val_class_name_dst_path = f"{dst_path}/val/{class_name}"

        os.makedirs(train_class_name_dst_path, exist_ok=True)
        os.makedirs(test_class_name_dst_path, exist_ok=True)
        os.makedirs(val_class_name_dst_path, exist_ok=True)
        image_list = tqdm(os.listdir(class_name_path))
        train_num = round(len(image_list) * 0.8)
        test_num = val_num = round(len(image_list) * 0.1)

        for idx, image in enumerate(image_list):
            image_path = os.path.join(class_name_path, image)
            if idx <= train_num:
                image_dst_path = os.path.join(train_class_name_dst_path, image)
                shutil.copy(image_path, image_dst_path)
            elif idx <= train_num + test_num:
                image_dst_path = os.path.join(test_class_name_dst_path, image)
                shutil.copy(image_path, image_dst_path)
            else:
                image_dst_path = os.path.join(val_class_name_dst_path, image)
                shutil.copy(image_path, image_dst_path)
elif mode == 1:
    pass

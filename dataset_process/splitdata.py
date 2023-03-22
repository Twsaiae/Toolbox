# spile_data.py
"""
输入：数据集地址+输出数据集地址+test比例+valid比例
输出：将总的比例改成
"""
import os
import shutil
from shutil import copy
import random
from tqdm import tqdm

data_path = r'C:\Users\Thor\Downloads\大面\四合一_placed_well\train_placed_well\train'
test_ratio = 0.2
valid_ratio = 0.2

dst_data_path = f"{data_path}_placed_well"
dst_data_path_train = f"{dst_data_path}/train"
dst_data_path_val = f"{dst_data_path}/val"
dst_data_path_test = f"{dst_data_path}/test"

assert 0 <= test_ratio <= 1 and 0 <= valid_ratio <= 1

for cls_name in os.listdir(data_path):
    src_path = os.path.join(data_path, cls_name)
    image_list = tqdm(os.listdir(src_path))
    image_num = len(image_list)
    test_num = image_num * test_ratio
    valid_num = image_num * valid_ratio
    train_dst_path = os.path.join(dst_data_path_train, cls_name)
    val_dst_path = os.path.join(dst_data_path_val, cls_name)
    test_dst_path = os.path.join(dst_data_path_test, cls_name)
    os.makedirs(train_dst_path, exist_ok=True)
    os.makedirs(val_dst_path, exist_ok=True)
    # if test_ratio != 0:
    os.makedirs(test_dst_path, exist_ok=True)
    count = 0

    first_valid = valid_num
    second_test = valid_num + test_num

    # 0-valid_num-valid_num+test_num-all
    for img in image_list:
        count += 1
        img_path = os.path.join(src_path, img)
        if count <= first_valid:
            dst_img_path = os.path.join(val_dst_path, img)
        elif count <= second_test:
            dst_img_path = os.path.join(test_dst_path, img)
        else:
            dst_img_path = os.path.join(train_dst_path, img)
        shutil.move(img_path, dst_img_path)

#
#
# def mkfile(file):
#     if not os.path.exists(file):
#         os.makedirs(file)
#
#
# file = 'D:/Downloads/flower_photos/flower_photos'
# flower_class = [cla for cla in os.listdir(file) if ".txt" not in cla]
# mkfile('D:/Downloads/flower_photos/train')
# for cla in flower_class:
#     mkfile('D:/Downloads/flower_photos/train/' + cla)
#
# mkfile('D:/Downloads/flower_photos/val')
# for cla in flower_class:
#     mkfile('D:/Downloads/flower_photos/val/' + cla)
#
# mkfile('D:/Downloads/flower_photos/test')
# for cla in flower_class:
#     mkfile('D:/Downloads/flower_photos/test/' + cla)
#
# split_rate = 0.2
# # split_val_rate = 0.1
# # split_test_rate = 0.3
# for cla in flower_class:
#     cla_path = file + '/' + cla + '/'
#     images = os.listdir(cla_path)
#     num = len(images)
#     eval_index = random.sample(images, k=int(num * split_rate))
#     num2 = len(eval_index)
#     test_index = random.sample(eval_index, k=int(num2 * 0.75))
#     # print(eval_index)
#     for index, image in enumerate(images):
#         # 如果images是被随机选中的作为val的，就放到val中
#         if image in eval_index:
#             if image in test_index:
#                 image_path = cla_path + image
#                 new_path = 'D:/Downloads/flower_photos/test/' + cla
#                 copy(image_path, new_path)
#             else:
#                 image_path = cla_path + image
#                 new_path = 'D:/Downloads/flower_photos/val/' + cla
#                 copy(image_path, new_path)
#         else:
#             image_path = cla_path + image
#             new_path = 'D:/Downloads/flower_photos/train/' + cla
#             copy(image_path, new_path)
#         print("\r[{}] processing [{}/{}]".format(cla, index + 1, num), end="")  # processing bar
#     print()
#
# print("processing done!")

# spile_data.py

import os
from shutil import copy
import random


def mkfile(file):
    if not os.path.exists(file):
        os.makedirs(file)


file = 'D:/Downloads/flower_photos/flower_photos'
flower_class = [cla for cla in os.listdir(file) if ".txt" not in cla]
mkfile('D:/Downloads/flower_photos/train')
for cla in flower_class:
    mkfile('D:/Downloads/flower_photos/train/' + cla)

mkfile('D:/Downloads/flower_photos/val')
for cla in flower_class:
    mkfile('D:/Downloads/flower_photos/val/' + cla)

mkfile('D:/Downloads/flower_photos/test')
for cla in flower_class:
    mkfile('D:/Downloads/flower_photos/test/' + cla)

split_rate = 0.4
# split_val_rate = 0.1
# split_test_rate = 0.3
for cla in flower_class:
    cla_path = file + '/' + cla + '/'
    images = os.listdir(cla_path)
    num = len(images)
    eval_index = random.sample(images, k=int(num * split_rate))
    num2 = len(eval_index)
    test_index = random.sample(eval_index, k=int(num2 * 0.75))
    # print(eval_index)
    for index, image in enumerate(images):
        # 如果images是被随机选中的作为val的，就放到val中
        if image in eval_index:
            if image in test_index:
                image_path = cla_path + image
                new_path = 'D:/Downloads/flower_photos/test/' + cla
                copy(image_path, new_path)
            else:
                image_path = cla_path + image
                new_path = 'D:/Downloads/flower_photos/val/' + cla
                copy(image_path, new_path)
        else:
            image_path = cla_path + image
            new_path = 'D:/Downloads/flower_photos/train/' + cla
            copy(image_path, new_path)
        print("\r[{}] processing [{}/{}]".format(cla, index + 1, num), end="")  # processing bar
    print()

print("processing done!")

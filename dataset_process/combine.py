"""
这个代码是把三份数据，分别两份合一起作为训练集，一份作为测试集
"""
import os
import shutil
from tqdm import tqdm
divide_number = 3
src = r'C:\Users\Thor\Downloads\大面\大面_脏污_output'
for i in range(1, divide_number + 1):
    print(f"第{i}个数据集开始整理")
    dst = f"{src}_for_train_{i}"

    for cls_name in os.listdir(src):
        cls_path = os.path.join(src, cls_name)
        train_dst_cls_path = f"{dst}/train/{cls_name}"
        test_dst_cls_path = f"{dst}/test/{cls_name}"
        os.makedirs(train_dst_cls_path, exist_ok=True)
        os.makedirs(test_dst_cls_path, exist_ok=True)
        for j in range(1, divide_number + 1):
            for img_name in tqdm(os.listdir(f"{cls_path}/{j}")):
                img_path = f"{cls_path}/{j}/{img_name}"
                if j == i:
                    dst_img_path = os.path.join(test_dst_cls_path, img_name)
                else:
                    dst_img_path = os.path.join(train_dst_cls_path, img_name)
                shutil.copy(img_path, dst_img_path)

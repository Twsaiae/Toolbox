"""

intput :
output :
"""
import os
import shutil
import random
from tqdm import tqdm

src = r'E:/qingxiang/number_test/old/number'
dst = f"{src}_train"
os.makedirs(dst, exist_ok=True)

want = {
    '0': 500,
    '1': 500,
    '2': 500,
    '3': 500,
    '4': 500,
    '5': 500,
    '6': 500,
    '7': 500,
    '8': 500,
    '9': 100
}

for i in os.listdir(src):
    new_dir = os.path.join(dst, i)
    os.makedirs(new_dir, exist_ok=True)
    dir_path = os.path.join(src, i)
    need_images_number = want[i]
    copy_images_list = tqdm(random.sample(os.listdir(dir_path), need_images_number))
    for name in copy_images_list:
        img_path = os.path.join(dir_path, name)
        img_dst_path = os.path.join(new_dir, name)
        shutil.copy(img_path, img_dst_path)

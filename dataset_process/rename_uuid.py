from uuid import uuid4
import os
import shutil
import time
from tqdm import tqdm

#    /home/vs/data_backup/zhuhai_20210823_output/中科0（used）
src = r'E:\pycharmproject\mm_cls\data\OK'
# dst = src+f'_{time.strftime("%Y%m%d", time.localtime())}'
dst = r'E:\pycharmproject\mm_cls\data\OK_output'

print(dst)
if not os.path.exists(dst):
    os.makedirs(dst)

# i = 0
# for root, dirs, files in os.walk(src):
#     # print(dirs)
#     for name in files:
#         i += 1
#         img = str(uuid4())
#         path = os.path.join(root, name)
#         out_path = os.path.join(dst, img+'.jpg')
#         shutil.copy(path, out_path)
#
# print('{} images rename done'.format(i))
num = 0
for i in os.listdir(src):
    num += 1
    i_path = os.path.join(src, i)
    dst_name = f'OK.{num}.bmp'
    dst_path = os.path.join(dst, dst_name)
    shutil.copy(i_path, dst_path)

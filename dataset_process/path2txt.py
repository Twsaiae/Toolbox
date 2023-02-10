"""
windows下将文件夹中所有数据地址遍历到一个txt中去
"""
import os

path = r'E:\pycharmproject\mm_cls\data\train'
txt_path = r'E:\pycharmproject\mm_cls\data\train.txt'

content = []
with open(txt_path, 'w') as f:
    for root, dirs, files in os.walk(path, topdown=False):
        for file in files:

            if 'NG' in root:
                file_path = os.path.join(root, file + ' 0\n')
            else:
                file_path = os.path.join(root, file + ' 1\n')

            content.append(file_path)
            # print(dirs)

    f.writelines(content)

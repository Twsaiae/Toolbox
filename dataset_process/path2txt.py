"""
windows下将文件夹中所有数据地址遍历到一个txt中去
"""
import os

path = r'C:\Users\Thor\Desktop\image1\dataset\my_dataset\val\images'
txt_path = r'C:\Users\Thor\Desktop\image1\dataset\my_dataset\val.txt'

content = []
with open(txt_path, 'w') as f:
    for root, dirs, files in os.walk(path, topdown=False):
        for file in files:
            file_path = os.path.join(root, file + '\n')
            # if 'NG' in root:
            #     file_path = os.path.join(root, file + ' 0\n')
            # else:
            #     file_path = os.path.join(root, file + ' 1\n')
            content.append(file_path)
            # print(dirs)

    f.writelines(content)

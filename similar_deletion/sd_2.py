# coding: utf-8
import os
import cv2
from skimage.metrics import structural_similarity as ssim


def delete(filename1):
    os.remove(filename1)


def list_all_files(root):
    files = []
    list = os.listdir(root)
    # os.listdir()方法：返回指定文件夹包含的文件或子文件夹名字的列表。该列表顺序以字母排序
    for i in range(len(list)):
        element = os.path.join(root, list[i])
        # 需要先使用python路径拼接os.path.join()函数，将os.listdir()返回的名称拼接成文件或目录的绝对路径再传入os.path.isdir()和os.path.isfile().
        if os.path.isdir(element):  # os.path.isdir()用于判断某一对象(需提供绝对路径)是否为目录
            # temp_dir = os.path.split(element)[-1]
            # os.path.split分割文件名与路径,分割为data_dir和此路径下的文件名，[-1]表示只取data_dir下的文件名
            files.append(list_all_files(element))

        elif os.path.isfile(element):
            files.append(element)
    # print('2',files)
    return files


def ssim_compare(img_files):
    count = 0
    for currIndex, filename in enumerate(img_files):  # 获得图片列表中的索引与文件名
        if not os.path.exists(img_files[currIndex]):  # 如果文件不存在
            print('not exist', img_files[currIndex])
            break
        len_img = len(img_files)
        if (img_flag_list[currIndex] == '1'):  # 判断当前图片是否可以访问，可以访问，就读取图片
            img = cv2.imread(img_files[currIndex])
        else:
            continue  # 图片不能访问，继续找下一个能访问的图片
        continus_count = 0  # 当前照片与后面的图片连续不相似的次数
        for sec_Index in range(len_img - currIndex - 1):  # 从当前照片索引未知的下一个位置开始遍历，一直遍历到最后，如果中间有连续不相似次数达到阈值，跳出循环
            if (continus_count < 3):  # 一直连续相似
                if (img_flag_list[currIndex + sec_Index + 1] == '1'):
                    img1 = cv2.imread(img_files[currIndex + sec_Index + 1])
                    ssim_value = ssim(img, img1, multichannel=True)
                    if ssim_value > 0.87:    # ok 4 89   NG
                        # 基数
                        count += 1
                        imgs_n.append(img_files[currIndex + sec_Index + 1])  # 图片加入删除列表
                        img_flag_list[currIndex + sec_Index + 1] = 0  # 图片设置不可访问
                        print('big_ssim:', img_files[currIndex][img_files[currIndex].rfind('/') + 1:],
                              img_files[currIndex + 1][img_files[currIndex + 1].rfind('/') + 1:], ssim_value)
                        continus_count = 0  # 连续不相似设置为0
                    else:  # 连续不相似次数开始累加
                        continus_count = continus_count + 1
                else:
                    continue
            else:  # 连续不相似
                break
        if currIndex + 1 >= len(img_files) - 1:  # 避免数组越界
            break
    return count


if __name__ == '__main__':
    path = r'E:\pycharmproject\resnet\data\cam\dataset\train_similiar\NG'  # 相似图片所在文件夹
    # path = r'E:\pycharmproject\resnet\data\cam\dataset\train_similiar\OK'  # 相似图片所在文件夹

    img_path = path
    imgs_n = []  # 要删除的照片的列表

    all_files = list_all_files(path)  # 返回包含完整路径的所有图片名的列表
    print('照片数量为:', len(all_files))
    len1 = len(all_files)
    print(len1)
    img_flag_list = ['1'] * len1  # 1可以访问的图片  0 要删除的图片，不用再访问了
    img_files = []  # 存储所有的图片
    for img in all_files:
        if img.endswith('.bmp'):
            img_files.append(img)  # 将所有图片名都放入列表中
    count = ssim_compare(img_files)  # 返回要删除的图片数量
    print(path, "路径下删除的图片数量为：", count)
    print(imgs_n)
    for image in imgs_n:
        delete(image)


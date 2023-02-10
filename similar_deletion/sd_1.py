# coding: utf-8
import os
import cv2
from skimage.metrics import structural_similarity as ssim


def delete(filename_):
    os.remove(filename_)


def list_all_files(root_):
    files = []
    list_ = os.listdir(root_)
    # os.listdir()方法：返回指定文件夹包含的文件或子文件夹名字的列表。该列表顺序以字母排序
    for i in range(len(list_)):
        element = os.path.join(root_, list_[i])
        # 需要先使用python路径拼接os.path.join()函数，将os.listdir()返回的名称拼接成文件或目录的绝对路径再传入os.path.isdir()和os.path.isfile().
        if os.path.isdir(element):  # os.path.isdir()用于判断某一对象(需提供绝对路径)是否为目录
            # os.path.split分割文件名与路径,分割为data_dir和此路径下的文件名，[-1]表示只取data_dir下的文件名
            files.append(list_all_files(element))

        elif os.path.isfile(element):
            files.append(element)
    # print('2',files)
    return files


def find_similar_pictures_and_remove_to_dst(image_list_):
    if not image_list_:
        print("请注意：图片list为空")
        return {'', []}
    image1_path = image_list_.pop(0)
    if image_list_:
        img1 = cv2.imread(image1_path)
        for image2_path in image_list_:
            img2 = cv2.imread(image2_path)
            ssim_value = ssim(img1, img2, multichannel=True)
            if ssim_value > 0.90:  # 0.95                    801-766 611 362
                image_list_.remove(image2_path)

    return image1_path, image_list_


if __name__ == '__main__':
    # src = r'E:\cls_data\number_cam\data1_for_train\train_fuben\3'
    src = r'E:\pycharmproject\resnet\data\cam\dataset\train\NG'
    # dst = ''
    image_list = list_all_files(src)
    the_remaining_picture_list = []
    while image_list:
        one_image_path, image_list = find_similar_pictures_and_remove_to_dst(image_list)
        print(one_image_path, len(image_list))
        the_remaining_picture_list.append(one_image_path)

    print(the_remaining_picture_list, len(the_remaining_picture_list))

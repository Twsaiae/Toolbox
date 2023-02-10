import os
import shutil

import cv2
import torch
import numpy as np
from PIL import Image
from torchvision import transforms
from tqdm import tqdm
import json


class Cutout(object):
    """Randomly mask out one or more patches from an image.
    Args:
        n_holes (int): Number of patches to cut out of each image.
        length (int): The length (in pixels) of each square patch.#固定长度的正方形边长
    """

    def __init__(self, n_holes, length):
        self.n_holes = n_holes
        self.length = length

    def __call__(self, img):
        """
        Args:
            img (Tensor): Tensor image of size (C, H, W).
        Returns:
            Tensor: Image with n_holes of dimension length x length cut out of it.
        """
        h = img.size(1)
        w = img.size(2)

        mask = np.ones((h, w), np.float32)

        for n in range(self.n_holes):
            # 正方形区域中心点随机出现
            y = np.random.randint(h)
            x = np.random.randint(w)
            # 划出正方形区域，边界处截断
            y1 = np.clip(y - self.length // 2, 0, h)
            y2 = np.clip(y + self.length // 2, 0, h)
            x1 = np.clip(x - self.length // 2, 0, w)
            x2 = np.clip(x + self.length // 2, 0, w)
            # 全0填充区域
            mask[y1: y2, x1: x2] = 0.

        #     expand_as（）函数与expand（）函数类似，功能都是用来扩展张量中某维数据的尺寸，区别是它括号内的输入参数是另一个张量，作用是将输入tensor的维度扩展为与指定tensor相同的size。
        mask = torch.from_numpy(mask)
        mask = mask.expand_as(img)
        img = img * mask

        return img


if __name__ == '__main__':

    # src_list_path = r'E:\pycharmproject\resnet\data\cam\dataset\train_copy\NG_cam_picked_cam'
    # json_list_path = r'E:\pycharmproject\resnet\data\cam\dataset\json_picked'
    # src3_list_path = r'E:\pycharmproject\resnet\data\cam\dataset\train_copy\NG_cam_picked'
    # dst = r'E:\pycharmproject\resnet\data\cam\dataset\train_copy\cutout'
    # os.makedirs(dst, exist_ok=True)
    # image_list = tqdm(os.listdir(src_list_path))
    # for img_name in image_list:
    #     src = os.path.join(src_list_path, img_name)
    #     # src = r'E:\pycharmproject\resnet\data\cam\dataset\train_copy\NG_cam_picked_cam\12022-01-07 02-07-59-691 P21_2.bmp'
    #
    #     img = cv2.imread(src)
    #     # 把灰度图变成01图，超过mean值的改成1
    #     h, w, c = img.shape
    #     # img2 = img < img.mean()
    #     img2 = ((img < img.mean()) * 1).astype(np.uint8)
    #
    #     # cv2.namedWindow('cam_aft', cv2.WINDOW_NORMAL)
    #     # cv2.imshow('cam_aft', img2)
    #     # 小于mean的设置成1，大于的设置成0，然后整体去乘
    #     json_path = f"{json_list_path}/{img_name}_label.json"
    #     # json_path = r"E:\pycharmproject\resnet\data\cam\dataset\json_picked\12022-01-07 02-07-59-691 P21.bmp_label.json"
    #     if os.path.exists(json_path):
    #         with open(json_path, 'r') as f:
    #             content = f.readline()
    #
    #         label_dict = json.loads(s=content)
    #
    #         # auxiliary_label = np.zeros((h, w, c), np.uint8)
    #         for j in label_dict['Labels']:
    #             str_pt1 = j['Points'][0]
    #             str_pt2 = j['Points'][1]
    #             pt1 = str_pt1.split(',')
    #             pt2 = str_pt2.split(',')
    #             x1 = max(round(float(pt1[0])), 0)
    #             y1 = max(round(float(pt1[1])), 0)
    #             x2 = min(round(float(pt2[0])), 64)
    #             y2 = min(round(float(pt2[1])), 128)
    #             # print(float(pt1[0]),float(pt1[1]),float(pt2[0]),float(pt2[1]))
    #             # print(y1, y2, x1, x2)
    #             img2[y1:y2, x1:x2, :] = np.ones((y2 - y1, x2 - x1, 3), np.uint8)
    #         src3 = os.path.join(src3_list_path, img_name)
    #         # src3 = r'E:\pycharmproject\resnet\data\cam\dataset\train_copy\NG_cam_picked\12022-01-07 02-07-59-691 P21.bmp'
    #         img3 = cv2.imread(src3)
    #         # cv2.namedWindow('src', cv2.WINDOW_NORMAL)
    #         # cv2.imshow('src', img3)
    #         img4 = img3 * img2
    #         save_path = os.path.join(dst, img_name)
    #         cv2.imwrite(save_path, img4)
    #     else:
    #         print(f"{json_path} not found")

    # cv2.namedWindow('output', cv2.WINDOW_NORMAL)
    # cv2.imshow('output', img4)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # 1、这些图片的热力图：黑白图，有热力的都为0，没有的为255
    # 2、从json里面读取标签：在1的黑白图里做操作，在框里的全搞成255
    # 3、对比：检测如果没有0则，如果有0

    src = r'E:\pycharmproject\resnet\data\cam\dataset\train_copy\OK'
    dst = r'E:\pycharmproject\resnet\data\cam\dataset\train_copy\OK_cutout'
    os.makedirs(dst,exist_ok=True)
    for i in os.listdir(src):
        img_path = os.path.join(src, i)
        dst_path = os.path.join(dst, i)

        # img_path = r'C:\Users\Administrator\Desktop\imgs\1.jpg'
        # cv:hwc   pil
        src_img = cv2.imread(img_path)
        # cv2.imshow('src', src_img)
        img = torch.from_numpy(src_img.transpose((2, 0, 1)))

        handling_method = Cutout(n_holes=1, length=30)
        dst_img = handling_method(img)
        dst_img = dst_img.numpy()
        output = dst_img.transpose((1, 2, 0))

        output = output.astype(np.uint8)
        # cv2.imshow('output', output)
        # cv2.waitKey(0)
        # shutil.copy(img_path,dst_path)
        cv2.imwrite(dst_path, output)

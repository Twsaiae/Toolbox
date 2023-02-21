import cv2
import torch
import numpy as np
from PIL import Image
from torchvision import transforms


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
    img_path = r'C:\Users\Administrator\Desktop\imgs\1.jpg'
    # opencv:hwc   pil
    src_img = cv2.imread(img_path)
    cv2.imshow('src', src_img)
    img = torch.from_numpy(src_img.transpose((2, 0, 1)))

    handling_method = Cutout(n_holes=1, length=50)
    dst_img = handling_method(img)
    dst_img = dst_img.numpy()
    output = dst_img.transpose((1, 2, 0))

    output = output.astype(np.uint8)
    cv2.imshow('output', output)
    cv2.waitKey(0)

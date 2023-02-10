"""
3d22d
"""
import cv2
import numpy as np
import time
import math


def outlier(image, x_value, y_value, w_value, h_value):
    """
    九个点计算
    """
    z = image[y_value][x_value]
    change = [-1, 0, 1]
    value = 0
    n = 0

    for i in change:

        for j in change:
            if y_value + i < 0 or y_value + i >= h_value:
                continue
            if x_value + j < 0 or x_value + j >= w_value:
                continue
            k_one = i ** 2 + j ** 2 + (image[y_value + i][x_value + j] - z) ** 2
            if k_one < 0:
                return 65535
            value += k_one ** 0.5
            n += 1

    return value / (n - 1)


if __name__ == '__main__':
    src = 'E:/3d/demo/img/tif/damian.tif'
    img = cv2.imread(src, -1)
    h, w = img.shape

    # k = np.zeros_like(img, dtype=np.uint16)
    k = np.zeros_like(img, dtype=np.uint8)
    wtf = []
    for y in range(h):
        for x in range(w):
            # print(round(outlier(img, x, y, w, h)))
            if round(outlier(img, x, y, w, h)) >= 116:
                k[y][x] =255
    # print(np.unique(k))
    cv2.imwrite('k1.png', k)
    # tmp = {}
    # mask = np.unique(k)
    # for v in mask:
    #     tmp[str(v)] = np.sum(k == v)
    # print(tmp)

import cv2
import numpy as np


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
                print("Problems appear")
            value += k_one ** 0.5
            n += 1

    return value / (n - 1)


if __name__ == '__main__':
    src = 'output.png'
    img = cv2.imread(src, -1)
    h, w = img.shape

    # k = np.zeros_like(img, dtype=np.uint16)
    k = np.zeros_like(img, dtype=np.uint8)
    wtf = []
    for y in range(h):
        for x in range(w):
            print(outlier(img, x, y, w, h))
            k[y][x] = round(outlier(img, x, y, w, h))
            wtf.append(round(outlier(img, x, y, w, h)))
    print(np.unique(wtf))
    cv2.imwrite('k1.png', k)

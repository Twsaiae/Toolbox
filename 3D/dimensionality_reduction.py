import cv2
import numpy as np
# import cv2 as opencv
from skimage import io
import matplotlib.pyplot as plt
from tqdm import tqdm
from pathlib import Path
from numba import jit


@jit
def make_3d_slices(image_path, dst_path, slices_num):
    img = cv2.imread(str(image_path), -1)
    # print(np.unique(img)[1])
    h, w = img.shape
    n = np.unique(img)[1]  # 18000   46300
    g = (np.unique(img)[-1] - n) / slices_num
    blank = np.zeros_like(img, dtype=np.uint8)
    for layer in tqdm(range(slices_num)):
        n += g
        for i in range(h):
            for j in range(w):
                # print(img[i][j])
                if img[i][j] >= n:
                    blank[i][j] += 1
    cv2.imwrite(f'{dst_path}/output.png', blank)


if __name__ == '__main__':
    # trackbar_lightness_demo()
    #
    # src = Path('C:/Users/Administrator/Desktop/src')
    src = Path('E:/3d/demo/img/tif')

    dst = Path('C:/Users/Administrator/Desktop/dst')
    image_list = tqdm(src.iterdir())
    for image_path in image_list:
        dst_path = dst.joinpath(image_path.stem)
        dst_path.mkdir(parents=True, exist_ok=True)
        # print(dst_path)
        make_3d_slices(image_path, dst_path, 255)

    # img = cv2.imread('damian.png')
    # blank = np.zeros_like(img, dtype=np.uint8)

    # cv2.namedWindow('result', cv2.WINDOW_AUTOSIZE)
    # cv2.createTrackbar('gray value', 'result', 30000, 36703, prt)
    # while True:
    #     n = cv2.getTrackbarPos('gray value', 'result')
    # n = 28800

    # cv2.namedWindow('blank', cv2.WINDOW_NORMAL)
    # cv2.imshow('blank', blank)
    # cv2.waitKey(0)

    # print(np.unique(blank))

    # print(type(blank[0][0]))
    # blank[0][0] = 1
    # print(blank[0][0])

    # for i in range(5):
    #     print(i)

    # img = cv2.imread('damian.png')
    # cv2.namedWindow('3d', cv2.WINDOW_NORMAL)
    # cv2.imshow('blank', blank)
    # cv2.imshow('3d', img)
    # cv2.waitKey(0)
    # cv2.imwrite('damian.png', img)

    # print(img.dtype)
    # print(img)
    # print(np.unique(img))
    # print(img[2000, 1000])

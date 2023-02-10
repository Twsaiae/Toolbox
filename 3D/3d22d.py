"""
3d22d
"""
import cv2
import numpy as np
import time

if __name__ == '__main__':
    # src = 'E:/3d/demo/img/tif/damian.tif'
    src = 'E:/3d/demo/img/tif/damianaoxian.tif'
    img = cv2.imread(src, -1)

    img = cv2.resize(img, dsize=(0,0),fx=0.5,fy=0.5, interpolation=cv2.INTER_NEAREST)
    print(img.shape)
    print(np.unique(img)[0], np.unique(img)[1], np.unique(img)[2],
          np.unique(img)[3], np.unique(img)[4], np.unique(img)[5], np.unique(img)[6], np.unique(img)[7],
          np.unique(img)[8], np.unique(img)[9], np.unique(img)[10], np.unique(img)[11], np.unique(img)[12],
          np.unique(img)[13], np.unique(img)[14], np.unique(img)[15], np.unique(img)[16], np.unique(img)[17])
    h, w = img.shape
    print(h,w)
    start = time.time()
    # # 归一化到255之间
    z_max = np.unique(img)[-1]
    z_min = np.unique(img)[1]
    thickness = z_max - z_min
    k = 255 / thickness
    print(z_min, z_max, thickness,k)
    # print(np.unique(img), z_max, z_min, thickness, thickness / 255, 255 * 250)
    blank = np.zeros_like(img, dtype=np.uint8)

    #
    for y in range(h):
        for x in range(w):
            # outlier(img, x, y)
            if img[y][x] < z_min:
                blank[y][x] = 0
            else:
                blank[y][x] = round((img[y][x] - z_min) * k)
            # print(round((img[y][x] - z_min) * k),blank[y][x])
    end = time.time()
    print(end - start)
    cv2.imwrite('output_src_real.png', blank)

    # z_max = np.unique(img)[-1]
    # z_min = np.unique(img)[1]
    # print(z_min, z_max, z_max - z_min)

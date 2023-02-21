"""
judge the contrast
"""
# coding=utf-8
import cv2
import numpy as np
import Nparts


def detect_blur(image, size=None):
    # 灰度化
    if len(image.shape) == 3:
        grayImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        grayImg = image.copy()
    # 缩放到固定撒小
    if size is not None:
        grayImg = cv2.resize(grayImg, size)
    # gray_lap = cv2.Laplacian(grayImg, cv2.CV_16S)
    gray_lap = cv2.Laplacian(grayImg, cv2.CV_64F)

    dst = cv2.convertScaleAbs(gray_lap)
    fm = dst.var()
    # text = "Not Blurry"
    # # if the focus measure is less than the supplied threshold,
    # # then the image should be considered "blurry"
    # if fm < threshold:
    #     text = "Blurry"
    # # show the image
    # cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30),
    #             cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
    # cv2.imshow("Image", image)
    # cv2.waitKey(0)
    print(fm)
    return fm


if __name__ == '__main__':
    # 整体雾
    f1 = "/home/vs/Pictures/雾或者脏/20211028085705710395167.jpg"
    f2 = '/home/vs/Pictures/雾或者脏/20211028080757599734799.jpg'
    f3 = '/home/vs/Pictures/雾或者脏/20211028085547797115614.jpg'
    # 部分雾
    f4 = "/home/vs/Pictures/水雾/20211012225148160741178.jpg"
    f5 = '/home/vs/Pictures/水雾/b11.jpg'
    f6 = '/home/vs/Pictures/水雾/20211013050747502101174.jpg'
    # 没有雾
    f7 = "/home/vs/Pictures/反光/a1055.jpg"
    f8 = '/home/vs/Pictures/反光/m4.jpg'
    f9 = '/home/vs/Pictures/反光/m2.jpg'
    # a = [f1,f2,f3,f4,f5,f6,f7,f8,f9]
    # b = [detect_blur(i) for i in a]
    # print(b)
    # detect_blur(f6)
    b4 = '/home/vs/Pictures/水雾/20211012225148160741178.jpg'
    b5 = '/home/vs/Pictures/水雾/20211012225444268338305.jpg'
    b6 = '/home/vs/Pictures/水雾/20211013010121103246590.jpg'
    b7 = '/home/vs/Pictures/水雾/20211013010440423907259.jpg'
    b8 = '/home/vs/Pictures/水雾/20211013010528379816064.jpg'
    b9 = '/home/vs/Pictures/水雾/20211013045912621378172.jpg'
    b10 = '/home/vs/Pictures/水雾/b10.jpg'
    b11 = '/home/vs/Pictures/水雾/b11.jpg'
    b12 = '/home/vs/Pictures/水雾/b12.jpg'
    b13 = '/home/vs/Pictures/水雾/20211013050336051296468.jpg'
    b14 = '/home/vs/Pictures/水雾/b14.jpg'
    b15 = '/home/vs/Pictures/水雾/20211013050747502101174.jpg'
    b16 = '/home/vs/Pictures/水雾/20211013050752078886325.jpg'
    b17 = '/home/vs/Pictures/水雾/20211013051215677257929.jpg'
    b18 = '/home/vs/Pictures/水雾/20211013052043616103247.jpg'
    img = cv2.imread(b18)
    if detect_blur(img)<1500:
        cv2.imshow('blur', img)
        cv2.waitKey(0)
        print(f'该图片被判定为模糊图片')

    # else:
    #     a = Nparts.n_part(img, 2)
    #     for i in range(len(a)):
    #         if detect_blur(a[i]) < 1500:
    #             # cv2.imshow('local blur', a[i])
    #             # cv2.waitKey(0)
    #             print(f'{i}存在部分模糊')

    a = Nparts.n_part(img, 2)
    for i in range(len(a)):
        if detect_blur(a[i]) < 1500:
            cv2.imshow('local blur', a[i])
            cv2.waitKey(0)
            print(f'{i}存在部分模糊')

                # break
    # for i in len(a)
    # b = detect_blur(a[3])





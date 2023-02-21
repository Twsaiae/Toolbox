"""
picture_evaluation
目标：输入图片，分析出图片是否为可鉴别的问题图片。

可鉴别问题图片1：摄像头角度造成的逆光照片，该类型图像反差大，图片属于高对比度图片。
可鉴别问题图片2：摄像头镜片变脏造成的整体模糊和下雨等恶劣天气造成的部分模糊。
可鉴别问题图片3：光照造成的图片的色偏情况。
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np
import math


def n_part(image, sub_image_num):
    """
    :param image: numpy数组类型的图片。
    :param sub_image_num: 将图片分成sub_image_num的平方份。
    :return: 一个装着所有分好图片的list。
    """
    # src = cv2.imread(image_path, -1)
    src = image.copy()
    sub_images = []
    # 横竖都分两份
    # sub_image_num = 2
    src_height, src_width = src.shape[0], src.shape[1]
    # 读取图片的长和宽，除去要分割的份数，然后得到不大于结果的最大一个整数，就是得到的数向下取整
    sub_height = src_height // sub_image_num
    sub_width = src_width // sub_image_num
    for j in range(sub_image_num):
        for i in range(sub_image_num):
            # 都正确，就执行
            if j < sub_image_num - 1 and i < sub_image_num - 1:
                image_roi = src[j * sub_height: (j + 1) * sub_height, i * sub_width: (i + 1) * sub_width, :]
                # j是高，如果高还没分完，就高继续，宽分完了，就保持宽的起始点
            elif j < sub_image_num - 1:
                image_roi = src[j * sub_height: (j + 1) * sub_height, i * sub_width:, :]
            elif i < sub_image_num - 1:
                image_roi = src[j * sub_height:, i * sub_width: (i + 1) * sub_width, :]
            else:
                image_roi = src[j * sub_height:, i * sub_width:, :]
            sub_images.append(image_roi)
    return sub_images


def judge_the_contrast(image, threshold=0.5):
    """
    :param image: numpy数组类型的图片。
    :param threshold: 极端的明亮和黑暗的像素点占总像素点的比例,默认值为0.50是根据vsais部分场景测试得出。
    :return: 图像是否为高对比图像的bool值，False为高对比图片，True为正常图片。
    """
    # 灰度化
    if len(image.shape) == 3:
        grayImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        grayImg = image.copy()
    # 效果展示
    # plt.hist(grayImg.ravel(), 256)
    # plt.show()
    # 规定极端明亮的像素区域和极端黑暗的像素区域
    dark_part = cv2.inRange(grayImg, 0, 60)
    bright_part = cv2.inRange(grayImg, 225, 256)
    # 如果传入的参数只有一个，则返回矩阵的元素个数；如果传入的第二个参数是0，则返回矩阵的行数；如果传入的第二个参数是1，则返回矩阵的列数。
    total_pixel = np.size(grayImg)
    dark_pixel = np.sum(dark_part > 0)  # 是一个true和false的数组
    bright_pixel = np.sum(bright_part > 0)
    dp = dark_pixel / total_pixel
    bp = bright_pixel / total_pixel
    percentage = dp + bp
    # 可以查看太亮和太暗像素的占比，和总占比
    # print(dp, bp, percentage)
    if percentage >= threshold:
        return False
    else:
        return True


def judge_the_blur(image, size=None, threshold=1500):
    """
    :param image: numpy数组类型的图片。
    :param size: 统一判定的图片尺寸，默认按照原图大小。
    :param threshold: 使用拉普拉斯算法后，所有像素值取方差(跟size有相关性)。
    :return: 判定图像模糊与否的bool值,False为模糊，True为不模糊。
    """
    # 灰度化
    if len(image.shape) == 3:
        grayImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        grayImg = image.copy()
    # 缩放到固定撒小
    if size is not None:
        grayImg = cv2.resize(grayImg, size)
    gray_lap = cv2.Laplacian(grayImg, cv2.CV_64F)
    dst = cv2.convertScaleAbs(gray_lap)
    fm = dst.var()
    # print(fm)
    text = "Not Blurry"
    if fm < threshold:
        text = "Blurry"
        # 效果展示
        # cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30),
        #             cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
        # cv2.imshow("Image", image)
        # cv2.waitKey(0)
        return False
    else:
        # 效果展示
        # cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30),
        #             cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
        # cv2.imshow("Image", image)
        # cv2.waitKey(0)
        return True


def judge_color_cast(image, threshold=1):
    """
    :param image: numpy数组类型的图片。
    :param threshold: 根据现有场景设定的偏色因子K的阈值。
    :return: 判定图像色偏与否的bool值，False为偏色图片，True为正常图片。
    """
    # image = cv2.imread(image_path)
    img_lab = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
    l, a, b = cv2.split(img_lab)
    h, w, _ = image.shape
    sum_a = np.sum(a)
    sum_b = np.sum(b)
    mn = w * h
    da = sum_a / mn - 128
    db = sum_b / mn - 128
    # 求平均色度
    D = math.sqrt(da * da + db * db)
    # 求色度中心距
    a = a.astype(np.int16)
    a2 = a - 128 - da
    a3 = np.maximum(a2, -a2)
    b = b.astype(np.int16)
    b2 = b - 128 - db
    b3 = np.maximum(b2, -b2)
    ma = np.sum(a3)
    mb = np.sum(b3)
    ma = ma / mn
    mb = mb / mn
    M = math.sqrt(ma * ma + mb * mb)
    # 阈值设置为1就行
    K = D / M
    # print(K)
    if K >= threshold:
        return False
    else:
        return True


def main(image_path):
    """
    :param image_path: 输入图像地址
    :return: 返回一个关于该图片质量的字典，'contrast':'normal'/'high','clarity':'normal'/'blur'/'local blur'，'color':'normal'/'color cast'
    """
    img = cv2.imread(image_path)
    quality = {
        'contrast': 'normal',
        'clarity': 'normal',
        'color': 'normal'
    }
    # 第一步判断是否有逆光
    if not judge_the_contrast(img):
        quality['contrast'] = 'high'
        print('注意：经过像素分析，检测到当前图像反差大，属于高对比度图片,该类图片特征表现不明显，可能导致检测效果下降。造成该问题出现的原因可能是摄像头位置朝向属于“坐北朝南”类型，可以尝试调整摄像头位置和朝向。')
    # 第二步判断是否有模糊
    if not judge_the_blur(img):
        quality['clarity'] = 'blur'
        print('注意：经过像素分析，检测到当前图片整体模糊，属于模糊图片，该类图片特征表现不明显，可能导致检测效果下降。造成该问题出现的原因可能是相机长时间使用或者恶劣天气弄脏了镜片，可以尝试使用酒精试纸擦拭镜头。')
    else:
        a = n_part(img, 2)
        j = 0
        for i in range(len(a)):
            if not judge_the_blur(a[i]):
                j += 1
        if j >= 2:
            quality['clarity'] = 'local blur'
            print('注意：经过像素分析，检测到当前图像有两处及以上模糊存在，属于模糊图片，该类图片特征表现不明显，可能导致检测效果下降。造成该问题出现的原因可能是相机长时间使用或者恶劣天气弄脏了镜片，可以尝试使用酒精试纸擦拭镜头。')
    if not judge_color_cast(img):
        quality['color'] = 'color cast'
        print('注意：经过像素分析，检测到当前图像存在色偏情况，属于偏色图片，该类图片特征表现不明显，可能导致检测效果下降。造成该问题出现的原因可能是场景特殊光照的影响，可以尝试调整摄像头的位置和朝向。')
    # else:
    #     a = n_part(img, 2)
    #     j = 0
    #     for i in range(len(a)):
    #         if not judge_color_cast(a[i]):
    #             j += 1
    #     if j >= 1:
    #         quality['color'] = 'local color cast'
    #         print('注意：经过像素分析，检测到当前图像有两处及以上色偏存在，属于色偏图片，该类图片特征表现不明显，可能导致检测效果下降。')
    return quality


if __name__ == "__main__":
    # 逆光
    f1 = '/home/vs/Pictures/反光/a5.jpg'
    f2 = '/home/vs/Pictures/反光/a6.jpg'
    f3 = '/home/vs/Pictures/反光/a7.jpg'
    f4 = '/home/vs/Pictures/反光/a8.jpg'
    f5 = '/home/vs/Pictures/反光/a9.jpg'
    f6 = '/home/vs/Pictures/反光/a105.jpg'
    f7 = '/home/vs/Pictures/反光/a1044.jpg'
    f8 = '/home/vs/Pictures/反光/a1055.jpg'
    f9 = '/home/vs/Pictures/反光/m1.jpg'
    f10 = '/home/vs/Pictures/反光/m2.jpg'
    f11 = '/home/vs/Pictures/反光/m4.jpg'
    # 整张模糊
    b1 = '/home/vs/Pictures/雾或者脏/20211028080757599734799.jpg'
    b2 = '/home/vs/Pictures/雾或者脏/20211028085547797115614.jpg'
    b3 = '/home/vs/Pictures/雾或者脏/20211028085705710395167.jpg'
    # 部分模糊
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

    test = '/home/vs/Pictures/图片偏红光/9.jpg'
    result = main(test)
    print(result)

    # img = cv2.imread(f10) 1 2
    # plt.hist(img.ravel(), 256, [0, 256])
    # plt.show()






















    # print(f)
    # 第二步检测全面模糊 b5 b7 b8 b9 b10 b11 b12 b16 b17 18
    # b = judge_the_blur(b18)
    # print(b)

    # a = Nparts.n_part(f6, 2)
    # b = detect_blur(a[3])























































# def judging_the_water_mist(image, threshold=1000):
#
#     image = cv2.imread(image)
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     lapl = cv2.Laplacian(gray, cv2.CV_64F)
#     fm = lapl.var()
#     # grayImag = cv2.GaussianBlur(grayImag, (3, 3), 0)
#     print('Laplacian : ' + str(fm))
#
#     cv2.putText(gray, str(int(fm)), (0, 40), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 2)
#
#     # longimag = np.hstack((image, gray, lapl))
#
#     cv2.imshow('shahuhu', lapl)
#     cv2.waitKey(0)
#
#     return True


# img = cv2.imread('/home/vs/Pictures/反光/a5.jpg')  # 0表示灰度图 , 0
# img2 = cv2.imread('/home/vs/Pictures/反光/a6.jpg')
# img3 = cv2.imread('/home/vs/Pictures/反光/a7.jpg')
# img4 = cv2.imread('/home/vs/Pictures/反光/a8.jpg')
# img5 = cv2.imread('/home/vs/Pictures/反光/a9.jpg')
# img6 = cv2.imread('/home/vs/Pictures/反光/a105.jpg')
# img6_1 = cv2.imread('/home/vs/Pictures/反光/a1044.jpg')
# img6_2 = cv2.imread('/home/vs/Pictures/反光/a1055.jpg')
# img7 = cv2.imread('/home/vs/Pictures/反光/m1.jpg')
# img8 = cv2.imread('/home/vs/Pictures/反光/m2.jpg')
# img9 = cv2.imread('/home/vs/Pictures/反光/m4.jpg')

# # 展示方式一：画的梯形图
# # 展示1
# plt.hist(img.ravel(), 256, [0, 256])
# plt.show()
# plt.hist(img.ravel(), 16)
# plt.show()
# plt.hist(img2.ravel(), 16)
# plt.show()
# plt.hist(img3.ravel(), 16)
# plt.show()
# plt.hist(img4.ravel(), 16)
# plt.show()
# plt.hist(img5.ravel(), 16)
# plt.show()
# plt.hist(img6.ravel(), 16)
# plt.show()
# plt.hist(img7.ravel(), 16)
# plt.show()
# plt.hist(img8.ravel(), 16)
# plt.show()
# plt.hist(img9.ravel(), 16)
# plt.show()

# 展示方式二：折线图
# plt.hist(img6.ravel(), 256, [0, 256])
# plt.show()


# a = img.ravel()
# b = a.astype(np.int16)
# b = 150 - b.ravel()
# # 比较两个数组的大小,用来绝对值整个数组
# b = np.maximum(b, -b)
# # 越大越不好，越大说明两边越大，图像反差大高对比度场景
# sum = np.sum(b)
# # b = value.astype(int)
# print(a)
# print(b)
# print(sum)

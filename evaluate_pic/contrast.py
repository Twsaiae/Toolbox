import cv2
import numpy as np
import matplotlib.pyplot as plt


def judge_the_contrast(image_path, threshold=0.50):
    """
    :param image_path: 图片地址
    :param threshold: 极端的明亮和黑暗的像素点占总像素点的比例
    :return: 图像是否为高对比图像的bool值
    """
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    dark_part = cv2.inRange(gray, 0, 60)
    bright_part = cv2.inRange(gray, 225, 256)
    # use histogram
    # dark_pixel = np.sum(hist[:30])
    # bright_pixel = np.sum(hist[220:256])
    # 如果传入的参数只有一个，则返回矩阵的元素个数；如果传入的第二个参数是0，则返回矩阵的行数；如果传入的第二个参数是1，则返回矩阵的列数。
    total_pixel = np.size(gray)
    # print(dark_part > 0)  # 是一个true和false的数组
    dark_pixel = np.sum(dark_part > 0)
    bright_pixel = np.sum(bright_part > 0)
    dp = dark_pixel/total_pixel
    bp = bright_pixel/total_pixel
    percentage = dp + bp
    print(dp, bp, percentage)
    if percentage >= threshold:
        print('注意：经过像素分析，检测到当前图像反差大，场景属于高对比度场景，特征表现不明显，导致检测效果下降。')
        return False
    else:
        print('图片没问题，属于可检测图片。')
        return True


if __name__ == "__main__":
    b10 = '/home/vs/Pictures/水雾/b10.jpg'
    b11 = '/home/vs/Pictures/水雾/b11.jpg'
    b12 = '/home/vs/Pictures/水雾/b12.jpg'
    b14 = '/home/vs/Pictures/水雾/b14.jpg'
    judge_the_contrast(b14)

    img = cv2.imread(b14)
    plt.hist(img.ravel(), 256, [0, 256])
    plt.show()

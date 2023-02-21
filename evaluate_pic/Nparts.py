import cv2


def n_part(image, sub_image_num):
    # src = cv2.imread(image_path, -1)
    sub_images = []
    src = image.copy()
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

# # 用enumerate就可以for i 和 img 一起
# for i, img in enumerate(sub_images):
    # cv2.imwrite('sub_img_' + str(i) + '.png', img)

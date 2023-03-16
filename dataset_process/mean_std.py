"""
数据集求mean和std
"""
import os
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
# from scipy.misc import imread
# from imageio import imread
import imageio.v2 as imageio
# filepath = 'E:/pycharmproject/mm_cls/data/train/1'  # the path of dataset
filepath = r'C:\Users\Thor\Downloads\ConvNextV2_Demo\ConvNextV2_Demo\data/train/baihe'  # the path of dataset
pathDir = os.listdir(filepath)

R_channel = 0
G_channel = 0
B_channel = 0
img_size = 0

for idx in range(len(pathDir)):
    filename = pathDir[idx]
    img = imageio.imread(os.path.join(filepath, filename))
    # img = img / 255.0
    img_size = img_size + img.shape[0] * img.shape[1]
    R_channel = R_channel + np.sum(img[:, :, 0])
    G_channel = G_channel + np.sum(img[:, :, 1])
    B_channel = B_channel + np.sum(img[:, :, 2])

R_mean = R_channel / img_size
G_mean = G_channel / img_size
B_mean = B_channel / img_size

R_channel = 0
G_channel = 0
B_channel = 0
for idx in range(len(pathDir)):
    filename = pathDir[idx]
    img = imageio.imread(os.path.join(filepath, filename))
    # img = img / 255.0
    R_channel = R_channel + np.sum((img[:, :, 0] - R_mean) ** 2)
    G_channel = G_channel + np.sum((img[:, :, 1] - G_mean) ** 2)
    B_channel = B_channel + np.sum((img[:, :, 2] - B_mean) ** 2)

R_var = (R_channel / img_size) ** 0.5
G_var = (G_channel / img_size) ** 0.5
B_var = (B_channel / img_size) ** 0.5

print("R_mean is %f, G_mean is %f, B_mean is %f" % (R_mean, G_mean, B_mean))
print("R_var is %f, G_var is %f, B_var is %f" % (R_var, G_var, B_var))

# R_mean is 0.515256, G_mean is 0.515256, B_mean is 0.515256
# R_var is 0.094835, G_var is 0.094835, B_var is 0.094835
# R_mean is 0.483194, G_mean is 0.483194, B_mean is 0.483194
# R_var is 0.093928, G_var is 0.093928, B_var is 0.093928

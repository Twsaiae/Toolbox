# cython: language_level=3
import os
import random
import numpy as np
import math
import torch
import torch.nn as nn
import torch.backends.cudnn as cudnn
import torch.nn.functional as F
import cv2 as cv
import copy
from torch.autograd import Variable
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from torchvision.datasets import ImageFolder
from torchvision import transforms
from PIL import Image, ImageDraw

# 以下是用户选择参数:
# contrastUL = 2 #对比度上限
# brightUL = 80 #亮度上限
# sharpUL = 20#锐化上限
# blurUL = 10#平滑上限
# noiseUL = 15#噪声上限
# contrastUL  = self.enHanceParamValueList[0]
# contrastLL  = self.enHanceParamValueList[1]
# brightUL    = self.enHanceParamValueList[2]
# brightLL    = self.enHanceParamValueList[3]
# sharpUL     = self.enHanceParamValueList[4]
# blurUL      = self.enHanceParamValueList[5]
# noiseUL     = self.enHanceParamValueList[6]
contrastUL = 1
contrastLL = 0
brightUL = 100
brightLL = -100
sharpUL = 10
blurUL = 5
noiseUL = 10


class MyDataset(Dataset):
    def __init__(self, data, transform, enHanceparam='', enHanceParamValueList=[]):
        p = ['SPFZ', 'XZ90', 'SPJB', 'SZFZ', 'XZ180', 'SZJB', 'FD', 'SJXZ', 'SJCJ',
             'LD', 'GGJR', 'TS', 'DBD', 'ABGS', 'GZJD',
             'BHB', 'SW', 'RH', 'SXBH', 'JZ', 'PH',
             'MBZD', 'BX']
        disable = ['SPJB', 'SZJB', 'GGJR', 'TS', 'ABGS', 'GZJD', 'BHB', 'SW', 'BX']
        self.data = data
        self.transform = transform
        self.enHanceParamValueList = 'TFFFFFFFFFFFFFFFFFFFFFFFFF'

        self.enHanceparam = ['NONE']
        for i in range(len(enHanceparam)):
            if enHanceparam[i] == 'T':
                if not p[i] in disable:
                    self.enHanceparam.append(p[i])
                    print(p[i])
            pass

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        srcimage = cv.imdecode(np.fromfile(self.data[idx][0], dtype=np.uint8), cv.IMREAD_COLOR)
        srcimage = self.__enHancement(srcimage, self.enHanceparam)
        srcimage = Image.fromarray(srcimage)
        image = self.transform(srcimage)
        return image, int(self.data[idx][1])

    ### 每次出一个选项
    def __enHancement(self, img, inEnHanceparam):
        t = random.randint(0, len(inEnHanceparam) - 1)
        t = inEnHanceparam[t]

        srcShape = tuple(img.shape[:2])
        if 'SPFZ' in t:
            ###水平翻转1
            img = cv.flip(img, 0)
        elif 'SZFZ' in t:
            ###竖直翻转2
            img = cv.flip(img, 1)
        elif 'DBD' in t:
            ###对比度3
            alpha = random.uniform(0.15, contrastUL)
            beta = 0
            blank = np.zeros(img.shape, img.dtype)  # 创建图片类型的零矩阵
            img = cv.addWeighted(img, alpha, blank, 1 - alpha, beta)  # 图像混合加权
        elif 'LD' in t:
            ###亮度4
            alpha = 1
            beta = random.randint(brightLL, brightUL)
            blank = np.zeros(img.shape, img.dtype)  # 创建图片类型的零矩阵
            img = cv.addWeighted(img, alpha, blank, 1 - alpha, beta)  # 图像混合加权
        elif 'XZ90' in t:
            ###90°旋转5
            shape = tuple(img.shape[:2])
            img = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
            img = cv.resize(img, dsize=(shape[1], shape[0]))
        elif 'XZ180' in t:
            ###180°旋转6               
            img = cv.rotate(img, cv.ROTATE_180)
        elif 'FD' in t:
            ###放大7
            alpha = random.uniform(1, 2)
            zoominImg = cv.resize(img, dsize=(int(img.shape[1] * alpha), int(img.shape[0] * alpha)))
            yStart = (zoominImg.shape[0] - img.shape[0]) / 2
            xStart = (zoominImg.shape[1] - img.shape[1]) / 2
            img = zoominImg[int(xStart):int(xStart) + img.shape[0], int(yStart):int(yStart) + img.shape[1]]
        elif 'RH' in t:
            ###锐化8
            alpha = random.uniform(0, sharpUL)
            blurimg = cv.GaussianBlur(img, (3, 3), 0)
            matBlur = blurimg / 255.0
            matSrc = img / 255.0
            matOut = alpha * (matSrc - matBlur) + matSrc
            matOut[matOut < 0] = 0
            matOut[matOut > 1] = 1
            # img = matOut*255
            img = (matOut * 255).astype(np.uint8)
        elif 'PH' in t:
            ###平滑9
            alpha = random.randint(0, blurUL)
            size = alpha * 2 + 1
            img = cv.GaussianBlur(img, (size, size), 0)
        elif 'SXBH' in t:
            ###色相变化 取代色调10
            hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
            bHue = random.randint(-255, 255)
            hueImg = copy.deepcopy(hsv)
            hueImg[:, :, 0] = cv.add(hueImg[:, :, 0], bHue)
            img = cv.cvtColor(hueImg, cv.COLOR_HSV2BGR)
        elif 'JZ' in t:
            ###加噪11
            prob = random.uniform(0, noiseUL)
            out = np.zeros(img.shape, dtype=int)
            mu = 0
            sigma = random.uniform(5, noiseUL)
            for i in range(img.shape[0]):
                for j in range(img.shape[1]):
                    for k in range(img.shape[2]):
                        xx = img[i, j, k]
                        out[i, j, k] = xx + random.gauss(mu=mu, sigma=sigma)
            out[out > 255] = 255
            out[out < 0] = 0
            img = out.astype(np.uint8)
        elif 'MBZD' in t:
            ###目标遮挡12
            srcHeight, srcWeigh = img.shape[:2]
            ww = int(srcWeigh / 3)
            hh = int(srcHeight / 3)
            xx = random.randint(0, srcWeigh - ww)
            yy = random.randint(0, srcHeight - hh)
            img = Image.fromarray(img)
            draw = ImageDraw.Draw(img)
            draw.rectangle((xx, yy, xx + ww, yy + hh), fill=(0, 0, 0))
            out = np.array(img)
            img = out
        elif 'SJXZ' in t:
            ###随机旋转 13
            srcHeight, srcWeigh = img.shape[:2]
            t_ = random.randint(0, 360)
            M = cv.getRotationMatrix2D((srcWeigh / 2, srcHeight / 2), t_, 1)
            img = cv.warpAffine(img, M, (srcWeigh, srcHeight))
        elif 'SJCJ' in t:
            ###随机裁剪14
            srcHeight, srcWeigh = img.shape[:2]
            bordH = srcHeight // 8
            bordW = srcWeigh // 8
            BLACK = [0, 0, 0]
            bordImg = cv.copyMakeBorder(img, bordH, bordH, bordW, bordW, cv.BORDER_CONSTANT, value=BLACK)
            startY = np.random.randint(0, bordH * 2)
            startX = np.random.randint(0, bordW * 2)
            # tempImg = cv.rectangle(bordImg,(startX,startY),(startX + srcWeigh,startY+srcHeight))
            tempImg = bordImg[startY:startY + srcHeight, startX:startX + srcWeigh]
            img = tempImg
        elif 'SPJB' in t:
            ###水平畸变15
            prob = random.uniform(0.01, 0.15)
            dir = random.randint(0, 1)
            srcHeight, srcWeigh = img.shape[:2]
            srcPoints = np.float32([[0, 0], [srcWeigh, 0], [0, srcHeight], [srcWeigh, srcHeight]])
            if dir == 0:
                canvasPoints = np.float32([[srcWeigh * prob * 2, srcHeight * prob],
                                           [srcWeigh, 0],
                                           [srcWeigh * prob * 2, srcHeight - srcHeight * prob],
                                           [srcWeigh, srcHeight]])
            else:
                canvasPoints = np.float32([[0, 0],
                                           [srcWeigh - srcWeigh * prob * 2, srcHeight * prob],
                                           [0, srcHeight],
                                           [srcWeigh - srcWeigh * prob * 2, srcHeight - srcHeight * prob]])
            perspectiveMatrix = cv.getPerspectiveTransform(np.array(srcPoints), np.array(canvasPoints))
            perspectiveImg = cv.warpPerspective(img, perspectiveMatrix, (img.shape[1], img.shape[0]))
            img = perspectiveImg
        elif 'SZJB' in t:
            ###竖直畸变16
            prob = random.uniform(0.01, 0.15)
            dir = random.randint(0, 1)
            srcHeight, srcWeigh = img.shape[:2]
            srcPoints = np.float32([[0, 0], [srcWeigh, 0], [0, srcHeight], [srcWeigh, srcHeight]])
            if dir == 0:
                canvasPoints = np.float32([[srcWeigh * prob, srcHeight * prob * 2],
                                           [srcWeigh - srcWeigh * prob, srcHeight * prob * 2],
                                           [0, srcHeight],
                                           [srcWeigh, srcHeight]])
            else:
                canvasPoints = np.float32([[0, 0],
                                           [srcWeigh, 0],
                                           [srcWeigh * prob, srcHeight - srcHeight * prob * 2],
                                           [srcWeigh - srcWeigh * prob, srcHeight - srcHeight * prob * 2]])
            perspectiveMatrix = cv.getPerspectiveTransform(np.array(srcPoints), np.array(canvasPoints))
            perspectiveImg = cv.warpPerspective(img, perspectiveMatrix, (img.shape[1], img.shape[0]))
            img = perspectiveImg
        elif 'BHD' in t:
            ###饱和度17
            hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
            bSat = random.randint(-50, 50)
            satImg = copy.deepcopy(hsv)
            satImg[:, :, 1] = cv.add(satImg[:, :, 1], bSat)
            img = cv.cvtColor(satImg, cv.COLOR_HSV2BGR)

        elif 'JB' in t:
            ###渐变 即：光照角度18
            srcHeight, srcWeigh = img.shape[:2]
            channel = img.shape[2]
            out = np.zeros([srcHeight, srcWeigh, channel], dtype=int)
            center_x = random.randint(0, srcHeight)
            center_y = random.randint(0, srcWeigh)
            distance = srcWeigh * srcWeigh + srcHeight * srcHeight
            radius = math.sqrt(distance)
            for i in range(srcHeight):
                for j in range(srcWeigh):
                    for k in range(channel):
                        value = img[i, j, k]
                        out[i, j, k] = math.sqrt((i - center_x) ** 2 + (i - center_x) ** 2) * (
                            -160) / radius + 80 + value
            out[out > 255] = 255
            out[out < 0] = 0
            img = out

        elif 'BX' in t:
            ###变形19
            row, col = img.shape[:2]
            channel = img.shape[2]
            new_img = np.zeros([row, col, channel], dtype=np.uint8)
            # center_x=row/2
            # center_y=col/2
            ## radius=math.sqrt(center_x*center_x+center_y*center_y)/2
            # radius = min(center_x,center_y)
            center_y = random.randint(0, col - 1)
            center_x = random.randint(0, row - 1)
            radius1 = min(center_x + 1, center_y + 1, col - center_y, row - center_x)
            radius = random.randint(round(radius1 / 5), radius1)
            for i in range(row):
                for j in range(col):
                    distance = ((i - center_x) * (i - center_x) + (j - center_y) * (j - center_y))
                    new_dist = math.sqrt(distance)
                    new_img[i, j, :] = img[i, j, :]
                    if distance <= radius ** 2:
                        new_i = np.int(np.floor(new_dist * (i - center_x) / radius + center_x))
                        new_j = np.int(np.floor(new_dist * (j - center_y) / radius + center_y))
                        new_img[i, j, :] = img[new_i, new_j, :]
            img = new_img
        if img.shape[1] != srcShape[1] or img.shape[0] != srcShape[0]:
            img = cv.resize(img, dsize=(srcShape[1], srcShape[0]))
        return img


if __name__ == '__main__':
    number = MyDataset()

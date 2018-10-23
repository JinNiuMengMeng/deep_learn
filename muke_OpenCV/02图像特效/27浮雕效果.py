import numpy as np
import cv2
import os

proPath = os.path.dirname(__file__)
print(proPath)
img = cv2.imread("../../Picture/water.png")
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# newP = gray0-gray1+150
# 新的像素值 = 相邻像素值之差(为了突出灰度的图片即边缘特征) + 一个恒定值(增强图片的浮雕灰度等级)
dst = np.zeros((height, width, 1), np.uint8)
for i in range(0, height):
    for j in range(0, width - 1):
        gray0 = int(gray[i, j])
        gray1 = int(gray[i, j + 1])
        newP = gray0 - gray1 + 150
        if newP > 255:
            newP = 255
        elif newP < 0:
            newP = 0
        else:
            pass
        dst[i, j] = newP
cv2.imshow("dst", dst)
cv2.waitKey(0)

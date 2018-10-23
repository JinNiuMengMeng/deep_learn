import cv2
import numpy as np

# 示例一
img1 = cv2.imread('../../Picture/water.jpg', 1)
img1Info = img1.shape
print("img.shape:", img1Info)  # 输出图片的[宽度, 高度, 图片的颜色组成方式]
cv2.imshow("img1", img1)
height1 = img1Info[0]
width1 = img1Info[1]

# canny 边缘检测
# 第一步: 将图片进行灰度处理: 所有边缘检测的处理几乎都是基于灰度图像的处理
# 第二步: 将图片进行高斯运算: 通过高斯滤波可以去除一些噪声的干扰
# 第三步: 将图片进行卷积运算
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
# 第一个参数是灰度图像data数据
# 第二个参数是模板大小
imgG1 = cv2.GaussianBlur(gray1, (3, 3), 0)
# 完成边缘检测
# 第一个参数表示图片的data数据
# 第二与第三个参数表示门线, (如果图片经过卷积之后的值, 大于这个门线我们就认为是边缘点)
dst1 = cv2.Canny(imgG1, 50, 50)
cv2.imshow("dst1", dst1)

# 示例二
img2 = cv2.imread('../../Picture/girl.png', 1)
img2Info = img2.shape
print("img.shape:", img2Info)  # 输出图片的[宽度, 高度, 图片的颜色组成方式]
cv2.imshow("img2", img2)
height2 = img2Info[0]
width2 = img2Info[1]

gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
imgG2 = cv2.GaussianBlur(gray2, (3, 3), 0)
dst2 = cv2.Canny(imgG2, 50, 50)
cv2.imshow("dst2", dst2)

# 示例三(源码形式)
import math

img3 = cv2.imread('../../Picture/sea.png', 1)
img3Info = img3.shape
height3 = img3Info[0]
width3 = img3Info[1]
cv2.imshow('src', img3)
# sobel 1 算子模版 2 图片卷积 3 阈值判决 
# [ 1  2  1          [ 1  0  -1
#   0  0  0            2  0  -2
#  -1 -2 -1 ]          1  0  -1 ]

# [1 2 3 4] [a b c d] a*1+b*2+c*3+d*4 = dst
# sqrt(a*a+b*b) = f>th
gray3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
dst3 = np.zeros((height3, width3, 1), np.uint8)
for i in range(0, height3 - 2):
    for j in range(0, width3 - 2):
        gy = gray3[i, j] * 1 + gray3[i, j + 1] * 2 + gray3[i, j + 2] * 1 - gray3[i + 2, j] * 1 - gray3[i + 2, j + 1] * 2 - \
             gray3[i + 2, j + 2] * 1
        gx = gray3[i, j] + gray3[i + 1, j] * 2 + gray3[i + 2, j] - gray3[i, j + 2] - gray3[i + 1, j + 2] * 2 - gray3[
            i + 2, j + 2]
        grad = math.sqrt(gx * gx + gy * gy)
        if grad > 50:
            dst3[i, j] = 255
        else:
            dst3[i, j] = 0
cv2.imshow('dst3', dst3)
cv2.waitKey(0)


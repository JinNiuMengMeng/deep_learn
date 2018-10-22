import numpy as np
import cv2

# 读图
img = cv2.imread('/home/ubuntu/PycharmProjects/tf_cv/pic/water.jpg', 1)

# 展示图
cv2.imshow('src', img)

# 获取图片信息
imgInfo = img.shape  # (170, 361, 3) 170*361矩阵 [宽度, 高度, 图片的颜色组成方式]
height = imgInfo[0]  # 矩阵的行数代表图片的高度
width = imgInfo[1]   # 矩阵的列数代表图片的宽度

# 设置一个偏移矩阵 两行三列数据  含义:沿着x轴向右移动了100，沿着y轴向下移动了0
matShift = np.float32([[1, 0, 100], [0, 1, 0]])  # 2*3

# 目标图片warpAffine，完成矩阵的映射。
# 参数1: 原图片 参数2: 移位矩阵 参数3: 当前图片的高宽
dst = cv2.warpAffine(img, matShift, (width, height))  # 1 data 2 matshift 3 info
cv2.imshow('dst', dst)


# 源码实现图片移位
dstt = np.zeros(imgInfo, np.uint8)
for i in range(0, height):
    for j in range(0, width - 100):
        dstt[i, j + 100] = img[i, j]
cv2.imshow("dstt", dstt)

print("img.shape:", img.shape)
print("dst.shape:", dst.shape)
print("dstt.shape:", dstt.shape)

cv2.waitKey(0)

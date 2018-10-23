import cv2
import numpy as np
import random

# random.random()  # 返回随机生成的一个实数，它在[0,1)范围内。
img = cv2.imread('../../Picture/girl.png', 1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
print("img.shape:", imgInfo)

dst = np.zeros(imgInfo, np.uint8)
# 设置毛玻璃的粗细
frosted_glass = 4

for i in range(0, height - frosted_glass):
    for j in range(0, width - frosted_glass):
        index = int(random.random() * frosted_glass)  # 产生[0-8]之间的随机数
        (b, g, r) = img[i + index, j + index]  # 获取随机数对应点的像素值
        dst[i, j] = (b, g, r)

cv2.imshow("dst", dst)
cv2.waitKey(0)

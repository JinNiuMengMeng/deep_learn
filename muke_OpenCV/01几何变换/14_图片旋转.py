import numpy as np
import cv2

img = cv2.imread('../../Picture/water.jpg', 1)
imgInfo = img.shape
print("img.shape:", imgInfo)  # 输出图片的[宽度, 高度, 图片的颜色组成方式]
cv2.imshow("img", img)
height = imgInfo[0]
width = imgInfo[1]
mode = imgInfo[2]

# 图像旋转getRotationMatrix2D()
# 第一个参数表示图片的中心点
# 第二个参数表示的度数
# 第三个参数表示缩放比例, 最大为1
for i in range(0, 360, 1):
    matRotate = cv2.getRotationMatrix2D((width / 2.0, height / 2.0), i, i / 360)
    dst = cv2.warpAffine(img, matRotate, (width, height))
    cv2.imshow("dst", dst)
    cv2.waitKey(10)

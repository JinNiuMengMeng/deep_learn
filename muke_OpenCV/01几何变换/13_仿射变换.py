import numpy as np
import cv2

img = cv2.imread('../../Picture/water.jpg', 1)
imgInfo = img.shape
print("img.shape:", imgInfo)  # 输出图片的[宽度, 高度, 图片的颜色组成方式]
cv2.imshow("img", img)
height = imgInfo[0]
width = imgInfo[1]
mode = imgInfo[2]

# src --> dst   (左上角, 左下角, 右上角)
matSrc = np.float32([[0, 0], [0, height - 1], [width - 1, 0]])  # 分别对应以上三个点
for i in range(0, 170):

    matDst = np.float32([[[0, 0], [i, height - i], [width - i, i]]])
    # 组合
    matAffine = cv2.getAffineTransform(matSrc, matDst)  # 将matSrc对应的三个点映射到matDst的三个点

    dst = cv2.warpAffine(img, matAffine, (width, height))
    cv2.imshow("dst", dst)
    cv2.waitKey(1)

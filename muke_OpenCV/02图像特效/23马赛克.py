import numpy as np
import cv2

img = cv2.imread('/home/ubuntu/PycharmProjects/tf_cv/pic/girl.png', 1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
print("img.shape:", imgInfo)

# 设置马赛克的粗细
Mosaic = 4

for i in range(400, 548, Mosaic):  # 绘制马赛克时会覆盖周围的10个像素, 所以步长设置为10, 减少不必要的循环
    for j in range(0, 300, Mosaic):
        if i % Mosaic == 0 and j % Mosaic == 0:  # 如果[i, j]这个点可以整除10, 接下来将10*10矩阵的每个像素设置为[i, j]这个点的像素值
            for m in range(0, Mosaic):
                for n in range(0, Mosaic):
                    (b, g, r) = img[i, j]
                    img[i + m, j + n] = (b, g, r)

cv2.imshow("img", img)
cv2.waitKey(0)

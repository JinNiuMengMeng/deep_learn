import cv2
import numpy as np

img = cv2.imread('../../Picture/water.jpg', 1)
imgInfo = img.shape
print("img.shape:", imgInfo)  # 输出图片的[宽度, 高度, 图片的颜色组成方式]
cv2.imshow("img", img)
height1 = imgInfo[0]
width1 = imgInfo[1]
mode = imgInfo[2]
# 放大 缩小 长与宽均乘以0.5 表示缩小一半
dstHeight1 = int(height1 * 0.5)
dstWidth1 = int(width1 * 0.5)

# openCV提供四种常见缩放方法: 1最近临域插值 2双线性插值 3像素关系重采样 4立方插值
# 参数一:需要缩放的图片  参数二: 生成的图片的宽度与长度
dst1 = cv2.resize(img, (dstWidth1, dstHeight1))
print("dst.shape:", dst1.shape)
cv2.imshow("dst1", dst1)

"""
最近临域插值法
src(10*20) --> dst(5*10)
x轴缩放比例=10/5 = 50%
y轴缩放比例=20/10 = 50%
src(x*y) --> dst(new_X*new_Y)
new_X = x * x轴缩放比例
new_Y = y * y轴缩放比例

双线性插值
A1 = 20%上 + 80%下
B1 = 30%左 + 70%右
"""
# 源码实现最近临域插值法
height2 = imgInfo[0]
width2 = imgInfo[1]
dstHeight2 = int(height2 / 2)
dstWidth2 = int(width2 / 2)
# 定义一个空矩阵; (dstHeight, dstWidth, 3)-->图片的长宽,3表示每个像素由三个基本颜色组成; np.uint8表示每个像素的基本类型
dstImage2 = np.zeros((dstHeight2, dstWidth2, 3), np.uint8)

for i in range(0, dstHeight2):  # 行
    for j in range(0, dstWidth2):  # 列
        ineww = int(i * (height2 * 1.0 / dstHeight2))
        jneww = int(j * (width2 * 1.0 / dstWidth2))
        dstImage2[i, j] = img[ineww, jneww]
cv2.imshow("dsImgg", dstImage2)
print("dstImagee:", dstImage2.shape)


# [[A1 A2 B1], [A3 A4 B2]]
# [[A1 A2], [A3, A4]] [[B1, B2]]
# newX = A1*x + A2*y + B1
# newY = A3*x + A4*y + B2
# x->x*0.5  y->y*0.5
# newX = 0.5*x

height3 = imgInfo[0]
width3 = imgInfo[1]
matScale = np.float32([[0.5, 0, 0], [0, 0.5, 0]])
dst3 = cv2.warpAffine(img, matScale, (int(width3/2), int(height3/2)))

cv2.imshow("dst3", dst3)

cv2.waitKey(0)
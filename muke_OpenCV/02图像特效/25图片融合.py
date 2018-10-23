import cv2
import numpy as np

img1 = cv2.imread('../../Picture/girl.png', 1)
imgInfo = img1.shape
height = imgInfo[0]
width = imgInfo[1]
print("img1.shape:", imgInfo)
img2 = cv2.imread("../../Picture/daimggirl.jpg", 1)
img2Info = img2.shape
print("img2.shape:", img2.shape)
# 将图片img2缩小一倍
img2New = cv2.resize(img2, (int(img2Info[1] / 2), int(img2Info[0] / 2)))
print("img2New.shape:", img2New.shape)

# ROI 截取感兴趣区域
roiH = height
roiW = width
img0ROI = img1[0:roiH, 0:roiW]
img1ROI = img2New[200:roiH + 200, 900:roiW + 900]
print("img0ROI.shape:", img0ROI.shape)
print("img1ROI.shape:", img1ROI.shape)

# 权重运算 dst = src1*a + scr2*(1-1)
# 第一个与第三个参数分别表示两张图片的data信息
# 第二与第四个参数表示权重系数, 两张图片融合后哪一个系数值大, 哪个图片越清晰
for i in np.arange(0, 1, 0.01): 
    # range不能生成float, 使用np.arange()方法;round(i, 2)保留i两位小数
    dst = cv2.addWeighted(img0ROI, round(i, 2), img1ROI, 1 - round(i, 2), 0)
    cv2.imshow("dst", dst)
    cv2.waitKey(50)

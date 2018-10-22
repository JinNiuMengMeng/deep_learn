import numpy as np
import cv2

img = cv2.imread("/home/ubuntu/PycharmProjects/tf_cv/pic/girl.png", 1)

# 方法一
img0 = cv2.imread("/home/ubuntu/PycharmProjects/tf_cv/pic/girl.png", 0)
cv2.imshow("img0", img0)
cv2.imshow("img1", img)
imgInfo0 = img0.shape
imgInfo = img.shape
print("img0.shape:", img0.shape)
print("img1.shape:", img.shape)

# 方法二
# 原始空间转换
# 第一个参数是原始图片的data数据
# 第二个参数是颜色转换的方式, cv2.COLOR_BGR2GRAY表示从BGR的模式转换为灰度GRAY的模式
dst = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("dst", dst)

# 方法三
# 灰度图像的特征R=G=B  -->  (b, g, r)=(R+G+B)/3
dst2 = np.zeros(imgInfo, np.uint8)
height = imgInfo[0]
width = imgInfo[1]
for i in range(height):
    for j in range(width):
        (b, g, r) = img[i, j]
        gray = (int(b) + int(g) + int(r)) / 3
        dst2[i, j] = np.uint8(gray)
cv2.imshow("dst2", dst2)

# 方法四
# 使用心理学计算公式 gray = r*0.299 + g*0.587 + b*0.114
dst3 = np.zeros(imgInfo, np.uint8)
for i in range(height):
    for j in range(width):
        (b, g, r) = img[i, j]
        gray = int(b) * 0.114 + int(g) * 0.587 + int(r) * 0.299
        dst3[i, j] = np.uint8(gray)
cv2.imshow("dst3", dst3)

# 方法五
# 使用移位方式优化算法
dst4 = np.zeros((height, width, 3), np.uint8)
for i in range(0, height):
    for j in range(0, width):
        (b, g, r) = img[i, j]
        b = int(b)
        g = int(g)
        r = int(r)
        # gray = (r+(g<<1)+b)>>2
        gray = (r + (g << 1) + b) >> 2
        dst4[i, j] = np.uint8(gray)
cv2.imshow("dst4", dst4)
cv2.waitKey(0)

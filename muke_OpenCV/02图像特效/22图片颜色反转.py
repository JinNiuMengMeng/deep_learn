import numpy as np
import cv2

img = cv2.imread('/home/ubuntu/PycharmProjects/tf_cv/pic/water.jpg', 1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
cv2.imshow("img", img)

# 灰度图片的颜色反转
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray, type(gray))
dst1 = np.zeros(imgInfo, np.uint8)
for i in range(height):
    for j in range(width):
        dst1[i, j] = 255 - gray[i, j]  # 255减去灰度图片每个像素的数据实现颜色反转
cv2.imshow("dst1", dst1)

# 彩色图片的颜色反转
dst2 = np.zeros(imgInfo, np.uint8)
for i in range(height):
    for j in range(width):
        (b, g, r) = img[i, j]  # 255减去每个像素的数据实现颜色反转
        dst2[i, j] = (255 - b, 255 - g, 255 - r)
cv2.imshow("dst2", dst2)
cv2.waitKey(0)

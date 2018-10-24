import cv2
import numpy as np

img = cv2.imread('../../Picture/sea.png', 1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
# 设置字体的类型
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.rectangle(img, (90, 310), (350, 260), (0, 255, 0), 1, cv2.LINE_AA)

# 文字
# 第一个参数图片的data数据
# 第二个参数文字的内容(不支持中文)
# 第三个参数文字起始位置
# 第四个参数文字的字体类型
# 第五个参数字体的大小
# 第六个参数字体的颜色
# 第七个参数字体的粗细
# 第八个参数线条的类型
cv2.putText(img, "This is big sea!", (100, 300), font, 1, (200, 100, 255), 2, cv2.LINE_AA)
cv2.imshow("src", img)

# 图片的装载
newHeight = int(imgInfo[0]*0.4)
newWidth = int(imgInfo[1]*0.4)
img2 = cv2.resize(img, (newWidth, newHeight))
for i in range(0, newHeight):
    for j in range(0, newWidth):
        img[i, j] = img2[i, j]

cv2.imshow("img2", img)
cv2.waitKey(0)
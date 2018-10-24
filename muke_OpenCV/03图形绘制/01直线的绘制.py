import numpy as np
import cv2

newImageInfo = (500, 500, 3)
dst = np.zeros(newImageInfo, np.uint8)

# 绘制线段
# 第一个参数: 图片data数据
# 第二个参数: 直线的起始点
# 第三个参数: 直线的终止点
# 第四个参数: 直线的颜色
# 第无个参数: 直线的粗细
# 第六个参数: 直线的type
cv2.line(dst, (100, 50), (400, 50), (0, 0, 255))
cv2.line(dst, (100, 80), (400, 80), (0, 255, 255), 20)
cv2.line(dst, (100, 110), (400, 110), (0, 255, 0), 20, cv2.LINE_AA)

# 绘制三角形
cv2.line(dst, (200, 150), (50, 250), (25, 100, 255), 20, cv2.LINE_AA)
cv2.line(dst, (50, 250), (400, 380), (25, 100, 255), 20, cv2.LINE_AA)
cv2.line(dst, (400, 380), (200, 150), (25, 100, 255), 20, cv2.LINE_AA)

cv2.imshow("dst", dst)
cv2.waitKey(0)
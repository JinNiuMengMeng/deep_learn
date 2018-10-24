import numpy as np
import cv2

newImageInfo = (500, 500, 3)
dst = np.zeros(newImageInfo, np.uint8)

# 绘制矩形
# 第一个参数图片的data数据
# 第二个参数矩形的左上角
# 第三个参数矩形的右下角
# 第四个参数矩形的颜色
# 第五个参数 -1:表示填充矩形, >0 表示矩形边框的粗细
# 第六个参数表示边框的样式
cv2.rectangle(dst, (100, 100), (300, 200), (0, 255, 255), 1, cv2.LINE_AA)

# 绘制圆
# 第一个参数图片的data数据
# 第二个参数圆的圆心
# 第三个参数圆的半径
# 第四个参数矩形的颜色
# 第五个参数 -1:表示填充矩形, >0 表示矩形边框的粗细
# 第六个参数表示边框的样式
cv2.circle(dst, (300, 200), (50), (0, 255, 0), 5, cv2.LINE_AA)

# 绘制椭圆
# 第一个参数图片的data数据
# 第二个参数椭圆的圆心
# 第三个参数椭圆的长轴与短轴
# 第四个参数椭圆的偏转角度
# 第五个参数椭圆的起始角度
# 第六个参数椭圆的终止角度
# 第七个参数椭圆的颜色
# 第八个参数 -1:表示填充矩形, >0 表示矩形边框的粗细
# 第九个参数表示边框的样式
cv2.ellipse(dst, (200, 100), (100, 50), 0, 0, 360, (255, 0, 0), 4, cv2.LINE_AA)

# 多边形绘制
points = np.array([[150, 50], [140, 140], [200, 170], [250, 250], [150, 50]], np.int32)
print(points.shape)
points = points.reshape((-1, 1, 2))  # 维度的转换
print(points.shape)
cv2.polylines(dst, [points], True, (0, 255, 255))

cv2.imshow("dst", dst)
cv2.waitKey(0)

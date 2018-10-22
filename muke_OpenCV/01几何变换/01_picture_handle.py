import cv2

# opencv
"""
图片的读取
1 文件的读取   2 封装格式解析    3 数据解码    4 数据加载
jpg   png    1 文件头   2 文件数据

img = cv2.imread("/home/ubuntu/PycharmProjects/tf_cv/pic/daimg.jpg", 1)
# 参数一:图片的路径
# 参数二:读取图片的类型, 0:表示灰度图片, 1:表示彩色图片
cv2.imshow("image", img)
# 参数一:窗体的名称
# 参数二:当前图片的内容
cv2.waitKey(0)  # 显示图片必须暂停一下, 不然看不到效果
print("done...")

# 图片的写入
img = cv2.imread("/home/ubuntu/PycharmProjects/tf_cv/pic/daimg.jpg", 1)
# 参数一:要写入的文件名
# 参数二:img为解码后的water.png图片数据, 原始数据
cv2.imwrite("/home/ubuntu/PycharmProjects/tf_cv/pic/daimg_copy.jpg", img)

# 图片压缩 - jpg   缺点: 1.有损压缩  2.无法设置透明度  优点: 压缩比高
img = cv2.imread("/home/ubuntu/PycharmProjects/tf_cv/pic/daimg.jpg", 1)
cv2.imwrite("/home/ubuntu/PycharmProjects/tf_cv/pic/daimg_copy.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 50])
# 第三个参数表示图片的质量, 有损压缩, 牺牲图片质量为代价, 范围是0-100, 数值越小, 图片大小越小, 失真度越高

# 图片压缩 - png   缺点: 压缩比底   优点: 1.无损压缩  2.可设置透明度
img = cv2.imread("/home/ubuntu/PycharmProjects/tf_cv/pic/daimg.jpg", 1)
cv2.imwrite("/home/ubuntu/PycharmProjects/tf_cv/pic/daimg_copy.png", img, [cv2.IMWRITE_PNG_COMPRESSION, 9])
# 第三个参数表示图片的质量, 范围是0-9, 数值越小, 压缩比越小, 图片越大
"""
# 图片像素操作
# 读取某个像素点的颜色值
img = cv2.imread("/home/ubuntu/PycharmProjects/tf_cv/pic/daimg.jpg", 1)
(b, g, r) = img[100, 100]
# 读取x, y轴坐标为(100, 100)像素点的颜色值, 返回值为bgr格式
# 注意不是RGB格式
print(b, g, r)

# 在图片中绘制一条直线, 从坐标为[10, 100] -- [110, 100]
for i in range(1, 100):
    img[10 + i, 100] = (255, 0, 0)  # 同样是bgr形式
cv2.imshow("image", img)  # 可观察到图片左上角出现一条蓝色直线
cv2.waitKey(1000)  # 1000ms之后程序会自动向下执行

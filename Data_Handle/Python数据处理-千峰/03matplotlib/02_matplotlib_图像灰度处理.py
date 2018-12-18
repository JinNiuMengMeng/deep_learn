# 图片灰度处理
from scipy import misc
import matplotlib.pyplot as plt
import numpy as np

face_g = misc.face(gray=True)  # 获取一张灰色的图片
plt.imshow(face_g, cmap="gray")

im_data = plt.imread("../../Picture/sea.png")
plt.imshow(im_data)
# plt.show()

# 图片灰度处理 方法一: 使用最大值法
print(im_data[0, 0])
im_data1 = im_data.max(axis=2)
plt.imshow(im_data1, cmap="gray")
# plt.show()

# 图片灰度处理 方法二: 求平均值
im_data2 = im_data.mean(axis=-1)
plt.imshow(im_data2, cmap="gray")
# plt.show()

# 加权平均值法  [0.299, 0.587, 0.114] --> r*0.299 + g*0.587 + b*0.114
a = np.array([0.299, 0.587, 0.114])
img_data3 = np.dot(im_data, a)
plt.imshow(img_data3, cmap="gray")
plt.show()
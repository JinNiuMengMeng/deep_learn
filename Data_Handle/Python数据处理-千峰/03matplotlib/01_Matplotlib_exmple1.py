# coding:utf-8
import matplotlib.pyplot as plt

fish = plt.imread('../../Picture/girl.png')
plt.imshow(fish)
plt.show()

fish1 = fish[::-1]  # 图片x轴镜像
plt.imshow(fish1)
plt.show()

fish2 = fish[::-1, ::-1]  # 图片x轴镜像之后, 再y轴镜像
plt.imshow(fish2)
plt.show()

fish4 = fish[::, ::, ::-1]  # 改变颜色
fish5 = fish[::5, ::5]  # xy两个方向每隔五个数取出一个数字(图像变模糊)
plt.imshow(fish5)
plt.show()
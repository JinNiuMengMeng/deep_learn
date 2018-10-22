# coding:utf-8
import matplotlib.pyplot as plt

fish = plt.imread('/home/ubuntu/Pictures/images.png')
fish1 = fish[::-1]  # 图片旋转180
fish2 = fish[::-1, ::-1]  # 图片反转360
fish3 = fish[::, ::, ::-1]  # 改变颜色
fish4 = fish[::5]  # 隔五个数取出一个数字
plt.imshow(fish4)
plt.show()

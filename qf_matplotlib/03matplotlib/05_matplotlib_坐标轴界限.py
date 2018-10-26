import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 9))

ax = plt.subplot(2, 3, 1)
# axis 方法, tight(默认), off, equal
# axis square/将当前坐标系图形设置为方形。横轴及纵轴比例是1：1
# axis equal/将横轴纵轴的定标系数设成相同值。
# 如果axis方法没有人和参数, 则返回当前坐标轴的上下限, axis(xmin=, ymax=)
x1 = np.random.rand(10)
# [xmin, xmax, ymin, ymax]
ax.plot(x1)
ax.axis([-5, 15, -5, 10])
ax.axis("off")  # 关闭坐标轴

ax2 = plt.subplot(2, 3, 2)
x2 = np.linspace(-np.pi, np.pi, 100)
ax2.plot(np.sin(x2), np.cos(x2))
ax2.axis("equal")  # 将横轴纵轴的定标系数设成相同值
ax2.axis("off")  # 关闭坐标轴

# xlim方法与ylim方法
ax4 = plt.subplot(2, 3, 3)
y = np.arange(0, 10, 1)
ax4.plot(y)
plt.ylim(2, 10)  # 从2开始到10结束
plt.xlim(4, 8)  # 从4开始到8结束

# 坐标轴标签
# xlabel方法和ylable方法
ax4 = plt.subplot(2, 3, 4)
x = np.arange(-5, 5, 0.1)
y = x ** 2 + 5
ax4.plot(x, y)

# horizontalalignment值: 'center', 'right', 'left'
plt.ylabel("f(x) = x**2 + 5", horizontalalignment="left")
# verticalalignment值: 'top', 'bottom', 'center', 'baseline', 'center_baseline'
# rotation表示倾斜角度
plt.xlabel("this is x", size=10, rotation=0, verticalalignment="top")
plt.show()


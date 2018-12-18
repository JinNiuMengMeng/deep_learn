import numpy as np
import matplotlib.pyplot as plt

# 图片标题
x1 = np.linspace(-np.pi, np.pi, 100)
plt.plot(x1, np.sin(x1))
# loc值: 'center', 'right', 'left'
plt.title("f(x) = sin(x)", fontsize=20, loc="right")
plt.show()

# 图例  legend方法
# 两种传参方法:
# 1. 在plot函数中增加label参数(推荐)
# 2. 在legend方法中传入字符串列表

# 方法一
ax3 = plt.subplot(1, 3, 2)
x3 = np.arange(0, 10, 1)
ax3.plot(x3, x3, label="normal")
ax3.plot(x3, x3 ** 2, label="_fast")  # label添加下划线_, 被隐藏
ax3.plot(x3, x3 / 2, label="slow")
# loc 位置值
# 'best': 0,
# 'upper right': 1,
# 'upper left': 2,
# 'lower left': 3,
# 'lower right': 4,
# 'right': 5,
# 'center left': 6,
# 'center right': 7,
# 'lower center': 8,
# 'upper center': 9,
# 'center': 10,

# ax3.legend(loc="right")
# ax3.legend(loc=(-0.2, 1))
# ax3.legend(loc=(0.5, 1))
ax3.legend(loc=(1, 0))

# 方法二
ax2 = plt.subplot(1, 3, 1)
x2 = np.arange(0, 10, 1)
ax2.plot(x2, x2, x2, x2 * 2, x2, x2 / 2)
ax2.legend(["normal", "fast", "slow"])
plt.show()

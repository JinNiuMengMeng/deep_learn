import numpy as np
import matplotlib.pyplot as plt

# plt面向对象
# 创建, 图形就是所谓的对象
# 设置整张图片的大小
plt.figure(figsize=(12, 9))
# 设置整张图片的图片名字
# plt.suptitle('Picture', fontsize='large', fontweight='bold')

# 参数一表示第几行, m
# 参数二表示第几行有几列, n
# 该图片在m*n个中哪个位置显示
axes1 = plt.subplot(2, 3, 1)
x1 = np.arange(-10, 10, 0.1)
axes1.grid(color="r", linestyle="-.", linewidth=2)
axes1.set_title('sin', fontsize='large', fontweight='bold')  # 设置图片1字体大小与格式
axes1.plot(x1, np.sin(x1))

axes2 = plt.subplot(2, 3, 2)
x2 = np.arange(-10, 10, 0.1)
axes2.grid(color="g", linestyle="--", linewidth=1)
axes2.set_title('cos', fontsize='large', fontweight='bold')  # 设置图片2字体大小与格式
axes2.plot(x2, np.cos(x2))

axes3 = plt.subplot(2, 3, 3)
x3 = np.arange(-10, 10, 0.1)
axes3.grid(color="b", linestyle="-.", linewidth=1)
axes3.set_title('y = x ** 2', fontsize='large', fontweight='bold')  # 设置图片1字体大小与格式
axes3.plot(x3, x3 ** 2)

axes4 = plt.subplot(2, 3, 5)
x4 = np.arange(-10, 10, 0.1)
axes4.grid(color="gray", linestyle="-.", linewidth=1)
axes4.set_title('y = 4x + 1', fontsize='large', fontweight='bold')  # 设置图片1字体大小与格式
axes4.plot(x4, 4 * x4 + 1)
plt.show()

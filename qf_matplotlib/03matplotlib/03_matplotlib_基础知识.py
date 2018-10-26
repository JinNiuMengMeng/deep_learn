import numpy as np
import matplotlib.pyplot as plt

"""
matplotlib 中的基本图表包括的元素

1. x轴和y轴: 水平和垂直的轴线
2. x轴和y轴的刻度: 刻度表示坐标轴的分隔, 包括最小刻度和最大刻度
3. x轴和y轴的标签: 表示特定坐标轴的值
4. 绘图区域: 实际绘图的区域
"""
# 可以使用多个plot函数, 在一个图中绘制多个曲线(推荐)
x = np.linspace(1, 10, 10)
plt.plot(x)
plt.plot(x, x ** 2)
plt.show()

# 也可以在一个plot函数中传入多对x, y值, 在一个图中绘制多个曲线
x = np.arange(0, 10, 1)
plt.plot(x, x ** 2, x, 5 * x, x, x / 3)
plt.grid(True)  # 添加网格线
plt.show()

# 绘制正弦曲线
# lw代表linewidth, 线的粗细
# alpha表示线的明暗程度(0-1)
# color表示线的颜色
x = np.arange(-np.pi, np.pi, 0.01)
plt.plot(x, np.sin(x), x, np.cos(x), lw=10, alpha=0.5, color="blue")
plt.grid(True)
plt.show()
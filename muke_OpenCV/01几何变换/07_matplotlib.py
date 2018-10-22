import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([3, 5, 7, 6, 2, 6, 10, 15])
plt.plot(x, y, 'b')  # 折线图(x轴坐标, y轴坐标, 颜色)
plt.plot(x, y, 'g', lw=10)  # 指的是line width线条宽度

# 第一第二个参数分别为x轴y轴坐标
# 第三个参数width是柱状图的宽度比例
# 第四个参数alpha表示图表的透明度
# 第五个color是图表颜色
plt.bar(x, y, width=1, alpha=1, color="b")
plt.show()
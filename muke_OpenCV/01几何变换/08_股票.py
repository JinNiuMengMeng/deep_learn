import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

data = np.linspace(1, 15, 15)

endPrice = np.array(
    [2511.90, 2538.26, 2510.68, 2591.66, 2732.98, 2701.69, 2701.29, 2678.67, 2726.50, 2681.50, 2739.17, 2715.07,
     2823.58, 2864.90, 2919.08])
beginPrice = np.array(
    [2438.71, 2500.88, 2534.95, 2512.52, 2594.04, 2743.26, 2697.47, 2695.24, 2678.23, 2722.13, 2674.93, 2744.13,
     2717.46, 2832.73, 2877.40])

highestPrice = np.array(
    [2551.90, 2588.26, 2550.68, 2699.66, 2752.98, 2799.69, 2741.29, 2698.67, 2786.50, 2691.50, 2789.17, 2755.07,
     2843.58, 2884.90, 2999.08])
lowestPrice = np.array(
    [2420.71, 2480.88, 2500.95, 2488.52, 2566.04, 2600.26, 2677.47, 2665.24, 2648.23, 2712.13, 2644.93, 2714.13,
     2707.46, 2802.73, 2870.40])


for i in range(15):  # 每一天有四个点(1, 最高点)(1, 最低点)(1, 收盘价)(1, 开盘价)
    dateOne = np.ones([2])
    priceOne = np.ones([2])
    shadowOne = np.ones([2])
    dateOne[0] = i
    dateOne[1] = i
    priceOne[0] = beginPrice[i]
    priceOne[1] = endPrice[i]
    shadowOne[0] = highestPrice[i]
    shadowOne[1] = lowestPrice[i]
    if beginPrice[i] > endPrice[i]:  # 开始大于结束, 绿色
        plt.plot(dateOne, priceOne, 'g', lw=10)
        plt.plot(dateOne, shadowOne, 'g', lw=2)
    else:
        plt.plot(dateOne, priceOne, 'r', lw=10)
        plt.plot(dateOne, shadowOne, 'r', lw=2)
plt.show()

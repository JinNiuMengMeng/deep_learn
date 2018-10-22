# coding:utf-8
from matplotlib.pyplot import *

x = [1, 2, 3, 4]
y = [5, 4, 3, 2]

figure()  # 调用该方法创建出新的图表

'''
接下来，调用subplot(231)方法把图表分割成2x3的网格。
也可以用subplot(3,2,1)这种形式来调用，其中第一个参数是行数，第二个参数是列数，第三个参数表示图形的标号。
'''
subplot(231)
plot(x, y)

subplot(232)
bar(x, y)   # 垂直柱状图

subplot(233)
barh(x, y)  # 水平柱状图

subplot(234)
bar(x, y)
y1 = [7, 8, 5, 3]
bar(x, y1, bottom=y, color='r')  # 堆叠柱状图

subplot(235)
boxplot(x)  # 箱线图

subplot(236)
scatter(x, y)

show()

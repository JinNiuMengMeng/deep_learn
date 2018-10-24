# coding:utf-8

import numpy as np

n = np.random.randint(0, 10, size=(4, 5))  # 产生4行5列， 0到10之间的数据(<type 'numpy.ndarray'>)

n2 = n + 10  # 所有的数据都加10， 原数据n不变。 （加减乘除结果类似）

n3 = np.add(n, n2)  # 将两个ndarray相对应的数据一一相加， n2也可以是一个数字

a1 = np.random.randint(0, 10, size=(2, 3))  # a1矩阵有两行， 与它相乘的a2必须有两列
a2 = np.random.randint(0, 10, size=(3, 2))
print(np.dot(a1, a2))  # 矩阵积（乘法）

'''
广播机制（重要）
ndarray广播机制的两条规则
1. 为缺失的维度补1
2. 假定缺失元素用已有值填充
'''
b1 = np.ones((2, 3))
b2 = np.arange(3)
print('b1 + b2:', b1 + b2)  # b1 有两行三列， b2 只有一行， 维度不对应， 自动补全b2

b3 = np.arange(3).reshape((3, 1))  # np.arange(3)生成的数据是一行三列， 使用reshape方法将该列数据转换为一列三行
b4 = np.arange(3)
print('b3 + b4:', b3 + b4)  # 自动将b3与b4补全为三行三列数据

b5 = np.ones((4, 1))
b6 = np.arange(4)
print('b5 + b6:', b5 + b6)

import numpy as np

data1 = np.array([1, 2, 3, 4, 5])
print(data1, type(data1))
print('---' * 10)
data2 = np.array([[1, 2], [3, 4]])
print(data2, type(data2))
print('---' * 10)
# 维度
print(data1.shape, data2.shape)
print('---' * 10)
# zero空矩阵 , ones单位矩阵
print(np.zeros([2, 3]))
print('---' * 10)
print(np.ones([2, 2]))
print('---' * 10)
# 改查
data2[1, 0] = 5
print(data2[1, 0])
print('---' * 10)
print(data2[1, 1])
print('---' * 10)
# 基本运算
data3 = np.ones([2, 3])
print(data3 * 2)  # 对应相乘
print('---' * 10)
print(data3 / 3)
print('---' * 10)
print(data3 + 2)
print('---' * 10)
# 矩阵的 + *
data4 = np.array([[1, 2, 3], [4, 5, 6]])
print(data3 + data4)
print('---' * 10)
print(data3 * data4)
print('---' * 10)

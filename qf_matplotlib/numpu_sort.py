# coding:utf-8
import numpy as np

n1 = np.array([1, 3, 5, 6, 2, 0])
n11 = np.sort(n1)  # 将排序后的n1返回， 不改变原数据n1
n2 = np.random.randint(0, 150, size=10)
n22 = np.sort(n2)
print '原数据 n1:', n1  # n1: [1 3 5 6 2 0]
print '排序后 n11:', n11  # n11: [0 1 2 3 5 6]
print '原数据 n2:', n2  # n2: [ 30 100  63  56  44  18 110 134  72  73]
print '排序后 n22:', n22  # [ 18  30  44  56  63  72  73 100 110 134]

n3 = np.array([1, 3, 5, 6, 2, 0])
np.ndarray.sort(n3)  # 没有返回值， 直接改变原数据
n4 = np.random.randint(0, 150, size=10)
np.ndarray.sort(n4)
print '原数据 n3:', n3  # n1: [1 3 5 6 2 0]
print '原数据 n4:', n4  # n2: [ 30 100  63  56  44  18 110 134  72  73]

n5 = np.random.randint(0, 150, size=15)
n55 = np.partition(n5, -5)  # 将最大的五个数字放到末尾(五个数字排列没有大小顺序)
n555 = np.partition(n5, 5)  # 将最小的五个数字放到前面(五个数字排列没有大小顺序)
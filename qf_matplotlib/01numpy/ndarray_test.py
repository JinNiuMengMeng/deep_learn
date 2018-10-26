# coding:utf-8
import numpy as np

n1 = np.array([2, 5, 6, 1, 3])


def sorth(nd):  # 冒泡排序
    for i in range(n1.size):
        for j in range(i, n1.size):
            if nd[i] > nd[j]:
                nd[i], nd[j] = nd[j], nd[i]
    return nd


def sortnd(nd):  # 冒泡排序优化版
    '''
    for循环nd[i:]切片得到被逐步分割的array列表
    [2 5 6 1 3]
    [5 6 2 3]
    [6 5 3]
    [5 6]
    [6]
    使用np.argmin（）方法求出对应列表的最小值的索引
    '''
    for i in range(nd.size):
        min_index = np.argmin(nd[i:]) + i
        nd[i], nd[min_index] = nd[min_index], nd[i]
    return nd


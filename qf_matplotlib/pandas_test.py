# coding:utf-8
import pandas
from pandas import Series, DataFrame
import numpy as np
import matplotlib.pyplot as plt

nd = np.array([1, 4, 5, 2, 4, 7])

s = Series(nd)
print type(s)
print s
s.index = list('abcdef')
print s
s2 = Series(nd, index=['张三', '李四', '王二', '哈哈', '微信', 'qq', ])
print s2

s3 = Series({'语文': 150, '数学': 150, '英语': 150, '理综': 300})
print s3
print '** ' * 20

ss = Series(np.random.random(10), index=list('abcdefghig'))
# 显示索引
print ss['a']
print ss[0]
print ss.loc['a']
# 隐式索引, 直接使用数字
print ss.iloc[0]
# 切片
print ss[0:3]
print ss.loc['a':'c']

print '** ' * 20
print s
print s.shape
print s.size
print s.index
print type(s.values)

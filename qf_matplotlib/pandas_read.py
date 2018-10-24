# coding:utf-8
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import numpy as np

csv_con = pd.read_csv('/home/ubuntu/Videos/alipay_return.csv')
subject = csv_con['subject']
print(type(csv_con))
print(subject)
print(type(subject))

s = Series([1, 26, None, np.nan], index=list('abcd'))
print(s)
print(type(None))
print(type(np.nan))

print(s.sum())
# # 如果s是ndarray类型，则没有这个属性
# ss = np.array([1, 2, 3])
# print(ss.sum()  )  # 正确
# sss = np.array([1, 2, 3, None, np.nan])
# print(sss.sum()  )  # 报错

# 可以使用pd.isnull(), pd.notnull(), 或自带isnull(), notnull()函数检测缺失数据
s_isnull = s.isnull()
s_notnull = s.notnull()
print(s[s_notnull])
print(s[s_isnull])
# Series对象本身及其实例都有一个name属性
print(s)
s.name = '哈哈哈'
print(s)
s1 = s.add(10, fill_value=10)
print(s1)

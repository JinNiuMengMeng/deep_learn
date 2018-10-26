# coding:utf-8
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import numpy as np

# sheetname:默认是sheetname为0,返回多表使用sheetname=[0,1],
# 若sheetname=None是返回全表.
# 注意:int/string返回的是dataframe,而none和list返回的是dict of dataframe.

csv_con = pd.read_excel('student_table_2.xls', sheet_name="2012级")
print(csv_con.index, csv_con.columns)
# print(csv_con["民族"][0])
csv_con.index = csv_con["姓名"]  # 改变列index
print(csv_con.index, csv_con.columns)
print(csv_con["家庭住址省内从市（县)写起"])

"""
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
"""

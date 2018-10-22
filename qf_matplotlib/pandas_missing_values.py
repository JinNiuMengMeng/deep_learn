# coding:utf-8
import numpy as np
from pandas import Series, DataFrame
import pandas as pd

# import time
# start = time.time()
# num = np.arange(0, 10000, dtype=float).sum()
# print num
# print time.time() - start

df = DataFrame(data={'age': np.random.randint(19, 24, size=5),
                     'salary': np.random.randint(10000, 20000, size=5)},
               index=['小赵', '张三', '李四', '王五', '老刘'],
               columns=['age', 'salary', 'work'])
print df
df.work['张三': '王五'] = 'Python'
print df.isnull()
print df.notnull()
# 根据获得的数据去除原来数据的空数据
# axis=1  index
# axis=0  columns
print df.isnull().any()  # any()方法只要一个是True就返回True(age与salary中全是False因此返回的都是False，work是True证明work中有NaN数据)
print df.notnull().any()
s1 = df.isnull().any(axis=1)  # 找出存在True的那列数据
print s1
print df[s1]  # 获取哪些数据为空
s3 = df.notnull().all(axis=1)  # all()方法只有全是True才返回True
print s3
print df[s3]

print '** ' * 10

print 'df:'
print df
print 'df.dropna(axis=1):'
print df.dropna(axis=1)

print "df.dropna(how='all'):"  # 如果数据某一行全部为空， 则过滤掉
print df.dropna(how='all')
df.loc['小赵'] = np.NaN
print 'df:'
print df
print "df.dropna(how='all'):"  # 小赵的数据被过滤掉
print df.dropna(how='all')

print 'df:'
print df
print "df.fillna(value='java'):"  # 并没有改变原数据
print df.fillna(value='java', inplace=False)  # inplace改为True,会改变原数据
print 'df:'
print df

print "df.fillna(method='backfill'):"
print df.fillna(method='backfill')
print "df.fillna(method='ffill'):"
print df.fillna(method='ffill')

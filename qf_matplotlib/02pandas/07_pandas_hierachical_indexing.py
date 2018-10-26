# coding:utf-8
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# 对DataFrame行， 多层索引
s = Series([1, 2, 3, 4], index=[['a', 'a', 'b', 'b'], ['期中', '期末', '期中', '期末']])
print(s)

df = DataFrame(np.random.randint(0, 150, size=(6, 3)), columns=['语文', '数学', 'python'],
               index=[['Micheal', 'Micheal', 'Lisa', 'Lisa', 'Po', 'Po'], ['Mid', 'End', 'Mid', 'End', 'Mid', 'End']])
print(df)

# 显示构造pd.multolndex
# 使用数组
df1 = DataFrame(np.random.randint(0, 150, size=(6, 3)), columns=['java', 'html5', 'python'],
                index=pd.MultiIndex.from_arrays(
                    [['张三', '张三', '侯少', '侯少', '温少', '温少'], ['期中', '期末', '期中', '期末', '期中', '期末']]))
print(df1)
# 使用tuple
df2 = DataFrame(np.random.randint(0, 150, size=(6, 3)), columns=['java', 'html5', 'python'],
                index=pd.MultiIndex.from_tuples(
                    tuples=(('张三', '期中'), ('张三', '期末'), ('侯少', '期中'), ('侯少', '期末'), ('温少', '期中'), ('温少', '期末'))))
print(df2)
# 使用product， 最简单， 推荐使用
df3 = DataFrame(np.random.randint(0, 150, size=(6, 3)), columns=['java', 'html5', 'python'],
                index=pd.MultiIndex.from_product(iterables=(['张三', '侯少', '温少'], ['期末', '期中'])))
print(df3)

# 对DataFrame列， 多层索引
df4 = DataFrame(np.random.randint(0, 150, size=(3, 6)), index=['张三', '侯少', '温少'],
                columns=pd.MultiIndex.from_product(iterables=(['java', 'html5', 'python'], ['期末', '期中'])))
print(df4)

print(s)
# s索引
# 第一个参数：多层索引的第一维， 第二个参数：多层索引的第二维
print(s['a', '期中'])
print(s[['a', '期中']])
# 切片
print(s['a':'b'])
print(s.iloc[0:3])

print(df4)
print(df4.stack())  # 对于多层索引的列而言0, 1, 2：从上往下计数.没人level==-1
print(df4.stack(level=0))
print(df4.stack(level=1))
print(df4.stack(level=-1))

print(df2)
print(df2.sum())  # 默认axis=0/行
print(df2.sum(axis=1))
print(df2.max())  # 每一个科目的最大值
print(df2.std(axis=1))  # 求方差

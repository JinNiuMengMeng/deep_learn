# coding:utf-8
import pandas as pd
from pandas import Series, DataFrame
import numpy as np
from pprint import pprint

# csv_con = pd.read_csv("/home/ubuntu/Videos/alipay_return.csv")
# print(csv_con.index)  
# print(csv_con.columns)  
# print(csv_con.values)  
# print(csv_con.values.shape)  
"""
df = DataFrame(data={"height": np.random.randint(165, 190, size=5), "weight(KG)": np.random.randint(40, 65, size=5),
                     "age": np.random.randint(17, 22, size=5), "sex": ["male", "female", "female", "male", "male"]},
               index=list("ABCDE"),
               columns=["height", "weight(KG)", "age", "sex", "class"])
print(df)  

'''
对于dataframe， 列名就相当于属性
Dataframe 是统计数据时用的表格， 是某一个事物的属性， 它的每一个属性对应Dataframe中的列名
'''

print(df.age, type(df.age)  )  # 直接用实例引用方法的方式
print(df.loc['A'])  
print(type(df.loc['A']))  

print(df.loc[['A', 'B']])  
print(type(df.loc[['A', 'B']]))  

print(df.loc['A':'C'])  
print(type(df.loc['A':'C']))  

print(df.loc['C']['height'])  
print(df.loc['C', 'height'])  
"""
# DataFrame与DataFrame之间的运算
df_1 = DataFrame(np.random.randint(0, 150, size=(4, 4)), index=['张三', '李四', '王五', '老刘'],
                 columns=['数学', '语文', '英语', 'python'])
df_2 = DataFrame(np.random.randint(0, 150, size=(5, 4)), index=['张三', '李四', '王五', '老刘', '小张'],
                 columns=['数学', '语文', '英语', 'python'])
print(df_1)  
print(df_2)  

# 当行索引存在差异时相加
print(df_1.add(df_2, fill_value=0))  

# 当列索引存在差异时相加
df_4 = DataFrame(np.random.randint(0, 150, size=(5, 3)), index=['张三', '李四', '王五', '老刘', '小赵'],
                 columns=['数学', '英语', 'python'])
print(df_4)  
print(df_1.add(df_4))  
df_5 = df_1.add(df_4, fill_value=0)
df_5['语文'].loc['小赵'] = 100
print(df_5)  

# DataFrame与Series之间的运算
# 两个数据相加时， 先看列索引是否相同， 列索引相同的部分相加减， 不同的地方为NaN
print('** ' * 20)  
s1 = df_5['python']  # 或者df_5.python(因为python是列， 列是属性)
s2 = df_5.loc['小赵']
print(s1.index)  
print(df_5.columns)  
print(s2.index)  

print(df_5.add(s1)  )  # 因为列索引不同， 所以数据全部为NaN
print(df_5.add(s2)  )  # 因为列索引相同， 因此正常相加减， s2只有一个， 因此相加减时执行了广播模式
print(df_5.add(s1, axis='index'))  

dff = DataFrame(data={'python': [98, 227, 133, 128, 138], '数学': [11.0, 111.0, 137.0, 190.0, 141.0],
                      '英语': [68.0, 221.0, 125.0, 151.0, 189.0], '语文': [100, 25, 149, 35, 132]},
                index=['小赵', '张三', '李四', '王五', '老刘'], columns=['python', '数学', '英语', '语文'])
s1 = dff['python']
print(s1)  
print(dff.add(s1, axis='index'))  
dff2 = DataFrame(data={'python': [98, 227, 133, 128, 138, 100], '数学': [11.0, 111.0, 137.0, 190.0, 141.0, 100.0],
                       '英语': [68.0, 221.0, 125.0, 151.0, 189.0, 100.0], '语文': [100, 25, 149, 35, 132, 100]},
                 index=['小赵', '张三', '李四', '王五', '老刘', 'new'], columns=['python', '数学', '英语', '语文'])
print(dff2)  
print(dff.add(dff2, fill_value=0) / 2)  

# coding:utf-8
import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# 生成2个3*3的矩阵， 对其分别进行两个维度上的级联

# nd = np.random.randint(0, 10, size=(3, 3))
# print(nd)  
# print(np.concatenate((nd, nd), axis=0)  )  # 0是第一维的方向 行
# print(np.concatenate((nd, nd), axis=1))  

# 1 级联
def make_df(cols, indx):
    dat = {c: [c + str(i) for i in indx] for c in cols}
    return DataFrame(data=dat, columns=cols, index=indx)


df1 = make_df(cols=['A', 'B'], indx=[0, 1])
df2 = make_df(cols=['A', 'B'], indx=[2, 3])
# 可以通过设置axis来改变级联的方向
print(pd.concat((df1, df2), axis=0))
print(pd.concat((df1, df2), axis=1))
# 注意index在级联时可以重复
df3 = make_df(cols=['A', 'B'], indx=[0, 1, 2])
df4 = make_df(cols=['A', 'B'], indx=[1, 2, 3])
print(pd.concat((df3, df4), axis=0))
print(pd.concat((df3, df4), axis=1))
# 也可以选择忽略ignore_index, 重新索引
print(pd.concat((df3, df4), ignore_index=True))
# 或者使用多层索引, keys可以使合并之后的数据更加清晰
df5 = make_df(cols=['X', 'Y'], indx=['a', 'b'])
df6 = make_df(cols=['X', 'Y'], indx=['A', 'B'])
print(pd.concat((df5, df6), keys=['X', 'Y']))
# 2 不匹配级联
# 不匹配级联指的是级联的维度的索引不一致。例如纵向级联时列索引不一致， 横向级联时行索引不一致
# 有三种连接方式：
# 外连接： 补NaN（默认方式）
# 内连接： 只连接匹配的项
# 连接指定轴join_axes

# 外连接
dff1 = make_df(cols=list('AB'), indx=[1, 3])
dff2 = make_df(cols=list('BC'), indx=[2, 4])
print(pd.concat((dff1, dff2)))

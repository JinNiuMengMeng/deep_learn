import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

apple = pd.read_csv("aapl.csv")
print(apple.dtypes)  # 可以看到Data是object类型
# pd.to_datetime() 可以将object类型转换为时间类型
apple["Date"] = pd.to_datetime(apple["Date"])

apple.set_index("Date", inplace=True)  # inplace在原表上做修改, 将列索引改成Date
# print(apple.index, apple.columns)
plot = apple["Adj Close"].plot(title="Adj close")
pic = plot.get_figure()
pic.set_size_inches(15, 12)
plt.show()



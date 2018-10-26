import numpy as np

np1 = np.random.randint(1, 9, (2, 4, 1))
print(np1, type(np1))

np3 = np.array([[[1, 2, 13], [3, 4, 14]], [[5, 6, 15], [7, 8, 16]], [[9, 10, 17], [11, 12, 18]]])
print(np3, type(np3), np3.shape)
print(np3[2, 1, -2])
print('-----------')
print(np3[0:2])
print('-----------')
print(np3[0:2, 0:1])
print('-----------')
print(np3[0:2, 0:1, -2:])

print('-----------')
np4 = np.arange(0, 10, 1)
print(np4[::2])  # 取值, 末尾数字表示步长

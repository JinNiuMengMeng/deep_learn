# coding:utf-8
import numpy as np
from numpy.fft import fft, ifft
from PIL import Image

cat = Image.open('../../Picture/sea.png')
# cat.show()


cat_data = np.fromstring(string=cat.tobytes(), dtype=np.int8)  # 转换成int类型， int8==128
print(cat_data)  # 结果中含有负数， 因为int8<125，颜色值0~255. 超过125的那部分数据用负数表示

# 傅里叶转换，傅里叶转换的结果包含实数和虚数
cat_data_fft = fft(cat_data)  # 将真实的数据转换成频域
print(cat_data_fft, type(cat_data_fft))

# 将傅里叶的数据去除低频的波， 设置为0
np.where(np.abs(cat_data_fft) < 1e5, 0, cat_data_fft)  # 将小于1e5的数据设置为0
cat_data_fft[np.where(np.abs(cat_data_fft) < 1e5)] = 0  # 同上面方法得到同样的结果

cat_data_ifft = ifft(cat_data_fft)  # 使用傅里叶进行数据反转
print(cat_data_ifft)

cat_data_real = np.real(cat_data_ifft)  # 获取实数
cat_data_result = np.int8(cat_data_real)  # 去除小数部分
cat_image = Image.frombytes(data=cat_data_result, size=cat.size, mode=cat.mode)  # 将一维数组，通过Image转换成图片数据

cat_image.show()  # 显示图片

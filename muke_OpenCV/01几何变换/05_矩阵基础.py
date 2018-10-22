import os
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

"""
M行N列 []
[[列1数据], [列2数据], [列3数据]] 中括号的整体是行数
[[1, 2], [3, 4], [5, 6]]  3行2列数据
[[1], [2], [3]]           3行1列
[[1, 2, 3]]               1行3列
"""
# 矩阵的索引
data1 = tf.constant([[1, 2], [3, 4], [5, 6]])
data2 = tf.constant([[1, 2, 3]])

with tf.Session() as sess:
    # print(sess.run(data1))  # 输出矩阵data1
    # print('--' * 20)
    # print(sess.run(data2))  # 输出矩阵data2
    # print('--' * 20)
    print(sess.run(data1[0]))  # 输出矩阵data1第一行
    print('--' * 20)
    print(sess.run(data1[0][1]))  # 输出data1第一行第二个元素
    print('--' * 20)
    print(sess.run(data1[:, 0]))  # 输出矩阵data1第一列
    print(sess.run(data1[:, 1]))  # 输出矩阵data1第二列

# 矩阵的四则运算
data3 = tf.constant([[6, 6]])
data4 = tf.constant([[2],
                     [2]])
data5 = tf.constant([[3, 3]])
data6 = tf.constant([[1, 2],
                     [3, 4],
                     [5, 6]])
data7 = tf.constant([[4, 5, 6],
                     [1, 4, 6]])
data8 = tf.constant([[1, 2, 3, 4],
                     [5, 6, 7, 8]])

matMul_1 = tf.matmul(data3, data4)  # [1, 2] * [2, 1] --> [1, 1]
Add = tf.add(data3, data5)  # [1, 2] + [1, 2] --> [1, 2]
matMul_2 = tf.matmul(data7, data6)  # [2, 3] * [3, 2] --> [2, 2]
# matMul_3 = tf.matmul(data8, data6) # 不符合矩阵运算规则 shapes [2, 4] -- [3, 2]
multiPly = tf.multiply(data3, data4)  # 注意与普通矩阵乘法的区别 [1, 2] * [2, 1] --> [2, 2]

with tf.Session() as sess:
    print('--' * 20)
    print(sess.run(matMul_1))
    print('--' * 20)
    print(sess.run(Add))
    print('--' * 20)
    print(sess.run(matMul_2))
    print('--' * 20)
    # print(sess.run(matMul_3))
    print(sess.run(multiPly))
    print(sess.run([matMul_1, matMul_2, multiPly]))

# 矩阵的生成
mat0 = tf.constant([[0, 0, 0], [0, 0, 0]])  # 方法一:生成使用0填充2*3的矩阵
mat1 = tf.zeros([2, 3])  # 方法二:生成使用0填充2*3的矩阵
mat2 = tf.ones(3, 2)  # 生成使用1填充2*3的矩阵
mat3 = tf.fill([2, 4], 100)  # 指定元素100填充2*4的矩阵

mat4 = tf.constant([[2], [3], [4]])  # 定义一个 3行1列 的矩阵
mat5 = tf.zeros_like(mat4)  # 生成维度与mat4相同的矩阵, 并使用0填充
mat6 = tf.ones_like(mat4)  # 生成维度与mat4相同的矩阵, 并使用1填充
mat7 = tf.linspace(0.0, 0.2, 11)  # 在0.0与0.2之间生成间隔为0.02的10个数据,(end-start)/(num-1)=0.2
mat8 = tf.random_uniform([2, 3], -1, 2)  # 生成维度为[2, 3]的随机数,区间为[-1, 2]

with tf.Session() as sess:
    print('--' * 20)
    print(sess.run([mat0, ]))
    print(sess.run([mat1, ]))
    print(sess.run([mat2, ]))
    print(sess.run([mat3, ]))
    print(sess.run([mat4, ]))
    print(sess.run([mat5, ]))
    print(sess.run([mat6, ]))
    print(sess.run([mat7, ]))
    print(sess.run([mat8, ]))

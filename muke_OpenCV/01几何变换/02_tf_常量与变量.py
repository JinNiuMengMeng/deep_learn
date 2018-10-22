# -*- coding:utf-8 -*-
import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

data1 = tf.constant(2.5, dtype=tf.float32)
data2 = tf.constant(2.0)
data3 = tf.Variable(10, name='var', dtype=tf.int32)
print(data1)  # 输出的是秒描述信息
print(data2)
print(data3)

# 方式一
"""
sess = tf.Session()  # 定义一个session
init = tf.global_variables_initializer()  # 初始化所有变量他也是一个计算图, 因此要放到session中运行
sess.run(init)
print(sess.run(data1))
print(sess.run(data2))
print(sess.run(data3))
sess.close()
"""
# 方式二
with tf.Session() as sess:
    print(sess.run(data1))

"""
tensorflow的本质: tf = 张量tensor + 计算图grahps
op: option值得是一个操作, tensorflow之间的加减乘除
张量tensor本质: 数据(变量,常量, 一维, 多维)
op: 四则运算操作, 赋值操作
计算图graphs: 数据 和 操作 的过程(所有的计算图都要放到session中运行)
"""

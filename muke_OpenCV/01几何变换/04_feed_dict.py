import os
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

data1 = tf.placeholder(tf.float32)
data2 = tf.placeholder(tf.float32)
data3 = tf.constant(45, dtype=tf.int32)
data4 = tf.Variable(5, dtype=tf.int32)
dataAdd = tf.add(data1, data2)
dataSub = tf.subtract(data3, data4)
with tf.Session() as sess:
    tf.global_variables_initializer().run()
    # feed_dict中的data3,data4替换掉原数据相应的值
    print(sess.run(dataAdd, feed_dict={data1: 6, data2: 2}))
    print(sess.run(dataSub, feed_dict={data3: 6, data4: 2}))
    # 由于feed只在调用他的方法范围内有效，所以这个打印的结果是 40
    print(sess.run(dataSub))
"""
sess.run() 中的feed_dict
我们都知道feed_dict的作用是给使用placeholder创建出来的tensor赋值。
其实，他的作用更加广泛：feed 使用一个 值临时替换一个 op 的输出结果.
你可以提供 feed 数据作为 run() 调用的参数. feed 只在调用它的方法内有效, 方法结束, feed 就会消失.
"""


import tensorflow as tf
import os 
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 定义一个变量 x
x = tf.Variable([1, 2])
# 定义一个常量 a
a = tf.constant([3, 3])
# 增加一个减法op
sub = tf.subtract(x, a)
# 增加一个加法op
add = tf.add(x, sub)

# 初始化变量
init = tf.global_variables_initializer()

with tf.Session() as sess:
	sess.run(init) # 激活变量
	print(sess.run(sub))
	print(sess.run(add))

import tensorflow as tf
import os 
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 创建一个常量op
m1 = tf.constant([[3, 3]])
m2 = tf.constant([[2], [3]])

# 创建一个矩阵乘法op, 把m1和m2传入
product = tf.matmul(m1, m2)
print(product)

# 方法一
# 定义一个回话, 启动默认图
sess1 = tf.Session()
# 调用sess的run方法, 执行矩阵的乘法
# run(product)触发了途中的三个op
result1 = sess1.run(product)
print(result1)
sess1.close()

# 方法二
with tf.Session() as sess2:
	result2 = sess2.run(product)
	print(result2)

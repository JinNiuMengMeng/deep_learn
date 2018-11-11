import tensorflow as tf
import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

martix1 = tf.constant([[3, 3]])
martix2 = tf.constant([[2], [2]])
product = tf.matmul(martix1, martix2)  # 矩阵的乘法

# method 1
sess = tf.Session()
result = sess.run(product)
print(result)
sess.close()

# method 2
with tf.Session() as sess:
    result2 = sess.run(product)
    print(result2)

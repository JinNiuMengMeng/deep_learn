import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# tf.constant 是一个计算, 这个计算的结果为一个张量, 保存在变量a中
a = tf.constant([1.0, 2.0], name="a")
b = tf.constant([2.0, 3.0], name="b")
result = tf.add(a, b, name="add")
print(result)
"""输出结果为:
Tensor("add:0", shape=(2,), dtype=float32)
"""
import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 常量与常量之间的四则运算

data1 = tf.constant(50)
data2 = tf.constant(5)

dataAdd = tf.add(data1, data2)
dataSub = tf.subtract(data1, data2)
dataMul = tf.multiply(data1, data2)
dataDiv = tf.divide(data1, data2)

with tf.Session() as sess:
    print(sess.run(dataAdd))
    print(sess.run(dataSub))
    print(sess.run(dataMul))
    print(sess.run(dataDiv))

print('--' * 20)
# 常量与变量之间的四则运算

data3 = tf.constant(50)
data4 = tf.Variable(5)

dataAdd = tf.add(data3, data4)
dataSub = tf.subtract(data3, data4)
dataMul = tf.multiply(data3, data4)
dataDiv = tf.divide(data3, data4)
init = tf.global_variables_initializer()

dataCopy = tf.assign(data4, dataAdd)  # 将dataAdd的值赋值给data4  55->data4

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(dataAdd))
    print(sess.run(dataSub))
    print(sess.run(dataMul))
    print(sess.run(dataDiv))
    print("sess.run(dataCopy):", sess.run(dataCopy))  # 运行33行的运算
    print("dataCopy.eval():", dataCopy.eval())    # 再次运行33行的运算
    print("tf.get_default_session():", tf.get_default_session().run(dataCopy))    # 再次运行33行的运算
print("end...")
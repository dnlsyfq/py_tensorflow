import tensorflow as tf 

with tf.compat.v1.Session() as sess:

    hello = tf.constant("Hello")
    print(sess.run(hello))

    a = tf.constant(20)
    b = tf.constant(22)

    print(sess.run(a+b))
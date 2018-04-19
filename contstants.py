import tensorflow as tf

zeros = tf.zeros([2,3])
ones  = tf.constant(1, shape=[2,3])

seq = tf.range(10,100,2)

with tf.Session() as sess:
    print(zeros.eval(session=sess))
    print(ones.eval(session=sess))
    print(seq.eval(session=sess))
    rint(tf.shape(seq))

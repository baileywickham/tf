import tensorflow as tf
import numpy as np

x = tf.random_normal([])
y = tf.random_normal([], mean=0, stddev=1)

with tf.Session() as sess:
    print(tf.cond(x > y, lambda: x + y, lambda: x - y).eval(session=sess))

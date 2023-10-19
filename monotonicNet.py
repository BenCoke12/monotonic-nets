#generate network
#set weights and biases - monotonic in range 0-1
#weight = 1
#bias = 0
#no need to train
#graph outputs
#export network
#graph networks outputs

import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np

model = keras.Sequential()
#model.add(keras.layers.Dense(1))
model.add(keras.layers.Dense(1, 
                             kernel_initializer=tf.keras.initializers.Ones(),
                             bias_initializer=tf.keras.initializers.Zeros(),
                             kernel_constraint=tf.keras.constraints.MinMaxNorm(
                                 min_value=1.0, max_value=1.0, rate=1.0, axis=1),
                             bias_constraint=tf.keras.constraints.MinMaxNorm(
                                 min_value=0.0, max_value=0.0, rate=1.0, axis=0), 
                                   activation=tf.nn.relu))
#model.add(keras.layers.Dense(1))


#kernel_constraint isn't fixing the weights, try training the model on dummy data to
#give a step to fix weights within
train_x = tf.expand_dims(tf.convert_to_tensor([[0.1], [0.2], [0.3], [0.4], [0.5], [0.6], [0.7], [0.8], [0.9]]), 0)
train_y = tf.expand_dims(tf.convert_to_tensor([[0.1], [0.2], [0.3], [0.4], [0.5], [0.6], [0.7], [0.8], [0.9]]), 0)
#print(train_x.shape)

#model.compile(optimizer='adam', loss=tf.keras.losses.MeanSquaredError(), metrics=['accuracy'])
#model.fit(train_x, train_y, epochs=3)

point = tf.expand_dims(tf.convert_to_tensor([0.7]), 0)
print("---start report---")
#print(point.shape)
print(model(point, training=False))
#print(model.summary())
print(model.trainable_variables)

for x in range(10):
    point = tf.expand_dims(tf.convert_to_tensor([x/10]), 0)
    print(point, model(point, training=False))

#save network
#prompt for name?
name = '1nYeX'

model.save(f'networks/{name}')
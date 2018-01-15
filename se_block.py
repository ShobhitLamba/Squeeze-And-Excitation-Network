# Implementation of Squeeze and Excite block
# Author: Shobhit Lamba
# e-mail: slamba4@uic.edu

from keras.layers import GlobalAveragePooling2D, Reshape, Dense, multiply

def squeeze_excite_block(input, ratio = 16):
    init = input
    channel_axis = -1 # Since we are using Tensorflow
    filters = init._keras_shape[channel_axis]
    shape = (1, 1, filters)

    se = GlobalAveragePooling2D()(init)
    se = Reshape(shape)(se)
    se = Dense(filters // ratio, activation = "relu", kernel_initializer = "he_normal", use_bias = False)(se)
    se = Dense(filters, activation = "sigmoid", kernel_initializer = "he_normal", use_bias = False)(se)

    output = multiply([init, se])
    
    return output

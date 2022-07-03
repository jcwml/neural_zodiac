# github.com/jcwml
import sys
import os
import math
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from random import seed, uniform, getrandbits
from time import time_ns
from sys import exit
from os.path import isfile
from os import mkdir
from os.path import isdir

# import tensorflow as tf
# from tensorflow.python.client import device_lib
# print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
# if tf.test.gpu_device_name():
#     print('Default GPU Device: {}'.format(tf.test.gpu_device_name()))
# else:
#     print("Please install GPU version of TF")
# print(device_lib.list_local_devices())
# print(tf.config.list_physical_devices())
# exit();

# disable warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# print everything / no truncations
np.set_printoptions(threshold=sys.maxsize)

# https://stackoverflow.com/questions/4601373/better-way-to-shuffle-two-numpy-arrays-in-unison
# def shuffle_in_unison(a, b):
#     rng_state = np.random.get_state()
#     np.random.shuffle(a)
#     np.random.set_state(rng_state)
#     np.random.shuffle(b)

# hyperparameters
seed(74035)
project = "neural_zodiac"
model_name = 'keras_model'
optimiser = 'adam'
activator = 'tanh'
inputsize = 12
outputsize = 1
epoches = 6
layers = 0
layer_units = 128
batches = 128

# load options
argc = len(sys.argv)
if argc >= 2:
    layers = int(sys.argv[1])
    print("layers:", layers)
if argc >= 3:
    layer_units = int(sys.argv[2])
    print("layer_units:", layer_units)
if argc >= 4:
    batches = int(sys.argv[3])
    print("batches:", batches)
if argc >= 5:
    activator = sys.argv[4]
    print("activator:", activator)
if argc >= 6:
    optimiser = sys.argv[5]
    print("optimiser:", optimiser)
if argc >= 7 and sys.argv[6] == '1':
    os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
    print("CPU_ONLY: 1")
if argc >= 8:
    epoches = int(sys.argv[7])
    print("epoches:", epoches)

# make sure save dir exists
if not isdir('models'): mkdir('models')
model_name = 'models/' + activator + '_' + optimiser + '_' + str(layers) + '_' + str(layer_units) + '_' + str(batches) + '_' + str(epoches)

##########################################
#   CREATE DATASET
##########################################
print("\n--Creating Dataset")
st = time_ns()

# Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, Sagittarius, Capricorn, Aquarius, Pisces
tss = int(os.stat("scraper/train_y.dat").st_size / 4)
print("Dataset Size:", "{:,}".format(tss))

if isfile("train_x.npy"):
    train_x = np.load("train_x.npy")
    train_y = np.load("train_y.npy")
else:
    load_x = []
    with open("scraper/train_x.dat", 'rb') as f:
        load_x = np.fromfile(f, dtype=np.float32)
    train_x = np.reshape(load_x, [tss, inputsize])

    load_y = []
    with open("scraper/train_y.dat", 'rb') as f:
        load_y = np.fromfile(f, dtype=np.float32)
    train_y = np.reshape(load_y, [tss, outputsize])
    
    np.save("train_x.npy", train_x)
    np.save("train_y.npy", train_y)

# shuffle_in_unison(train_x, train_y) 
# train_x = np.reshape(train_x, [tss, inputsize])
# train_y = np.reshape(train_y, [tss, outputsize])

# print(train_x.shape)
# print(train_x)
# print(train_y.shape)
# print(train_y)
# exit()

timetaken = (time_ns()-st)/1e+9
print("Time Taken:", "{:.2f}".format(timetaken), "seconds")

##########################################
#   TRAIN
##########################################
print("\n--Training Model")

# construct neural network
model = Sequential()

model.add(Dense(layer_units, activation=activator, input_dim=inputsize))

for x in range(layers):
    model.add(Dense(layer_units, activation=activator))

model.add(Dense(outputsize))

# output summary
model.summary()

if optimiser == 'adam':
    optim = keras.optimizers.Adam(learning_rate=0.001)
elif optimiser == 'sgd':
    #lr_schedule = keras.optimizers.schedules.ExponentialDecay(initial_learning_rate=0.3, decay_steps=epoches*tss, decay_rate=0.1)
    lr_schedule = keras.optimizers.schedules.ExponentialDecay(initial_learning_rate=0.1, decay_steps=epoches*tss, decay_rate=0.01)
    optim = keras.optimizers.SGD(learning_rate=lr_schedule, momentum=0.0, nesterov=False)
    #optim = keras.optimizers.SGD(learning_rate=0.01, momentum=0.0, nesterov=False)
elif optimiser == 'momentum':
    optim = keras.optimizers.SGD(learning_rate=0.01, momentum=0.9, nesterov=False)
elif optimiser == 'nesterov':
    optim = keras.optimizers.SGD(learning_rate=0.01, momentum=0.9, nesterov=True)
elif optimiser == 'nadam':
    optim = keras.optimizers.Nadam(learning_rate=0.001)
elif optimiser == 'adagrad':
    optim = keras.optimizers.Adagrad(learning_rate=0.001)
elif optimiser == 'rmsprop':
    optim = keras.optimizers.RMSprop(learning_rate=0.001)
elif optimiser == 'adadelta':
    optim = keras.optimizers.Adadelta(learning_rate=0.001)
elif optimiser == 'adamax':
    optim = keras.optimizers.Adamax(learning_rate=0.001)
elif optimiser == 'ftrl':
    optim = keras.optimizers.Ftrl(learning_rate=0.001)

model.compile(optimizer=optim, loss='mean_squared_error')

# train network
history = model.fit(train_x, train_y, epochs=epoches, batch_size=batches)
model_name = model_name + "_" + "a{:E}".format(history.history['loss'][-1])
timetaken = (time_ns()-st)/1e+9
print("\nTime Taken:", "{:.2f}".format(timetaken), "seconds")

##########################################
#   EXPORT
##########################################
print("\n--Exporting Model")
st = time_ns()

# save weights for C array
print("\nExporting weights...")
li = 0
f = open(model_name + "_layers.h", "w")
f.write("#ifndef " + project + "_layers\n#define " + project + "_layers\n\n")
if f:
    for layer in model.layers:
        total_layer_weights = layer.get_weights()[0].flatten().shape[0]
        total_layer_units = layer.units
        layer_weights_per_unit = total_layer_weights / total_layer_units
        #print(layer.get_weights()[0].flatten().shape)
        #print(layer.units)
        print("+ Layer:", li)
        print("Total layer weights:", total_layer_weights)
        print("Total layer units:", total_layer_units)
        print("Weights per unit:", int(layer_weights_per_unit))

        f.write("const float " + project + "_layer" + str(li) + "[] = {")
        isfirst = 0
        wc = 0
        bc = 0
        if layer.get_weights() != []:
            for weight in layer.get_weights()[0].flatten():
                wc += 1
                if isfirst == 0:
                    f.write(str(weight))
                    isfirst = 1
                else:
                    f.write("," + str(weight))
                if wc == layer_weights_per_unit:
                    f.write(", /* bias */ " + str(layer.get_weights()[1].flatten()[bc]))
                    #print("bias", str(layer.get_weights()[1].flatten()[bc]))
                    wc = 0
                    bc += 1
        f.write("};\n\n")
        li += 1
f.write("#endif\n")
f.close()

# save keras model
model.save(model_name)

# save prediction model
seed(457895)

f = open(model_name + "_pd.csv", "w")
if f:
    
    f.write("onehot | prediction\n")

    p = model.predict(train_x)
    for i in range(tss):
        f.write(str(train_x[i]) + ", " + str(p[i][0]) + "\n")

    f.close()

# save random prediction model
predict_x = np.empty([2048, 12], float)
for i in range(2048):
    predict_x[i] = [getrandbits(1),getrandbits(1),getrandbits(1),getrandbits(1),getrandbits(1),getrandbits(1),getrandbits(1),getrandbits(1),getrandbits(1),getrandbits(1),getrandbits(1),getrandbits(1)]

f = open(model_name + "_rnd.csv", "w")
if f:
    
    f.write("onehot | prediction\n")

    p = model.predict(predict_x)
    for i in range(2048):
        f.write(str(predict_x[i]) + ", " + str(p[i][0]) + "\n")

    f.close()

# save random prediction model 2
predict_x = np.empty([2048, 12], float)
for i in range(2048):
    predict_x[i] = [getrandbits(1)+uniform(0, 3),getrandbits(1)+uniform(0, 3),getrandbits(1)+uniform(0, 3),getrandbits(1)+uniform(0, 3),getrandbits(1)+uniform(0, 3),getrandbits(1)+uniform(0, 3),getrandbits(1)+uniform(0, 3),getrandbits(1)+uniform(0, 3),getrandbits(1)+uniform(0, 3),getrandbits(1)+uniform(0, 3),getrandbits(1)+uniform(0, 3),getrandbits(1)+uniform(0, 3)]

f = open(model_name + "_rnd2.csv", "w")
if f:
    
    f.write("onehot | prediction\n")

    p = model.predict(predict_x)
    for i in range(2048):
        f.write(str(predict_x[i]) + ", " + str(p[i][0]) + "\n")

    f.close()

timetaken = (time_ns()-st)/1e+9
print("Time Taken:", "{:.2f}".format(timetaken), "seconds\n")
print(model_name + "\n")
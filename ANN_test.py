import os
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
import keras.models

x = []
y = []
count_succ = 0
count_fail = 0
for file in os.listdir('data'):
    x.append(np.load('data/%s'%file))
    if 'fail' in file:
        y.append(0)
        count_fail += 1
    if 'succ' in file:
        y.append(1)
        count_succ += 1

x = np.array(x)
y = np.array(y)
p = np.random.permutation(len(x))
x = x[p]
y = y[p]
print('succ: ',count_succ)
print('fail: ',count_fail)
if count_succ<10 or count_fail<10:
    print('warning, you do not have enough data for training a ANN model')
    print('please run the main script without enabled ANN to collect more data')


model = keras.models.load_model('NN_model')
model.evaluate(x, y)



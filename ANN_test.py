import os
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
import keras.models

x = []
y = []
for file in os.listdir('data'):
    #print (file)
    x.append(np.load('data/%s'%file))
    if 'fail' in file:
        y.append(0)
    if 'succ' in file:
        y.append(1)

x = np.array(x)
y = np.array(y)
#print(x.shape)
#print(y.shape)

p = np.random.permutation(len(x))
x = x[p]
y = y[p]
#print(x.shape)
#print(y.shape)
#print(y)
if count_succ<10 or count_fail<10:
    print('warning, you do not have enough data for training a ANN model')
    print('please run the main script without enabled ANN to collect more data')


model = keras.models.load_model('NN_model')
model.evaluate(x, y)
print(model.predict(x))
pred = model.predict(x)
prediction = np.round(pred)
for i in range(246):
    #print(x[i], end = ' ')
    print(y[i], end = ' ')
    print(prediction[i], end = ' ')
    if y[i]!=prediction[i]:
        print(pred[i])
    else:
        print('')


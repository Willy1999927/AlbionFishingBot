import os
import numpy as np
from keras.models import Sequential
from keras.layers import Dense

#print(os.listdir('data'))
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
print(x.shape)
print(y.shape)

p = np.random.permutation(len(x))
x = x[p]
y = y[p]
print(x.shape)
print(y.shape)
print(y)

model = Sequential()
model.add(Dense(4096, input_dim=4096, activation='relu'))
model.add(Dense(4096, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary(line_length=None, positions=None, print_fn=None)
model.fit(x, y, epochs=12, batch_size=10,validation_split=0.2)

model.save('NN_model')

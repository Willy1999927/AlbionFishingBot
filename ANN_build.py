import os
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout

#print(os.listdir('data'))
x = []
y = []
count_succ = 0
count_fail = 0
for file in os.listdir('data'):
    #print (file)
    x.append(np.load('data/%s'%file))
    if 'fail' in file:
        y.append(0)
        count_fail+=1
    if 'succ' in file:
        y.append(1)
        count_succ+=1

x = np.array(x)
y = np.array(y)
print('succ: ',count_succ)
print('fail: ',count_fail)

p = np.random.permutation(len(x))
x = x[p]
y = y[p]
print(x.shape)
print(y.shape)
#print(y)

model = Sequential()
model.add(Dense(1024, input_dim=4096, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(512, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary(line_length=None, positions=None, print_fn=None)
model.fit(x, y, epochs=15, batch_size=50,validation_split=0.2)

model.save('NN_model')

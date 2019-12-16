from numpy import array
from keras.models import Sequential
from keras.layers import Dense, LSTM
import numpy as np

#1. 데이터
x = array([[1,2,3], [2,3,4], [3,4,5], [4,5,6], [5,6,7], [6,7,8], [7,8,9], [8,9,10], [9,10,11], [10,11,12], [20,30,40], [30,40,50], [40,50,60]])
y = array([4,5,6,7,8,9,10,11,12,13,50,60,70])
print(x)
x1 = x[:10]
y1 = y[:10]
x2 = x[10:]
y2 = y[10:]

x1 = np.transpose(x1)
y1 = np.transpose(y1)
x2 = np.transpose(x2)
y2 = np.transpose(y2)

print("x1.shape : ", x1.shape)
print("x2.shape : ", x2.shape) #(4, 3)
print("y1.shape : ", y1.shape)
print("y2.shape : ", y2.shape) #(4, )

x1 = x1.reshape((x1.shape[0], x1.shape[1], 1))
x2 = x2.reshape((x2.shape[0], x2.shape[1], 1))

print(x)
print("x1.shape : ", x1.shape)
print("x2.shape : ", x2.shape)      #(4, 3, 1)

#2. 모델 구성
from keras.models import Sequential, Model
from keras.layers import Dense, Input, LSTM

model = Sequential()
model.add(LSTM(5, activation='relu', input_shape=(3,1)))
model.add(Dense(1000))
model.add(Dense(5))
model.add(Dense(3))

model.add(LSTM(5, activation='relu', input_shape=(3,1)))
model.add(Dense(1000))
model.add(Dense(5))
model.add(Dense(3))

from keras.layers.merge import concatenate
merge1 = concatenate([middle1, middle2])

output1 = Dense(30)(merge1)
output1 = Dense(13)(output1)
output1 = Dense(3)(output1)

output2 = Dense(15)(merge1)
output2 = Dense(32)(output2)
output2 = Dense(3)(output2)

model = Model(inputs = [input1, input2], outputs = [output1, output2])
model.summary()
# model.summary()

#3. 실행
model.compile(loss='mse', optimizer='adam', metrics=['mse']) # metrics=['accuracy'])
from keras.callbacks import EarlyStopping

early_stopping = EarlyStopping(monitor='loss', patience=10, mode='auto')
model.fit([x1_train, x2_train], [y1_train, y2_train], epochs=5, batch_size=1, validation_data=([x1_val, x2_val], [y1_val, y2_val]))

x_input = array([25,35,45])
x_input = x_input.reshape((1,3,1))

yhat = model.predict(x_input)
print(yhat)
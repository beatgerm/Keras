import numpy as np
from keras.models import Sequential
from keras.layers import Dense, LSTM

#1. 데이터
a = np.array(range(1,11))
x = a
size = 5
def split_x(seq, size): # seq = 10개 (1,2,3,4,5,6,7,8,9,10)
    aaa = []
    for i in range(len(seq)- size + 1):
        subset = seq[i:(i+size)]
        aaa.append([item for item in subset])
    print(type(aaa))
    return np.array(aaa)


dataset = split_x(a, size)
print("============")
print(dataset)  

x_train = dataset[:,0:-1]
y_train = dataset[:,-1]

print(x)
print(x_train.shape) #(6,4)
print(y_train.shape) #(6,)

x_train = x_train.reshape((x_train.shape[0], x_train.shape[1], 1))

print(x)
print("x.shape : ", x.shape)    

# lstm model
model = Sequential()
model.add(LSTM(5, activation='relu', input_shape=(4,1)))
model.add(Dense(1000))
model.add(Dense(5))
model.add(Dense(1000))
model.add(Dense(5))
model.add(Dense(1))

model.compile(loss='mse', optimizer='adam')
model.fit(x_train, y_train, epochs=1)

x2 = np.array([7,8,9,10])
x2 = x2.reshape((1, 4, 1))
y_predict = model.predict(x2)
print(y_predict)





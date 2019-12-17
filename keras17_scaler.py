from numpy import array
from keras.models import Sequential
from keras.layers import Dense, LSTM

#1. 데이터
x = array([[1,2,3], [2,3,4], [3,4,5], [4,5,6], [5,6,7], 
            [6,7,8], [7,8,9], [8,9,10], [9,10,11], [10,11,12], 
            [20000,30000,40000], [30000,40000,50000], [40000,50000,60000]])
y = array([4,5,6,7,8,9,10,11,12,13,50000,60000,70000])

from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.preprocessing import RobustScaler, MaxAbsScaler

scaler = StandardScaler
# scaler = MinMaxScaler
scaler.fit(x)
x = scaler.transform(x)
print(x)

print("x.shape : ", x.shape) #(4, 3)
print("y.shape : ", y.shape) #(4, )

# x = x.reshape((x.shape[0], x.shape[1], 1))
# print("x.shape : ", x.shape)      #(4, 3, 1)

#2. 모델 구성

model = Sequential()
# model.add(LSTM(5, activation='relu', input_shape=(3,1)))
model.add(Dense(1000, activation='relu', input_shape=(3,)))
model.add(Dense(5, activation='linear'))
model.add(Dense(5))
model.add(Dense(1))
# model.summary()

#3. 실행
model.compile(optimizer='adam', loss='mse')
model.fit(x, y, epochs=1000, verbose=0)

x_input = array([25,35,45])
x_input = np.transform(x_input)
# x_input = scaler.transform(x_input)

print(x_input.shape)

# x_input = x_input.reshape((1,3,1))

yhat = model.predict(x_input, verbose=2)
print(yhat)
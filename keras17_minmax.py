from numpy import array
from keras.models import Sequential
from keras.layers import Dense, LSTM

#1. 데이터
x = array([[1,2,3], [2,3,4], [3,4,5], [4,5,6], [5,6,7], 
            [6,7,8], [7,8,9], [8,9,10], [9,10,11], [10,11,12], 
            [20000,30000,40000], [30000,40000,50000], [40000,50000,60000], [100,200,300]])
y = array([4,5,6,7,8,9,10,11,12,13,50000,60000,70000,400])

print("x.shape : ", x.shape) #(14, 3)
print("y.shape : ", y.shape) #(14, )

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler
scaler.fit(x)
x = scaler.transform(x)
print(x)

x_trian = x[:13]
x_predict = x[13:]
y_train = y[:13]
y_predict = y[13:]

#train과 predict로 나눌것
#train = 1번째부터 13번째까지
#predict = 14번째
#2. 모델 구성

model = Sequential()
# model.add(LSTM(5, activation='relu', input_shape=(3,1)))
model.add(Dense(1000, activation='relu', input_shape=(3,1)))
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
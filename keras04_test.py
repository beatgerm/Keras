from keras.models import Sequential
from keras.layers import Dense


import numpy as np
x_train = np.array([1,2,3,4,5,6,7,8,9,10])
y_train = np.array([1,2,3,4,5,6,7,8,9,10])
x_test = np.array([11,12,13,14,15,16,17,18,19,20]) 
y_test = np.array([11,12,13,14,15,16,17,18,19,20])

model = Sequential()
model.add(Dense(200, input_dim=1, activation='relu'))
model.add(Dense(170))
model.add(Dense(150))
model.add(Dense(130))
model.add(Dense(110))
model.add(Dense(90))
model.add(Dense(70))
model.add(Dense(50))
model.add(Dense(30))
model.add(Dense(10))
model.add(Dense(5))
model.add(Dense(3))
model.add(Dense(1))

model.summary()

model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])
model.fit(x_train,y_train, epochs=200)

loss, acc = model.evaluate(x_test, y_test)
print("acc : ", acc)

print("loss : ", loss)
y_predict = model.predict(x_test)
print(y_predict)

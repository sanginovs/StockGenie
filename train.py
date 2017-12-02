from keras.models import Sequential
from keras.layers import Dense
import numpy as np
from app import mainDB, models
# fix random seed for reproducibility
np.random.seed(7)

#Grab all the stocks whose symbol is apple
query = models.StockData.select().where(models.StockData.symbol =='AAPL').order_by(models.StockData.date.desc())

data = []

for entry in query:
    row = []
    row.append(entry.open)
    row.append(entry.high)
    row.append(entry.low)
    row.append(entry.close)
    data.append(row)

#Make the data a numpy array so we can slice list of lists
data = np.asarray(data,dtype=np.float32)

length = len(data)
#All days except the currenty day
X = data[:length-1]
#Only the closing price for all days except the very first day
Y = data[1:,3:]

model = Sequential()
model.add(Dense(12, input_shape=(4,), activation='linear'))
model.add(Dense(8, activation='linear'))
model.add(Dense(1, activation='linear'))

model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])

model.fit(X, Y, epochs=150, batch_size=10)

scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
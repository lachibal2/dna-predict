# Lachi's Machine Learning Code
# dependencies
from keras.models import Sequential
from keras.layers import Dense, Activation, LSTM, Embedding
from keras.losses import categorical_crossentropy
from keras.utils import to_categorical
import numpy as np
import sys

from get_data import main

sys.setrecursionlimit(1500)

# data
main_data = main()
trainX = main_data[:int(0.6 * len(main_data))][0]
trainY = main_data[:int(0.6 * len(main_data))][1]

valX = main_data[int(0.6 * len(main_data)):int(0.8 * len(main_data))][0]

testX = main_data[int(0.8 * len(main_data)):][0]
testY = main_data[int(0.8 * len(main_data)):][1]

# labels
labels = ["A", "C", "G", "T"]
one_hot_labels = to_categorical(labels, num_classes=4)

# set up model
model = Sequential()
model.add(Embedding(4, 2, input_length=3))
model.add(LSTM(2))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy']) # compile model

# train, predict, and evaluate model
model.fit(trainX, trainY, epochs=5)
classes = model.predict(valX, batch_size=1)
print(classes)
print(model.evaluate(testX, testY))
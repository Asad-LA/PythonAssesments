# importing modules 
import tensorflow as tf 
import numpy as np 
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Flatten #Converting data into flat layer so it can be further classified 
from tensorflow.keras.layers import Dense #middle layer or hidden layer
from tensorflow.keras.layers import Activation #sigmoid function activaion function
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data() 

x_train=x_train.astype('float32')
x_test=x_test.astype('float32')
gray_scale=255
x_train/=gray_scale
x_test/=gray_scale

print('feature matrix:',x_train.shape)
print('target matrix:',x_test.shape)
print('feature matrix:',y_train.shape)
print('target matrix:',y_test.shape)

fig,ax=plt.subplots(10,10)
k=0
for i in range (10):
    for j in range(10):
        ax[i][j].imshow(x_train[k].reshape(28,28),aspect='auto')
        
        k+=1
plt.show()


model=Sequential([
    Flatten(input_shape=(28,28)),
    Dense(2048,activation='sigmoid'),
    Dense(1024,activation='sigmoid'),
    Dense(512,activation='sigmoid'),
    Dense(256,activation='sigmoid'),
    Dense(128,activation='sigmoid'),
    Dense(64,activation='sigmoid'),
    Dense(10,activation='sigmoid'),
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',metrics=['accuracy'])

model.fit(x_train,y_train, epochs=200,batch_size=2000,validation_split=0.1)

results = model.evaluate(x_test, y_test, verbose = 0) 
print('test loss, test acc:', results)



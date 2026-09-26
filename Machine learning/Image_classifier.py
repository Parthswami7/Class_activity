import keras 
import numpy as np
import matplotlib.pyplot as plt 
import tensorflow.keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense , Flatten , Dropout , Conv2D , MaxPooling2D
from keras.constraints import max_norm
from keras.utils import np_utils 
from tensorflow.keras.optimizers import SGD
from keras.datasets import cifar10
from keras.utils import to_categorical
from google.colab import files

(x_train , y_train),(x_test , y_test) = cifar10.load_data()

for i in range(9):

    plt.subplot(330 +1 +i)

    plt.imshow(x_train[i],cmap=plt.get_cmap('gray'))

plt.show()

num_classes = 10

y_train = to_categorical(y_train , num_classes)

y_test = to_categorical(y_test , num_classes)

x_train = x_train.astype('float32')

x_test = x_test.astype('float32')

x_train /= 255

x_test /= 255

print('x_train shape:', x_train.shape)

print(x_train.shape[0], 'train samples')

print(x_test.shape[0], 'test samples')

model = Sequential()

model.add(Conv2D(32, (3, 3), input_shape=(32,32,3), activation='relu', padding='same')) 

model.add(Dropout(0.2)) 

model.add(Conv2D(32, (3, 3), activation='relu', padding='same')) 

model.add(MaxPooling2D(pool_size=(2, 2))) 

model.add(Conv2D(64, (3, 3), activation='relu', padding='same')) 

model.add(Dropout(0.2)) 

model.add(Conv2D(64, (3, 3), activation='relu', padding='same')) 

model.add(MaxPooling2D(pool_size=(2, 2))) 

model.add(Conv2D(128, (3, 3), activation='relu', padding='same')) 

model.add(Dropout(0.2)) 

model.add(Conv2D(128, (3, 3), activation='relu', padding='same')) 

model.add(MaxPooling2D(pool_size=(2, 2))) 

model.add(Flatten()) 

model.add(Dropout(0.2)) 

model.add(Dense(1024, activation='relu', kernel_constraint=maxnorm(3))) 

model.add(Dropout(0.2)) 

model.add(Dense(512, activation='relu', kernel_constraint=maxnorm(3))) 

model.add(Dropout(0.2)) 

model.add(Dense(num_classes, activation='softmax'))

print(model.summary())

opt = SGD(learning_rate=0.01, momentum=0.9, decay=0.0002, nesterov=False)

model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])


model.fit(x_train , y_train ,batch_size=32, epochs=10, verbose=1,validation_data=(x_test,y_test))

print('The model has successfully trained')

model.save('classifier.keras')

print('Saving the model as classifier.keras')

score = model.evaluate(x_test,y_test,verbose=0)

print('Test loss:',score[0])

print('Test accuracy:',score[1])

uploaded = files.upload()

filename = list(uploaded.keys())[0]

def load_image(filename):

    img = load_image(filename,target_size=(32,32))

    img = img_to_array(img)

    img = img.astype('float32') / 255.0

    img = np.expand_dims(img , axis=0)

    return img 

def run_example():

    img = load_image(filename)

    loaded_model = loaded_model('classifier.keras')

    result = loaded_model.predict(img)

    predicted_index = argmax(result[0])

    print('Predicted class:',class_names[predicted_index].title())

run_example()
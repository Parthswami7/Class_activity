import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

from sklearn.preprocessing import LabelEncoder , StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score

import keras 
from keras.models import Sequential
from keras.layers import Dense , LeakyReLU , PReLU , ELU , Dropout


df = pd.read_csv('Churn_Modelling.csv')
print(df.head())

print(df.info())

print(df.describe())

lb = LabelEncoder()

df['Geography'] = lb.fit_transform(df['Geography'])
df['Gender'] = lb.fit_transform(df['Gender'])

print(df)

print(df.info())

df = df.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1)

print(df.shape)

y = df.pop('Exited')
X = df

print(X.shape)

print(y.shape)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

print(X_train)

classifier = Sequential()
classifier.add(Dense(units = 6, kernel_initializer = 'he_uniform',activation='relu',input_dim = 10))
classifier.add(Dense(units = 6, kernel_initializer = 'he_uniform',activation='relu'))
classifier.add(Dense(units = 1, kernel_initializer = 'glorot_uniform', activation = 'sigmoid'))
classifier.compile(optimizer = 'Adamax', loss = 'binary_crossentropy', metrics = ['accuracy'])
model_history=classifier.fit(X_train, y_train, batch_size = 10, epochs = 100)
classifier.summary()

Y_pred = classifier.predict(X_test)
print(Y_pred)

Y_pred = (Y_pred > 0.5)

print(Y_pred)

cm = confusion_matrix(y_test, Y_pred)
print(cm)

score=accuracy_score(Y_pred,y_test)

print(score)

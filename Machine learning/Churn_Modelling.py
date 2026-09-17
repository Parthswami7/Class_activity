import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler , LabelEncoder

df = pd.read_csv('Churn_Modelling.csv')
print(df)
print(df.head())
print(df.info())
print(df.describe())

lb = LabelEncoder()

df['Geography'] = lb.fit_transform(df['Geography'])
df['Gender'] = lb.fit_transform(df['Gender'])

print(df)

print(df.info())

df = df.drop(['RowNumber','CustomerId','Surname'],axis=1)
print(df.shape)

y = df.pop('Exited')
X = df
print(X.shape)
print(y.shape)

X_train , X_test , y_train , y_test = train_test_split(X,y,test_size=0.2 , random_state=0)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)
print(X_train)

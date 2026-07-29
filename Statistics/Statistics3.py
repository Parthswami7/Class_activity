import pandas as pd 
import numpy as np 
import statistics as stats 
import matplotlib.pyplot as plt 
import seaborn as sns
data = pd.read_csv('C:\\Users\\ASUS\\Desktop\\classactivity\\Statistics\\Titanic Dataset.csv')
data.head()
median_age = np.median(data['Age'])
print("Median value of Age -", median_age)
median_fare = np.median(data['Fare'])
print("Median value of Fare -", median_fare)
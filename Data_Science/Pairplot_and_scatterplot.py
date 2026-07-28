import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt
HouseDF = pd.read_csv('C:\\Users\\ASUS\\Desktop\\classactivity\\Data_Science\\USA_Housing.csv')
HouseDF.head()
HouseDF.info()
HouseDF.columns
sns.pairplot(HouseDF)
plt.show()
sns.heatmap(HouseDF.corr(), annot=True)
plt.show()
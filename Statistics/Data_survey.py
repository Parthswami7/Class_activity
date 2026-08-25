import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Titanic Dataset.csv')
print(data.head(5))

"""#### **Passengers belonging from which gender survived the most**"""
# FIX: Explicitly assign x and data 
sns.countplot(data=data, x='Gender', hue='Survived')
plt.show()

"""#### **Passengers belonging from which PClass survived the most and the least**"""
# FIX: Explicitly assign x and data 
sns.countplot(data=data, x='Pclass', hue='Survived')
plt.show()

"""#### **Highest number of passengers belong to which Age**"""
# FIX: distplot is deprecated in newer Seaborn versions, histplot is the modern replacement
sns.histplot(data=data, x='Age', kde=False, bins=40)
plt.show()

"""#### **Highest number of passengers belong to which Gender**"""
# FIX: Explicitly assign x and data 
sns.countplot(data=data, x='Gender')
plt.show()

"""#### **Is SibSp correlated/associated with Survived feature**"""
sns.countplot(data=data, x='Survived', hue='SibSp', palette="mako")
plt.show()

"""#### **Is Parch correlated/associated with Survived feature**"""
sns.countplot(data=data, x='Survived', hue='Parch', palette="mako")
plt.show()

"""#### **Is the feature Fare having normal distribution/spread of data**"""
# FIX: Changed to histplot and added kde=True to show the distribution curve
sns.histplot(data=data, x='Fare', kde=True)
plt.show()

"""#### **Check the age group of majority of people belonging to PClass=1**"""
sns.boxplot(data=data, x='Pclass', y='Age', palette='winter')
plt.show()

"""#### **Check the correlation of all the features with target variable ‘Survived’**"""
# FIX: Added numeric_only=True to prevent ValueError from non-numeric columns like 'Name' or 'Ticket'
sns.heatmap(data.corr(numeric_only=True)) 
plt.show()
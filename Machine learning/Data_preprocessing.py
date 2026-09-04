import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Read dataset
Titanic = pd.read_csv(r"Titanic Dataset.csv")

# Display first 5 rows
print(Titanic.head())

# Check shape
print(Titanic.shape)

# Check missing values
print(Titanic.isnull().sum())

# Show missing values using heatmap
sns.heatmap(Titanic.isnull(), cmap="spring")
plt.show()

# Display first 5 rows
print(Titanic.head())

# Remove Cabin column
Titanic.drop("Cabin", axis=1, inplace=True)

print(Titanic.head())

# Remove rows containing missing values
Titanic.dropna(inplace=True)

# Check missing values again
sns.heatmap(Titanic.isnull(), cbar=False)
plt.show()

print(Titanic.isnull().sum())

# Convert Gender into dummy variables
print(pd.get_dummies(Titanic["Gender"]).head())

Gender = pd.get_dummies(Titanic["Gender"], drop_first=True)

print(Gender.head(4))

# Convert Embarked into dummy variables
print(pd.get_dummies(Titanic["Embarked"]).head(4))

Embarked = pd.get_dummies(Titanic["Embarked"], drop_first=True)

# Convert Pclass into dummy variables
Pclass = pd.get_dummies(Titanic["Pclass"], drop_first=True)

print(Pclass.head(4))

# Add converted columns to dataset
Titanic = pd.concat([Titanic, Gender, Embarked, Pclass], axis=1)

print(Titanic.head())
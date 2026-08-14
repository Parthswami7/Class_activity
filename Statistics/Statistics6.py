import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 
data = sns.load_dataset('iris')
categories = ['setosa','virginica','versicolor']
data['flower_num'] = pd.Categorical(data['species'],categories, ordered=True)
median_value = np.median(data['flower_num'].cat.codes)
median_text = categories[int(median_value)]
print("Meidan Value of Species -", median_text)
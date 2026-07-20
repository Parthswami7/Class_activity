import pandas as pd 
import matplotlib.pyplot as plt 
countries_df = pd.read_csv('countries.csv')
countries = countries_df
countries.head(3)
c_52 = countries.loc[countries['year'] == 1952 ]
c_52.head()
c_07 = countries.loc[countries['year'] == 2007 ]
c_07.head()
type(c_52)
c_merge = c_52.merge(c_07, left_on='country',right_on='country')
c_merge.head()
c_merge.drop(['year_x', 'year_y'], axis=1)
c_merge.head()

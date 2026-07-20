import numpy as np 
import matplotlib.pyplot as plt 
barwidth = 0.25
fig = plt.subplots(figsize =(12,8))
IT = [12,30,1,8,22]
ECE = [28,6,16,5,10]
CSE = [29,3,24,25,17]
br1 = np.arange(len(IT))
br2 = [x + barwidth for x in br1]
br3 = [x + barwidth for x in br2]
plt.bar(br1, IT, color='r', width= barwidth,edgecolor = 'grey', label = 'IT')
plt.bar(br2, ECE, color='g', width= barwidth, edgecolor = 'grey', label = 'ECE')
plt.bar(br3, CSE, color='b', width= barwidth, edgecolor = 'grey', label = 'CSE')
plt.xlabel('Branch', fontweight = 'bold', fontsize = 15)
plt.ylabel('Students passed', fontweight = 'bold', fontsize = 15)
plt.xticks([r + barwidth for r in range (len(IT))], ['2015', '2016','2017', '2018', '2019'])
plt.legend()
plt.show()
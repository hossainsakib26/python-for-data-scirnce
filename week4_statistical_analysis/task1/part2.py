# imported libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#generate random dataset from 0 to 100 size will be 20
MyDataSet = np.random.randint(low=0, high=101, size=20, dtype='int')
print('\nmyDataSet: ', MyDataSet)

#visualize data point and plot the data set
#in data set x axis size will be 20 and y axis size will be 0 to 100
plt.plot(MyDataSet, marker='v') #marker means design of point
#plt.show()

#get Mean, Mode, Lower quartile, Median, Upper quartile, Interquartile range
MyDataSet1 = pd.Series(data=MyDataSet, dtype='int')
print('\nmy Dataset 1 from line 18:\n', MyDataSet1.to_string())

D = MyDataSet1.describe() #initialise series for numerical description
print('initialise numerical statistical description:\n', D.to_string())

#display statistical values
print('mean: ', np.mean(MyDataSet1))
print('mode: ', MyDataSet1.mode())

print('Lower Quartile (Q1): ', int(D.iloc[4]))
print('median (Q2): ', int(D.iloc[5]))
print('Upper Quartile (Q3): ', int(D.iloc[6]))
print('inter Quartile range: ', int(D.iloc[6]) - int(D.iloc[4]))

S = float(0)
for i in range(0, 20):
    S = S + np.square(MyDataSet[i] - np.mean(MyDataSet))
    SD = np.sqrt(S / MyDataSet.size)

print('Standard deviation using calculation:', round(SD, 2))
print('Standard deviation using Builtin:', round(MyDataSet.std(), 2))
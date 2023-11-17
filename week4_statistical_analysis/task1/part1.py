# imported libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#generate random dataset from 0 to 100 size will be 20
MyDataSet = np.random.randint(low=0, high=100, size=20, dtype='int')
print('\nmyDataSet: ', MyDataSet)

#visualize data point and plot the data set
#in data set x axis size will be 20 and y axis size will be 0 to 100
plt.plot(MyDataSet, marker='v') #marker means design of point
plt.plot()
plt.show()


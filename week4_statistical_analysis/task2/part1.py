# imported libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#initilize 2d array
MyDataSet2 = np.empty(shape=(5,10), dtype=int)
for i in range(0,5):
    for j in range(0, 10):
        MyDataSet2[i,j] = int(np.random.randint(0,10))
#print values
print(MyDataSet2)
#plot first two rows
plt.plot(MyDataSet2[0,], marker='o', color='g')
plt.plot(MyDataSet2[1,], marker='s', color='r')
plt.plot(MyDataSet2[3,], marker='v', color='y')
plt.show() #used to show the plot

#------------------------------------part 2------------------------------------
#get mean mode and standard deviation of each row
MeanByRow = np.mean(MyDataSet2, axis=1)
print('from line 21:', MeanByRow) #shows array of mean
MedianByRow = np.median(MyDataSet2, axis=1)
print('from line 23:', MedianByRow) #shows array of median
SDByRow = np.std(MyDataSet2, axis=1)
print('from line 23:', SDByRow) #shows array of Standard Deviation

#------------------------------------part3--------------------------------------

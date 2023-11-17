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

#Part 3 Initialise a one-dimensional array representing a normal distribution of 1000 data
#points with mean value 17 and standard deviation 0.2.
Mean = float(17.0)
SD = float(0.2)
#dataset size
Size = int(1000)
#generate nomal distribution with 1000 datapoint and mean 17 and SD 0.2
MyDataSet3 = np.random.normal(Mean, SD, Size)
print('from line 37',MyDataSet3)

#------------------------------------part4--------------------------------------

#Find the maximum and the minimum values of the dataset and calculate the range
MinimumValue = round(np.min(MyDataSet3), 2)
print('minimum value of dataset 3: ', MinimumValue)
MaximumValue = round(np.max(MyDataSet3), 2)
print('minimum value of dataset 3: ', MaximumValue)
RangeValue = MaximumValue - MinimumValue
print('Range between minimum and maximum in dataset 3: ', round(RangeValue, 2))

#------------------------------------part5--------------------------------------

#Visualise the dataset by using a histogram with 10 bins. Visualise the probability density function.

#Where X represents the data points, μ is the mean value and σ is the standard deviation

#plot the histogram

A,X,C = plt.hist(MyDataSet3, bins=10, density=True)
#calculate the probability density function
f = (1/ (SD*np.sqrt(2*np.pi)))*np.exp(-((X-Mean)**2/(2*SD**2)))
# Plot the probability density function
plt.plot(X, f)
# Visualise the diagrams
plt.show()
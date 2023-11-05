#imports
import pandas as pd
import numpy as np
import calendar

myArray = np.random.randint(low=65, high=75, size=12)
print(myArray)

#consider myArray to fahrenheit array
fahrenheitArray = myArray
print('Fahrenheit Array: ',fahrenheitArray)

#(32°F − 32) × 5/9 = 0°C
def fahrenheit_to_celsius(temp):
    return round(((temp - 32) * 5/9), 2)

celsius_array = []
for i in range(0, len(fahrenheitArray)):
    celsius_array.append(fahrenheit_to_celsius(fahrenheitArray[i]))

print('celsius array: ', celsius_array)

Months = []
for i in range(1, 13):
    Months.insert(i, calendar.month_name[i])
print('months: ', Months)

#make series
my_series = pd.Series(data=celsius_array, name='average temperature', index=Months)
print('My Series: ', my_series.to_string())

#Mode is the value which occurs most frequently in a dataset
most_frequent_temp = my_series.mode()
print('most frequent temp: ', most_frequent_temp[0])

#count frequent occurance time
count_frequent_values = my_series.value_counts()
print('frequent repeated temperature by occurrence times: ',count_frequent_values.to_string())

print('it happens in',count_frequent_values[most_frequent_temp[0]], 'months')
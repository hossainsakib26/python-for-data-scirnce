import numpy as np
import pandas as pd
import calendar

tempArray = np.array([5.2, 5.3, 7.6, 9.9, 13.3, 16.5, 18.7, 18.5, 15.7, 12.0, 8.0, 5.5], dtype=float)
print('temperature of London: ', tempArray)

Months = []

for i in range(1, 13):
    # Months.append(calendar.month_name[i]) #add value in array using append method
    Months.insert(i, calendar.month_name[i]) #add value in array using insert method

print('\nMonths in a year',Months)

def celcious_to_fahrenheit(temp):
    return round(((temp * (9/5)) + 32), 2)
    # (0°C × 9 / 5) + 32 = 32°F

tempArray_in_fahrenheit = []
for i in range(0, len(tempArray)):
    tempArray_in_fahrenheit.append(celcious_to_fahrenheit(tempArray[i]))

print('temp in fahrenheit: ', tempArray_in_fahrenheit)

my_series = pd.Series(data=tempArray, name='temp in celsius', index=Months)
print('\nmy series in celsius\n',my_series.to_string())

my_series_fahrenheit = pd.Series(data=tempArray_in_fahrenheit, name='temp in fahrenheit', index=Months)
print('\nmy series in fahrenheit\n',my_series_fahrenheit.to_string())
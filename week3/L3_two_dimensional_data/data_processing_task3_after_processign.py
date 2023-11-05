import numpy as np
import pandas as pd

file_path = 'D:\masters gre\python\week3\lab_session/'

#load processed csv
my_dataFrame_3 = pd.read_csv(file_path+'NewFile.csv', delimiter=',')

#store description column 'median_house_value' in a series
median_house_value_Series_A = my_dataFrame_3['median_house_value'].describe()
print('series of median_house_value: \n', median_house_value_Series_A.to_string())
print('mean of median_house_value\n', median_house_value_Series_A[1])
print('median of median_house_value\n', median_house_value_Series_A[5])

#range calculation
print('range calculation: \n', median_house_value_Series_A[7] - median_house_value_Series_A[3])

#convert median income column with multipling 10,000
for i in range(0, 25):
    my_dataFrame_3.at[i, 'median_income'] = (my_dataFrame_3.at[i, 'median_income']*10000)

print('new dataframe content: \n', my_dataFrame_3.to_string())
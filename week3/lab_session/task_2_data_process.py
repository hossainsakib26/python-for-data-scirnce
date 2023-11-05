import pandas as pd
import numpy as np
import calendar

file_path = 'D:\masters gre\python\week3\lab_session/'

data_frame = pd.read_csv(file_path+'Dataset.csv', delimiter=',')
print(data_frame.to_string())

#missing or NAN values
print('\n',data_frame[data_frame.isnull().T.any()].to_string())

#access single points or cell
print('access single points or cell: ',data_frame.at[11, 'ocean_proximity'])

#set value to specific cell by observing others
data_frame.at[11, 'ocean_proximity'] = 'INLAND'
print('new value of cell cell: ',data_frame.at[11, 'ocean_proximity'])
#if any value can not be guess row could be deleted
data_frame1 = data_frame.dropna()

print('new data frame: ', data_frame1.to_string())

#duplicat rows
duplicates = data_frame1.duplicated()
print('duplicates files:\n',duplicates.to_string())

#drop duplicates data
data_frame2 = data_frame1.drop_duplicates()
print('data frame after removing duplicates\n', data_frame2.to_string())


#column 3 shows 4 deciml place for housing_median age which is not necessary
#set values with an integer variable
temp = int(data_frame2.at[3, 'housing_median_age'])
data_frame2.at[3, 'housing_median_age'] = temp

print(data_frame2.to_string())

#fixed the incorrect values of ocean proximity in rows 17, 18
#initialise variable correct the value and get the value from row 16

print('ocean proximity: for 16 no Row', data_frame2.at[16, 'ocean_proximity'])
#set data type
data_frame2['ocean_proximity'].apply(str)

#assign the value we got from row 16
data_frame2.at[17, 'ocean_proximity'] = data_frame2.at[16, 'ocean_proximity']
data_frame2.at[18, 'ocean_proximity'] = data_frame2.at[16, 'ocean_proximity']

print('after change values of ocean proximity for row 17, 18\n',data_frame2.to_string())

#save dataframe into new csv
data_frame2.to_csv(file_path+'NewFile.csv', index=False) #set a name for csv, ignore column number using index

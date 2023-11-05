#imports
import pandas as pd

#read the file
#data load into dataframe from csv file.
file_path = str('D:\masters gre\python\week3') #set file's path
#load the csv file into dataframe
my_data_frame = pd.read_csv(file_path+'\Vehicles.csv', delimiter=',')

print(my_data_frame.to_string())
#read end

#get duplicats
#print the data frame
print('Duplicate rows:\n', my_data_frame.duplicated().to_string())
#finding duplicates end

#remove duplicate rows
data_frame_without_duplicates = my_data_frame.drop_duplicates()
#print in data frame
#remove ends

#initilise value where NaN
my_data_frame_1 = data_frame_without_duplicates
# print('\tdata frame without duplicates\n', my_data_frame_1.to_string())

#missing value at row 6
#initialising values with 0 where NaN using at method.

my_data_frame_1.at[6, '2018Q1'] = int(0)
my_data_frame_1.at[6, '2018Q2'] = int(0)
my_data_frame_1.at[6, '2018Q3'] = int(0)
my_data_frame_1.at[6, '2018Q4'] = int(0)
my_data_frame_1.at[6, '2019Q1'] = int(0)

print('\t0 replace to NAN\n',my_data_frame_1.to_string())

#remove row where value is missing
my_data_frame_2 = my_data_frame_1.dropna()
print('dataframe after drop:\n', my_data_frame_2.to_string())

#make field float to integer
my_data_frame_2.at[3, '2019Q1'] = round(int(my_data_frame_2.at[3, '2019Q1']))
print('make 2019Q1 field integer:\n', my_data_frame_2.to_string())

#change the magnitude of the value
my_data_frame_2.at[4, 'Price'] = int(my_data_frame_2.at[4, 'Price'] * 1000)
print('after change the magnitude of the value:\n', my_data_frame_2.to_string())

# Reset the indices with the 'in-place' option
my_data_frame_2.reset_index(drop=True, inplace=True)
# Display the updated data frame
print('\tafter reset the indicates\n',my_data_frame_2.to_string())

#Generate numerical description into a separate data frame
D = my_data_frame_2.describe()
print(round(D, 3))
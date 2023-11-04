#imports
import numpy as np
import pandas as pd

#read the file
#data load into dataframe from csv file.
file_path = str('D:\masters gre\python\week3') #set file's path
#load the csv file into dataframe
my_data_frame = pd.read_csv(file_path+'\Vehicles.csv', delimiter=',')

# print(my_data_frame.to_string())
#read end

#get duplicats
#dataset path
file_path_2 = str('D:\masters gre\python\week3')
#for setting the file name and reading file
my_data_frame_2 = pd.read_csv(file_path_2+'\Vehicles.csv', delimiter=',')
#print the data frame
print(my_data_frame_2.to_string())
print('Duplicate rows:\n', my_data_frame_2.duplicated())
#duplicate end

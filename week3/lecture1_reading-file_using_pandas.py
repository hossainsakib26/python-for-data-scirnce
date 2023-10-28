import pandas as pd

my_data_Frame = pd.DataFrame(index=[1, 2, 5, 3], columns=['city', 'population', 'country'])
my_data_Frame.loc[1, 'city'] = 'Dhaka'
my_data_Frame.loc[1, 'population'] = 23400019
my_data_Frame.loc[1, 'country'] = 'Bangladesh'

my_data_Frame.loc[2, 'city'] = 'Delhi'
my_data_Frame.loc[2, 'population'] = 53400219
my_data_Frame.loc[2, 'country'] = 'India'

my_data_Frame.loc[3, 'city'] = 'London'
my_data_Frame.loc[3, 'population'] = 2400219
my_data_Frame.loc[3, 'country'] = 'United Kingdom'

my_data_Frame.loc[4, 'city'] = 'New Yourk'
my_data_Frame.loc[4, 'population'] = 3400219
my_data_Frame.loc[4, 'country'] = 'United States'

my_data_Frame.loc[5, 'city'] = 'Lisbon'
my_data_Frame.loc[5, 'population'] = 3400219
my_data_Frame.loc[5, 'country'] = 'portugal'

try:
    my_data_Frame.to_csv('My_data_frame.csv')
except:
    print('writing failure! Because file is open!')
finally:
    print('save successfully')

try:
    reading_file = pd.read_csv('My_data_frame.csv', index_col=0)
    print(reading_file.head())
except:
    print('not possible to read')
finally:
    print('done!')
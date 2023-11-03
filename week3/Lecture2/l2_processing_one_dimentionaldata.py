import pandas as pd
#initialise series directly
#without index
my_series = pd.Series(data=[2,3,4,5], dtype='int')
# print('without .to_string()\n', my_series)
# print('with .to_string()\n', my_series.to_string())

#with index
my_series_with_index = pd.Series(data=[2,3,4,5], index=['a','b','c','d'], dtype='int')

#print('\n',my_series_with_index)

print('\ninitialise series from list')
arrList = [32,12,4,11,26,2,5]
my_series_from_list = pd.Series(data=arrList, dtype='int')
# print(my_series_from_list.to_string())
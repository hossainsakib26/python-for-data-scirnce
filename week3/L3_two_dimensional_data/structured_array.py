#imports
import numpy as np
import pandas as pd

structured_arr_A = np.empty(shape=5, dtype=[('Title', 'U10'), ('Year', int), ('Price', float)])

#print('structured array: ', structured_arr_A)

structured_arr_A[0] = ('Mathematics', 2021, 4)
structured_arr_A[1] = ('Biology', 2019, 4.5)
structured_arr_A[2] = ('Law', 2023, 3)
structured_arr_A[3] = ('Data Science', 2011, 4.54)
structured_arr_A[4] = ('History', 2015, 5)

print(structured_arr_A)

#initialise dataframe using constants
Dataframe = pd.DataFrame(columns=['A', 'B'], data=[[1,2],[3,4],[5,6]])
print(Dataframe.to_string())
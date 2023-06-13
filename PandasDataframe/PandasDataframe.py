'''File: PandasDataframe.py
Author: Bobby Parsons
Date: 9/21/21

Shows the capabilities of Dataframes in the pandas library
'''

import pandas as pd

temp_data_dict = {'Day of week': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
'Max Temp': [47, 44, 33, 34, 30, 29, 45],
'Min Temp': [36, 30, 27, 30, 16, 12, 24]}

temp_data = pd.DataFrame(data=temp_data_dict)

# print(temp_data)

print('Mean: ')
print(temp_data.mean(axis=0,numeric_only=True))
print('Standard deviation: ')
print(temp_data.std(axis=0,numeric_only=True))
print('Minimum: ')
print(temp_data.min(axis=0,numeric_only=True))
print('Maximum: ')
print(temp_data.max(axis=0,numeric_only=True))

snow_data_dict = {'Day of week': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
'Precip': [0.21, .01, 0, .01 , 0.01, 0, 0],
'New Snow': [0, 0, 0, 0.1, 0.3, 0, 0]}

snow_data = pd.DataFrame(data=snow_data_dict)

# print(snow_data)

merged_data = snow_data.merge(temp_data, how='left', on = ['Day of week'])

print(merged_data)

merged_data.set_index('Day of week', inplace=True)

ave_temps = []

for i in merged_data.index:
    merged_data.at[i, 'Max Temp'] = (merged_data.at[i, 'Max Temp'] - 32) * 5 / 9
    merged_data.at[i, 'Min Temp'] = (merged_data.at[i, 'Min Temp'] - 32) * 5 / 9

    ave_temps.append((merged_data.at[i, 'Max Temp'] + merged_data.at[i, 'Min Temp']) / 2)

merged_data['Ave Temp'] = ave_temps

# no need to reindex I guess, it's already in the right place

print(merged_data)
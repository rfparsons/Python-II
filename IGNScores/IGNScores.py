'''File: IGNScores.py
Author: Bobby Parsons
Date: 9/21/21

Uses pandas to display information about review scores from IGN
'''

import pandas as pd

scores = pd.read_csv('ign.csv')

# print(scores.head())
print(scores.shape)

scores = scores.iloc[:, 1:]

print(scores.loc[:, ['title', 'genre', 'release_year']])

print('Score data:')
mean = scores['score'].mean()
print('Mean: ' + str(mean))
print('Max: ' + str(scores['score'].max()))
print('Standard deviation: ' + str(scores['score'].std()))

for i in scores.index:
    scores.at[i, 'score'] = scores.at[i, 'score'] * 10

above_average = scores.loc[scores['score'] > mean * 10]

# print(above_average.shape)

print(above_average['platform'].value_counts())
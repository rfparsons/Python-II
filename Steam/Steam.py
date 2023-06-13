'''File: Steam.py
Author: Bobby Parsons
Date: 9/27/21

Uses pandas to display information about games available on Steam
'''

from numpy import True_
import pandas as pd

# Load the dataset into a Pandas dataframe (please put the file in the same directory as your program when importing for grading simplicity)
games = pd.read_csv('steam.csv')

print(games.shape)

# Create a new dataframe from the original that only contains data for publishers that have at least 50 positive ratings.
#     Create a temp frame that is grouped by publisher and summed
publisher_frame = games.groupby(['publisher']).sum()
#print(publisher_frame['positive_ratings'])

#     From this grouped frame create a list of rows that need to be deleted based on having less than 50 positive ratings
rows_to_delete = publisher_frame[publisher_frame['positive_ratings'] < 50].index
print(rows_to_delete.shape)
# rows_to_delete = list(rows_to_delete)

# Using your list of publishers to delete and your original dataframe, create a new dataframe that has the publishers with at least 50 ratings
filtered_games = games.set_index('publisher').drop(rows_to_delete)
print(filtered_games.shape)

# Sort your new dataframe descending on positive ratings.  Your top name should be "Counter-Strike: Global Offensive"
filtered_games.sort_values(by='positive_ratings', inplace=True, ascending=False)
# print(filtered_games['name'])

# Do a describe on the frame to see some quick stats on it
print(filtered_games.describe())

# Remove the appid column using iloc because we don't need it
filtered_games = filtered_games.iloc[:, 1:]

# Remove any rows for games that have less than 20000 owners
filtered_games = filtered_games.loc[filtered_games['owners'] != '0-20000']
print(filtered_games.shape)

#--------------------------Assignment 2--------------------------

# Create a frame from your original dataset that includes owners, positive ratings, and negative ratings
owners_frame = games.loc[:, ['owners', 'positive_ratings', 'negative_ratings']]

# Group the frame by owners and sum it
owners_frame = owners_frame.groupby('owners').sum()

# Print the grouped, summed frame
print(owners_frame)

# Add % positive and % negative columns
pc_positive = [] # "pc" meaning PerCent
pc_negative = []

for i in owners_frame.index:
    positives = owners_frame.at[i, 'positive_ratings']
    negatives = owners_frame.at[i, 'negative_ratings']

    pc_positive.append(positives / (positives + negatives))
    pc_negative.append(negatives / (positives + negatives))

owners_frame['%_positive'] = pc_positive
owners_frame['%_negative'] = pc_negative

# sort the frame
owners_frame.sort_values(by='%_positive', inplace=True, ascending=False)

print(owners_frame)

# Create a frame that has publisher, positive_ratings, negative ratings, using your dataframe from the end of the topic 1 assignment
publisher_ratings = filtered_games.loc[:, ['positive_ratings', 'negative_ratings']]

# group and sum
publisher_ratings_sum = publisher_ratings.groupby('publisher').sum()
print(publisher_ratings_sum)

# Add % positive and % negative columns
pc_positive = [] # "pc" meaning PerCent
pc_negative = []

for i in publisher_ratings_sum.index:
    positives = publisher_ratings_sum.at[i, 'positive_ratings']
    negatives = publisher_ratings_sum.at[i, 'negative_ratings']

    pc_positive.append(positives / (positives + negatives))
    pc_negative.append(negatives / (positives + negatives))

publisher_ratings_sum['%_positive'] = pc_positive
publisher_ratings_sum['%_negative'] = pc_negative

# sort the frame
publisher_ratings_sum.sort_values(by='%_positive', inplace=True, ascending=False)

print(publisher_ratings_sum)

# Dexion games appears to be left due to having more than 50 total ratings in the raw data. 
# I'm not totally sure why it's set to 1 rating at this point, might be an issue with how it was filtered

#drop rows that don't have at least 1000 positive ratings
rows_to_delete = publisher_ratings_sum[publisher_ratings_sum['positive_ratings'] < 1000].index
print(rows_to_delete.shape)

publisher_ratings_sum.drop(rows_to_delete, inplace=True)

print(publisher_ratings_sum)

# Drop publishers with less than 5 games
publisher_games = publisher_ratings.reset_index()['publisher'].value_counts()
#print(publisher_games)
rows_to_delete = publisher_ratings_sum[publisher_games < 5].index
publisher_ratings_sum.drop(rows_to_delete, inplace=True)

print(publisher_ratings_sum)
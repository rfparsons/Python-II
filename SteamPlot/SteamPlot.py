'''File: SteamPlot.py
Author: Bobby Parsons
Date: 10/6/21

Uses pandas to display information about games available on Steam
'''

from numpy import True_
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset into a Pandas dataframe (please put the file in the same directory as your program when importing for grading simplicity)
games = pd.read_csv('steam.csv')

# Create a new dataframe from the original that only contains data for publishers that have at least 50 positive ratings.
#     Create a temp frame that is grouped by publisher and summed
publisher_frame = games.groupby(['publisher']).sum()
#print(publisher_frame['positive_ratings'])

#     From this grouped frame create a list of rows that need to be deleted based on having less than 50 positive ratings
rows_to_delete = publisher_frame[publisher_frame['positive_ratings'] < 50].index
# rows_to_delete = list(rows_to_delete)

# Using your list of publishers to delete and your original dataframe, create a new dataframe that has the publishers with at least 50 ratings
filtered_games = games.set_index('publisher').drop(rows_to_delete)

# Sort your new dataframe descending on positive ratings.  Your top name should be "Counter-Strike: Global Offensive"
filtered_games.sort_values(by='positive_ratings', inplace=True, ascending=False)
# print(filtered_games['name'])

# Remove the appid column using iloc because we don't need it
filtered_games = filtered_games.iloc[:, 1:]

# Remove any rows for games that have less than 20000 owners
filtered_games = filtered_games.loc[filtered_games['owners'] != '0-20000']

# below code didn't produce an interesting graph

# # Create a frame from your original dataset that includes owners, positive ratings, and negative ratings
# ratings_frame = games.loc[:, ['name', 'positive_ratings', 'negative_ratings']]

# # Add % positive and % negative columns
# pc_positive = [] # "pc" meaning PerCent
# pc_negative = []

# for i in ratings_frame.index:
#     positives = ratings_frame.at[i, 'positive_ratings']
#     negatives = ratings_frame.at[i, 'negative_ratings']

#     pc_positive.append(positives / (positives + negatives))
#     pc_negative.append(negatives / (positives + negatives))

# ratings_frame['%_positive'] = pc_positive
# ratings_frame['%_negative'] = pc_negative

# # sort the frame
# ratings_frame.sort_values(by='%_positive', inplace=True, ascending=False)

# #drop rows that don't have at least 1000 positive ratings
# rows_to_delete = ratings_frame[ratings_frame['positive_ratings'] < 1000].index
# print(rows_to_delete.shape)

# ratings_frame.drop(rows_to_delete, inplace=True)

# best_games = ratings_frame[:10].loc[:, ['name', '%_positive']]

# plt.bar(best_games['name'], best_games['%_positive'])

# Create a frame that has publisher, positive_ratings, negative ratings, using your dataframe from the end of the topic 1 assignment
publisher_ratings = filtered_games.loc[:, ['positive_ratings', 'negative_ratings']]

# group and sum
publisher_ratings_sum = publisher_ratings.groupby('publisher').sum()

# Add % positive and % negative columns
pc_positive = [] # "pc" meaning PerCent
# pc_negative = []

for i in publisher_ratings_sum.index:
    positives = publisher_ratings_sum.at[i, 'positive_ratings']
    negatives = publisher_ratings_sum.at[i, 'negative_ratings']

    pc_positive.append(positives / (positives + negatives))
    # pc_negative.append(negatives / (positives + negatives))

publisher_ratings_sum['%_positive'] = pc_positive
# publisher_ratings_sum['%_negative'] = pc_negative

# Get the publishers with the most games
publisher_games = publisher_ratings.reset_index()['publisher'].value_counts()
publisher_games.sort_values(inplace=True, ascending=False)
#print(publisher_games)
rows_to_delete = publisher_ratings_sum[publisher_games < 45].index
top_publishers = publisher_ratings_sum.drop(rows_to_delete)

# print(publisher_games)
# print(publisher_ratings_sum)

top_publishers.reset_index(inplace=True)

plt.bar(top_publishers['publisher'], top_publishers['%_positive'] * 100)
plt.xticks(rotation=45, size=7, ha='right')
plt.title("Overall rating of publishers on Steam with 45 or more games\nwith more than 20,000 owners")
plt.tight_layout()

plt.show()

# Create a frame from your original dataset that includes owners, positive ratings, and negative ratings
ratings_frame = games.loc[:, ['publisher', 'positive_ratings', 'negative_ratings']]

# Add % positive and % negative columns
pc_positive = [] # "pc" meaning PerCent
# pc_negative = []

for i in ratings_frame.index:
    positives = ratings_frame.at[i, 'positive_ratings']
    negatives = ratings_frame.at[i, 'negative_ratings']

    pc_positive.append(positives / (positives + negatives))
    # pc_negative.append(negatives / (positives + negatives))

ratings_frame['%_positive'] = pc_positive
# ratings_frame['%_negative'] = pc_negative

# Add one-word summaries of the review scores
review_summary = []

for i in ratings_frame.index:
    score = ratings_frame.at[i, '%_positive']

    if (score >= 0.70):
        summary = 'Positive'
    elif (score <= 0.30):
        summary = 'Negative'
    else:
        summary = 'Mixed'

    review_summary.append(summary)

ratings_frame['summary'] = review_summary

# print(publisher_ratings_sum.reset_index()[publisher_ratings_sum.reset_index()['publisher'] == 'SEGA'])

grouped_ratings = ratings_frame.groupby(['publisher','summary']).size().reset_index()

# print(grouped_ratings)

fig, axs = plt.subplots(2,2, gridspec_kw={'width_ratios':[3,3],'height_ratios':[3,3]}, sharey="all", sharex="all") # Can change each figure here

sega = grouped_ratings[grouped_ratings['publisher'] == 'SEGA']
ea = grouped_ratings[grouped_ratings['publisher'] == 'Electronic Arts']
deep_silver = grouped_ratings[grouped_ratings['publisher'] == 'Deep Silver']
valve = grouped_ratings[grouped_ratings['publisher'] == 'Valve']

sega.columns = ['publisher', 'summary', 'games']
ea.columns = ['publisher', 'summary', 'games']
deep_silver.columns = ['publisher', 'summary', 'games']
valve.columns = ['publisher', 'summary', 'games']

axs[0,0].bar(sega['summary'], sega["games"], color=['yellow', 'red', 'green'])
axs[0,0].axes.get_xaxis().set_visible(False)
axs[0,0].title.set_text("SEGA")
axs[1,1].bar(ea['summary'], ea["games"], color=['yellow', 'red', 'green'])
axs[1,1].axes.get_xaxis().set_visible(True)
axs[1,1].title.set_text("EA")
axs[1,0].bar(deep_silver['summary'], deep_silver["games"], color=['yellow', 'red', 'green'])
axs[1,0].axes.get_xaxis().set_visible(True)
axs[1,0].title.set_text("Deep Silver")
axs[0,1].bar(valve['summary'], valve["games"], color=['yellow', 'green']) # No negative reviews for Valve!
axs[0,1].axes.get_xaxis().set_visible(False)
axs[0,1].title.set_text("Valve")

plt.show()
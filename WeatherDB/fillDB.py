'''File: fillDB.py
Author: Bobby Parsons
Date: 10/12/21

Fills in the weather daya for Polk and Story county from a CSV file and plots it
'''

import csv
from DBlib import *
import pandas as pd
import matplotlib.pyplot as plt

database = 'weather_tracking.db'
conn = create_connection(database)
cur = conn.cursor()

counties = [('Polk', 'IA'), ('Dallas', 'IA')]

cur.executemany('REPLACE INTO Location (county, state) VALUES (?, ?)', counties)

with open('weather.csv','r') as input_file:
    data = csv.DictReader(input_file)
    to_db = [(i['COUNTY'],i['DATE'],i['PRCP']) for i in data]
    
    to_db_data_insert = [[] for item in to_db]
    for x in range(0,len(to_db)):
        to_db_data_insert[x] = tuple([to_db[x][0],to_db[x][1],to_db[x][2]])

cur.executemany('REPLACE INTO Precipitation (location, date, precipitation) VALUES (?, ?, ?)', to_db_data_insert)

conn.commit()

weather_df = pd.read_sql_query("SELECT * FROM Precipitation",conn)

data_polk = weather_df[weather_df['location'] == "Polk"]
data_polk.sort_values('date',inplace=True)
plot_y_polk = list(data_polk['precipitation'])

data_story = weather_df[weather_df['location'] == "Story"]
data_story.sort_values('date',inplace=True)
plot_y_story = list(data_story['precipitation'])

plot_x = list(data_polk['date'])
# print(plot_x)

ax = plt.subplot(111)
plt.rcParams['figure.dpi'] = 250

ax.plot(plot_x, plot_y_polk, color='g',label="Polk County, IA")
ax.plot(plot_x, plot_y_story, color='orange',label = "Story County, IA")

ax.axes.set_xticks(plot_x)
ax.axes.set_xticklabels(plot_x,rotation = 45,ha ='right',Fontsize=5)
ax.legend()
ax.title.set_text('Precipitation in October 2020 in Polk and Story County, IA')

plt.show()

conn.close()
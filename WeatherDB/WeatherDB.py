'''File: WeatherDB.py
Author: Bobby Parsons
Date: 10/12/21

Uses a sqlite3 database to store weather information
'''
import sqlite3
from sqlite3 import Error
from DBlib import *

database = "weather_tracking.db"

sql_create_precipitation_table = """ CREATE TABLE IF NOT EXISTS Precipitation (
                                        location text,
                                        date text, 
                                        precipitation float, 
                                        precip_type text,
                                        FOREIGN KEY (location) 
                                            REFERENCES Location (county)
                                    ); """

sql_create_location_table = """CREATE TABLE IF NOT EXISTS Location (
                                    county text PRIMARY KEY,
                                    state text
                                );"""

if (__name__ == '__main__'):
    # create a database connection and database if it doesn't already exist
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create Location table
        create_table(conn, sql_create_location_table)

        # create Precipitation table
        create_table(conn, sql_create_precipitation_table)

        # Code pulled/modified from https://stackoverflow.com/questions/305378/list-of-tables-db-schema-dump-etc-using-the-python-sqlite3-api
        # Using with command to automatically close the connection

        with conn as db:
            newline_indent = '\n   '

            cur = db.cursor()

            result = cur.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
            table_names = sorted(list(zip(*result))[0])
            print ("\ntables are:"+newline_indent+newline_indent.join(table_names))

            for table_name in table_names:
                result = cur.execute("PRAGMA table_info('%s')" % table_name).fetchall()
                column_names = list(zip(*result))[1]
                print (("\ncolumn names for %s:" % table_name)
                       +newline_indent
                       +(newline_indent.join(column_names)))
    else:
        print("Error! cannot create the database connection.")
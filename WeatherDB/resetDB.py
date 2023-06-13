#Sometimes, you just need to wipe the table clean so you can reimport.  Here's a code snippet to do that.

import sqlite3
from sqlite3 import Error
from DBlib import *

database = 'weather_tracking.db'

conn = create_connection(database)
cur = conn.cursor()

cur.execute("DELETE FROM Location")
cur.execute("DELETE FROM Precipitation")

conn.commit()
conn.close()
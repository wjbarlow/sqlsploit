__author__ = 'will@threadtheweb.co.uk'
# Search implementation - Keyword Table Search
from sqlsploit.dbconnector import *

# Select database to be searched


# Search for keyword matching for table names
# CHOICE - using database scheme now, could potentially just search table names instead
cur = conn.cursor()

cur.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME like '%user%' AND TABLE_SCHEMA = 'test'")

print(cur.description)

print()

for row in cur:
    print(row)

    cur.close()
    conn.close()
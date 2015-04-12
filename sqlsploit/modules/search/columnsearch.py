from sqlsploit.dbconnector import *
from sqlsploit.cli import *

__author__ = 'will@threadtheweb.co.uk'
# Search implementation - Keyword Column Search
import PyMySQL

# Select database to be searched


# Select tables to be searched


# Keyword based matching for column names for each table
def mysqlcolumnsearch(host, username, password, keyword, ):
    conn = PyMySQL.connect(host=host, port=3306, user=username, passwd=password, db='test')
    cur = conn.cursor()
    logging.info("Connected to MySQL")
    cur.execute("SHOW COLUMNS FROM users LIKE '%?%'", keyword)
    count = 0
    print('Column Matches:')
    print(cur.description)
    print()

    for row in cur:
        print(row)
        count += 1
    print("%s rows." % count)

    cur.close()
    conn.close()
    logging.info('Closed SQL Connection')

__author__ = 'will@threadtheweb.co.uk'
# dbconnector.py - connect to databases

# import modules
import PyMySQL

from sqlsploit.cli import *


# import classes


# Connect to MySQL
def mysqlconnect(host, username, password):
    conn = PyMySQL.connect(host=host, port=3306, user=username, passwd=password, db='test')
    cur = conn.cursor()
    logging.info("Connected to MySQL")
    cur.execute("SELECT firstname,lastname FROM users")
    print(cur.description)
    print()
    logging.info("connect to %s" % host)

    for row in cur:
        print(row)

        cur.close()
        conn.close()
        logging.info('Closed SQL Connection')

# Connect to SQL Server
# Connect to Oracle
# Connect to Postgresql
# Connect to SQLite
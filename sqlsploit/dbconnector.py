__author__ = 'will@threadtheweb.co.uk'
# dbconnector.py - connect to databases

# import modules
#import MySQLdb
import sys
import click
import SQLAlchemy
import peewee

from peewee import *

# Connect to MySQL
db = MySQLDatabase('test', user='test', passwd='test')

#class

#SQLAlchemy.create_engine('mysql://')

#connection = MySQLdb.connect(host="127.0.0.1")

#from sqlalchemy import create_engine
#engine = create_engine('sqlite:///:memory:', echo=True)

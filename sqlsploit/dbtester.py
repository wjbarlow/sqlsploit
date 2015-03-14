__author__ = 'will@threadtheweb.co.uk'
# SQLLite DB Test Creation

from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:', echo=True)

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

metadata = MetaData()
users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('password', String),
              )

userinfo = Table('userinfo', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('user_id', None, ForeignKey('users.id')),
                 Column('national_insurance', String, nullable=False),
                 Column('passport', String, nullable=False)
                 )
metadata.create_all(engine)
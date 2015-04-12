__author__ = 'will@threadtheweb.co.uk'
# SQLLite DB Test Creation

from peewee import *


db = SqliteDatabase('test.db')


class Users(Model):
    ID = int()
    username = CharField()
    password = CharField()
    email = CharField()


class UserInfo(Model):
    ID = ForeignKeyField(Users, related_name='ID')
    NI = CharField()
    passport = CharField()


class Meta:
    database = db
    db._connect()
    db.create_tables([Users, UserInfo])

    user1 = Users(ID='1', password='password1', email='test1@test.com')
    user2 = Users(ID='2', password='password2', email='test2@test.com')
    user3 = Users(ID='3', password='password3', email='test3@test.com')
    userinfo1 = UserInfo(NI='NI1', passport='passport1')
    userinfo2 = UserInfo(NI='NI2', passport='passport2')
    userinfo3 = UserInfo(NI='NI3', passport='passport3')
    user1.save()
    user2.save()
    user3.save()
    userinfo1.save()
    userinfo2.save()
    userinfo3.save()
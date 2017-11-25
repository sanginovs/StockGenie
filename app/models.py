from peewee import *
import os

# Create a database
from app.loadConfig import *
here = os.path.dirname(__file__)
cfg       = load_config(os.path.join(here, 'config.yaml'))
mainDB    = SqliteDatabase(cfg['databases']['dev'])

# Creates the class that will be used by Peewee to store the database
class dbModel (Model):
  class Meta: 
    database = mainDB
    
"""
When adding new tables to the DB, add a new class here 
Also, you must add the table to the config.yaml file

Example of creating a Table

class tableName (dbModel):
  column1       = PrimaryKeyField()
  column2       = TextField()
  column3       = IntegerField()

For more information look at peewee documentation
"""

class Stocks (dbModel):
    sid = PrimaryKeyField()
    companyName = TextField()
    stockAbbr = TextField(unique=True)
    timesSearched = IntegerField()
  
  
class Users (dbModel):
    uid = PrimaryKeyField()
    firstName = TextField()
    lastName = TextField()
    username  = TextField(unique = True)
    password = TextField()
    email = TextField(unique = True)
    timestamp = TimestampField()
  
class Predictions (dbModel):
    pid = PrimaryKeyField()
    uid = ForeignKeyField(Users)
    sid = ForeignKeyField(Stocks)
    open = FloatField()
    high = FloatField()
    low = FloatField()
    close = FloatField()
    timestamp = TimestampField()

class FavoriteStocks(dbModel):
    fid = PrimaryKeyField()
    uid = ForeignKeyField(Users)
    sid = ForeignKeyField(Stocks)


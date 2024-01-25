from peewee import Model
from peewee import CharField, DateField, BooleanField
from database import database
from datetime import datetime

class Todo(Model):
    name = CharField()
    completed = BooleanField(default=False)
    createdAt = DateField(datetime.now().strftime('%x'))
    
    class Meta:
        database = database
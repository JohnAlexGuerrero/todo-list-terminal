from peewee import Model
from peewee import CharField, ManyToManyField, DecimalField
from todo import Todo
from database import database

class Task(Model):
    title = CharField()
    todos = ManyToManyField(Todo, backref='todos')
    progress = DecimalField(max_digits=3, decimal_places=1, auto_round=True)
    
    class Meta:
        database = database
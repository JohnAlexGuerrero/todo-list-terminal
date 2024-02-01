from peewee import Model
from peewee import CharField, TextField
from database import database

class Commands(Model):
    name = CharField(unique=True)
    description = TextField()
    syntax = CharField()
    error = CharField()
    
    class Meta:
        database = database
        
    def poblations(self, arr):
        for x in arr:
            co = Commands(name=x['name'], description=x['description'],syntax=x['syntax'])
            if co:
                co.save()

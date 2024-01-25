from peewee import Model
from peewee import CharField, TextField
from database import database
from migrations_commands import comands

class Commands(Model):
    name = CharField(unique=True)
    description = TextField()
    syntax = CharField()
    
    class Meta:
        database = database
        
    def poblations(self, *args, **kwargs):
        for x in comands:
            co = Commands(name=x['name'], description=x['description'],syntax=x['syntax'])
            if co:
                co.save()
        # return super(Commands, self).save(*args, **kwargs)
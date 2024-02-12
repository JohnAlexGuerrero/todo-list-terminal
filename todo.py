from peewee import Model
from peewee import CharField, DateField, BooleanField, TimeField
from database import database
from datetime import datetime

class Todo(Model):
    description = CharField(max_length=150)
    is_priority  = BooleanField(default=False)
    completed = BooleanField(default=False)
    createdAt = DateField(datetime.now().strftime('%d, %B %Y'))
    do_it_in = DateField(datetime.now().strftime('%d, %B %Y'))
    time = TimeField(datetime.now().strftime('%H:%M'))
    
    class Meta:
        database = database
        
    def three_priority(self):
        if self.is_priority:
            return True
        return False
    
    def all_todos(self):
        todos = Todo.select()
        data = []
        
        for todo in todos:
            data.append({"description": todo.description.upper()})
            
        return data
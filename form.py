from datetime import datetime
from todo import Todo

class Form:
    def __init__(self, description, is_priority, do_it, time) -> None:
        self.description = description
        self.is_priority = is_priority.lower()
        self.created_at = datetime.now()
        self.do_it = do_it
        self.time = time
    
    def is_valid(self)->bool:
        if self.description_valid() and self.is_priority_valid() and self.date_do_it_valid():
          return True
        return False
    
    def description_valid(self):
        if self.description == None:
            return False
        elif len(self.description) > 150:
            return False
        elif self.description == ' ':
            return False
        return True
    
    def is_priority_valid(self):
        if self.is_priority in ['yes','no','y','n','si','s']:
            if self.is_priority in ['yes','y','si','s']:
                self.is_priority = True
            if self.is_priority in ['no','n']:
                self.is_priority = False
            
            return True
        return False
    
    def date_do_it_valid(self):
        day, month, year = [int(f) for f in self.do_it.split('-')]
        if day < 31 and month < 12 and year < 2050:
            self.do_it = datetime(year, month, day)
            return True
        return False
    
    def save(self):
        todo = Todo(
            description=self.description,
            is_priority=self.is_priority,
            createdAt=self.created_at,
            do_it_in=self.do_it,
            time=self.time,
        )
        
        todo.save()
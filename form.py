class Form:
    def __init__(self, description, is_priority, completed, createdAt, do_it, time) -> None:
        self.description = description
        self.is_priority = is_priority
        self.completed = completed
        self.createdAt = createdAt
        self.do_it = do_it
        self.time = time
    
    def is_valid(self)->bool:
        
        return False
    
    def description_valid(self):
        if self.description != None:
            return False
        elif len(self.description) > 50:
            return False
        elif self.description:
            pass
        return True
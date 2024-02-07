from help import Help

class Terminal:
    
    def __init__(self, action, key_name, description=None) -> None:
        self.action = action
        self.key_name = key_name
        self.description_ = description
    
    def action_is_valid(self):
        actions = ['create','update','delete','']
        return True
    
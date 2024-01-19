from datetime import datetime
from todo import Todo
from typing import List

class UI:
    def __init__(self) -> None:
        self.todos = self.getTodos()
        self.datetime = datetime.today()
       
    def add(self, todo):
        todo = Todo.create(name=todo, completed=False, createdAt=self.datetime)
        if todo:
            return True
        return False

    def getTodos(self):
        self.todos = Todo.select()
        return self.todos
    
    def showTodos(self):   
        if len(self.todos) == 0:
            print('\nNo hay tareas pendientes.')
            return '\n'
        
        for todo in self.getTodos():
            print(self.getTodo(todo.id))
    
    def getTodo(self, id):
        todo = Todo.get(Todo.id==id)
        if todo:
            return f'{todo.id}->{'[X]' if todo.completed else '[ ]'} {todo.name.capitalize()}'
        return 'Todo not exist.'
    
    def actions(self, action=[]):
        todo = ''
        
        if len(action)==1:
            if action[0] == 'todos':
                self.showTodos()
        
        if len(action) >= 2:
            funct_tuple = ('todo','add','done','update','filter','delete')
            indx = funct_tuple.index(action[0])
            
            if indx:
                for x in action[1:]:
                    todo += x + ' '
                
                if self.add(todo):
                    self.showTodos()
                else:
                    print('No fue posible agregar el todo.')
            else:
                print('Error command.')
            
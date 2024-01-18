from datetime import datetime
from todo import Todo
from typing import List

class UI:
    def __init__(self) -> None:
        self.todos = Todo.select()
        self.datetime = datetime.today()
       
    
    def add(self, todo):
        todo = Todo.create(name=todo, completed=False, createdAt=self.datetime)
        if todo:
            return True
        return False
        
    def list(self):
        todos = Todo.select()
        self.todos = [x for x in todos]
        return self.todos
    
    def showTodos(self):       
        if len(self.todos) == 0:
            print('\nNo hay tareas pendientes.')
            return '\n'
        
        for todo in self.todos:
            print(self.getTodo(todo['id']))
    
    def getTodo(self, id):
        todo = Todo.get(Todo.id==id)
        if todo:
            return f'{'[X]' if todo.completed else '[ ]'} {todo.name.capitalize()}'
        return 'Todo not exist.'
    
    def actions(self, action=[]):
        if len(action)==1:
            if action[0] == 'todos':
                self.showTodos()
        
        if len(action)==2:
            if action[0] == 'todo':
                print(f'1 {self.getTodo(action[1])}')
            elif action[0] == 'add':
                print(self.add(action[1]))
                self.showTodos()
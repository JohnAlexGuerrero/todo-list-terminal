from datetime import datetime
from todo import Todo
from typing import List

class UI:
    def __init__(self, todos:List) -> None:
        self.todos = todos
        self.datetime = datetime.today()
    
    def add(self,todo):
        todo = Todo.create(name=todo, completed=False, createdAt=self.datetime)
        self.todos.append(todo)
    
    def list(self):
        todos = Todo.select()
        self.todos = [x for x in todos]
        return self.todos
    
    def showTodos(self):       
        if len(self.todos) == 0:
            print('\nNo hay tareas pendientes.')
            return '\n'
        
        for todo in self.todos:
            print(f'{todo['item']} {'[X]' if todo['completed'] else '[ ]'} {todo['name'].capitalize()}')
    
    def actions(self, action=None):
        if action == None:
            return ''
        
        # if action == 'todos' and task == None:
        #     print(f'Todo List {self.datetime.strftime('%x')}')
        #     self.showTodos()
        # elif action == 'add'and task != None:
        #     self.add(task)
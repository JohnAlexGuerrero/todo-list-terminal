from datetime import date
from todo import Todo

class UI:
    def __init__(self) -> None:
        self.todos = []
        self.date = date.today()
    
    def add(self,todo):
        todo = Todo.create(name=todo)
        self.todos.append(todo)
    
    def list(self):
        todos = Todo.select()
        self.todos = [x for x in todos]
        return self.todos
    
    def show_todos(self):
        title = "Todos List 2024"
        # todos = self.list()
        print(f'{title} \nNo hay tareas pendientes.')
    
    def detail_todo(self, index, todo):
        return f'{index} {'[X]' if todo.completed else '[ ]'} {todo.name.capitalize()}'
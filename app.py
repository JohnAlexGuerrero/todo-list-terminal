from todo import Todo
from ui import UI
from database import database
import re

database.connect()
# database.create_tables([Todo])
todos = []

def set_todos(list):
    items_count = 0
    
    for item in list:
        todo = {
            "item": items_count + 1,
            "id":item.id,
            "name": item.name,
            "completed":item.completed,
            "create": item.createdAt
        }
        todos.append(todo)

def main():
    
    ui = UI()
    # opt = 'todos, todo 1, delete 2, done 2, create 2024-01-12, update 3, add'
    
    while True:
        actions = input('command>')
        print('TodoList 2024')
        
        actions_str = [x for x in actions.split(' ')]

        ui.actions(actions_str)
        
        
        if actions == 'exit':
            break

if __name__ == '__main__':
    main()

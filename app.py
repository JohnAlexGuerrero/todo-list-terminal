from todo import Todo
from task import Task
from command import Commands
from database import database
from datetime import datetime

database.connect()
database.create_tables([Todo, Task, Commands])

def getTodos():
    return Todo.select()

def getTodo(todo):
    todo = Todo.get(id=todo)
    return f'{todo.id}->{'[X]' if todo.completed else '[ ]'} {todo.name.capitalize()}'

def addTodo(todo):
    todo = Todo.create(name=todo, completed=False, createdAt=datetime.today())


def doneTodo(todo):
    obj = Todo.get(id=todo)
    obj.completed = True
    obj.save()

def updateTodo(todo_id,todo):
    obj = Todo.get(todo_id)
    obj.name = todo
    obj.createdAt = datetime.today()
    obj.save()

def filterTodo():
    pass

def deleteTodo(todo):
    qry=Todo.delete().where (Todo.id==todo)
    qry.execute()

def editTodo():
    pass

def show():
    todos = getTodos()
    for todo in todos:
        print(getTodo(todo))

def getFunctionIndex(name_function):
    funct_tuple = (
        'todos','todo','add','done','update','filter','delete','edit'
    )
    return funct_tuple.index(name_function)

def getFunction(index, todo):
    if index == 0:
        show()
    else:
        if index == 1:
            getTodo(todo=todo)
        elif index == 2:
            addTodo(todo=todo)
        elif index == 3:
            doneTodo(todo=todo)
        elif index == 4:
            updateTodo(todo=todo)
        elif index == 5:
            filterTodo()
        elif index == 6:
            deleteTodo(todo=todo),
        elif index == 7:
            editTodo()
        
        show()

def main():   
    todo = None
 
    while True:
        command_input = input('task>')
        
        command_str = [x for x in command_input.split(' ')]
        
        
        if command_input == 'exit':
            break
        
        print(command_str)
        # print('TodoList 2024')
        # print('#  completed  task')
        

        # if len(command_str) > 1:
        #     result = map(lambda x : x, command_str[1:])
        #     todo = " ".join(list(result))
            
        # try:
        #     index = getFunctionIndex(command_str[0])
        #     getFunction(index, todo)
            
        #     todo = None

        # except:
        #     print(f'Error command. {command_str[0]}')
        

if __name__ == '__main__':
    command = Commands().poblations()
    
    main()
    print('GoodBye!')

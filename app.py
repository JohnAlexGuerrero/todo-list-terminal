from todo import Todo
from database import database
from datetime import datetime

from calendar import calendar
import pandas as pd

database.connect()
# database.create_tables([Todo])

def create_todo():
  description = str(input('Description:'))
  is_priority = bool(input('Is Priority(si/no):'))
  make_it = datetime(input('Make It(dia-mes-año):'))
  time = datetime(input('Time(H:M):'), "%H:%M")

  return (description, is_priority, make_it, time)

def main():   
  pass

if __name__ == '__main__':

  print('DAILY TO DO LIST\n')
  print(f'DATE: {datetime.now().strftime('%d, %B %Y')}')
  
  todo_tuple = create_todo()
  
  #validacion de vacios
  for i in range(len(todo_tuple)):
    print(type(todo_tuple[i]))
  
  main()

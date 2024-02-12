from todo import Todo
from database import database
from datetime import datetime
from form import Form

from calendar import calendar
import pandas as pd

database.connect()
database.create_tables([Todo])

def todo_form():
  description = input('Description:')
  is_priority = input('Is Priority(si/no):')
  make_it = input('Make It(dia-mes-año):')
  time = input('Time(H:M):')

  return (description, is_priority, make_it, time)

def todo_list():
  print("TODO")
  data = Todo().all_todos()
  
  df = pd.DataFrame(
    data, index=['[1]'])
  
  print(df)

def main():   
  pass

if __name__ == '__main__':

  print('DAILY TO DO LIST\n')
  print(f'DATE: {datetime.now().strftime('%d, %B %Y')}')
  
  while True:
    # description, priority, make_it, time = todo_form()
    
    # form = Form(description=description, is_priority=priority, do_it=make_it, time=time)
    
    # if form.is_valid():
    #   form.save()
    #   print('\nla tarea fue agregada con exito.')
    # else:
    #   print('no is valid')
    
    todo_list()
    
    break

      
        
      
  
  main()

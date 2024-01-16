from todo import Todo
from ui import UI
from database import database

database.connect()
# database.create_tables([Todo])

todos = [
    "1. [] terminar matricula en ka universidad",
    "2. [] pagar factura de edupar"
]

if __name__ == '__main__':
    ui = UI()
    
    ui.show_todos()
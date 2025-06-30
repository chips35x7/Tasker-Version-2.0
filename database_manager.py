import sqlite3 

from pyinstaller_resource_path import resource_path


class ToDoDatabase:
    def __init__(self):
        self.connection = sqlite3.connect(resource_path('todo.db'))
        self.manager = self.connection.cursor()
        self.manager.execute("""
                    CREATE TABLE IF NOT EXISTS tasks(
                    id INTEGER PRIMARY KEY,
                    tasks TEXT,
                    is_complete INTEGER)
                    """)
        self.connection.commit()

    
if __name__=='__main__':
    database = ToDoDatabase()
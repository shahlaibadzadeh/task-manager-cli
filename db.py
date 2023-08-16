import sqlite3

task_db = sqlite3.connect('tasks.db')

task_db.execute(f'''create table tasks
                (id integer primary key not null,
                name text not null,
                description text,
                deadline text,
                created_at text,
                updated_at text,
                is_done integer default 0
                );
''')

class Db_manager:
    def __init__(self, name, description, deadline, created_at, updated_at, task_status):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_done = task_status

    



print("created")
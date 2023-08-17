import datetime
import sqlite3

task_db = sqlite3.connect('tasks.db')
cursor = task_db.cursor()
print("db created")
# cursor.execute("DROP TABLE tasks")
try:

    task_db.execute(f'''create table tasks
                    (id integer primary key autoincrement,
                    name text not null,
                    description text,
                    deadline text,
                    created_at text,
                    updated_at text,
                    is_done integer default 0
                    );
    ''')
except:

    class Db_manager:
        def __init__(self, name, description, deadline, created_at, updated_at, is_done):
            self.name = name
            self.description = description
            self.deadline = deadline
            self.created_at = created_at
            self.updated_at = updated_at
            self.is_done = is_done

        def add_task(self):
            print(self.updated_at)
            cursor.execute('''insert into tasks(name, description, deadline, created_at, updated_at, is_done) values
                (?, ?, ?, ?, ?, ?)''', (self.name, self.description, self.deadline, self.created_at, self.updated_at, self.is_done)
                           )
            print(self.created_at)
            task_db.commit()
            print("inserted")
            # task_db.close()

      


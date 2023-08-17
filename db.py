import datetime
import sqlite3

task_db = sqlite3.connect('tasks.db')
cursor = task_db.cursor()

try:
    # Creation of table
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
            task_db.commit()
            print("Task added successfully!")
            # task_db.close()

        def list_names_of_tasks():
            cursor.execute('select * from tasks')
            rows = cursor.fetchall()
            for row in rows:
                print(f'{row[0]}. {row[1]}')

        def update_task(task_id, info_to_update, new_data):

            if info_to_update == "1":
                cursor.execute(
                    'Update tasks set name = ? where id = ?', (new_data, task_id))
                task_db.commit()
                print("Task updated successfully")
            elif info_to_update == "2":
                cursor.execute(
                    'Update tasks set description = ? where id = ?', (new_data, task_id))
                task_db.commit()
                print("Task updated successfully")
            elif info_to_update == "3":
                cursor.execute(
                    'Update tasks set deadline = ? where id = ?', (new_data, task_id))
                task_db.commit()
                print("Task updated successfully")
            elif info_to_update == "4":
                cursor.execute(
                    'Update tasks set is_done = ? where id = ?', (new_data, task_id))
                task_db.commit()
                print("Task updated successfully")
            else:
                print("Wrong choice")

        def delete_task(deleted_task_id):
            cursor.execute(
                'Delete from tasks where id = ?', (deleted_task_id,))
            task_db.commit()
            print("Task deleted successfully!")

        def list_tasks():
            if cursor.execute('select * from tasks'):
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
            print("There are no tasks! ")

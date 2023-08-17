import db
import datetime

if __name__ == "__main__":
    print("Welcome!", "Choose one option from the list: ", "1. Add task",
          "2. Update task", "3. Delete task", "4. List tasks", sep="\n")

    user_input = input("Enter your option: ")

    if user_input == "1":
        while True:
            task_name = input("Enter task name: ")
            task_description = input("Enter task description: ")
            task_deadline = input("Enter task deadline (YYYY-MM-DD): ")
            task_created_at = datetime.datetime.now()
            task_updated_at = datetime.datetime.now()
            is_done = input("Enter the status of task (0 or 1): ")
            db.Db_manager(task_name, task_description, task_deadline,
                          task_created_at, task_updated_at, is_done).add_task()
            if input("Add another task? Y/N: ").lower() == "n":
                break

  

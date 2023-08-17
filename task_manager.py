from db import Db_manager
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
            Db_manager(task_name, task_description, task_deadline,
                          task_created_at, task_updated_at, is_done).add_task()
            
            if input("Add another task? Y/N: ").lower() == "n":
                break

    elif user_input == "2":
        print("Which task do you want to update? ")
        Db_manager.list_names_of_tasks() 
        task_id_input = int(input("Enter your option: "))
        print("Which information do you want to update? ", "1. Name",
              "2. Description", "3. Deadline", "4. Task Status", sep="\n")
        info_to_update = input("Enter your option: ")
        new_data_input = input("Enter new information: ")
        Db_manager.update_task(task_id_input, info_to_update, new_data_input)

    elif user_input == "3":
        print("Which task do you want to delete? ")
        Db_manager.list_names_of_tasks() 
        deleted_task_id_input = int(input("Enter your option: "))
        Db_manager.delete_task(deleted_task_id_input)

    elif user_input == "4":
        Db_manager.list_tasks()



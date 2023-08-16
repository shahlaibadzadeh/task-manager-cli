import db

if __name__ == "__main__":
    print("Welcome!", "Choose one option from the list: ", "1. Add task",
          "2. Update task", "3. Delete task", "4. List tasks", sep="\n")

    user_input = input("Enter your option: ")

    if user_input == "1":
        task_name = input("Enter task name: ")
        task_description = input("Enter task description: ")
        task_deadline = input("Enter task deadline: ")
        task_created_at = input("Enter date task created: ")
        task_updated_at = input("Enter date task updated: ")
        task_is_done = input("Enter the status of task: ")
        

        

    elif user_input == "2":
        print("Which information do you want to update?", "1. Name", "2. Description", "3. Deadline", "4. Task Status", sep="\n")
        info_to_update = input("Enter your option: ")
        # if info_to_update == "1":
            
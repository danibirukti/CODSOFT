tasks = []
def add_task(task):
    tasks.append({"task": task, "completed": False})

def display_tasks():
    for idx, task in enumerate(tasks):
        status = "Done" if task["completed"] else "Not Done"
        print(f"{idx + 1}. {task['task']} - {status}")

def update_task(task_number, new_task):
    if 0 <= task_number < len(tasks):
        tasks[task_number]["task"] = new_task
    else:
        print("Invalid task number")

def complete_task(task_number):
    if 0 <= task_number < len(tasks):
        tasks[task_number]["completed"] = True
    else:
        print("Invalid task number")

def main():
    while True:
        print("\n1. Add Task")
        print("2. Display Tasks")
        print("3. Update Task")
        print("4. Complete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            display_tasks()
        elif choice == '3':
            task_number = int(input("Enter task number to update: ")) - 1
            new_task = input("Enter new task description: ")
            update_task(task_number, new_task)
        elif choice == '4':
            task_number = int(input("Enter task number to complete: ")) - 1
            complete_task(task_number)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


# simple_to_do.py

tasks = []  # List to store tasks

def show_tasks():
    """Display the list of tasks."""
    if not tasks:
        print("\nYour task list is empty.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    """Add a new task to the list."""
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

def update_task():
    """Update an existing task."""
    show_tasks()
    try:
        task_num = int(input("Enter the task number to update: ")) - 1
        new_task = input("Enter the updated task: ")
        tasks[task_num] = new_task
        print("Task updated successfully!")
    except (IndexError, ValueError):
        print("Invalid task number!")

def delete_task():
    """Delete a task from the list."""
    show_tasks()
    try:
        task_num = int(input("Enter the task number to delete: ")) - 1
        removed_task = tasks.pop(task_num)
        print(f"Task '{removed_task}' deleted!")
    except (IndexError, ValueError):
        print("Invalid task number!")

def menu():
    """Display the menu and handle user input."""
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    menu()

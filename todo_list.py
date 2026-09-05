
# Task 1: To-Do List

tasks = []


def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 35)
    print("           TO-DO LIST")
    print("=" * 35)
    print("1. Add Task")
    print("2. Delete Task")
    print("3. View Tasks")
    print("4. Exit")
    print("=" * 35)


def add_task():
    """Add a new task to the list."""
    task = input("Enter your task: ").strip()

    if not task:
        print("Error: Task cannot be empty.")
        return

    tasks.append(task)
    print("Task added successfully!")


def delete_task():
    """Delete a task using its number."""
    if not tasks:
        print("No tasks available to delete.")
        return

    view_tasks()

    try:
        task_number = int(input("Enter the task number to delete: "))

        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            print(f'Task "{deleted_task}" deleted successfully!')
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid task number.")


def view_tasks():
    """Display all tasks with their numbers."""
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


def main():
    """Run the To-Do List application."""
    print("Welcome to the To-Do List Application!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_task()

        elif choice == "2":
            delete_task()

        elif choice == "3":
            view_tasks()

        elif choice == "4":
            print("Thank you for using the To-Do List. Goodbye!")
            break

        else:
            print("Invalid choice. Please select an option from 1 to 4.")


if __name__ == "__main__":
    main()

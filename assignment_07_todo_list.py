
def display_menu():
    print("============================")
    print("     TO-DO LIST MENU")
    print("============================")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")
 
 
def add_task(tasks):
    """Prompt for a task description and append it to `tasks`."""
    description = input("Enter task: ")
    tasks.append(description)
    print(f'Task added: "{description}"')
 
 
def view_tasks(tasks):
    """Display all tasks, numbered from 1. Show a message if there are none."""
    if not tasks:
        print("Your to-do list is empty. Add a task to get started!")
        return
 
    print("Your Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
 
 
def delete_task(tasks):
    """Show tasks, ask which one to remove, and remove it if valid."""
    if not tasks:
        print("Your to-do list is empty. There is nothing to delete.")
        return
 
    view_tasks(tasks)
    choice = input("Enter task number to delete: ")
 
    if not choice.isdigit():
        print("Error: Please enter a valid task number.")
        return
 
    index = int(choice)
 
    if index < 1 or index > len(tasks):
        print("Error: That task number does not exist.")
        return
 
    removed = tasks.pop(index - 1)
    print(f'Task "{removed}" has been removed.')
 
 
def main():
    tasks = []
 
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        print()
 
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number from 1 to 4.")
 
        print()
 
 
if __name__ == "__main__":
    main()
 
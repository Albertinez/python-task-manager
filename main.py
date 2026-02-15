# main.py

from task_manager import task_utils

def main():
    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            try:
                task_utils.add_task(title, description, due_date)
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == '2':
            task_utils.view_pending_tasks()
            index = int(input("Enter task number to mark as complete: "))
            task_utils.mark_task_as_complete(index)
        
        elif choice == '3':
            task_utils.view_pending_tasks()
        
        elif choice == '4':
            progress = task_utils.calculate_progress()
            print(f"Progress: {progress:.2f}%")
        
        elif choice == '5':
            print("Exiting Task Manager.")
            break
        
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

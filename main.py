from task_manager.task_utils import (
    add_task,
    mark_task_complete,
    view_pending_tasks,
    calculate_progress
)

tasks = []

def main():
    while True:
        print("--- Task Manager ---")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            mark_task_complete(tasks)
        elif choice == "3":
            view_pending_tasks(tasks)
        elif choice == "4":
            progress = calculate_progress(tasks)
            print(progress)
        elif choice == "5":
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()

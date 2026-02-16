from .validation import validate_task_title, validate_task_description, validate_due_date

tasks = []  # Global list to store tasks

def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")


def mark_task_complete(tasks):
    if len(tasks) == 0:
        print("No tasks available.")
        return

    for i, task in enumerate(tasks, start=1):
        if not task["completed"]:
            print(f"{i}. {task['title']} - Due: {task['due_date']}")

    task_number = int(input("Enter task number to mark as complete: "))

    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Invalid task number.")


def view_pending_tasks(tasks):
    for i, task in enumerate(tasks, start=1):
        if not task["completed"]:
            print(f"{i}. {task['title']} - Due: {task['due_date']}")


def calculate_progress(tasks):
    if len(tasks) == 0:
        return 0

    completed = 0
    for task in tasks:
        if task["completed"]:
            completed += 1

    return (completed / len(tasks)) * 100

from .validation import validate_task_title, validate_task_description, validate_due_date

tasks = []  # Global list to store tasks

def add_task(title, description, due_date):
    title = validate_task_title(title)
    description = validate_task_description(description)
    due_date = validate_due_date(due_date)

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    print(f"Task '{title}' added successfully!")

def mark_task_as_complete(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        print(f"Task '{tasks[task_index]['title']}' marked as complete!")
    else:
        print("Invalid task number.")

def view_pending_tasks():
    pending = [task for task in tasks if not task['completed']]
    if not pending:
        print("No pending tasks!")
    else:
        for i, task in enumerate(pending):
            print(f"{i}. {task['title']} - Due: {task['due_date']}")

def calculate_progress():
    if not tasks:
        return 0
    completed_count = sum(task['completed'] for task in tasks)
    return (completed_count / len(tasks)) * 100

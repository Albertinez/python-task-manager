import datetime

def validate_task_title(title):
    if not title.strip():
        raise ValueError("Title cannot be empty.")
    return title.strip()

def validate_task_description(description):
    if not description.strip():
        raise ValueError("Description cannot be empty.")
    return description.strip()

def validate_due_date(due_date):
    try:
        datetime.datetime.strptime(due_date, "%Y-%m-%d")
        return due_date
    except ValueError:
        raise ValueError("Due date must be in YYYY-MM-DD format.")
# validation.py
def validate_description(description):
    """
    Raises ValueError if the task description is too long (>500 characters)
    """
    if len(description) > 500:
        raise ValueError("Description too long")

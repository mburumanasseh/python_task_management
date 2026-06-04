from datetime import datetime

def validate_task_title(title):
    if not isinstance(title, str):
        return False
    if title.strip() == "":
        return False
    return True

def validate_task_description(description):
    if not isinstance(description, str):
        return False
    if description.strip() == "":
        return False
    return True

def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        return False

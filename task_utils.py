from datetime import datetime

# Import validation functions
from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []


# Implement add_task function
def add_task(title, description, due_date):
    is_valid, error_message = validate_task_title(title)
    if not is_valid:
        print(error_message)
        return

    is_valid, error_message = validate_task_description(description)
    if not is_valid:
        print(error_message)
        return

    is_valid, error_message = validate_due_date(due_date)
    if not is_valid:
        print(error_message)
        return

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "status": "pending",
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    # Convert 1-based input index to 0-based list index
    zero_index = index - 1
    if 0 <= zero_index < len(tasks):
        tasks[zero_index]["status"] = "complete"
        tasks[zero_index]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Invalid task index. Please enter a valid index.")
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending_tasks = [task for task in tasks if task["status"] == "pending"]
    for task in pending_tasks:
        print(f"Title: {task['title']}, Description: {task['description']}, Due Date: {task['due_date']}")

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    total_tasks = len(tasks)
    if total_tasks == 0:
        print("No tasks currently.")
        return 0
    # Support both "completed" boolean key and "status" string key
    completed_tasks = len([
        task for task in tasks
        if task.get("completed") == True or task.get("status") == "complete"
    ])
    progress = (completed_tasks / total_tasks * 100)
    return progress
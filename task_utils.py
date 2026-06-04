from datetime import datetime
from validation import validate_task_title, validate_task_description, validate_due_date

tasks = []

def add_task(title, description, due_date):
    if not validate_task_title(title):
        print("Invalid title. Title cannot be empty.")
        return
    if not validate_task_description(description):
        print("Invalid description. Description cannot be empty.")
        return
    if not validate_due_date(due_date):
        print("Invalid due date. Please use the format YYYY-MM-DD.")
        return

    task = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date.strip(),
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")

def mark_task_as_complete(index, tasks=tasks):
    if index < 1 or index > len(tasks):
        print("Invalid task number.")
        return
    tasks[index - 1]["completed"] = True
    print("Task marked as complete!")

def view_pending_tasks(tasks=tasks):
    pending = [task for task in tasks if not task["completed"]]

    if not pending:
        print("No pending tasks.")
        return

    print("\nPending Tasks:")
    print("-" * 45)
    for i, task in enumerate(pending, start=1):
        print(f"{i}. {task['title']}")
        print(f"   Description: {task['description']}")
        print(f"   Due Date:    {task['due_date']}")
    print("-" * 45)

def calculate_progress(tasks=tasks):
    total = len(tasks)
    if total == 0:
        progress = 0
    else:
        completed = len([task for task in tasks if task["completed"]])
        progress = (completed / total) * 100

    print("\nProgress Tracker:")
    print("-" * 45)
    print(f"Total tasks:     {total}")
    print(f"Completed tasks: {len([t for t in tasks if t['completed']])}")
    print(f"Pending tasks:   {len([t for t in tasks if not t['completed']])}")
    print(f"Completion:      {progress:.1f}%")
    print("-" * 45)
    return progress

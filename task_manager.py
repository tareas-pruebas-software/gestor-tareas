import json
import os
import datetime

TASKS_FILE = "tasks/tasks.json"
ARCHIVED_TASKS_FILE = "tasks/archived_tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(title, description, due_date, label):
    tasks = load_tasks()
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "label": label,
        "status": "pending"
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Tarea '{title}' añadida con éxito.")

def list_tasks(status=None, label=None, due_date=None):
    tasks = load_tasks()
    print("Tareas:")
    for task in tasks:
        if (status and task["status"] != status) or (label and task["label"] != label or (due_date and datetime.strptime(task["due_date"], '%Y-%m-%d') > due_date)):
            continue
        print(f"Título: {task['title']}, Descripción: {task['description']}, Vencimiento: {task['due_date']}, Estado: {task['status']}, Etiqueta: {task['label']}")
    print('---')

def update_task(title, new_status=None, new_due_date=None, new_label=None):
    tasks = load_tasks()
    for task in tasks:
        if task["title"] == title:
            if new_status:
                task["status"] = new_status
            if new_due_date:
                task["due_date"] = new_due_date
            if new_label:
                task["label"] = new_label
            save_tasks(tasks)
            print(f"Tarea '{title}' actualizada con éxito.")
            print(f"Título: {task['title']}, Descripción: {task['description']}, Vencimiento: {task['due_date']}, Estado: {task['status']}, Etiqueta: {task['label']}")
            return
    print(f"Tarea '{title}' no encontrada.")

def delete_task(title):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["title"] != title]
    save_tasks(tasks)
    print(f"Tarea '{title}' eliminada con éxito.")

def archive_completed_tasks():
    tasks = load_tasks()
    completed_tasks = [task for task in tasks if task["status"] == "completed"]
    tasks = [task for task in tasks if task["status"] != "completed"]
    
    if os.path.exists(ARCHIVED_TASKS_FILE):
        with open(ARCHIVED_TASKS_FILE, "r") as file:
            archived_tasks = json.load(file)
    else:
        archived_tasks = []

    archived_tasks.extend(completed_tasks)
    
    with open(ARCHIVED_TASKS_FILE, "w") as file:
        json.dump(archived_tasks, file, indent=4)
    
    save_tasks(tasks)
    print("Tareas completadas archivadas con éxito.")

def list_archived_tasks():
        try:
            with open(ARCHIVED_TASKS_FILE, 'r') as file:
                archived_tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            archived_tasks = []
            print("No se encontraron tareas archivadas.")
            return

        print("Tareas archivadas:")
        for task in archived_tasks:
            print(f"Título: {task['title']}, Vencimiento: {task['due_date']}, Estado: {task['status']}, Etiqueta: {task['label']}")
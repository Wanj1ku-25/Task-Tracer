# print("Hello, Task Tracer!") 

import json
import os
import sys

# The file where tasks are stored
task_file = "tasks.json"

# a function to load tasks
def load_tasks():
    if not os.path.exists(task_file):
        return[]
    with open(task_file, 'r') as file:
        return json.load(file)
    
#function to save tasks
def save_tasks(tasks):
    with open(task_file, 'w') as file:
        json.dump(tasks, file, indent=4)

# a function to add a task
def add_task(title):
    tasks = load_tasks()
    task = {
        "id": len(tasks) +1,
        "title":title,
        "status":"not done"
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task added: {title}")

# main function and command handlling
def main():
    if len(sys.argv) < 2:
        print("Please provide a command(add,list,etc)")
        return
    command = sys.argv[1]
    if command == "add":
        if len(sys.argv)<3:
            print("Please provide a task title")
        else:
            title = " ".join(sys.argv[2:])  # all words after "add"
            add_task(title)
    elif command == "done":
        if len(sys.argv) < 3:
            print("⚠️ Please provide a task ID.")
        else:
            update_status(sys.argv[2], "done")

    elif command == "list":
        list_tasks()
    elif command == "list_done":
        list_by_status("done")

    elif command == "list_not_done":
        list_by_status("not done")

    elif command == "list_progress":
        list_by_status("in progress")
    else:
        print("Unknown command")


#function to list all tasks
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available")
        return
    for task in tasks:
        print(f"{task['id']}. {task['title']} - {task['status']}")



# Add status to the lists
def list_by_status(status):
    tasks=load_tasks()
    filtered = [task for task in tasks if task["status"] == status]
    if not filtered:
        print(f"No tasks with status '{status}'")
        return
    for task in filtered:
        print(f"{task['id']}. {task['title']} - {task['status']}")

# update the status of the task
def update_status(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == int(task_id):
            task["status"] = status
            save_tasks(tasks)
            print(f"🔄 Task {task_id} marked as {status}.")
            return
    print("❌ Task not found.")


if __name__ == "__main__":
    main()


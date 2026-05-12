import json
import uuid
from datetime import datetime

TASKS_FILE = "tasks.json"


# ---------- JSON persistence ----------

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)


# ---------- Core operations ----------

def add_task(tasks, name, description, due_date):
    task = {
        "id": str(uuid.uuid4())[:8],
        "name": name,
        "description": description,
        "due_date": due_date,
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d"),
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"\n✓ Added task [{task['id']}]: {name}")


def view_tasks(tasks):
    pending = [t for t in tasks if not t["completed"]]
    done = [t for t in tasks if t["completed"]]

    print("\n===== PENDING =====")
    if pending:
        for t in pending:
            print(f"  [{t['id']}] {t['name']} | Due: {t['due_date']}")
            print(f"       {t['description']}")
    else:
        print("  (none)")

    print("\n===== COMPLETED =====")
    if done:
        for t in done:
            print(f"  [{t['id']}] {t['name']} | Due: {t['due_date']}")
    else:
        print("  (none)")


def mark_complete(tasks, task_id):
    for t in tasks:
        if t["id"] == task_id:
            t["completed"] = True
            save_tasks(tasks)
            print(f"\n✓ Task [{task_id}] marked as completed.")
            return
    print(f"\n✗ Task [{task_id}] not found.")


def delete_task(tasks, task_id):
    before = len(tasks)
    tasks[:] = [t for t in tasks if t["id"] != task_id]
    if len(tasks) < before:
        save_tasks(tasks)
        print(f"\n✓ Task [{task_id}] deleted.")
    else:
        print(f"\n✗ Task [{task_id}] not found.")


def search_tasks(tasks, keyword):
    keyword = keyword.lower()
    results = [
        t for t in tasks
        if keyword in t["name"].lower()
        or keyword in t["description"].lower()
        or keyword in t["due_date"]
    ]
    print(f"\n===== SEARCH RESULTS for '{keyword}' =====")
    if results:
        for t in results:
            status = "✓" if t["completed"] else "○"
            print(f"  {status} [{t['id']}] {t['name']} | Due: {t['due_date']}")
    else:
        print("  No tasks found.")


# ---------- Input validation ----------

def get_valid_date(prompt):
    while True:
        date_str = input(prompt).strip()
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("  Invalid date. Use format YYYY-MM-DD.")


def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  This field cannot be empty.")


# ---------- CLI ----------

def menu():
    print("\n========= TASK MANAGER =========")
    print("  1. Add task")
    print("  2. View all tasks")
    print("  3. Mark task as complete")
    print("  4. Delete task")
    print("  5. Search tasks")
    print("  6. Exit")
    print("=================================")
    return input("Choose an option: ").strip()


def main():
    tasks = load_tasks()
    print("Welcome to Python Task Manager!")

    while True:
        choice = menu()

        if choice == "1":
            name = get_non_empty("Task name: ")
            description = get_non_empty("Description: ")
            due_date = get_valid_date("Due date (YYYY-MM-DD): ")
            add_task(tasks, name, description, due_date)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            task_id = get_non_empty("Enter task ID to complete: ")
            mark_complete(tasks, task_id)

        elif choice == "4":
            task_id = get_non_empty("Enter task ID to delete: ")
            delete_task(tasks, task_id)

        elif choice == "5":
            keyword = get_non_empty("Search keyword or date (YYYY-MM-DD): ")
            search_tasks(tasks, keyword)

        elif choice == "6":
            print("\nGoodbye!")
            break

        else:
            print("\n✗ Invalid option. Please choose 1-6.")


if __name__ == "__main__":
    main()

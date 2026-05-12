# Python Task Manager

A command-line task management application built with Python.

## Description

Manage your daily tasks from the terminal. Tasks are saved to a local JSON file so they persist between sessions.

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/python-task-manager.git
cd python-task-manager
python3 task_manager.py
```

No external dependencies required — uses Python standard library only.

## How to Run

```bash
python3 task_manager.py
```

## Features

| Feature | Description |
|---|---|
| Add task | Name, description, due date, auto-generated ID |
| View tasks | Separated into Pending and Completed |
| Mark complete | Mark a task done by ID |
| Delete task | Remove a task by ID |
| Search | Search by keyword or due date (YYYY-MM-DD) |
| Persistent storage | All tasks saved to `tasks.json` |

## Example Usage

```
===== TASK MANAGER =====
1. Add task
2. View all tasks
3. Mark task as complete
4. Delete task
5. Search tasks
6. Exit

Choose an option: 1
Task name: Buy groceries
Description: Milk, eggs, bread
Due date (YYYY-MM-DD): 2026-05-15

✓ Added task [a3f2b1c0]: Buy groceries
```

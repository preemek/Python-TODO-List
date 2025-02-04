import json
from datetime import datetime

class TaskManager:
    def __init__(self, file_name):
        self.file_name = file_name
        self.tasks = self.load_tasks()
        self.save_tasks()

    def load_tasks(self):
        try:
            with open(self.file_name, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    def save_tasks(self):
        with open(self.file_name, "w") as file:
            json.dump(self.tasks, file, indent=4)
    def add_task(self, title, description, deadline, priority):
        task = {
            "title": title,
            "description": description,
            "deadline": deadline,
            "priority": priority,
            "done": False
        }
        self.tasks.append(task)
        self.save_tasks()

    def mark_task_done(self, index):
        self.tasks[index]["done"] = True
        self.save_tasks()

    def delete_task(self, index):
        self.tasks.pop(index)
        self.save_tasks()
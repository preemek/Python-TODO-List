from tkinter import Tk
from task_manager import TaskManager
from task_app import TaskApp

if __name__ == "__main__":
    FILE_NAME = "zadania.json"
    task_manager = TaskManager(FILE_NAME)
    root = Tk()
    app = TaskApp(root, task_manager)
    root.mainloop()

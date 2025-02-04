import tkinter
from tkinter import messagebox, simpledialog
from datetime import datetime
from task_manager import TaskManager

class TaskApp:
    def __init__(self, root, manager):
        self.manager = manager
        self.root = root
        self.root.title("To-Do List")

        self.task_list = tkinter.Listbox(root, width=80, height=20)
        self.task_list.pack()
        button_frame = tkinter.Frame(root)
        button_frame.pack()
        add_button = tkinter.Button(button_frame, text="➕ Dodaj zadanie", command=self.add_task)
        add_button.pack(side=tkinter.LEFT)

        mark_done_button = tkinter.Button(button_frame, text="✅ Oznacz jako wykonane", command=self.mark_done)
        mark_done_button.pack(side=tkinter.LEFT)
        delete_button = tkinter.Button(button_frame, text="🗑️ Usuń zadanie", command=self.delete_task)
        delete_button.pack(side=tkinter.LEFT)

        self.refresh_tasks()

    def add_task(self):
        title = simpledialog.askstring("Dodaj zadanie", "Podaj tytuł zadania:")
        if title:
            description = simpledialog.askstring("Dodaj zadanie", "Podaj opis zadania:")
            deadline = simpledialog.askstring("Dodaj zadanie", "Podaj termin (yyyy-mm-dd):")
            priority = simpledialog.askstring("Dodaj zadanie", "Podaj priorytet (wysoki/średni/niski):")
            try:
                datetime.strptime(deadline, "%Y-%m-%d")
            except ValueError:
                messagebox.showerror("Błąd", "Nieprawidłowy format daty. Użyj yyyy-mm-dd.")
                return

            self.manager.add_task(title, description, deadline, priority)
            self.refresh_tasks()
    def mark_done(self):
        selected = self.task_list.curselection()
        if selected:
            task_index = selected[0]
            self.manager.mark_task_done(task_index)
            self.refresh_tasks()
    def delete_task(self):
        selected = self.task_list.curselection()
        if selected:
            task_index = selected[0]
            self.manager.delete_task(task_index)
            self.refresh_tasks()
    def refresh_tasks(self):
        self.task_list.delete(0, tkinter.END)
        for task in self.manager.tasks:
            status = "[X]" if task["done"] else "[ ]"
            self.task_list.insert(tkinter.END, f"{status} {task['title']} ({task['priority']}, {task['deadline']})")
    
    def notify_deadlines(self):
        today = datetime.now().date()
        for task in self.manager.tasks:
            if not task["done"]:
                deadline = datetime.strptime(task["deadline"], "%Y-%m-%d").date()
                days_left = (deadline - today).days
                if days_left == 1:
                    messagebox.showinfo("Przypomnienie", f"Zadanie '{task['title']}' ma termin jutro!")
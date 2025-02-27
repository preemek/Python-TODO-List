# Illia
import json
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from task import Task

ZADANIA = "zadania.json"

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []
        self.load_tasks()

        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.pack(pady=10)
        self.task_listbox.bind("<Double-Button-1>", self.show_task_details)  # Обработчик двойного клика

        self.add_button = tk.Button(root, text="Dodaj zadanie", command=self.add_task)
        self.add_button.pack(pady=5)

        self.done_button = tk.Button(root, text="Oznacz jako ukończone", command=self.mark_task_done)
        self.done_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Usuń zadanie", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for i, task in enumerate(self.tasks):
            status = "✅" if task.status else "❌"
            self.task_listbox.insert(tk.END, f"{i}. {task.title} (do {task.deadline}) {status}")

    def show_task_details(self, event):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            task = self.tasks[index]
            messagebox.showinfo("Opis zadania", f"📌 {task.title}\n\n{task.description}\n\n🗓 Deadline: {task.deadline}")

    def add_task(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Dodaj zadanie")

        tk.Label(add_window, text="Nazwa:").pack()
        title_entry = tk.Entry(add_window)
        title_entry.pack()

        tk.Label(add_window, text="Opis:").pack()
        desc_entry = tk.Entry(add_window)
        desc_entry.pack()

        tk.Label(add_window, text="Termin (YYYY-MM-DD):").pack()
        deadline_entry = tk.Entry(add_window)
        deadline_entry.pack()

        def save_task():
            title = title_entry.get()
            desc = desc_entry.get()
            deadline = deadline_entry.get()
            if title and deadline:
                self.tasks.append(Task(title, desc, deadline))
                self.save_tasks()
                self.update_task_list()
                add_window.destroy()
            else:
                messagebox.showwarning("Błąd", "Wymagany jest tytuł i termin!")

        tk.Button(add_window, text="Save", command=save_task).pack()

    def mark_task_done(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index].mark_as_done()
            self.save_tasks()
            self.update_task_list()

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            self.save_tasks()
            self.update_task_list()

    def save_tasks(self):
        with open(ZADANIA, "w", encoding="utf-8") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def load_tasks(self):
        try:
            with open(ZADANIA, "r", encoding="utf-8") as file:
                self.tasks = [Task.from_dict(task) for task in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

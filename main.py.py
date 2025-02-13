import json
import os
import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime

TASKS_FILE = "zadania.json"

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        
        self.tasks = []
        self.load_tasks()
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)
        
        self.task_listbox = tk.Listbox(self.frame, width=50, height=10)
        self.task_listbox.pack(side=tk.LEFT)
        
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)
        
        self.add_button = tk.Button(self.root, text="Dodaj Zadanie", command=self.add_task)
        self.add_button.pack(pady=5)
        
        self.complete_button = tk.Button(self.root, text="Oznacz jako wykonane", command=self.mark_completed)
        self.complete_button.pack(pady=5)
        
        self.delete_button = tk.Button(self.root, text="Usuń Zadanie", command=self.delete_task)
        self.delete_button.pack(pady=5)
        
        self.display_tasks()
    
    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r") as file:
                self.tasks = json.load(file)
    
    def save_tasks(self):
        with open(TASKS_FILE, "w") as file:
            json.dump(self.tasks, file, indent=4)
    
    def display_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "[✔]" if task["completed"] else "[ ]"
            self.task_listbox.insert(tk.END, f"{status} {task['title']} - {task['due_date']}")
    
    def add_task(self):
        title = simpledialog.askstring("Dodaj Zadanie", "Podaj tytuł zadania:")
        if not title:
            return
        
        description = simpledialog.askstring("Dodaj Zadanie", "Podaj opis zadania:")
        due_date = simpledialog.askstring("Dodaj Zadanie", "Podaj termin (YYYY-MM-DD):")
        
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Błąd", "Niepoprawny format daty. Użyj YYYY-MM-DD.")
            return
        
        new_task = {"title": title, "description": description, "due_date": due_date, "completed": False}
        self.tasks.append(new_task)
        self.save_tasks()
        self.display_tasks()
    
    def mark_completed(self):
        selected_index = self.task_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Błąd", "Wybierz zadanie do oznaczenia jako wykonane.")
            return
        
        index = selected_index[0]
        self.tasks[index]["completed"] = True
        self.save_tasks()
        self.display_tasks()
    
    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Błąd", "Wybierz zadanie do usunięcia.")
            return
        
        index = selected_index[0]
        del self.tasks[index]
        self.save_tasks()
        self.display_tasks()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

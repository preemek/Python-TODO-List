import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime


FILE_PATH = "/to_do_list/zadania.json"


class Task:
    def __init__(self,title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = "Nie wykonane"

    def mark_done(self):
        self.status = "Wykonane"

    def __str__(self):
            return f'{self.title} - {self.due_date} - {self.status}'
    

class TaskManager:
    def __init__(self):
          self.tasks = self.load_tasks()

    def load_tasks(self):

        try:
             with open(FILE_PATH, r) as file:
                  tasks_data = json.load(file)
                  tasks = [Task(task['title'], task['description'], task['due_date']) for task in tasks_data]
        except (FileNotFoundError, json.JSONDecodeError):
             tasks = []
        return tasks
    
    def save_tasks(self):
         
         tasks_data = [{
              "title": task.title,
              "description": task.description,
              "due_date": task.due_date,
              "status": task.status    
         } for task in self.tasks]

         with open(FILE_PATH, 'w') as file:
              json.dump(tasks_data, file, indent=4)

    def add_task(self, title, description, due_date):
         task = Task(title, description, due_date)
         self.tasks.append(task)
         self.save_tasks()

    def delete_task(self, task):
         self.tasks.remove(task)
         self.save_tasks()

    def mark_task_done(self, task):
         task.mark_done()
         self.save_tasks()


class TaskApp:
     
     def __init__(self, root, task_manager):
          self.root = root
          self.task_manager = task_manager


          self.create_widgets()
          self.update_task_list()

     def create_widgets(self):
          self.label_title = tk.Label(self.root, text="Tytuł zadania:")
          self.label_title.pack()

          self.entry_title = tk.Entry(self.root, width=50)
          self.entry_title.pack()

          self.label_description = tk.Label(self.root, text="Opis zadania:")
          self.label_description.pack()

          self.entry_description = tk.Entry(self.root, width=50)
          self.entry_description.pack()

          self.label_due_date = tk.Label(self.root, text="Termin (RRRR-MM-DD):")
          self.label_due_date.pack()

          self.entry_due_date = tk.Entry(self.root, width=50)
          self.entry_due_date.pack()

          self.button_add_task = tk.Button(self.root, text="Dodaj zadanie", command=self.add_task)
          self.button_add_task.pack()

          self.listbox_tasks = tk.Listbox(self.root, width=50, height=10)
          self.listbox_tasks.pack()
          self.listbox_tasks.bind("<ListboxSelect>", self.show_task_details)

          self.label_task_details = tk.Label(self.root, text="Szczegóły zadania:")
          self.label_task_details.pack()

          self.button_mark_done = tk.Button(self.root, text="Oznacz jako wykonane", command=self.mark_task_done)
          self.button_mark_done.pack()

          self.button_delete_task = tk.Button(self.root, text="Usuń zadanie", command=self.delete_task)
          self.button_delete_task.pack()

     def update_task_list(self):
          self.listbox_tasks.delete(0, tk.END)
          for task in self.task_manager.tasks:
               self.listbox_tasks.insert(tk.END, str(task))

     def show_task_details(self):





        


         
            
                  
                  
                  

        
    

    









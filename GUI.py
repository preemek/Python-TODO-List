from tasks import task_list
import tkinter as tk
from tkinter import ttk

class PyToDoList:
    def __init__ (self,root:tk.Tk):
        self.task_list=task_list()
        self.root=root
        self.root.geometry("400x500")
        self.main_menu()
    def main_menu (self):
        def update_task_selection_box():
            task_selection_box.delete(0,tk.END)
            for task in self.task_list.list_of_tasks:
                task_selection_box.insert(tk.END,task.title)

        self.root.rowconfigure(1,weight=1,minsize=100)
        task_selection_box=tk.Listbox()
        task_selection_box.grid(row=1,column=0,sticky="NS")
        update_task_selection_box()

        filterbutton = tk.Menubutton(self.root, text = "Menu")    
        filterbutton.menu = tk.Menu(filterbutton)   
        filterbutton["menu"]= filterbutton.menu   

        reverse = tk.BooleanVar()
        filterbutton.menu.add_command(label = "alphabetical",command=lambda:[self.task_list.sort_list_of_tasks("alphabetical",reverse=reverse.get()),update_task_selection_box()])
        filterbutton.menu.add_command(label="update",command=update_task_selection_box)   
        filterbutton.menu.add_checkbutton(label = "reverse", variable=reverse) 
        # filterbutton.menu.add_checkbutton(label = "Careers",) 

        filterbutton.grid(row=0,column=0)
        

a=tk.Tk()
app=PyToDoList(a)
a.mainloop()
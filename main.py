# Illia
import tkinter as tk
from tkinter import messagebox
import re

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tytul_label = tk.Label(root, text="Wpisz tytuł zadania, które chcesz wykonać:", font=("Arial", 20))
        self.tytul_label.pack(pady=10)

        self.tytul_text_box = tk.Text(root, height=2, width=50)
        self.tytul_text_box.pack(pady=10)
        
        self.opis_label = tk.Label(root, text="Napisz opis zadania", font=("Arial", 14))
        self.opis_label.pack(pady=10)

        self.opis_text_box = tk.Text(root, height=10, width=50)
        self.opis_text_box.pack(pady=10)

        self.termin_label = tk.Label(root, text="Wpisz termin realizacji zadania")
        self.termin_label.pack(pady=10)

        self.termin_text_box = tk.Text(root, height=1, width=50)
        self.termin_text_box.pack(pady=10)

        self.termin_text_box.bind("<KeyPress>", self.validate_input)

    def validate_input(self, event):
        char = event.char
        allowed_chars = "0123456789."

        if event.keysym in ["BackSpace", "Delete", "Left", "Right"]:
            return
        
        if char not in allowed_chars:
            return "break"
        

if __name__ == "__main__":
    root = tk.Tk()
    todolist = ToDoList(root)
    root.mainloop()
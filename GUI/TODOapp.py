import customtkinter as ctk
from customtkinter import CTkButton
from GUI.ConfirmationWindow import CTkConfirmationWindow

from DataBase.sqlalchemy_todo_db import TODO_db, connect_url
from sqlalchemy.orm import Session

todo_db = TODO_db(connect_url)

class ButtonFrameList(ctk.CTkFrame):
    def __init__(self, master, radio_frame_list):
        super().__init__(master)
        self.master = master
        self.delete_list_confirmation = None
        self.radio_frame_list = radio_frame_list
        self.grid_columnconfigure((0,1), weight=1)
        self.button_new_list = ctk.CTkButton(self, text="New List"
                                             , command=self.new_list_command, corner_radius=6)
        self.button_new_list.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.button_delete_list = ctk.CTkButton(self, text="Delete List"
                                             , command=self.delete_list_command, corner_radius=6)
        self.button_delete_list.grid(row=0, column=1, padx=10, pady=10, sticky="ew")


    def new_list_command(self):
        dialog = ctk.CTkInputDialog(text="Put your new list name:", title="New List")
        new_list_name = dialog.get_input()
        todo_db.add_new_list(new_list_name)
        self.radio_frame_list.remove_radiobuttons()
        self.radio_frame_list.add_radiobuttons()


    def delete_list_command(self):
        dialog = CTkConfirmationWindow(text="Are you sure you want to delete the list and all tasks?", title="Delete List confirmation")
        conf = dialog.get_input()
        list_id_to_delete = self.radio_frame_list.variable.get()
        if conf == 'Yes':
            todo_db.delete_list(list_id_to_delete)
        self.radio_frame_list.remove_radiobuttons()
        self.radio_frame_list.add_radiobuttons()




class ButtonFrameTask(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.grid_columnconfigure((0,1), weight=1)
        self.button_new_task = ctk.CTkButton(self, text="New Task"
                                             , command=self.new_task_command, corner_radius=6)
        self.button_new_task.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.button_delete_task = ctk.CTkButton(self, text="Delete Task"
                                             , command=self.delete_task_command, corner_radius=6)
        self.button_delete_task.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    @staticmethod
    def new_task_command():
        dialog = ctk.CTkInputDialog(text="Put your new task name:", title="New Task")
        print("New task name:", dialog.get_input())

    @staticmethod
    def delete_task_command():
        dialog = CTkConfirmationWindow(text="Are you sure you want to delete the task?",
                                       title="Delete Task confirmation")
        print("Delete task confirmation:", dialog.get_input())


class ScrollableFrameList(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.radiobuttons = []
        self.variable = ctk.StringVar(value="")
        self.lists = []

    def remove_radiobuttons(self):
        self.lists = []
        for r in self.radiobuttons:
            r.destroy()
        self.radiobuttons = []

    def add_radiobuttons(self):
        list_rows = todo_db.get_all_lists()
        for l in list_rows:
            self.lists.append((l.id,l.name))


        for i, l in enumerate(self.lists):
            radiobutton = ctk.CTkRadioButton(self, text=l[1], value=l[0], variable=self.variable)
            radiobutton.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
            self.radiobuttons.append(radiobutton)



class ScrollableFrameTask(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.radiobuttons = []
        self.variable = ctk.StringVar(value="")
        self.tasks = ['Task 1', 'Task 2', 'Task 3']
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)

        for i, t in enumerate(self.tasks):
            radiobutton = ctk.CTkRadioButton(self, text=t, value=t, variable=self.variable)
            radiobutton.grid(row=i, column=0, padx=5, pady=(5, 0), sticky="w")
            label_date = ctk.CTkLabel(self, text="2025-02-06", fg_color="transparent")
            label_date.grid(row=i, column=1, padx=5, pady=5, sticky="ew")
            label_status = ctk.CTkLabel(self, text="In progress", fg_color="transparent")
            label_status.grid(row=i, column=2, padx=5, pady=5, sticky="ew")
            label_status = ctk.CTkLabel(self, text="High", fg_color="transparent")
            label_status.grid(row=i, column=3, padx=5, pady=5, sticky="ew")
            self.radiobuttons.append(radiobutton)


class DetailsFrameTask(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure((0,1), weight=1)
        self.switch_var = ctk.StringVar(value="on")
        self.combobox_var = ctk.StringVar(value="Low")

        self.textbox = ctk.CTkTextbox(self, height=60, width=300, corner_radius=6)
        self.textbox.grid(row=0, column=0, padx=10, pady=(5,5), sticky="nsew", rowspan=3)
        self.textbox.insert("0.0", "Some example text!\n" * 5)
        self.switch = ctk.CTkSwitch(self, text="Done", command=self.switch_command,
                                         variable=self.switch_var, onvalue="on", offvalue="off")
        self.switch.grid(row=0, column=1, padx=20, pady=(5,5), sticky="e")
        self.combobox = ctk.CTkComboBox(self, values=['Low', 'Medium', 'High'],
                                        command=self.combobox_command, variable=self.combobox_var)
        self.combobox.grid(row=1, column=1, padx=20, pady=(5,5), sticky="e")
        self.update_button = ctk.CTkButton(self, text="Update"
                                             , command=self.update_task_command, corner_radius=6)
        self.update_button.grid(row=2, column=1, padx=20, pady=(5,5), sticky="e")

    def switch_command(self):
        print("switch toggled, current value:", self.switch_var.get())

    def combobox_command(self, choice):
        print("combobox dropdown clicked:", choice)

    def update_task_command(self):
        pass


class MainFrameForList(ctk.CTkFrame):
    def __init__(self, master, title):
        super().__init__(master)
        self.master = master
        self.title = title
        self.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(self, text=self.title, fg_color='gray30', corner_radius=6)
        self.title_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")
        self.radio_frame_list = ScrollableFrameList(self, height=355)
        self.radio_frame_list.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        self.radio_frame_list.add_radiobuttons()
        self.buttons_frame_list = ButtonFrameList(self, self.radio_frame_list)
        self.buttons_frame_list.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")


class MainFrameForTask(ctk.CTkFrame):
    def __init__(self, master, title):
        super().__init__(master)
        self.master = master
        self.title = title
        self.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(self, text=self.title, fg_color='gray30', corner_radius=6)
        self.title_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")
        self.radio_frame_task = ScrollableFrameTask(self,height=237)
        self.radio_frame_task.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        self.task_details = DetailsFrameTask(self)
        self.task_details.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        self.buttons_frame_task = ButtonFrameTask(self)
        self.buttons_frame_task.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")


class TODOapp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("TODO task manager")
        self.geometry("800x500")
        self.minsize(800, 500)
        self.maxsize(800, 500)
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.main_list_frame = MainFrameForList(self, title="Lists" )
        self.main_list_frame.grid(column=0, row=0, padx=(10,5), pady=(10, 10), sticky='nsew')
        self.main_task_frame = MainFrameForTask(self, title="Tasks")
        self.main_task_frame.grid(column=1, row=0, padx=(5,10), pady=(10, 10), sticky='nsew',columnspan=3)





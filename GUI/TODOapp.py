from datetime import datetime
import customtkinter as ctk


from GUI.ConfirmationWindow import CTkConfirmationWindow
from DataBase.sqlalchemy_todo_db import TODO_db, connect_url

todo_db = TODO_db(connect_url)

class ButtonFrameList(ctk.CTkFrame):
    def __init__(self, master, radio_frame_list):
        super().__init__(master)
        self.master = master
        self.delete_list_confirmation = None
        self.radio_frame_list = radio_frame_list
        self.radio_frame_task = None
        self.task_details = None
        self.grid_columnconfigure((0,1), weight=1)
        self.button_new_list = ctk.CTkButton(self, text="New List"
                                             , command=self.new_list_command, corner_radius=6)
        self.button_new_list.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.button_delete_list = ctk.CTkButton(self, text="Delete List"
                                             , command=self.delete_list_command, corner_radius=6)
        self.button_delete_list.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    def set_radio_frame_task(self, radio_frame_task):
        self.radio_frame_task = radio_frame_task

    def set_task_details(self, task_details):
        self.task_details = task_details

    def new_list_command(self):
        dialog = ctk.CTkInputDialog(text="Put your new list name:", title="New List")
        new_list_name = dialog.get_input()
        if new_list_name:
            todo_db.add_new_list(new_list_name)
            self.radio_frame_list.remove_radiobuttons()
            self.radio_frame_list.add_radiobuttons()
            self.radio_frame_task.remove_radiobuttons()
            self.task_details.clear_task_details()

    def delete_list_command(self):
        dialog = CTkConfirmationWindow(text="Are you sure you want to delete the list and all tasks?", title="Delete List confirmation")
        conf = dialog.get_input()
        list_id_to_delete = self.radio_frame_list.variable.get()
        if conf == 'Yes':
            todo_db.delete_list(list_id_to_delete)
            self.radio_frame_list.remove_radiobuttons()
            self.radio_frame_list.add_radiobuttons()
            self.radio_frame_task.remove_radiobuttons()
            self.task_details.clear_task_details()


class ButtonFrameTask(ctk.CTkFrame):
    def __init__(self, master, radio_frame_list, radio_frame_task):
        super().__init__(master)
        self.master = master
        self.radio_frame_list = radio_frame_list
        self.radio_frame_task = radio_frame_task
        self.task_details = None
        self.grid_columnconfigure((0,1), weight=1)
        self.button_new_task = ctk.CTkButton(self, text="New Task"
                                             , command=self.new_task_command, corner_radius=6)
        self.button_new_task.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.button_delete_task = ctk.CTkButton(self, text="Delete Task"
                                             , command=self.delete_task_command, corner_radius=6)
        self.button_delete_task.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    def set_task_details(self, task_details):
        self.task_details = task_details

    def new_task_command(self):
        dialog = ctk.CTkInputDialog(text="Put your new task name:", title="New Task")
        new_task_name = dialog.get_input()
        if new_task_name:
            list_id = self.radio_frame_list.variable.get()
            todo_db.add_new_task(list_id, new_task_name)
            self.radio_frame_task.remove_radiobuttons()
            self.radio_frame_task.add_radiobuttons()
            self.task_details.clear_task_details()

    def delete_task_command(self):
        dialog = CTkConfirmationWindow(text="Are you sure you want to delete the task?",
                                       title="Delete Task confirmation")
        task_to_delete = self.radio_frame_task.variable.get()
        if dialog.get_input() == "Yes":
            todo_db.delete_task(task_to_delete)
            self.radio_frame_task.remove_radiobuttons()
            self.radio_frame_task.add_radiobuttons()
            self.task_details.clear_task_details()


class ScrollableFrameList(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.radiobuttons = []
        self.radio_frame_task = None
        self.task_details = None
        self.variable = ctk.StringVar(value="")
        self.lists = []

    def set_radio_frame_task(self, radio_frame_task):
        self.radio_frame_task = radio_frame_task

    def set_task_details(self, task_details):
        self.task_details = task_details

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
            radiobutton = ctk.CTkRadioButton(self, text=l[1], value=l[0], command=self.radiobutton_event
                                             ,variable=self.variable)
            radiobutton.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
            self.radiobuttons.append(radiobutton)

    def radiobutton_event(self):
        self.radio_frame_task.remove_radiobuttons()
        self.radio_frame_task.add_radiobuttons()
        self.task_details.clear_task_details()



class ScrollableFrameTask(ctk.CTkScrollableFrame):
    def __init__(self, master, radio_frame_list, **kwargs):
        super().__init__(master, **kwargs)
        self.radio_frame_list = radio_frame_list
        self.task_details = None
        self.radiobuttons = []
        self.variable = ctk.StringVar(value="")
        self.tasks = []
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)

    def set_task_details(self, task_details):
        self.task_details = task_details

    def remove_radiobuttons(self):
        for r in self.radiobuttons:
            r.destroy()
        self.tasks = []
        self.radiobuttons = []

    def add_radiobuttons(self):
        list_id = self.radio_frame_list.variable.get()
        task_rows = todo_db.get_all_tasks(list_id)

        for t in task_rows:
            self.tasks.append((t.id,t.list_id,t.name, t.deadline, t.status))

        for i, t in enumerate(self.tasks):
            date_and_name = f'{t[3]} : {t[2]}'
            task_deadline = t[3]
            task_status = t[4]
            current_date = datetime.now().date()
            if task_status == '1':
                radiobutton = ctk.CTkRadioButton(self, text=date_and_name, value=t[0],
                                                 command=self.radiobutton_event,
                                                 variable=self.variable, text_color='green')
            else:
                if task_deadline and current_date > task_deadline:
                    radiobutton = ctk.CTkRadioButton(self, text=date_and_name, value=t[0],
                                                     command=self.radiobutton_event,
                                                     variable=self.variable, text_color='red')
                else:
                    radiobutton = ctk.CTkRadioButton(self, text=date_and_name, value=t[0],
                                                     command=self.radiobutton_event,
                                                     variable=self.variable)
            radiobutton.grid(row=i, column=0, padx=5, pady=(5, 0), sticky="w")
            self.radiobuttons.append(radiobutton)

    def radiobutton_event(self):
        self.task_details.clear_task_details()
        self.task_details.fill_task_details()


class DetailsFrameTask(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.radio_frame_task = None
        self.grid_columnconfigure((0,1), weight=1)
        self.switch_var = ctk.StringVar(value="0")
        self.combobox_var = ctk.StringVar(value="")

        self.task_description = ctk.CTkTextbox(self, height=60, corner_radius=6)
        self.task_description.grid(row=0, column=1, padx=10, pady=(5, 5), sticky="nsew", rowspan=2)

        self.task_status = ctk.CTkSwitch(self, text="Done",
                                         variable=self.switch_var, onvalue="1", offvalue="0")
        self.task_status.grid(row=0, column=0, padx=20, pady=(5, 5), sticky="ew")
        self.task_priority = ctk.CTkComboBox(self, values=['','Low', 'Medium', 'High'],
                                             variable=self.combobox_var)
        self.task_priority.grid(row=1, column=0, padx=20, pady=(5, 5), sticky="ew")
        self.task_deadline = ctk.CTkEntry(self, placeholder_text='YYYY-mm-dd')
        self.task_deadline.grid(row=2, column=0, padx=20, pady=(5, 5), sticky="ew")
        self.update_button = ctk.CTkButton(self, text="Update Task"
                                             , command=self.update_task_command, corner_radius=6)
        self.update_button.grid(row=2, column=1, padx=10, pady=(5,5), sticky="ew")

    def set_radio_frame_task(self, radio_frame_task):
        self.radio_frame_task = radio_frame_task

    def clear_task_details(self):
        self.task_description.delete(0.0, 'end')
        self.task_status.deselect()
        self.task_priority.set('')
        self.task_deadline.delete(0, 'end')
        self.task_deadline.insert(0, 'YYYY-mm-dd')

    def fill_task_details(self):
        task_id = self.radio_frame_task.variable.get()
        task = todo_db.get_task(task_id)
        if task.description:
            self.task_description.insert("0.0", task.description)
        if task.status == '1':
            self.task_status.select()
        if task.priority:
            self.task_priority.set(task.priority)
        if task.deadline:
            self.task_deadline.delete(0, 'end')
            self.task_deadline.insert(0, task.deadline)

    def update_task_command(self):
        task_id = self.radio_frame_task.variable.get()
        task_description = self.task_description.get("0.0", "end")
        task_status = self.switch_var.get()
        task_priority = self.task_priority.get()
        task_deadline = self.task_deadline.get()
        if task_id:
            todo_db.update_task(task_id, task_description, task_status, task_priority, task_deadline)
        self.radio_frame_task.remove_radiobuttons()
        self.radio_frame_task.add_radiobuttons()

class MainFrameForList(ctk.CTkFrame):
    def __init__(self, master, title):
        super().__init__(master)
        self.master = master
        self.title = title
        self.main_task_frame = None
        self.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(self, text=self.title, fg_color='gray30', corner_radius=6)
        self.title_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")
        self.radio_frame_list = ScrollableFrameList(self, height=355)
        self.radio_frame_list.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        self.radio_frame_list.add_radiobuttons()
        self.buttons_frame_list = ButtonFrameList(self, self.radio_frame_list)
        self.buttons_frame_list.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

    def set_main_task_frame(self, main_task_frame):
        self.main_task_frame = main_task_frame
        self.radio_frame_list.set_radio_frame_task(self.main_task_frame.radio_frame_task)
        self.radio_frame_list.set_task_details(self.main_task_frame.task_details)
        self.buttons_frame_list.set_radio_frame_task(self.main_task_frame.radio_frame_task)
        self.buttons_frame_list.set_task_details(self.main_task_frame.task_details)


class MainFrameForTask(ctk.CTkFrame):
    def __init__(self, master, title, main_list_frame):
        super().__init__(master)
        self.master = master
        self.title = title
        self.main_list_frame = main_list_frame
        self.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(self, text=self.title, fg_color='gray30', corner_radius=6)
        self.title_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")
        self.radio_frame_task = ScrollableFrameTask(self,height=237
                                                    , radio_frame_list = self.main_list_frame.radio_frame_list)
        self.radio_frame_task.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        self.task_details = DetailsFrameTask(self)
        self.task_details.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        self.buttons_frame_task = ButtonFrameTask(self, self.main_list_frame.radio_frame_list
                                                  , self.radio_frame_task)
        self.buttons_frame_task.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
        self.radio_frame_task.set_task_details(self.task_details)
        self.task_details.set_radio_frame_task(self.radio_frame_task)
        self.buttons_frame_task.set_task_details(self.task_details)


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

        self.main_list_frame = MainFrameForList(self, title="Lists")
        self.main_list_frame.grid(column=0, row=0, padx=(10,5), pady=(10, 10), sticky='nsew')
        self.main_task_frame = MainFrameForTask(self, title="Tasks", main_list_frame = self.main_list_frame)
        self.main_list_frame.set_main_task_frame(self.main_task_frame)
        self.main_task_frame.grid(column=1, row=0, padx=(5,10), pady=(10, 10), sticky='nsew',columnspan=3)






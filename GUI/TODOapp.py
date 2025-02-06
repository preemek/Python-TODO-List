import customtkinter as ctk

class ButtonFrameList(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.grid_columnconfigure((0,1), weight=1)
        self.button_new_list = ctk.CTkButton(self, text="New List"
                                             , command=self.new_list_command, corner_radius=6)
        self.button_new_list.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.button_delete_list = ctk.CTkButton(self, text="Delete List"
                                             , command=self.delete_list_command, corner_radius=6)
        self.button_delete_list.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    def new_list_command(self):
        pass
    def delete_list_command(self):
        pass


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

    def new_task_command(self):
        pass
    def delete_task_command(self):
        pass


class ScrollableFrameList(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.radiobuttons = []
        self.variable = ctk.StringVar(value="")
        self.lists = ['Lista 1', 'Lista 2', 'Lista 3']

        for i, l in enumerate(self.lists):
            radiobutton = ctk.CTkRadioButton(self, text=l, value=l, variable=self.variable)
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
        self.grid_columnconfigure(0, weight=1)

        self.textbox = ctk.CTkTextbox(self, height=60, corner_radius=6)
        self.textbox.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
        self.textbox.insert("0.0", "Some example text!\n" * 5)


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
        self.buttons_frame_list = ButtonFrameList(self)
        self.buttons_frame_list.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")


class MainFrameForTask(ctk.CTkFrame):
    def __init__(self, master, title):
        super().__init__(master)
        self.master = master
        self.title = title
        self.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(self, text=self.title, fg_color='gray30', corner_radius=6)
        self.title_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")
        self.radio_frame_task = ScrollableFrameTask(self,height=285)
        self.radio_frame_task.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        self.task_details = DetailsFrameTask(self)
        self.task_details.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        self.buttons_frame_task = ButtonFrameTask(self)
        self.buttons_frame_task.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")


class TODOapp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("800x500")
        self.minsize(800, 500)
        self.maxsize(800, 500)
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.main_list_frame = MainFrameForList(self, title="Lists" )
        self.main_list_frame.grid(column=0, row=0, padx=(10,5), pady=(10, 10), sticky='nsew')
        self.main_task_frame = MainFrameForTask(self, title="Tasks")
        self.main_task_frame.grid(column=1, row=0, padx=(5,10), pady=(10, 10), sticky='nsew')





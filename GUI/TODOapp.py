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
    def __init__(self, master):
        super().__init__(master)
        self.radiobuttons = []
        self.variable = ctk.StringVar(value="")
        self.lists = ['Lista 1', 'Lista 2', 'Lista 3']

        for i, l in enumerate(self.lists):
            radiobutton = ctk.CTkRadioButton(self, text=l, value=l, variable=self.variable)
            radiobutton.grid(row=i + 1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.radiobuttons.append(radiobutton)


class ScrollableFrameTask(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)
        self.radiobuttons = []
        self.variable = ctk.StringVar(value="")
        self.tasks = ['Task 1', 'Task 2', 'Task 3']

        for i, t in enumerate(self.tasks):
            radiobutton = ctk.CTkRadioButton(self, text=t, value=t, variable=self.variable)
            radiobutton.grid(row=i + 1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.radiobuttons.append(radiobutton)




class MainFrameForList(ctk.CTkFrame):
    def __init__(self, master, title):
        super().__init__(master)
        self.master = master
        self.title = title
        self.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(self, text=self.title, fg_color='gray30', corner_radius=6)
        self.title_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")
        self.radio_frame_list = ScrollableFrameList(self)
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
        self.radio_frame_task = ScrollableFrameTask(self)
        self.radio_frame_task.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        self.buttons_frame_task = ButtonFrameTask(self)
        self.buttons_frame_task.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")




class TODOapp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("800x500")
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.main_list_frame = MainFrameForList(self, title="Lists" )
        self.main_list_frame.grid(column=0, row=0, padx=(10,5), pady=(10, 10), sticky='nsew')
        self.main_task_frame = MainFrameForTask(self, title="Tasks")
        self.main_task_frame.grid(column=1, row=0, padx=(5,10), pady=(10, 10), sticky='nsew')





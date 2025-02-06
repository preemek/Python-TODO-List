import customtkinter as ctk

class MainFrameForList(ctk.CTkFrame):
    def __init__(self, master, title):
        super().__init__(master)
        self.master = master
        self.title = title

        self.title_label = ctk.CTkLabel(self, text=self.title, fg_color='gray30', corner_radius=6)
        self.title_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

class MainFrameForTask(ctk.CTkFrame):
    def __init__(self, master, title):
        super().__init__(master)
        self.master = master
        self.title = title

        self.title_label = ctk.CTkLabel(self, text=self.title, fg_color='gray30', corner_radius=6)
        self.title_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")



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




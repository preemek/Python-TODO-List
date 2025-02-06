import customtkinter as ctk


class TODOapp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("400x220")

        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')

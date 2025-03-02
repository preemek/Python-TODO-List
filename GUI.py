from tasks import task_list
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from typing import Literal

class PyToDoList:
    def __init__ (self,root:tk.Tk):
        self.task_list=task_list()
        self.root=root
        self.root.geometry("800x500")
        self.root.protocol("WM_DELETE_WINDOW",self.save)
        self.selected_index=0
        self.main_menu()
    def save(self):
        self.task_list.save_list_to_json()
        self.root.destroy()
    def main_menu (self):
        def sort_list():
            def convert_values(var:tk.StringVar) -> str:
                if var.get() == "Alphabetical":
                    return "alphabetical"
                elif var.get() == "By date":
                    return "completion_date"
                elif var.get() == "Completion":
                    return "completion"
                elif var.get() == "Deadline":
                    return "deadline"
                elif var.get() == "Prioroty":
                    return "priority"
                elif var.get() == "None":
                    return "none"
                
            selected_sorting=convert_values(sorting_type)
            selected_extra_sorting=convert_values(extra_sorting_type)

            self.task_list.sort_list_of_tasks(selected_sorting,extra_sorting=selected_extra_sorting,reverse=reverse.get(),extra_reverse=extra_reverse.get())
        def create_filters():
            filterbutton = tk.Menubutton(self.root, text = "Menu")    
            filterbutton.menu = tk.Menu(filterbutton)   
            filterbutton["menu"]= filterbutton.menu
            filterbutton.menu.add_command(label="add task",command=add_task)
            filterbutton.menu.add_command(label="edit task",command=lambda:add_task("edit"))
            filterbutton.menu.add_command(label="delete task",command=delete_task)
            filterbutton.menu.add_separator()
            filterbutton.menu.add_cascade(label="Sorting")
            filterbutton.menu.add_radiobutton(label="Alphabetical",variable=sorting_type,command=update_task_selection_box)
            filterbutton.menu.add_radiobutton(label="By date",variable=sorting_type,command=update_task_selection_box)
            filterbutton.menu.add_checkbutton(label="Reverse", variable=reverse,command=update_task_selection_box)
            filterbutton.menu.add_separator() 
            filterbutton.menu.add_cascade(label="Extra Sorting")
            filterbutton.menu.add_radiobutton(label="None",variable=extra_sorting_type,command=update_task_selection_box)
            filterbutton.menu.add_radiobutton(label="Prioroty",variable=extra_sorting_type,command=update_task_selection_box)
            filterbutton.menu.add_radiobutton(label="Completion",variable=extra_sorting_type,command=update_task_selection_box)
            filterbutton.menu.add_radiobutton(label="Deadline",variable=extra_sorting_type,command=update_task_selection_box)
            filterbutton.menu.add_checkbutton(label="Reverse", variable=extra_reverse,command=update_task_selection_box)
            
            filterbutton.grid(row=0,column=0,sticky="NEW")
        def update_task_selection_box():
            sort_list()
            task_selection_box.delete(0,tk.END)

            for task in self.task_list.list_of_tasks:
                completion_mark=""
                if task.completion:
                    completion_mark="✓"
                task_selection_box.insert(tk.END,task.title+completion_mark)
                if task.after_deadline and not task.completion:
                    task_selection_box.itemconfig(tk.END,foreground="#bf0028")
        def on_select(event:tk.Event):
            w:tk.Listbox = event.widget
            try:
                self.selected_index = int(w.curselection()[0])
            except:
                return 0
            colour=task_selection_box.itemcget(self.selected_index,"foreground")
            task_selection_box.config(selectforeground=colour)
            show_task_info(self.selected_index)
        def show_task_info(index:int):
            selected_task=self.task_list.list_of_tasks[index]
            Title_var.set(selected_task.title)
            date_list=selected_task.completion_date.split("-")
            date_str=date_list[2]+"-"+date_list[1]+"-"+date_list[0]
            Date_var.set(date_str)
            colour=task_selection_box.itemcget(index,"foreground")
            Task_Date.config(foreground=colour)
            Priority_var.set(selected_task.priority)
            Description.configure(state="normal")
            Description.delete('1.0',tk.END)
            Description.insert(tk.END,selected_task.description)
            Description.configure(state="disabled")
            Complete_task_checkbtt_var.set(selected_task.completion)
            Complete_task_checkbtt.configure(command=lambda:[self.task_list.toogle_completion(index),update_task_selection_box()])
        def delete_task():
            self.task_list.delete_task(self.selected_index)
            update_task_selection_box()
        def add_task(function:Literal["add","edit"]="add"):
            task_selection_box.config(state="disabled")
            def fisnish_adding_task(abort:bool):
                task_selection_box.config(state="normal") # state needs to ba changed earlier beacause then updating_task_selection_box doesnt work as intended
                if not abort:
                    Title=Entry_Title.get()
                    selected_Description=Description.get('1.0',tk.END)
                    Completion_date=Entry_Date_year.get()+"-"+Entry_Date_month.get()+"-"+Entry_Date_day.get()
                    try:
                        int(Entry_Date_day.get())
                        int(Entry_Date_month.get())
                        int(Entry_Date_year.get())
                    except:
                        messagebox.showwarning("wrong date","Date wasn't chosen corectly")
                        return 0
                    Priority=ComBox_Priority.get()
                    # crate new task
                    if function=="edit":
                        delete_task()
                    self.task_list.add_task(Title,selected_Description,Completion_date,Priority)
                    update_task_selection_box()
                
                # delete all added widgets
                Entry_Title.destroy()
                ComBox_Priority.destroy()
                Finish_btt1.destroy()
                Finish_btt2.destroy()
                Date_frame.destroy()
                Description.delete('1.0',tk.END)
                Description.config(state="disabled")
                Hide_completion.destroy()
                
                
                

            if function == "edit":
                index=self.selected_index
                Title=self.task_list.list_of_tasks[index].title
                Deescription_val=self.task_list.list_of_tasks[index].description
                Priority=self.task_list.list_of_tasks[index].priority
                Date=self.task_list.list_of_tasks[index].completion_date.split("-")
                Date_d=Date[2]
                Date_m=Date[1]
                Date_y=Date[0]
            else:
                Title="Title"
                Deescription_val=""
                Priority="none"
                Date_d="d"
                Date_m="m"
                Date_y="y"

            Entry_Title=tk.Entry(frame,background="#f0f0f0")
            Entry_Title.insert(tk.END,Title)
            Entry_Title.grid(row=0,column=0,sticky="NW")
            
            Date_frame=tk.Frame(frame,relief="flat")
            Date_frame.grid(row=0,column=2)

            Entry_Date_day=ttk.Spinbox(Date_frame,from_=1,to=31,width=3)
            Entry_Date_day.set(Date_d)
            Entry_Date_day.pack(side="left")

            Entry_Date_month=ttk.Spinbox(Date_frame,from_=1,to=12,width=3)
            Entry_Date_month.set(Date_m)
            Entry_Date_month.pack(side="left")

            Entry_Date_year=ttk.Spinbox(Date_frame,from_=2020,to=2100,width=5)
            Entry_Date_year.set(Date_y)
            Entry_Date_year.pack(side="left")


            Description.config(state="normal")
            Description.delete('1.0',tk.END)
            Description.insert(tk.END,Deescription_val)
            Hide_completion=ttk.Label(frame,text="")
            Hide_completion.grid(row=0,column=5,columnspan=2,sticky="NWE")
            ComBox_Priority=ttk.Combobox(frame,values=["high","medium","low","none"])
            ComBox_Priority.set(Priority)
            ComBox_Priority.config(state="readonly")
            ComBox_Priority.grid(row=0,column=4)
            
            Finish_btt1=ttk.Button(frame,text="finish",command=lambda:fisnish_adding_task(False))
            Finish_btt1.grid(row=3,column=5)
            Finish_btt2=ttk.Button(frame,text="close",command=lambda:fisnish_adding_task(True))
            Finish_btt2.grid(row=3,column=4)



            
        reverse = tk.BooleanVar()
        extra_reverse = tk.BooleanVar()
        sorting_type = tk.StringVar(value="Alphabetical")
        extra_sorting_type = tk.StringVar(value="none")
        Title_var = tk.StringVar(value="Title")
        Date_var = tk.StringVar(value="dd-mm-yyyy")
        Priority_var = tk.StringVar(value="none")
        Complete_task_checkbtt_var = tk.BooleanVar(value=False)

        self.root.rowconfigure(1,weight=1,minsize=100)
        self.root.columnconfigure(1,weight=1)
        task_selection_box=tk.Listbox(selectbackground="#e5e5e5",selectforeground="black",activestyle="dotbox",background="#f0f0f0")
        task_selection_box.grid(row=1,column=0,sticky="NS")
        task_selection_box.bind('<<ListboxSelect>>', on_select)
        update_task_selection_box()

        create_filters()

        frame=tk.Frame(self.root,relief="raised",bd=1)
        frame.grid(row=0,rowspan=2,column=1,sticky="NESW")
        frame.rowconfigure(2,weight=1)
        frame.columnconfigure(0,weight=1)
        
        Title=ttk.Label(frame,textvariable=Title_var,anchor="w")
        Title.grid(row=0,column=0,sticky="NW")

        Date_Label=ttk.Label(frame,text="Scheduled for:") 
        Date_Label.grid(row=0,column=1,sticky="NE")
        Task_Date=ttk.Label(frame,textvariable=Date_var)
        Task_Date.grid(row=0,column=2,sticky="NE",padx=(0,20))

        Priority_Label=ttk.Label(frame,text="Priority:",anchor="e")
        Priority_Label.grid(row=0,column=3,sticky="NE")
        Task_Priority=ttk.Label(frame,textvariable=Priority_var)
        Task_Priority.grid(row=0,column=4,sticky="NW",padx=(0,20))

        Complete_task_Label=ttk.Label(frame,text="Task Completed",anchor="e")
        Complete_task_Label.grid(row=0,column=5,sticky="NE")
        Complete_task_checkbtt=ttk.Checkbutton(frame,variable=Complete_task_checkbtt_var)
        Complete_task_checkbtt.grid(row=0,column=6,sticky="NW")

        scrollbar = tk.Scrollbar(frame, orient="vertical")


        Description=tk.Text(frame,relief="flat",background="#f0f0f0",yscrollcommand=scrollbar.set,bd=2)
        scrollbar.config(command=Description.yview)
        Description.config(state="disabled")
        Description.grid(row=2,column=0,columnspan=5,sticky="NESW")

        scrollbar.grid(row=2,column=7,sticky="NS")

        ttk.Separator(frame,orient="horizontal").grid(row=1,column=0,columnspan=7,sticky="EW")
        
# testing only
# a=tk.Tk()
# app=PyToDoList(a)
# a.mainloop()
import json
from typing import Literal
import time

class task:
    def __init__(self,title,description,completion_date,priority:Literal["none","low","medium","high"],completion=False):
        self.title:str = title
        self.description:str = description
        self.completion_date:str = completion_date
        self.completion:bool = completion
        self.priority:str = priority

class tasks:
    def __init__(self):
        self.list_of_tasks:list[task]=[]
        with open('data.json','r') as file:
            loaded_data = json.load(file)
            for dict in loaded_data:
                self.add_task(dict["title"],dict["description"],dict["completion_date"],dict["priority"],dict["completion"])
    
    def save_list_to_json (self):
        data=[]
        for task in self.list_of_tasks:
            data.append(task.__dict__)
        with open("data.json", "w") as outfile:
            json.dump(data, outfile)

    def modify_title (self,title): 
        """if title is already in list_of_tasks, add number to it"""
        i=2
        if title in self.list_of_tasks:
            title = title +" (" + str(i) + ")"
        else:
            return title

        while True:
            i+=1 
            if title in self.list_of_tasks:
                x=title.rfind(" (")
                new_title = title[:x] +" (" + str(i) + ")"

                title=new_title
            else:
                return title
            
    def add_task(self,title,description,completion_date,priority:Literal["none","low","medium","high"],completion=False):
        """ ``completion_date`` date format is y-m-d """
        modified_title = self.modify_title(title)
        self.list_of_tasks.append(task(modified_title,description,completion_date,priority,completion=completion))

    def toogle_completion (self,index):
        self.list_of_tasks[index].completion = not self.list_of_tasks[index].completion



# zadania=tasks()
# print(zadania.list_of_tasks[0].completion_date)
# zadania.save_list_to_json()

"""
# <date> > time.strftime("%Y-%m-%d") current date is bigger than <date>, your task is late
# <date> == time.strftime("%Y-%m-%d") current date is the same as <date>, your task was scheduled for today



"""
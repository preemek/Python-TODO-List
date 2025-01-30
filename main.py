import json
from typing import Literal
import time

class task:
    def __init__(self,title,description,completion_date,priority:Literal["none","low","medium","high"],completion=False):
        self.title=title
        self.description=description
        self.completion_date=completion_date
        self.completion=completion
        self.priority=priority

class tasks:
    def __init__(self):
        self.list_of_tasks=[]
        with open('Python-TODO-List\data.json','r') as file:
            loaded_data = json.load(file)
            for dict in loaded_data:
                self.add_task(dict["title"],dict["description"],dict["completion_date"],["priority"])
    def save_list_to_json (self):
        data=[]
        for task in self.list_of_tasks:
            data.append(task.__dict__)
        with open("Python-TODO-List\data.json", "w") as outfile:
            json.dump(data, outfile)

    def modify_title (self,title): 
        """if title is already in zadania, add number to it"""
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
            
    def add_task(self,title,description,completion_date,priority:Literal["none","low","medium","high"]):
        """ ``date`` format is y-m-d """
        modified_title = self.modify_title(title)
        self.list_of_tasks.append(task(modified_title,description,completion_date,priority))
zadania=tasks()


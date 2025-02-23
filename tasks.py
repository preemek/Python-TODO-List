import json
from typing import Literal
import time

class task:
    def __init__(self,title,description,completion_date,priority:Literal["none","low","medium","high"]="none",completion=False):
        self.title:str = title
        self.description:str = description
        self.completion_date:str = completion_date
        self.completion:bool = completion
        self.priority:str = priority
        self.after_deadline:bool=False
        if self.completion_date < time.strftime("%Y-%m-%d"):
            self.after_deadline=True

    def __str__ (self):
        return(f"Title: {self.title}, Description: {self.description}, Completion_date: {self.completion_date}, Completion: {self.completion}, Priority: {self.priority}, Is Late: {self.after_deadline}")
class task_list:
    def __init__(self):
        self.list_of_tasks:list[task]=[]
        with open("Python-TODO-List\data.json", "r") as file:
            loaded_data = json.load(file)
            for dict in loaded_data:
                self.add_task(dict["title"],dict["description"],dict["completion_date"],dict["priority"],dict["completion"])
    
    def save_list_to_json (self):
        data=[]
        for task in self.list_of_tasks:
            data.append(task.__dict__)
        with open("Python-TODO-List\data.json", "w", encoding="UTF-8") as outfile:
            json.dump(data, outfile)

    def modify_title (self,title:str): 
        """if title is already in list_of_tasks, add number to it"""
        i=2
        list_of_names=[]
        for task in self.list_of_tasks:
            list_of_names.append(task.title)
        if title in list_of_names:
            title = title +" (" + str(i) + ")"
        else:
            return title

        while True:
            i+=1 
            if title in list_of_names:
                x=title.rfind(" (")
                new_title = title[:x] +" (" + str(i) + ")"

                title=new_title
            else:
                return title
    
    def add_task(self,title:str,description,completion_date,priority:Literal["none","low","medium","high"]="none",completion=False):
        """ ``completion_date`` date format is y-m-d """
        modified_title = self.modify_title(title)
        self.list_of_tasks.append(task(modified_title,description,completion_date,priority,completion=completion))
    def delete_task (self,index):
        self.list_of_tasks.pop(index)
    def change_priority(self,index:int,new_priority:Literal["none","low","medium","high"]):
        self.list_of_tasks[index].priority=new_priority

    def toogle_completion (self,index:int):
        self.list_of_tasks[index].completion = not self.list_of_tasks[index].completion

    def sort_list_of_tasks (self,sorting_type:Literal["alphabetical","completion_date"],reverse:bool=False,extra_sorting:Literal["completion","deadline","priority"]="none",extra_reverse:bool=False):
        priority=lambda x: 4 if x.priority=="none" else (3 if x.priority=="low" else (2 if x.priority=="medium" else 1))
        reversed_priority=lambda x: 4 if x.priority=="high" else (3 if x.priority=="medium" else (2 if x.priority=="low" else 1))
        second_reverse=lambda x: x if extra_reverse else not x

        def sort_key(key,varible:task):
            """if ther eis no extra sorting, it will just return key"""
            if extra_sorting == "completion":
                return (second_reverse(varible.completion),key)
            elif extra_sorting == "deadline":
                return (second_reverse(varible.after_deadline),key)
            elif extra_sorting == "priority":
                if extra_reverse:
                    return (reversed_priority(varible),key)
                else:
                    return (priority(varible),key)
            return key
        
        if sorting_type == "alphabetical":
            self.list_of_tasks.sort(key=lambda x:sort_key(x.title,x),reverse=reverse)
        elif sorting_type == "completion_date":
            self.list_of_tasks.sort(key=lambda x:sort_key(x.completion_date,x),reverse=reverse)

# a=task_list()
"""
# <date> < time.strftime("%Y-%m-%d") current date is bigger than <date>, your task is late
# <date> == time.strftime("%Y-%m-%d") current date is the same as <date>, your task was scheduled for today
[{"title": "hej", "description": "im testing function", "completion_date": "2025-01-31", "completion": false, "priority": "high"}, {"title": "second hej", "description": "im testing function twice", "completion_date": "2025-02-31", "completion": false, "priority": "low"}]

class xx:
    def __init__(self,priorit):
        self.priority=priorit


def func(varible:xx):
    return lambda:4 if varible.priority!="none" else (3 if varible.priority!="low" else (2 if varible.priority!="medium" else 1))
print()
"""
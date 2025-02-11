
from settings import DATABASE
from sqlalchemy import URL, create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

connect_url = URL.create(
    'postgresql+psycopg2',
    username=DATABASE['default'].get('USER'),
    password=DATABASE['default'].get('PASSWORD'),
    host=DATABASE['default'].get('HOST'),
    port=DATABASE['default'].get('PORT'),
    database=DATABASE['default'].get('NAME'))



class TODO_db:
    def __init__(self, connect_url):
        self.engine = create_engine(connect_url)
        self.Base = automap_base()
        self.Base.prepare(self.engine)
        self.List = self.Base.classes.list
        self.Task = self.Base.classes.task

    def get_all_lists(self):
        with Session(self.engine) as session:
            list = session.query(self.List).all()
        return list

    def add_new_list(self, list_name):
        with Session(self.engine) as session:
            new_list = self.List(name = list_name)
            session.add(new_list)
            session.commit()

    def delete_list(self, list_id):
        with Session(self.engine) as session:
            list_to_delete = session.query(self.List).filter(self.List.id == list_id).one()
            session.delete(list_to_delete)
            session.commit()

    def get_all_tasks(self, list_id):
        with Session(self.engine) as session:
            tasks = session.query(self.Task).filter(self.Task.id == list_id).all()
        return tasks

    def add_new_task(self, list_id, task_name):
        with Session(self.engine) as session:
            new_task = self.Task(name = task_name, list_id = list_id)
            session.add(new_task)
            session.commit()






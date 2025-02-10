from streamlit import connection

from settings import DATABASE
import psycopg2

class ToDoDataBase:
    def __init__(self, connection):
        self.connection = connection

    def add_list(self,name):
        query = 'INSERT INTO list (name) VALUES (%s) RETURNING id;'
        with self.connection.cursor() as cursor:
            cursor.execute(query, (name))
            list_id = cursor.fetchone()[0]
            self.connection.commit()

        return list_id

    def get_list(self,list_id):
        query = 'SELECT * FROM list WHERE id = %s'
        with self.connection.cursor() as cursor:
            cursor.execute(query, (list_id))
            list = cursor.fetchone()
            self.connection.commit()

        return list

    def get_lists(self):
        query = 'SELECT * FROM list'
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            lists = cursor.fetchall()
            self.connection.commit()

        return lists

    def update_list(self,id,name):
        query = 'UPDATE list SET name = %s WHERE id = %s'
        with self.connection.cursor() as cursor:
            cursor.execute(query, (name,id))
            self.connection.commit()
            if cursor.rowcount == 1:
                list_id = cursor.fetchone()[0]
            else:
                list_id = 0

        return list_id

    def delete_list(self,id):
        query = 'DELETE FROM list WHERE id = %s'
        with self.connection.cursor() as cursor:
            cursor.execute(query, (id))
            self.connection.commit()
            if cursor.rowcount == 1:
                list_id = cursor.fetchone()[0]
            else:
                list_id = 0

        return list_id

    def insert_list(self, name):
        query = 'INSERT INTO list (name) VALUES (%s)'
        with self.connection.cursor() as cursor:
            cursor.execute(query, (name))
            self.connection.commit()
            if cursor.rowcount == 1:
                list_id = cursor.fetchone()[0]
            else:
                list_id = 0

        return list_id


try:
    connection = psycopg2.connect(host=DATABASE['default'].get('HOST'),
                                  database=DATABASE['default'].get('NAME'),
                                  user=DATABASE['default'].get('USER'),
                                  password=DATABASE['default'].get('PASSWORD'),
                                  port=DATABASE['default'].get('PORT')
                                  )
    todo_db = ToDoDataBase(connection)
    print(todo_db.get_list('2'))
    print(todo_db.get_lists())
except (Exception, psycopg2.DatabaseError) as error:
    print('error in db connection')
    print(error)
finally:
    if connection:
        connection.close()
        print('db connection closed')
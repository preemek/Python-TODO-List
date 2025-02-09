from streamlit import connection

from settings import DATABASE
import psycopg2

print(DATABASE['default'].get('ENGINE'))
print(DATABASE['default'].get('NAME'))
print(DATABASE['default'].get('USER'))
print(DATABASE['default'].get('PASSWORD'))
print(DATABASE['default'].get('HOST'))
print(DATABASE['default'].get('PORT'))


try:
    connection = psycopg2.connect(host=DATABASE['default'].get('HOST'),
                                  database=DATABASE['default'].get('NAME'),
                                  user=DATABASE['default'].get('USER'),
                                  password=DATABASE['default'].get('PASSWORD'),
                                  port=DATABASE['default'].get('PORT')
                                  )
    print('db connected')
except (Exception, psycopg2.DatabaseError) as error:
    print('error in db connection')
    print(error)
finally:
    if connection:
        connection.close()
        print('db connection closed')
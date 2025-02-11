
from settings import DATABASE
from sqlalchemy import URL
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine

connect_url = URL.create(
    'postgresql+psycopg2',
    username=DATABASE['default'].get('USER'),
    password=DATABASE['default'].get('PASSWORD'),
    host=DATABASE['default'].get('HOST'),
    port=DATABASE['default'].get('PORT'),
    database=DATABASE['default'].get('NAME'))

engine = create_engine(connect_url)
Base = automap_base()
Base.prepare(engine)
List = Base.classes.list








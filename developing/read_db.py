from psycopg import connect
from dotenv import load_dotenv
import os

def get_cities():

    load_dotenv()
    try:
        port = int(os.environ.get('PG_PORT', default='5432'))
    except ValueError:
        port = 5432
    data = {
        'host': os.environ.get('PG_HOST', default='127.0.0.1'),
        'port': port,
        'dbname': os.environ.get('PG_DBNAME', default='test'),
        'user': os.environ.get('PG_USER', default='test'),
        'password': os.environ.get('PG_PASSWORD'),
    }
    connection = connect(**data)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM cities;')
    return cursor.fetchall()

get_cities()
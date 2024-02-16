from psycopg import connect
from dotenv import load_dotenv
import os

def connect_db():
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
    return connect(**data)


def get_cities():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM cities;')
    return cursor.fetchall()

def fill_cities() -> None:
    exit_msg = 'q'
    connection = connect_db()
    cursor = connection.cursor()
    request = "INSERT INTO cities (name, latitude, longtitude) VALUES ('{}', {}, {})"
    while True:
        name = input(f'Input name city or place: [{exit_msg}] to exit: ')
        if name == exit_msg:
            break
        coordinates = input(f'Input their coordinates ", ": ')
        try:
            lat, lon = coordinates.split(', ')
            lat, lon = float(lat), float(lon)
        except ValueError:
            print('Wrong format for coordinates')
            continue
        cursor.execute(request.format(name, lat, lon))
    connection.commit()
    connection.close()

fill_cities()
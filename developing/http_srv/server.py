from http.server import BaseHTTPRequestHandler, HTTPServer

import db
import json
from typing import Optional, Callable
from dotenv import load_dotenv

import weather
from config import *


def database_connection(class_: type) -> type:
    conn_name, cursor_name = 'db_connection', 'db_cursor'
    connection, cursor = db.connect()
    setattr(class_, conn_name, connection)
    setattr(class_, cursor_name, cursor)
    return class_


@database_connection
class CustomHandler(BaseHTTPRequestHandler):
    def respond(
            self, status: int, body: str, 
            headers: Optional[dict] = None, 
            message: Optional[str] = None,
        ) -> None:
        self.send_response(status, message)
        self.send_header('Content-Type', 'text')
        if headers:
            for header, value in headers.items():
                self.send_header(header, value)
        self.end_headers()
        self.wfile.write(body.encode())

    def not_allowed(self, methods: Optional[str] = None) -> None:
        headers = {'Allow': methods} if methods else {'Allow': '[GET]'}
        self.respond(NOT_ALLOWED, '', headers=headers)

    def cities_page(self) -> None:
        try:
            cities = db.get_cities(self.db_cursor)
        except Exception as error:
            status, body = SERVER_ERROR, f'Database error: {error}'
        else:
            status, body = OK, '\n'.join(str(city) for city in cities)
        self.respond(status, body)

    def weather_page(self) -> None:
        city_name = self.path[self.path.rindex('/')+1:]
        db_response = db.coordinates_by_city(self.db_cursor, city_name)
        if not db_response:
            self.respond(OK, f'No city named {city_name} in database')
            return
        self.respond(OK, str(weather.get_weather(*db_response)))

    def do_GET(self) -> None:
        if self.path.startswith('/cities'):
            self.cities_page()
        elif self.path.startswith('/weather'):
            self.weather_page()
        else:
            pass
            #self.main_page()

    def do_POST(self) -> None:
        try:
            body_len = int(self.headers.get('Content-Length'))
        except ValueError:
            self.respond(BAD_REQUEST, 'Content-Length header error')
            return
        try:
            city = json.loads(self.rfile.read(body_len))
        except json.JSONDecodeError:
            self.respond(BAD_REQUEST, 'Invalid JSON')
            return
        if any(key not in city.keys() for key in CITY_KEYS) or len(city) != len(CITY_KEYS):
            self.respond(BAD_REQUEST, f'City json data is invalid, required keys: {CITY_KEYS}')
            return
        self.change_db(db.add_city, (self.db_cursor, self.db_connection, [city[key] for key in CITY_KEYS]), 'created', CREATED)

    def do_DELETE(self) -> None:
        city_name = self.path[1:]
        if not city_name:
            self.respond(BAD_REQUEST, 'City is not specified')
            return
        self.change_db(db.delete_city, (self.db_cursor, self.db_connection, city_name), 'deleted', NO_CONTENT)

    def change_db(self, method: Callable, params: tuple, action: str, success_code: int) -> None:
        try:
            deleted = method(*params)
        except Exception as error:
            self.respond(SERVER_ERROR, f'Database error: {error}')
            self.db_connection.rollback() # Roll back the transaction if it failed
            return
        if deleted:
            self.respond(success_code, f'Record with {params[-1]} was {action}')
        else:
            self.respond(SERVER_ERROR, f'City was not {action}: {params[-1]}')


if __name__ == '__main__':
    server = HTTPServer((HOST, PORT), CustomHandler)
    print(f'Server is running on http://{HOST}:{PORT}')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('Closed by user')
    finally:
        server.server_close()

CITIES_SELECT = 'SELECT * FROM cities;'
CITIES_INSERT = 'INSERT INTO cities (name, latitude, longtitude) VALUES (%s, %s, %s)'
CITIES_COORD_BY_CITY = 'SELECT latitude, longtitude FROM cities WHERE name=%s'
CITY_KEYS = 'name', 'lat', 'lon'
CITIES_DELETE_BY_NAME = 'DELETE FROM city WHERE name=%s'

HOST, PORT = ('127.0.0.1', 8000)
OK = 200
CREATED = 201
SERVER_ERROR = 500
BAD_REQUEST = 400
NOT_ALLOWED = 405
NO_CONTENT = 204


YANDEX_KEY_HEADER = 'X-Yandex-API-Key'
URL = 'https://api.weather.yandex.ru/v2/informers?'
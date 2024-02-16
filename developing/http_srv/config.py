CITIES_SELECT = 'SELECT * FROM cities;'
CITIES_INSERT = 'INSERT INTO cities (name, latitude, longtitude) VALUES (%s, %s, %s)'
CITIES_COORD_BY_CITY = 'SELECT latitude, longtitude FROM cities WHERE name=%s'

HOST, PORT = ('127.0.0.1', 8000)
OK = 200
CREATED = 201
SERVER_ERROR = 500
BAD_REQUEST = 400
CITY_KEYS = 'name', 'lat', 'lon'
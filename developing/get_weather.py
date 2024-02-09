import requests
from dotenv import load_dotenv
import os 
import json
from read_db import get_cities

load_dotenv()

URL = 'https://api.weather.yandex.ru/v2/informers?'
headers = {'X-Yandex-API-Key': os.environ.get('YANDEX_KEY')}
OK = 200
EXIT_MSG = 'q'

class ForecastAPIError(Exception):
    def __init__(self, api_name: str, status: int) -> None:
        super().__init__(f'API {api_name} request failed with {status}')

def get_weather(latitude: float = 55.75396, longtitude: float = 37.620393) -> dict:
    coordinates = {'lat': latitude, 'lon': longtitude}
    response = requests.get(URL, params=coordinates, headers=headers)
    if response.status_code != OK:
        raise ForecastAPIError('Yandex.Weather', response.status_code)
    return json.loads(response.content)

if __name__ == '__main__':
    cities = get_cities()
    menu = '\n'.join([f'{ind+1}. {city[0]}' for ind, city in enumerate(cities)])

    while True:
        msg = 'Choice youre place in menu:\n'
        answer = input(f'{msg}{menu}\n')
        try:
            city, lat, long = cities[int(answer) - 1]
        except ValueError:
            print(f'Number must be int, not another, or input {EXIT_MSG} to exit')
        except IndexError:
            print(f'Number must be in list')
        else:
            weather = get_weather(lat, long)
            fact = weather['fact']
            print(f'Temperature in {city}: {fact["temp"]}')
            print(f'Feels like: {fact["feels_like"]}')
            print(f'Wind speed: {fact["wind_speed"]}')

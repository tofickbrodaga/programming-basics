import requests
from config import *
import os 
import json

class ForecastAPIError(Exception):
    def __init__(self, api_name: str, status: int) -> None:
        super().__init__(f'API {api_name} request failed with {status}')

def get_weather(latitude: float = 55.75396, longtitude: float = 37.620393) -> dict:
    headers = {YANDEX_KEY_HEADER    : os.environ.get('YANDEX_KEY')}
    coordinates = {'lat': latitude, 'lon': longtitude}
    response = requests.get(URL, params=coordinates, headers=headers)
    if response.status_code != OK:
        raise ForecastAPIError('Yandex.Weather', response.status_code)
    return json.loads(response.content)
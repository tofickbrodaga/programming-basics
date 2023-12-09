# Компоновщик
class NotTemperatureException(Exception):
    pass

class Product:
    def __init__(self, name: str, storage_temp = int) -> None:
        self.name, self.storage_temp = name, storage_temp
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, new_name: str) -> None:
        if not isinstance(new_name, str):
            raise TypeError('Name must be a string')
        self._name = new_name
    
    @property
    def storage_temp(self) -> None:
        return self._storage_temp
    
    @storage_temp.setter
    def storage_temp(self, new_storage_temp: int) -> None:
        if not isinstance(new_storage_temp, int):
            raise TypeError('Storage temperature must be an integer')
        self._storage_temp = new_storage_temp

class Fridge:
    def __init__(self, fridge: list[Product], freezer: list[Product], freezer_temp_range: tuple[int, int], fridge_temp_range: tuple[int, int]) -> None:
        self.fridge, self.freezer = fridge, freezer
        self.fridge_temp_range, self.freezer_temp_range = fridge_temp_range, freezer_temp_range

    def check_is_product(self, item: Product) -> None:
        if not isinstance(item, Product):
            raise TypeError('Product must be a Products, hehe')

    @property
    def fridge(self) -> list[Product]:
        return self._fridge
    
    @fridge.setter
    def fridge(self, new_fridge: list[Product]) -> None:
        if not isinstance(new_fridge, list):
            raise TypeError('Fridge must be a list')
        for item in new_fridge:
            self.check_is_product(item)
        self._fridge = new_fridge
    
    @property
    def freezer(self) -> list[Product]:
        return self._freezer
    
    @freezer.setter
    def freezer(self, new_freezer: list[Product]) -> None:
        if not isinstance(new_freezer, list):
            raise TypeError('Freezer must be a list')
        for item in new_freezer:
            self.check_is_product(item)
        self._freezer = new_freezer
    
    @property
    def freezer_temp_range(self) -> tuple[int, int]:
        return self._freezer_temp_range
    
    @freezer_temp_range.setter
    def freezer_temp_range(self, new_freezer_temp_range: tuple[int, int]) -> None:
        if not isinstance(new_freezer_temp_range, tuple):
            raise TypeError('Freezer temperature range must be a tuple')
        if len(new_freezer_temp_range) != 2:
            raise ValueError('Freezer temperature range must be a tuple of length 2')
        if not isinstance(new_freezer_temp_range[0], int) or not isinstance(new_freezer_temp_range[1], int):
            raise TypeError('Freezer temperature range must be a tuple of integers')
        self._freezer_temp_range = new_freezer_temp_range
    
    @property
    def fridge_temp_range(self) -> tuple[int, int]:
        return self._fridge_temp_range
    
    @fridge_temp_range.setter
    def fridge_temp_range(self, new_fridge_temp_range: tuple[int, int]) -> None:
        if not isinstance(new_fridge_temp_range, tuple):
            raise TypeError('Fridge temperature range must be a tuple')
        if len(new_fridge_temp_range) != 2:
            raise ValueError('Fridge temperature range must be a tuple of length 2')
        if not isinstance(new_fridge_temp_range[0], int) or not isinstance(new_fridge_temp_range[1], int):
            raise TypeError('Fridge temperature range must be a tuple of integers')
        self._fridge_temp_range = new_fridge_temp_range

    def add(self, product: Product) -> None:
        self.check_is_product(product)
        if product.storage_temp <= self.fridge_temp_range[1] and product.storage_temp >= self.fridge_temp_range[0]:
            self.fridge.append(product)
        elif product.storage_temp <= self.freezer_temp_range[1] and product.storage_temp >= self.freezer_temp_range[0]:
            self.freezer.append(product)
        else:
            raise NotTemperatureException(f'Product {product.name} is not in the temperature range')

    def remove(self, product: Product) -> None:
        self.check_is_product(product)
        if product in self.fridge:
            self.fridge.remove(product)
        elif product in self.freezer:
            self.freezer.remove(product)
        else:
            raise ValueError(f'Product {product.name} is not in the fridge or freezer')

    @property
    def products(self) -> str:
        return f'Fridge: {self.fridge}, Freezer: {self.freezer}'

    def get(self, name: str) -> list:
        products = []
        for product in self.fridge:
            if name in product.name:
                products.append(product)
        for product in self.freezer:
            if name in product.name:
                products.append(product)
        if len(products) == 0:
            raise ValueError(f'Product {name} is not in the fridge or freezer')
        return products


# Builder
from abc import ABC

class Vehicle:
    def init(self, surface: str, speed: int):
        self.surface, self.speed = surface, speed

    def move(self) -> None:
        print(f'{self.__class__.__name__}: surface: {self.surface}, speed: {self.speed}')

    def set_surface(self, surface: str) -> None:
        self.surface = surface

    def set_speed(self, speed: int) -> None:
        self.speed = speed

class VehicleCreator(ABC):
    _surface: str
    _speed: int

    @classmethod
    def create(cls, speed: int) -> Vehicle:
        vehicle = Vehicle()
        vehicle.set_surface(cls._surface)
        vehicle.set_speed(speed)
        return vehicle

class BoatCreator(VehicleCreator):
    _surface = 'water'
    _speed = 6
    
class CarCreator(VehicleCreator):
    _surface = 'road'
    _speed = 33


# Flyweight  -> Singleton
import random
from faker import Faker
from typing import Self


class PersonAttrsCreator:
    _pool: dict = dict()
    __ages = set()

    def __new__(cls, *args, **kwargs) -> Self:
        key = hash((cls, args, frozenset(kwargs.items())))
        if key not in cls._pool.keys():
            cls._pool[key] = super().__new__(cls)
        return cls._pool[key]

    def age(self):
        if len(self.__ages) == 100:
            self.__ages.clear()
        age = random.randint(0, 99)
        while age in self.__ages:
            age = random.randint(0, 99)
        self.__ages.add(age)
        return age

    def name(self):
        faker = Faker()
        return faker.name()

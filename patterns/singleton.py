from typing import Self
from psutil import Process

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs) -> Self:
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance
    

class Person(Singleton):
    def __init__(self, name: str) -> None:
        self.name = name


class Cat(Singleton):
    def __init__(self, name: str) -> None:
        self.name = name

people = [Person('егрр') for _ in range(10 ** 7)]

print(f'memory used: {Process().memory_info().vms / 1024 / 1024}')
print(len(people))
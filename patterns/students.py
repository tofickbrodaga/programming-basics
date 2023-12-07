from typing import Callable

class Student:
    def __init__(self, name: str, age: int) -> None:
        self.name, self.age = name, age


def add_property(attr: str, checkers: list[Callable]):
    def decorator(cls: type) -> type:
        
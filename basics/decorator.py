from typing import Callable

def ensure(attr: str, checker: Callable) -> Callable:
    def add_property(class_: type) -> type:
        def getter(self):
            return getattr(self, f'_{attr}')
        def setter(self, value):
            checker(value)
            setattr(self, f'_{attr}', value)
        
        setattr(class_, attr, property(getter, setter))

        return class_
    return add_property

def check_positive_int(value: int) -> None:
    if not isinstance(value, int):
        return TypeError(f'Value expected to be int, not {type(value).__name__}')
    if value < 0:
        return ValueError(f'Value {value} is expected to be posititve')


@ensure('age', check_positive_int)
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name, self.age = name, age


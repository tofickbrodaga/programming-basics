from abc import ABCMeta
from copy import deepcopy
from typing import Self

class PrototypeMixin(metaclass=ABCMeta):
    def prototype(self) -> Self:
        return deepcopy(self)
    
    def prototype_parametrize(self, **kwargs) -> Self:
        copy = deepcopy(self)
        for attr, value in kwargs.items():
            setattr(copy, attr, value)
        return copy
    
class Person(PrototypeMixin):
    def __init__(self, name: str, age: int) -> None:
        self.name, self.age = name, age
    
    def __str__(self) -> str:
        return super().__str__()
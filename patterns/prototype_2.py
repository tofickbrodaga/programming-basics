from abc import ABC, abstractmethod
from copy import deepcopy


class Prototype(ABC):
    def prototype(self) -> None:
        return deepcopy(self)
    
    def prototype_parametrize(self, **kwargs) -> None:
        copy = deepcopy(self)
        for arg, value in kwargs.items():
            setattr(copy, arg, value)
        return copy
    

class Person(Prototype):
    def __init__(self, name: str, age: int) -> None:
        self.name, self.age = name, age

    def __str__(self) -> str:
        return f'{self.__class__.__name__} name={self.name} age={self.age}'

ivan = Person('Ivan', 20)
petr_poroshenko = ivan.prototype()
petr_poroshenko.name = 'Petr'
vasya = petr_poroshenko.prototype_parametrize(name='Vasya')
print(ivan, petr_poroshenko, vasya, sep='\n')
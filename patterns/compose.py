# Composite has methods: add, remove, get, interface()
# Composite aggragate object тоже имеют interface()
from abc import ABC, abstractmethod
import random


class EmptyStationery(Exception):
    def __init__(self, stationery_name: str) -> None:
        super().__init__(f'Stationery {stationery_name} is empty')


class Stationery:
    _status_length_ratio: int | float 

    @abstractmethod
    def __init__(self, color: str) -> None:
        self.color = color
        self._status: int | float = 100
    
    @property
    def status(self) -> int | float:
        return self._status
    
    def __str__(self) -> str:
        return f'{self.__class__.__name__} {self.color} status={self.status}'

    def draw(self, length: int | float) -> int | float:
        if not self._status:
            raise EmptyStationery(self.__class__.__name__)
        can_draw = self._status / self._status_length_ratio
        if can_draw >= length:
            self._status -= length * self._status_length_ratio
            print(f'{self} has drawn {length} length')
            return length
        else:
            self._status = 0
            print(f'{self} has drawn {can_draw} length')
            return can_draw

class Pen(Stationery):
    _status_length_ratio = 0.1

    def __init__(self, color: str) -> None:
        super().__init__(color)

class Pencil(Stationery):
    _status_length_ratio = 0.08

    def __init__(self, color: str) -> None:
        super().__init__(color)

class Case:
    def __init__(self, stationery: list[Stationery] | tuple[Stationery]) -> None:
        self.stationery = stationery

    @property
    def stationery(self):
        return self._stationery
    
    @staticmethod
    def check_stationery(item: Stationery) -> None:
        if not isinstance(item, Stationery):
                raise TypeError(f'Case expects Stationery instances, not {type(item).__name__}')

    @stationery.setter
    def stationery(self, stationery: tuple[Stationery] | list[Stationery]) -> None:
        if not isinstance(stationery, (list, tuple)):
            raise TypeError(f'Case expects stationery to be list or tuple')
        for item in stationery:
            self.check_stationery(item)
        self._stationery = list(stationery)

    def get(self, color: str) -> Stationery:
        filtered = list(filter(lambda item: item.status and item.color == color, self._stationery))
        return random.choice(filtered) if filtered else None
    
    def add(self, item: Stationery) -> None:
        self.check_stationery(item)
        self._stationery.append(item)

    def remove(self, item: Stationery) -> None:
        if item not in self._stationery:
            raise ValueError(f'Stationery {item} is not present in this Case')
        self._stationery.remove(item)

    def clean(self) -> None:
        self._stationery = list(filter(lambda item: item.status, self._stationery))

    def draw(self, length: int | float, color: str) -> None:
        item = self.get(color)
        if not item:
            print(f'No available stationery with color {color} in this case at the moment')
            print(f'Length {length} was not drawn')
            return
        drawn = item.draw(length)
        if drawn < length:
            self.draw(length - drawn, color)

    def __str__(self) -> str:
        stationery = ', '.join([str(st) for st in self._stationery])
        return f'{self.__class__.__name__} with stationery {stationery}'

pens = [Pen('blue'), Pen('blue')]
pencils = [Pencil('blue'), Pencil('grey')]
roganov_case = Case(pens + pencils)
roganov_case.draw(3000, 'blue')
print(roganov_case)
roganov_case.clean()
print(roganov_case)
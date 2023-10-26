from abc import ABC, abstractmethod
from typing import Any

class InvalidEquipment(Exception):
    def __init__(self, item: Any) -> None:
        super().__init__(f'Класс {type(item).__name__} не является классом Equipment')

class ItemNotFound(Exception):
    pass

class Equipment(ABC):
    @abstractmethod
    def __init__(self, weight: float):
        self.weight = weight

    @property
    def weight(self) -> float:
        return self._weight
    
    @weight.setter
    def weight(self, new_weight: float) -> None:
        if not isinstance(new_weight, float):
            raise TypeError(f'Wrong type, weight must be float, not {type(new_weight).__name__}')
        self._weight = new_weight

    def __str__(self) -> str:
        return f'{self.__class__.__name__} {self.weight} kg'

class Ball(Equipment):
    __sport_coeff = {
        'volleyball': 0.3,
        'basketball': 0.5,
        'football': 0.4,
    }
    __default_weight = 0.4
    __size_coeff = 1.1

    def __init__(self, size: int, sport: str):
        self.size, self.sport = size, sport
        self.__set_weight()
    
    def __set_weight(self) -> None:
        if self.sport in self.__sport_coeff.keys():
            weight = self.__sport_coeff[self.sport]
        else:
            weight = self.__default_weight
        self.weight = round(weight * self.__size_coeff ** (self.size - 1), 3)

class Human:
    def __init__(self, name: str, items: list[Equipment]):
        self.name, self.items = name, items
    
    @property
    def items(self) -> list[Equipment]:
        return self._items
    
    @items.setter
    def items(self, new_items: list[Equipment]) -> None:
        for item in new_items:
            if not isinstance(item, Equipment):
                raise InvalidEquipment(item)
        self._items = new_items
    
    def add_item(self, new_item: Equipment) -> None:
        if not isinstance(new_item, Equipment):
            raise InvalidEquipment(new_item)
        self._items.append(new_item)
    
    def remove_item(self, item: Equipment) -> None:
        if not isinstance(item, Equipment):
            raise InvalidEquipment(item)
        if item not in self._items:
            raise ItemNotFound(f'{item} was not found')
        self._items.remove(item)
    
    def get_items_weight(self) -> float:
        return round(sum([item.weight for item in self._items]), 3)
                

krivenkos_balls = [Ball(7, 'rugby'), Ball(3, 'Water Polo'), Ball(10, 'golf')]
print(*krivenkos_balls)
print(Human('Artyom', krivenkos_balls).get_items_weight())
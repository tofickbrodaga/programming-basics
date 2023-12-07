from abc import ABC, abstractmethod
from random import randint, choice


class Place(ABC):
    @abstractmethod
    def __init__(self, title: str) -> None:
        self.title = title

class Gallery(Place):
    def __init__(self, title: str, pictures: list[str]) -> None:
        self.pictures = pictures
        super().__init__(title)

class Restraurant(Place):
    def __init__(self, title: str, dishes: list[str]) -> None:
        self.dishes = dishes
        super().__init__(title)

class Visitor:
    _restraurant_dishes_range = 1, 5

    def visit(self, place: Place) -> None:
        if not isinstance(place, Place):
            raise TypeError(f'Visitor can only visit place: Place instance.')
        if isinstance(place, Gallery):
            pictures = ', '.join(place.pictures)
            print(f'Enjoying scenic view on pictures at {place.title}, pictures: {pictures}')
        elif isinstance(place, Restraurant):
            dishes = ', '.join([choice(place.dishes) for _ in range(randint(*self._restraurant_dishes_range))])
            print(f'Enjoying and drinking {dishes} at Restraurant {place.title}')
        else:
            print(f'Unknown type{type(place).__name__} {place.title}, just wondering.')


clod_minet = Restraurant('Клод монет', ['Салат Красное море', 'Салат вкусный', 'Салат осенний'])
erarta = Gallery('Эрарта', ['"Гвоздь в сметане"', '"Горел асфальт"', '"Рождённый пешками"'])

tyurin = Visitor()
tyurin.visit(erarta)
tyurin.visit(clod_minet)
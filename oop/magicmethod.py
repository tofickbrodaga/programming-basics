from typing import Self
from random import randint

class Point:
    def __init__(self, x: int = 0, y: int = 0):
        self.x, self.y = x, y
    
    def __str__(self) -> str:
        return f'{self.__class__.__name__} {self.x=}, {self.y=}'
    
    def __gt__(self, other: Self) -> bool:
        return self.x > other.x and self.y > other.y
    
    def __lt__(self, other: Self) -> bool:
        return self.x < other.x and self.y < other.y
    
    def __ge__(self, other: Self) -> bool:
        x_eq = self.x == other.x and self.y > other.y
        y_eq = self.y == other.y and self.x > other.x
        return x_eq or y_eq

    def __ge__(self, other: Self) -> bool:
        not self > other
    def __le__(self, other: Self) -> bool:
        not self > other
    
    def __eq__(self, other: Self) -> bool:
        return self.x == other.x and self.y == other.y
    
    def __ne__(self, other: Self) -> bool:
        return not self == other

points = [Point(randint(0, 10), randint(0, 10)) for _ in range(10)]

print(*[str(point) for point in points])

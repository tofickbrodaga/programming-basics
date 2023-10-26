import math

class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    @property
    def radius(self) -> float:
        return self.__radius
    
    @radius.setter
    def radius(self, new_radius: float) -> None:
        if not isinstance(new_radius, float, int):
            raise TypeError(f'Radius must be float or int, not {type(new_radius)}')
        if new_radius < 0:
            raise ValueError
        self.__radius = new_radius

def length(self) -> float:
    return round(math.pi * 2 * self.radius, 2)

def area(self) -> float:
    return round(math.pi * self.radius ** 2, 2)

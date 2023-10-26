from math import sqrt

class Triangle:
    def __init__(self, side_a: float, side_b: float, side_c: float) -> None:
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
    
    @property
    def square(self) -> float:
        p = (self.side_a + self.side_b + self.side_c) / 2
        return round(sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)), 2)
    
    @square.setter
    def square(self, new_square: float) -> None:
        if not isinstance(new_square, float, int):
            raise TypeError(f'Square must be float or int, not {type(new_square)}')
        if new_square < 0:
            raise ValueError
        self.__square = new_square
    
    @property
    def Triangle_is_right(self):
        return self.side_a, self.side_b, self.side_c
    
    @Triangle_is_right.setter
    def Triangle_is_right(self, new_sides: tuple[float, float, float]) -> None:
        for side in new_sides:
            if not isinstance(side, (float, int)):
                raise TypeError(f'Side must be float or int, not {type(side)}')
            if side < 0:
                raise ValueError('Side must be positive, not negative')
        if new_sides[0]**2 == new_sides[1]**2 + new_sides[2]**2 or \
           new_sides[1]**2 == new_sides[0]**2 + new_sides[2]**2 or \
           new_sides[2]**2 == new_sides[0]**2 + new_sides[1]**2:
            self.side_a, self.side_b, self.side_c = sorted(new_sides)
        else:
            raise ValueError('Triangle is not right-angled')


triangle = Triangle(3, 4, 5)
print(triangle.Triangle_is_right)
triangle.Triangle_is_right = (10, 3, 4)
print(triangle.Triangle_is_right)

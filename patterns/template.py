from abc import ABC, abstractmethod
from typing import Self


class WrongDirection(Exception):
    def __init__(self, direction) -> None:
        super().__init__(f'Wrong direction {direction} of type {type(direction).__name__}')


class ClassicalDancer(ABC):
    _twist_angle: int
    _full_circle: int = 360
    _fourth: int = 90
    _steps: tuple[int] = 0, 1, 0, -1
    _directions: tuple[str] = 'forward', 'right', 'backward', 'left'

    @abstractmethod
    def __init__(self, name: str, position: tuple[int, int] = (0, 0)) -> None:
        self.name, self.position = name, list(position)
        self.angle = 0

    @abstractmethod
    def move(self) -> None:
        pass

    def __str__(self) -> str:
        return f'{self.__class__.__name__} {self.name} \
            position={self.position} angle={self.angle}'

    @property
    def angle(self) -> None:
        return self._angle

    @angle.setter
    def angle(self, new_angle: int) -> int:
        self._angle = new_angle % self._full_circle

    def _check_direction(self, direction: str) -> None:
        if direction not in self._directions:
            raise WrongDirection(direction)

    def __add_position(self, direction: str, angle_change: int = None) -> None:
        angle_shift = self.angle // self._fourth
        self._check_direction(direction)
        direction_shift = self._directions.index(direction)
        shift = angle_shift + direction_shift
        shift %= len(self._steps)
        if shift < len(self._steps) - 1:
            x, y = self._steps[shift], self._steps[shift+1]
        else:
            x, y = self._steps[shift], self._steps[0]
        self.position = [self.position[0] + x, self.position[1] + y]

    def __step(self, direction: str) -> None:
        self.__add_position(direction)

    def __step_with_twist(self, direction: str, positive: bool = False) -> None:
        self.__add_position(direction)

        angle_change = self._twist_angle if positive else -self._twist_angle
        self.angle += angle_change

    def _left_foot(self, direction: str) -> Self:
        self.__step(direction)
        return self

    def _right_foot(self, direction: str) -> Self:
        self.__step(direction)
        return self

    def _left_foot_with_twist(self, direction: str, positive: bool = False) -> Self:
        self.__step_with_twist(direction, positive)
        return self

    def _right_foot_with_twist(self, direction: str, positive: bool = False) -> Self:
        self.__step_with_twist(direction, positive)
        return self

class WaltzDancer(ClassicalDancer):
    _twist_angle: int = 180

    def __init__(self, name: str, position: tuple[int, int] = (0, 0)) -> None:
        super().__init__(name, position)

    def move(self) -> None:
        return (
            self
                ._left_foot_with_twist('forward')
                ._right_foot_with_twist('backward')
        )

class TangoDancer(ClassicalDancer):
    _twist_angle: int = 90

    def __init__(self, name: str, position: tuple[int, int] = (0, 0)) -> None:
        super().__init__(name, position)

    def move(self) -> None:
        return (
            self
                ._right_foot_with_twist('forward', True)
                ._left_foot_with_twist('backward', True)
                ._right_foot_with_twist('forward', True)
                ._left_foot_with_twist('backward', True)
        )
    
litvinov = WaltzDancer('Jegor')
print(litvinov.move())
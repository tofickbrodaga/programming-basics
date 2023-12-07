import time
from typing import Callable

class AdsGetter:
    def __init__(self, ads_content: list[str]) -> None:
        self._ads = ads_content

class Size:
    def __init__(self, width: int, height: int) -> None:
        self.width, self.height = width, height

    @staticmethod
    def check_positive(method: Callable) -> None:
        def wrapped(self, value: int):
            if not isinstance(value, int):
                raise TypeError(f'value must be int> not {type(value).__name__}')
            if value < 0:
                raise ValueError(f'value {value} must be positive')
            return method(self, value)
        return wrapped

    @property
    def width(self):
        return self._width

    @width.setter
    @check_positive
    def width(self, new_width: int) -> None:
        self._width = new_width
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    @check_positive
    def width(self, new_height: int) -> None:
        self._height = new_height
    
    def __str__(self) -> str:
        return f'width={self.width}, height={self.height}'

class BillBoard: # Facade
    def __init__(self, ads: AdsGetter, size: Size, sleep: int) -> None:
        self._ads, self._size, self._sleep = ads, size, sleep
    
    def show(self) -> None:
        while True:
            print(f'Ad: <{self._ads.get()}> sized: {self._size}')
            time.sleep(self._sleep)

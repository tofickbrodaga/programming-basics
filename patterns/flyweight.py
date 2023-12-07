from typing import Self

class FlyWeightMixin():
    _pool: dict = dict()
    def __new__(cls, *args, **kwargs) -> Self:
        key = hash((cls, args, frozenset(kwargs.items())))
        if key not in cls._pool.keys():
            cls._pool[key] = super().__new__(cls)
        return cls._pool[key]

class Ball(FlyWeightMixin):
    def __init__(self, color: str, size: int) -> None:
        self.color, self.size = color, size


class Leaf(FlyWeightMixin):
    def __init__(self, color: str, size: int) -> None:
        self.color, self.size = color, size

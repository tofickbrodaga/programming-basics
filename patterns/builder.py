from abc import ABC
from typing import Self


class Engine:
    def __init__(self, model: str, horsepower: int) -> None:
        self.model, self.horsepower = model, horsepower


class Car:
    def set_wheels(self, wheels: int) -> Self:
        self.wheels = wheels
        return self

    def set_seats(self, seats: int) -> Self:
        self.seats = seats
        return self

    def set_model(self, model: str) -> Self:
        self.model = model
        return self

    def set_engine(self, engine: Engine) -> Self:
        self.engine = engine
        return self


class CarBuilder(ABC):
    _model: str
    _horsepower: int
    _seats: int
    _wheels: int

    @classmethod
    def build(cls) -> Car:
        engine  = Engine(cls._model, cls._horsepower)
        return (
            Car()
            .set_engine(engine)
            .set_model(cls._model)
            .set_seats(cls._seats)
            .set_wheels(cls._wheels)
        )
    

class LadaBuilder(CarBuilder):
    _model = 'Lada'
    _horsepower = 60
    _seats = 5
    _wheels = 4


class HavalBuilder(CarBuilder):
    _model = 'Haval'
    _horsepower = 150
    _seats = 6
    _wheels = 4

print(LadaBuilder.build().engine.horsepower)
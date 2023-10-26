import random
import time

# счетчик Counter
class Counter:
    def __init__(self) -> None:
        self.__value = 0
    
    @property
    def value(self) -> int:
        return self.__value
    
    def increment(self) -> None:
        self.__value += 1
    
    def reset(self) -> None:
        self.__value = 0

# Race game
# Car: attrs: model: str, speed: int
# Race: 
# N circle on one circle - one car delete with random 
# attrs: cars: list[Car], laps: int = 5, crash_prob: int = 30
# methods: start() -> None

class Car:
    def __init__(self, model: str, speed: int | float) -> None:
        self.model, self.speed = model, speed

    @property
    def speed(self) -> int|float:
        return self._speed
    @speed.setter
    def speed(self, new_speed: int|float) -> None:
        if not isinstance(new_speed, (int, float)):
            raise TypeError(f'{type(new_speed).__name__} is not int|float')
        if new_speed < 0:
            raise ValueError(f'Speed of car {self.model} {new_speed} < 0')
        self._speed = new_speed

class Race:
    def __init__(self, cars: list[Car], laps: int = 5, crash_prob: int = 30):
        self.cars, self.laps, self.crash_prob = cars, laps, crash_prob
        self.__counter = Counter()
    
    @property
    def cars(self) -> list[Car]:
        return self.__cars
    
    @cars.setter
    def cars(self, new_cars: list[Car]) -> None:
        for car in new_cars:
            if not isinstance(car, Car):
                raise TypeError(f'{type(car).__name__} is not a Car instance')
        self.__cars = new_cars

    def check_positive_int(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError(f'{type(value).__name__} is not a int')
        if value < 0:
            raise ValueError(f'Value {value} is less than zero')
    
    @property
    def laps(self) -> int:
        return self._laps
    
    @laps.setter
    def laps(self, new_laps: int) -> None:
        self.check_positive_int(new_laps)
        self._laps = new_laps
    
    @property
    def crash_prob(self) -> int:
        return self.__crash_prob
    
    @crash_prob.setter
    def crash_prob(self, new_prob: int) -> None:
        self.check_positive_int(new_prob)
        if new_prob > 100:
            raise ValueError(f'Probability {new_prob} > 100')
        self.__crash_prob = new_prob

    def is_crash(self, crash_prob: int):
        new_prob = crash_prob * self.speed / 100 if self.speed > 100 else crash_prob
        return random.randint(0, 99) < new_prob

    def start(self):
        self.cars.sort(key =lambda car: car.speed, reverse=True)
        print('Please greet warmly Race participants!')
        print(''.join([f'{car.model}: {car.speed} ' for car in self.cars]))
        while self.cars and self.__counter.value < self.laps:
            to_remove = []
            for car in self.cars:
                if self.is_crash(self.crash_prob):
                    to_remove.append(car)
            for car in to_remove:
                print(f'Car {car.model} has crashed on lap {self.__counter.value + 1}')
                self.cars.remove(car)
            self.__counter.increment()
        
        self.__counter.reset()
        if self.cars:
            for place, car in enumerate(self.cars):
                print(f'{place + 1}: {car.model}')
        else:
            print('All cars have crashed in this Race!')

car_names = (
    'Dodge Challenger', 'Lada Priora GT Turbo', 'Lightning McQueen', 'Daewoo Matiz', 'BeeCycle', 'Krivenko', ''
)

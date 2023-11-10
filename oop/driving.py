from typing import Any

class Driving:
    def __init__(self, speed: int | float) -> None:
        self.speed = speed
    
    def drive(self, distance: int|float) -> float:
        time = round(distance/self.speed, 3)
        print(f'{time}')
        return time

class Washing:
    def __init__(self, time_per_item: int | float) -> None:
        self._time_per_item = time_per_item
    
    def wash(self, items: list[Any]) -> int|float:
        time = 0
        for item in items:
            print(f'Washing {item}')
            time += self._time_per_item
        print(f'Washing {len(items)} item took {time} time')
        return True

class Machine:
    def __init__(self, power: int|float, charge_per_time: int|float) -> None:
        self.charge_level = 0
        self.power, self.charge_per_time = power, charge_per_time
    
    def charge(self, time: int|float) -> None:
        new_level = self.charge_level + time * self.charge_per_time
        new_level = new_level if new_level < 100 else 100

class WashingMachine(Machine, Washing):
    def __init__(self, power: int | float, charge_per_time: int | float, time_per_item: int | float) -> None:
        super().__init__(power, charge_per_time)
        super(Machine, self).__init__(time_per_item)

class DrivingMachine(Driving, Machine):
    def __init__(self, speed: int | float, power: int | float, charge_per_time: int | float) -> None:
        super().__init__(speed)
        super(Driving, self).__init__(power, charge_per_time)

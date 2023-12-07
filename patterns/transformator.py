from random import uniform
from abc import ABC, abstractmethod

class PowerSource(ABC):
    voltage: float
    current: float

    def __init__(self, delta: int | float) -> None:
        self.delta = delta

    def get(self) -> float:
        inaccurancy = self.voltage * (self.delta / 100)
        return self.voltage + uniform(-inaccurancy, inaccurancy)
    
class Transformator:
    @staticmethod
    def adapt(powersouce: PowerSource, target_voltage: int | float) -> PowerSource:
        if powersouce.voltage != target_voltage:
            coef = powersouce.voltage / target_voltage
            powersouce.voltage = target_voltage
            powersouce.current *= coef
        return powersouce

class Device:
    def __init__(self, name: str, voltage: float, source: PowerSource) -> None:
        self.name, self.voltage, self.source = name, voltage, source

    @property
    def source(self) -> PowerSource:
        return self.__source
    
    @source.setter
    def source(self, new_source: PowerSource) -> None:
        if not isinstance(new_source, PowerSource):
            raise TypeError(f'{type(new_source).__name__} was given instead of PowerSource.')
        self.__source = Transformator.adapt(new_source, self.voltage)

class Charger(PowerSource):
    voltage = 12
    current = 3.3
    def __init__(self, delta: int | float) -> None:
        super().__init__(delta)

tyurin = Charger(0.1)
Xiamomi_redmi_harry_potter_something_note_999 = Device('XIMI', 220, tyurin)
print(Xiamomi_redmi_harry_potter_something_note_999.source.voltage)
print(Xiamomi_redmi_harry_potter_something_note_999.source.current)

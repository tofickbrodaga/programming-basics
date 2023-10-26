class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name, self.age = name, age
    
    def walk(self, miles: float) -> None:
        print(f'{self.__class__.__name__} {self.name} is walking {miles} miles')

krivenko = Person('Tyomuh', 14)
print(krivenko.age)
krivenko.walk(10)

class Student(Person):
    tired_coeff = 100
    sleep_coeff = 30
    tiredness_threshold = 900
    def __init__(self, name: str, age: int, group: str) -> None:
        super().__init__(name, age)
        self.group = group
        self.tiredness = 0
    
    def study(self, hours: float = 1.5) -> None:
        self.tiredness += hours * self.__class__.tired_coeff
        print(f'{self.name} was studying for {hours} hours')
        print(f'{self.name} tiredness increased to {self.tiredness}')
        self.tiredness += hours * self.__class__.tired_coeff
        if self.tiredness > self.__class__.tiredness_threshold:
            print(f'{self.tiredness} > {self.tiredness_threshold}')
    
    def sleep(self, hours: float = 8.) -> None:
        restore = self.__class__.sleep_coeff * hours
        new_tiredness = self.tiredness - restore
        self.tiredness = new_tiredness if new_tiredness >= 0 else 0
        print()
    
    def eat(self, kcal: float) -> None:
        print(f'{self.name} tiredness increased to {self.tiredness}')

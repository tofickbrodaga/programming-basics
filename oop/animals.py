# class Base:
#     def method(self):
#         print('base')

# class A(Base):
#     def method(self):
#         print('A')
#         super().method()

# class B(Base):
#     def method(self):
#         print('B')
#         super.method()

# class C(A, B):
#     def method(self):
#         print('C')
#         super().method()

# print([class_.__name__ for class_ in C.__mro__])
# class animal is abstract -> classes: tailed, horned, hoofed, furry, wing

from abc import ABC, abstractmethod

class Animal(ABC):
    horns = fur = hoofs = tail = wings = False
    @abstractmethod
    def __init__(self, age: int) -> None:
        self.age = age
    
    def __str__(self) -> str:
        attrs = ['horns', 'fur', 'hoofs', 'tail', 'wings']
        attrs = ', '.join([attr for attr in attrs if getattr(self, attr)])
        return f'{self.__class__.__name__} with {attrs}'

class Tailed(Animal):
    def __init__(self, age: int) -> None:
        self.tail = True
        super().__init__(age)

class Furry(Animal):
    def __init__(self, age: int) -> None:
        self.fur = True
        super().__init__(age)

class Horned(Animal):
    def __init__(self, age: int) -> None:
        self.horns = True
        super().__init__(age)

class Hoofed(Animal):
    def __init__(self, age: int) -> None:
        self.hoofs = True
        super().__init__(age)

class Winged(Animal):
    def __init__(self, age: int) -> None:
        self.wings = True
        super().__init__(age)

class Cat(Horned, Tailed, Furry):
    pass

print(Cat(17))
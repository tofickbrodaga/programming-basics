# public obj.attr
# private obj.__attr
# hidden(protected) obj._attr

class Person:
    def __init__(self, name: str, age: int, passport: str) -> None:
        self.name = name
        self._age = age
        self.__passport = passport

arsenovich = Person('Marko', 16, '0319 225763')
print(arsenovich._age)
print(arsenovich.__passport)

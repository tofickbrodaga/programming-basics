from typing import Any
import json

class JSONable(type):
    def __init__(cls, name: str, bases: tuple[type], attrs: dict[str, Any]):
        def to_json(self) -> str:
            return json.dumps(self.__dict__)

        def from_json(cls, json_attrs: str):
            return cls(**json.loads(json_attrs))

        cls.to_json = to_json
        cls.from_json = classmethod(from_json)

class Person(metaclass=JSONable):
    def __init__(self, name: str, age: int) -> None:
        self.name, self.age = name, age

print(Person('Vasilenko', 17).to_json())


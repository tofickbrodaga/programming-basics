import json

def make_jsonable(class_: type) -> type:
    def to_json(self) -> str:
        return json.dumps(self.__dict__)

    def from_json(cls, json_attrs: str):
        return cls(**json.loads(json_attrs))

    setattr(class_,'to_json', to_json())
    setattr(class_, 'from_json', classmethod(from_json))

    return class_

class Maroon:
    def __init__(self, number: str) -> None:
        self.number = number
        self.data = '1', '2', '3'

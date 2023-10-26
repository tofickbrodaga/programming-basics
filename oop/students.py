from typing import Optional

class Student:
    def __init__(self, name: str, age: int, marks: Optional[list[int]] = None):
        self.name, self.age, self.marks = name, age, marks
    
    @property
    def marks(self) -> list[int]:
        return self.__marks
    
    @marks.setter
    def marks(self, new_marks: list[int]) -> None:
        if not isinstance(new_marks, list):
            raise TypeError('you should have given a list of marks')
        for mark in new_marks:
            if not isinstance(mark, int):
                raise TypeError(f'marks should be int, not {type(mark).__name__}')
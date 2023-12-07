from typing import Self, Generator
import random

class DownwardCounter:
    def __init__(self, start: int) -> None:
        self._current = start

    def _set_current(self, new: int) -> None:
        if not isinstance(new, int):
            raise TypeError(f'{self.__class__.__name__} expects start to be int')
        if new < 0:
            raise ValueError(f'{self.__class__.__name__} expects positive start')
        self._current = new

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> int:
        if not self._current:
            raise StopIteration
        self._current -= 1
        return self._current + 1

# counter = DownwardCounter(5)
# for value in counter:
#     print(value)

class Student:
    def __init__(self, name: str, avg_score: float) -> None:
        self.name, self.avg_score = name, avg_score

class Group:
    def __init__(self, title: str, students: list[Student]) -> None:
        self.students, self.title = students, title
        self.__iterator = students.copy()

    @property
    def avg_score(self):
        return sum([st.avg_score for st in self.students]) / len(self.students)

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> Student:
        if not self.__iterator:
            self.__iterator = self.students.copy()
            raise StopIteration
        return self.__iterator.pop(0)

class Teacher:
    def __init__(self, name: str, score_range: tuple[int, int]) -> None:
        self.name, self._set_score = name, score_range
    
    def _set_score(self, score_range: tuple[int, int]) -> None:
        def generator():
            while True:
                yield random.randint(*score_range)
        self._score_generator = generator()
    
    def __iter__(self) -> Generator:
        return self._score_generator
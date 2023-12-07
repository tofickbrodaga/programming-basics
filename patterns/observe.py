from typing import Any

class ItemNotInList(Exception):
    pass

class GithubRepo:
    def __init__(self, title: str, owner: str) -> None:
        self.title = title
        self.owner = owner
        self._homeworks = []
        self._students = []
    
    @property
    def homeworks(self) -> list[str]:
        return self._homeworks
    
    def add_hw(self, homework: str) -> None:
        self._homeworks.append(homework)
        self.notify_all(f'Added homework {homework}')
    
    def remove_hw(self, homework: str) -> None:
        if homework not in self._homeworks:
            raise ItemNotInList(f'{homework} not in homeworks list')
        self._homeworks.remove(homework)
    
    def subscribe(self, student: Any) -> None:
        self._students.append(student)
    
    def unsubscribe(self, student: Any) -> None:
        if student not in self._students:
            raise ItemNotInList(f'{student} not in students list')
        self._students.remove(student)
    
    def notify_all(self, message: str):
        for student in self._students:
            student.notify(message)

class Student:
    def __init__(self, name: str) -> None:
        self.name = name
    
    def notify(self, message: str):
        print(f'{self.__class__.__name__} {self.name} have a message: {message}')

grigoryan = Student('Artyom')
osipov = Student('Vladislave')

homeworks_23 = GithubRepo('homeworks_23', 'siriusdevs')
homeworks_23.subscribe(grigoryan)
homeworks_23.subscribe(osipov)

homeworks_23.add_hw('hw2 hard, you are expelled')
    
    


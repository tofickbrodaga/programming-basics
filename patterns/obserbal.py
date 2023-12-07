from abc import ABC, abstractmethod
from typing import Any, Optional


class Observable(ABC):
    @abstractmethod
    def __init__(self, *args, **kwargs) -> None:
        self._observers = []
        super().__init__(*args, **kwargs)

    def subscribe(self, subscriber: Any) -> None:
        self._observers.append(subscriber)

    def notify(self, message: str) -> None:
        for observer in self._observers:
            observer.update(message, self.__class__.__name__)

class Observer(ABC):
    @abstractmethod
    def update(self, message: str) -> None:
        pass

class VKPublicCollegeSirius(Observable):
    def __init__(self, *args, **kwargs) -> None:
        self.posts = []
        super().__init__(*args, **kwargs)

    def add_posts(self, post: str) -> None:
        self.posts.append(post)
        self.notify(post)

class Student(Observer):
    def __init__(self, name: str) -> None:
        self.name = name
        super().__init__()

    def update(self, message: str, notifier: Optional[str] = None) -> None:
        notifier = f'from notifier {notifier}' if notifier else ''
        print(f'{self.__class__.__name__} {self.name} has recieved message {notifier}: <{message}>')
    
public_vk = VKPublicCollegeSirius()
students = Student('Litvinov'), Student('Roganov'), Student('Shishkin')
for student in students:
    public_vk.subscribe(student)

public_vk.add_posts('Скоро новогодний бал, который состоится в соответствии с паттерном шаблонный метод')
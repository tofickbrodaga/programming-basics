from abc import ABC


class Technology(ABC):
    def __str__(self) -> str:
        return f'Technology {self.__class__.__name__}'
    
class Python(Technology):
    pass

class JavaScript(Technology):
    pass

class Pascal(Technology):
    pass

class WorkPractice(ABC):
    def __str__(self) -> str:
        return f'WorkPractice {self.__class__.__name__}'
    
class VK(WorkPractice):
    pass

class GazpromNeft(WorkPractice):
    pass

class RogaAndKopytaTechnologies(WorkPractice):
    pass

class College:
    def __init__(
            self,
            title: str,
            practice_places: list[WorkPractice],
            technologies: list[Technology],
    ) -> None:
        self.title, self.practice_places, self.technologies = title, practice_places, technologies

    @staticmethod
    def get_joined(items: list) -> str:
        return ', '.join([str(item) for item in items])

    def get_technologies(self) -> str:
        return self.get_joined(self.technologies)

    def get_practice_places(self) -> str:
        return self.get_joined(self.practice_places)

    def get_lesson(self) -> None:
        print(f'You are getting a lesson with technologies {self.get_techologies()}')

    def get_practice(self) -> None:
        print(f'You are  going to practice techologies {self.get_technologies()}')
        print(f'at {self.get_practice_places()}')

class CollegeFactory(ABC):
    practice_places: list[WorkPractice]
    technologies: list[Technology]
    
    def create(self, title: str) -> College:
        return College(title, self.practice_places, self.technologies)
    
class SiriusCollegeFactory(CollegeFactory):
    practice_places = [VK(), GazpromNeft()]
    technologies = [Python(), JavaScript()]

class UsualCollegeFactory(CollegeFactory):
    practice_places = [RogaAndKopytaTechnologies()]
    technologies = [Pascal()]

SiriusCollegeFactory().create('Sirius').get_practice()
UsualCollegeFactory().create('Воронежский Государственный Колледж Программирования при Воронежском Арграрном Университете').get_practice()
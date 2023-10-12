# декораторы используют args и kwargs, 
# распаковывают функцию, 
# которая была до этого

from typing import Callable
from random import choice

STUDENTS = ['Zorina', 'Dyatlova', 'Sheina', 'Grigoryan', 'Vasilenko']
CATS = ['^..^', '^=..=^', '^_.._^', '^#..#^']

def get_students(func: Callable) -> Callable:
    def add_student_with_cat(*args, **kwargs) -> str:
        return f'{func(*args, **kwargs)} is this cat: {choice(CATS)}'
    return add_student_with_cat


@get_students
def get_answer():
    return choice(STUDENTS)

print(get_answer())



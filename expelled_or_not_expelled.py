from typing import Callable
from random import choice


EXPELLING = ['expelled', 'not expelled']
STUDENTS = ['Kriv', 'Otroshko', 'Dyatel', 'Tenizhkin', 'Grigoryev', 'Otryzhko', 'Nehoroshii-Horoshii']

def who_is_expelled(func: Callable) -> Callable:
    def message(*args, **kwargs) -> str:
        return f'{func(*args, **kwargs)} she/he is {choice(EXPELLING)}'
    return message

@who_is_expelled
def last_name_expelled():
    
    return choice(STUDENTS)

print(last_name_expelled())

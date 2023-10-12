# случайные имена студентов и их оценки, имея диапазон длины имен и диап. оценок

from string import ascii_lowercase as ascii_lc
from random import randint, choice
from typing import Generator


def name_and_mark(
        quantity: int,
        range_name: tuple[int, int] = (2, 10),
        range_mark: tuple[int, int] = (2, 5),
        ) -> Generator:
    while quantity > 0:
        name = ''.join([choice(ascii_lc) for _ in range(randint(*range_name))])
        yield name.capitalize(), randint(*range_mark)
        quantity -= 1

for name, mark in name_and_mark(100):
    print(f'Name: {name}, mark:{mark}')
    input()

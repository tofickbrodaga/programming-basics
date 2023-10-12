from random import randint
from typing import Generator

def get_random_number_in_array (quantity: int, range_num: tuple[int, int] = (0, 10)) -> Generator:
    while quantity > 0:
        yield randint(*range_num)
        quantity -= 1

for num in get_random_number_in_array(5, (0, 5)):
    print(num)
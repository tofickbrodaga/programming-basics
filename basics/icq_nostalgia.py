from typing import Callable

def isq_message(func: Callable) -> Callable:
    def message(*args, **kwargs) -> str:
        result = func(*args, **kwargs)
        return ''.join(sym.upper() if i % 2 == 0 else sym.lower() for i, sym in enumerate(result))
    return message

@isq_message
def give_my_message(msg: str):
    return msg

print(give_my_message('Привет, как дела? :) Меня зовут позитиффка :")'))

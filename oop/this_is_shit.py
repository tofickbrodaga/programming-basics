from typing import Callable

def log_class_call(classname: str):
    def log_call(func: Callable) -> Callable:
        def wrapped(*args, **kwargs):
            print(f'Running{classname}.{func.__name__}')
            return func(*args, **kwargs)
        return wrapped
    return log_call

def print_method_call(class_:type) -> type:
    for attr, value in class_.__dict__.items():
        if callable(value):
            setattr(class_, attr, log_class_call(class_.__name__)(value))
    return class_

@print_method_call
class Person:
    def walk(self) -> None:
        print('Person is walking')
from random import randint
from typing import Any, Self

class InvalidWorker(Exception):
    def __init__(self, worker: Any) -> None:
        super().__init__(f'Класс {type(worker).__name__} не является классом Worker')

class WorkerNotFound(Exception):
    def __init__(self, power: Any) -> None:
        super().__init__(f'Нет такого работника со степенью {power}')

class Worker:

    _name_len = (2, 11)
    _power_range = (-10, 10)

    def __init__(self, name: str, power: int) -> None:
        self.name, self.power = name, power

    def __str__(self) -> str:
        return f'Worker {self.name} -> {self.power}'
    
    def __call__(self, num: int) -> float:
        return num ** self.power

    @classmethod
    def generate_random(cls) -> Self:
        name = ''.join([chr(randint(128, 175)) for _ in range(randint(*cls._name_len))])
        return cls(name, randint(cls._power_range))

class Boss:
    def __init__(self, name: str, workers: list[Worker]) -> None:
        self.name, self.workers = name, workers

    @property
    def check_workers(self) -> list[Worker]:
        return self._workers

    @check_workers.setter
    def check_workers(self, new_workers: list[Worker]):
        for worker in new_workers:
            if not isinstance(worker, Worker):
                raise InvalidWorker(worker)
        self._workers = new_workers

    def __call__(self, data: list[tuple[int]]) -> list[float|int]:
        workers_data = []
        for numb, pow in data:
            for worker in self._workers:
                if worker.power == pow:
                    workers_data.append(worker(numb))
                    break
                else:
                    raise WorkerNotFound(pow)
        return workers_data

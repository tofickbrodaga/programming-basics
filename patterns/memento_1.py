from abc import ABC, abstractmethod


class Memento(ABC):
    @abstractmethod
    def __init__(self, *args, **kwargs) -> None:
        self._set_state()
        super().__init__(*args, **kwargs)

    def _set_state(self) -> None:
        self._state = self.__dict__.copy()

    def _get_state(self) -> dict:
        return self._state

    def _reset(self) -> None:
        for attr, value in self._state.items():
            setattr(self, attr, value)


class Person(Memento):
    def __init__(self, name: str, money: float) -> None:
        self.name, self.money = name, money
        super().__init__()

    def pay(self, amount: float) -> bool:
        self._set_state()

        # потенциально чреватая ошибками и сложная логика оплаты
        self.money -= amount

        # обработка возникновения ошибки оплаты
        if self.money < 0:
            self._reset()
            return False
        return True

roganov = Person('Jegor', 1000)
print(roganov.pay(1001))
print(roganov.money)
